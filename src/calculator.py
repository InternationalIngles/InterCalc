import os
from PySide6 import QtWidgets, QtGui, QtCore
from widgets import PngButton, PngLogo

if getattr(__import__('sys'), 'frozen', False):
    BASE_DIR = __import__('sys')._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ICONS_DIR = os.path.join(BASE_DIR, "icons")

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InterCalculator")
        self.setFixedSize(400, 600)
        self.dark_mode = False

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout(central_widget)
        vbox.setContentsMargins(20, 20, 20, 20)
        vbox.setSpacing(10)

        header = QtWidgets.QHBoxLayout()
        title = QtWidgets.QLabel("InterCalculator")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont("Exo 2", 20)
        font.setWeight(QtGui.QFont.Weight.Bold)
        title.setFont(font)
        header.addWidget(title)
        header.addStretch()
        menu_btn = QtWidgets.QPushButton()
        self.menu_btn = menu_btn
        self.update_menu_icon()
        menu_btn.setFixedSize(50, 50)
        menu_btn.setFlat(True)
        menu_btn.clicked.connect(self.show_menu)
        header.addWidget(menu_btn)
        vbox.addLayout(header)

        self.entry = QtWidgets.QLineEdit()
        self.entry.setFixedHeight(80)
        entry_font = QtGui.QFont("Exo 2", 60)
        self.entry.setFont(entry_font)
        self.entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        vbox.addWidget(self.entry)

        grid_widget = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(grid_widget)
        grid.setSpacing(5)
        vbox.addWidget(grid_widget)

        buttons = [
            ("7", self.on_button_clicked), ("8", self.on_button_clicked), ("9", self.on_button_clicked), ("/", self.on_button_clicked),
            ("4", self.on_button_clicked), ("5", self.on_button_clicked), ("6", self.on_button_clicked), ("*", self.on_button_clicked),
            ("1", self.on_button_clicked), ("2", self.on_button_clicked), ("3", self.on_button_clicked), ("-", self.on_button_clicked),
            (".", self.on_button_clicked), ("0", self.on_button_clicked), ("=", self.on_equal_clicked), ("+", self.on_button_clicked),
            ("C", self.on_clear_clicked),
        ]

        row = 0
        col = 0
        plus_row = 0
        plus_col = 0
        for idx, (label, callback) in enumerate(buttons):
            png_path = self.get_icon_filename(label)
            button = PngButton(png_path, label, callback)
            grid.addWidget(button, row, col)
            if label == "+":
                plus_row = row
                plus_col = col
            col += 1
            if col > 3:
                col = 0
                row += 1

        logo_filename = "logod.png" if self.dark_mode else "logo.png"
        logo = PngLogo(os.path.join(ICONS_DIR, logo_filename), size=80)
        logo.setMinimumSize(1, 1)
        logo.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        grid.addWidget(logo, plus_row + 1, 0, 1, 4, alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

    def get_icon_filename(self, label):
        label_map = {
            "+": "plus", "-": "minus", "*": "multiply", "/": "divide",
            "=": "equal", ".": "dot", "C": "clear"
        }
        name = label_map.get(label, label)
        return os.path.join(ICONS_DIR, f"{name}.png")

    def on_button_clicked(self, button):
        current = self.entry.text()
        label = button.label_value
        self.entry.setText(current + label)

    def on_equal_clicked(self, button):
        try:
            result = eval(self.entry.text())
            self.entry.setText(str(result))
        except Exception:
            self.entry.setText("Error")

    def on_clear_clicked(self, button):
        self.entry.setText("")

    def show_menu(self):
        menu = QtWidgets.QMenu(self)
        about_action = menu.addAction("About")
        about_action.triggered.connect(self.on_about_clicked)
        mode_action = menu.addAction("Toggle Light/Dark Mode")
        mode_action.triggered.connect(self.on_toggle_mode)
        menu.exec(self.mapToGlobal(QtCore.QPoint(self.width() - 60, 60)))

    def on_about_clicked(self):
        about = QtWidgets.QDialog(self)
        about.setWindowTitle("About")
        about.setFixedSize(250, 300)
        vbox = QtWidgets.QVBoxLayout(about)
        logo_filename = "logod.png" if self.dark_mode else "logo.png"
        logo = PngLogo(os.path.join(ICONS_DIR, logo_filename), size=80)
        vbox.addWidget(logo, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        label = QtWidgets.QLabel("InterCalculator\nVersion 1.0\nBy Nilton Perim")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(label)
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(about.accept)
        vbox.addWidget(close_btn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        about.exec()

    def update_menu_icon(self):
        icon_name = "dmenu.png" if self.dark_mode else "lmenu.png"
        png_path = os.path.join(ICONS_DIR, icon_name)
        size = 50
        pixmap = QtGui.QPixmap(png_path)
        icon = QtGui.QIcon(pixmap.scaled(size, size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation))
        self.menu_btn.setIcon(icon)

    def on_toggle_mode(self):
        self.dark_mode = not self.dark_mode
        self.update_menu_icon()
        logo_filename = "logod.png" if self.dark_mode else "logo.png"
        for i in range(self.centralWidget().layout().count()):
            item = self.centralWidget().layout().itemAt(i)
            widget = item.widget()
            if isinstance(widget, PngLogo):
                widget.setPixmap(widget.get_png_pixmap(os.path.join(ICONS_DIR, logo_filename), 150))
        if self.dark_mode:
            QtWidgets.QApplication.instance().setStyleSheet("""
                QWidget { background-color: #232629; color: #f0f0f0; }
                QLineEdit { background: #232629; color: #f0f0f0; }
                QPushButton { background: #333; color: #f0f0f0; border: 1px solid #444; }
            """)
        else:
            QtWidgets.QApplication.instance().setStyleSheet("")