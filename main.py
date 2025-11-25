import os
import sys
import time
import signal

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from widgets.main_widget import MainWidget


signal.signal(signal.SIGINT, signal.SIG_DFL)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        self.setWindowTitle("Kinematic Simulator")
        self.control = MainWidget((self.window_width, self.window_height))
        self.setCentralWidget(self.control)

        logoPath = os.path.join(os.path.dirname(__file__), 'resources/images/logo.png')

        self.setWindowIcon(QPixmap(logoPath))


    def move_window_to_center(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())


if __name__ == '__main__':
    app = QApplication()

    logoPath = os.path.join(os.path.dirname(__file__), 'resources/images/logo.png')
    splash = QSplashScreen(QPixmap(logoPath))
    splash.show()
    app.processEvents()

    mw = MainWindow()

    def show_main():
        splash.finish(mw)
        mw.show()
        mw.move_window_to_center()

        QTimer.singleShot(2000, lambda: (
            mw.raise_(),
            mw.activateWindow(),
            mw.setWindowState(mw.windowState() | Qt.WindowActive)
        ))

    QTimer.singleShot(10, show_main)

    sys.exit(app.exec())



