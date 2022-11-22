import json
import sys
from functools import partial
from pathlib import Path
from enum import IntEnum

import dataclasses
from PySide2.QtCore import (
    Qt,
)
from PySide2.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
)

from rs.core import (
    config,
    pipe as p,
    util,
)
from rs.gui import (
    appearance,
)
from rs_fusion.tool.importer.importer_ui import Ui_MainWindow

APP_NAME = '読み込み(PsdSplitter用)'


class TatieStyle(IntEnum):
    EXPRESSION = 0
    CONNECTION = 1


@dataclasses.dataclass
class ConfigData(config.Data):
    json_path: str = ''
    style: TatieStyle = TatieStyle.CONNECTION
    space_x: int = 400
    space_y: int = 600


class MainWindow(QMainWindow):
    def __init__(self, parent=None, fusion=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(APP_NAME)
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowCloseButtonHint
            | Qt.WindowStaysOnTopHint
        )
        self.resize(300, 200)

        self.fusion = fusion

        # config
        self.config_file: Path = config.CONFIG_DIR.joinpath('%s.json' % APP_NAME)
        self.load_config()

        # style sheet
        self.ui.importButton.setStyleSheet(appearance.in_stylesheet)

        # event

        self.ui.jsonToolButton.clicked.connect(partial(self.toolButton_clicked))

        self.ui.closeButton.clicked.connect(self.close)
        self.ui.importButton.clicked.connect(self.import_json, Qt.QueuedConnection)

    def import_json(self) -> None:
        X_OFFSET = 1
        Y_OFFSET = 4

        resolve = self.fusion.GetResolve()
        if resolve and resolve.GetCurrentPage() != 'fusion':
            print('Fusion Pageで実行してください。')
            return

        # comp check
        comp = self.fusion.CurrentComp
        if comp is None:
            print('コンポジションが見付かりません。')
            return
        flow = comp.CurrentFrame.FlowView

        ver = self.fusion.Version

        # func
        def set_x(node, x):
            _x, _y = flow.GetPosTable(node).values()
            flow.SetPos(node, x * X_OFFSET, _y)

        def set_orange(node):
            node.TileColor = {
                '__flags': 256,
                'R': 0.92156862745098,
                'G': 0.431372549019608,
                'B': 0,
            }

        def uc_button(mg, node, page, layer_name, width):
            if node is None:
                lua = [
                    'local mg = comp:FindTool("%s")' % mg.Name,
                    'mg.Foreground = nil',
                ]
            else:
                lua = [
                    'local mg = comp:FindTool("%s")' % mg.Name,
                    'local node = comp:FindTool("%s")' % node.Name,
                    'mg:ConnectInput("Foreground", node)',
                ]
            return {
                'LINKS_Name': layer_name,
                'LINKID_DataType': 'Number',
                'INPID_InputControl': 'ButtonControl',
                'INP_Integer': False,
                'BTNCS_Execute': '\n'.join(lua),
                'INP_External': False,
                'ICS_ControlPage': page,
                'ICD_Width': width,
            }

        def add_xf_bg(pos_x, pos_y, size_x, size_y, name):
            xf = comp.AddTool('Transform', pos_x * X_OFFSET, pos_y * Y_OFFSET)
            xf.SetAttrs({'TOOLS_Name': name})
            bg = comp.AddTool('Background', pos_x * X_OFFSET, (pos_y - 1) * Y_OFFSET)
            bg.UseFrameFormatSettings = 0
            bg.Width = size_x
            bg.Height = size_y
            bg.TopLeftAlpha = 0
            bg.Depth = 1
            return xf, bg

        def add_ld(pos_x, pos_y, path):
            node = comp.AddTool('Loader', pos_x * X_OFFSET, pos_y * Y_OFFSET)
            node.Clip[1] = path
            node.Loop[1] = 1
            node.PostMultiplyByAlpha = 1 if ver < 10 else 0
            node.GlobalIn = -1000
            node.GlobalOut = -1000
            return node

        def add_node_A(pos_x, pos_y, size_x, size_y, data, name):
            pos_x += 1
            xf, bg = add_xf_bg(pos_x, pos_y, size_x, size_y, name)
            pos_x += 1
            pos_y -= 2

            # main
            user_controls = {}
            cb_name = ''
            cb_cnt: int = 0
            pre_node = bg
            for i, layer in enumerate(data):
                layer_name: str = layer['name']
                layer_name_en: str = layer['name_en']
                visible: bool = layer['visible']
                layer_data = layer['data']
                mg = comp.AddTool('Merge', pos_x * X_OFFSET, (pos_y + 1) * Y_OFFSET)
                if type(layer_data) is list:
                    node, _, pos_x = add_node_A(pos_x, pos_y, size_x, size_y, layer_data, layer_name)
                    set_x(mg, pos_x - 1)
                else:
                    node = add_ld(pos_x, pos_y, comp.ReverseMapPath(layer_data.replace('/', '\\')))
                    pos_x += 1
                mg.ConnectInput('Foreground', node)
                mg.ConnectInput('Background', pre_node)
                if layer_name.startswith('*'):
                    if cb_name == '':
                        cb_name = 'N' + str(i).zfill(3)
                        user_controls[cb_name] = {
                            'LINKID_DataType': 'Number',
                            'INPID_InputControl': 'ComboControl',
                            'LINKS_Name': name if name != 'Root' else 'Select',
                            'INP_Integer': True,
                            'INP_Default': 0,
                            'ICS_ControlPage': 'User',
                        }
                    dct = user_controls[cb_name]
                    dct[cb_cnt + 1] = {'CCS_AddString': '%s' % layer_name}
                    if visible:
                        dct['INP_Default'] = cb_cnt
                    mg.Blend.SetExpression('iif(%s.%s == %d, 1, 0)' % (xf.Name, cb_name, cb_cnt))
                    cb_cnt += 1
                else:
                    uc_name = 'N' + str(i).zfill(3) + '_' + layer_name_en
                    user_controls[uc_name] = {
                        'LINKID_DataType': 'Number',
                        'INPID_InputControl': 'CheckboxControl',
                        'LINKS_Name': layer_name,
                        'INP_Integer': True,
                        'CBC_TriState': False,
                        'INP_Default': 1 if visible else 0,
                        'ICS_ControlPage': 'User',
                        # 'ICS_ControlPage': 'Controls',
                    }
                    mg.Blend.SetExpression('%s.%s' % (xf.Name, uc_name))

                pre_node = mg

            # user control
            user_controls['Grp_' + name] = {
                'LINKS_Name': name,
                'LINKID_DataType': 'Number',
                'INPID_InputControl': 'LabelControl',
                'LBLC_DropDownButton': True,
                'LBLC_NumInputs': len(user_controls),
                'INP_Default': 1,
                'ICS_ControlPage': 'User',
            }
            if name == 'Root':
                user_controls['Refresh'] = {
                    'LINKS_Name': 'Refresh',
                    'LINKID_DataType': 'Number',
                    'INPID_InputControl': 'ButtonControl',
                    'INP_Integer': False,
                    'BTNCS_Execute': "comp:StartUndo('RS Refresh');"
                                     "local tool_list = comp:GetToolList(false, 'Fuse.RS_GlobalStart');"
                                     "for k,v in pairs(tool_list) do v:Refresh() end;"
                                     "comp:EndUndo(true)\n",
                    'ICS_ControlPage': 'Tools',
                }
            xf.ConnectInput('Input', pre_node)
            uc = {'__flags': 2097152}  # 順番を保持するフラグ
            for k, v in reversed(list(user_controls.items())):
                uc[k] = v
            xf.UserControls = uc
            xf = xf.Refresh()

            #
            set_x(xf, pos_x - 1)
            set_orange(xf)
            return xf, bg, pos_x

        def make_A(dct, sp_x, sp_y):
            _, bg, _ = add_node_A(0, 0, dct['x'], dct['y'], dct['data'], dct['name'])
            # bg
            bg.Width = dct['x'] + sp_x
            bg.Height = dct['y'] + sp_y

        def add_node_B(pos_x, pos_y, size_x, size_y, data, name, uc):
            pos_x += 1
            xf, bg = add_xf_bg(pos_x, pos_y, size_x, size_y, name)
            pos_x += 1
            pos_y -= 2

            # data sort
            a_data = []
            b_data = []
            c_data = []
            for layer in data:
                if layer['name'].startswith('*'):
                    b_data.append(layer)
                else:
                    if len(b_data) == 0:
                        a_data.append(layer)
                    else:
                        c_data.append(layer)
            _data = a_data + b_data + c_data

            # main
            pre_node = bg
            a_mg = None
            name_list = []
            for i, layer in enumerate(_data):
                layer_name: str = layer['name']
                layer_name_en: str = layer['name_en']
                visible: bool = layer['visible']
                layer_data = layer['data']
                uc_name = 'N' + str(i).zfill(3) + '_' + layer_name_en

                # add loader
                if type(layer_data) is list:
                    node, _, pos_x, uc, _name_list = add_node_B(pos_x, pos_y, size_x, size_y, layer_data, layer_name,
                                                                uc)
                    name_list += _name_list
                else:
                    node = add_ld(pos_x, pos_y, comp.ReverseMapPath(layer_data.replace('/', '\\')))

                # mg
                if layer_name.startswith('*'):
                    if a_mg is None:
                        a_mg = comp.AddTool('Merge', pos_x * X_OFFSET, (pos_y + 1) * Y_OFFSET)
                        a_mg.SetAttrs({'TOOLS_Name': xf.Name + '_MG'})
                        a_mg.ConnectInput('Background', pre_node)
                        name_list.append(a_mg.Name)
                    else:
                        set_x(a_mg, pos_x)
                    if visible or a_mg.Foreground.GetConnectedOutput() is None:
                        a_mg.ConnectInput('Foreground', node)
                    pre_node = a_mg
                    if not layer_name.startswith('!'):
                        uc[uc_name + str(pos_x)] = uc_button(a_mg, node, xf.Name, layer_name, 1.0)
                else:
                    mg = comp.AddTool('Merge', pos_x * X_OFFSET, (pos_y + 1) * Y_OFFSET)
                    mg.SetAttrs({'TOOLS_Name': layer_name + '_MG'})
                    name_list.append(mg.Name)
                    mg.ConnectInput('Background', pre_node)
                    if visible or layer_name.startswith('!'):
                        mg.ConnectInput('Foreground', node)
                    pre_node = mg
                    if not layer_name.startswith('!'):
                        uc[uc_name + '_hide_' + str(pos_x)] = uc_button(mg, None, xf.Name, layer_name + ' hide', 0.5)
                        uc[uc_name + '_show_' + str(pos_x)] = uc_button(mg, node, xf.Name, layer_name + ' show', 0.5)
                pos_x += 1

            #
            pos_x -= 1
            xf.ConnectInput('Input', pre_node)
            set_x(xf, pos_x)

            return xf, bg, pos_x, uc, name_list

        def make_B(dct, sp_x, sp_y):
            # main
            xf, bg, _, _uc, name_list = add_node_B(0, 0, dct['x'], dct['y'], dct['data'], dct['name'], {})

            # xf
            uc = {'__flags': 2097152}  # 順番を保持するフラグ
            for k, v in reversed(list(_uc.items())):
                uc[k] = v
            xf.UserControls = uc
            xf = xf.Refresh()
            set_orange(xf)

            xf.Comments = '\n'.join(reversed(name_list))

            # bg
            bg.Width = dct['x'] + sp_x
            bg.Height = dct['y'] + sp_y

        # main
        c = self.get_data()
        comp.Lock()
        comp.StartUndo('RS Import')
        json_path: Path = Path(comp.MapPath(c.json_path))
        json_data = json.loads(json_path.read_text(encoding='utf-8'))
        if c.style == TatieStyle.EXPRESSION:
            make_A(json_data, c.space_x, c.space_y)
        else:
            make_B(json_data, c.space_x, c.space_y)
        comp.EndUndo(True)
        comp.Unlock()
        QMessageBox.information(self, "Info", 'Done!')
        print('Done!')

    def toolButton_clicked(self) -> None:
        w = self.ui.jsonLineEdit
        path, _ = QFileDialog.getOpenFileName(
            self,
            'Select JSON File',
            w.text(),
            'JSON File (*.json)',
        )
        if path != '':
            w.setText(path)

    def set_data(self, c: ConfigData):
        self.ui.jsonLineEdit.setText(c.json_path)
        if c.style == TatieStyle.EXPRESSION:
            self.ui.expRadioButton.setChecked(True)
        else:
            self.ui.connectRadioButton.setChecked(True)
        self.ui.xSpinBox.setValue(c.space_x)
        self.ui.ySpinBox.setValue(c.space_y)

    def get_data(self) -> ConfigData:
        c = ConfigData()
        c.json_path = self.ui.jsonLineEdit.text()
        if self.ui.expRadioButton.isChecked():
            c.style = TatieStyle.EXPRESSION
        else:
            c.style = TatieStyle.CONNECTION
        c.space_x = self.ui.xSpinBox.value()
        c.space_y = self.ui.ySpinBox.value()

        return c

    def load_config(self) -> None:
        c = ConfigData()
        if self.config_file.is_file():
            c.load(self.config_file)
        self.set_data(c)

    def save_config(self) -> None:
        config.CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        c = self.get_data()
        c.save(self.config_file)

    def closeEvent(self, event):
        self.save_config()
        super().closeEvent(event)


def run(fusion) -> None:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(appearance.palette)
    app.setStyleSheet(appearance.stylesheet)

    window = MainWindow(fusion=fusion)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    pass