from PySide6 import QtWidgets, QtGui, QtCore

class PngButton(QtWidgets.QPushButton):
    def __init__(self, png_path, label_value, callback):
        super().__init__()
        self.png_path = png_path
        self.label_value = label_value
        self.setFixedSize(80, 80)
        self.setIcon(self.get_png_icon(png_path))
        self.setIconSize(QtCore.QSize(80, 80))
        self.clicked.connect(lambda: callback(self))

    def get_png_icon(self, png_path):
        pixmap = QtGui.QPixmap(png_path)
        return QtGui.QIcon(pixmap.scaled(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation))

class PngLogo(QtWidgets.QLabel):
    def __init__(self, png_path, size=100):
        super().__init__()
        self.setFixedSize(size, size)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setPixmap(self.get_png_pixmap(png_path, size))

    def get_png_pixmap(self, png_path, size):
        pixmap = QtGui.QPixmap(png_path)
        return pixmap.scaled(size, size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)