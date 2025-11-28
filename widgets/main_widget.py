import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSplitter
from PySide6.QtCore import Qt

from widgets.visualizer import Visualizer
from widgets.parameter_input import ParameterInput

class MainWidget(QWidget):
    def __init__(self, win_size: tuple[float, float]):
        super().__init__()
        self.win_size = win_size

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        splitter = QSplitter(Qt.Vertical, self)

        self.visualizer = Visualizer()
        splitter.addWidget(self.visualizer)

        self.param_input = ParameterInput()
        splitter.addWidget(self.param_input)

        total_height = self.win_size[1]
        splitter.setSizes([int(total_height * 2 / 3), int(total_height * 1 / 3)])
        main_layout.addWidget(splitter)

        self.param_input.v_input.textChanged.connect(self.auto_update)
        self.param_input.theta_slider.valueChanged.connect(self.auto_update)
        self.param_input.azimuthal_slider.valueChanged.connect(self.auto_update)
        self.param_input.g_input.textChanged.connect(self.auto_update)
        self.param_input.t_start_input.textChanged.connect(self.auto_update)
        self.param_input.t_end_input.textChanged.connect(self.auto_update)
        self.param_input.x0_input.textChanged.connect(self.auto_update)
        self.param_input.y0_input.textChanged.connect(self.auto_update)
        self.param_input.z0_input.textChanged.connect(self.auto_update)
        self.param_input.reset_button.pressed.connect(self.reset_visualizer)

    def auto_update(self):
        try:
            required_fields = [
                self.param_input.v_input,
                self.param_input.g_input,
                self.param_input.t_start_input,
                self.param_input.t_end_input,
                self.param_input.x0_input,
                self.param_input.y0_input,
                self.param_input.z0_input,
            ]
            if any(field.text() == "" for field in required_fields):
                return

            v = float(self.param_input.v_input.text())
            theta = self.param_input.theta_slider.value()
            azimuth = self.param_input.azimuthal_slider.value()
            g = float(self.param_input.g_input.text())
            t_start = float(self.param_input.t_start_input.text())
            t_end = float(self.param_input.t_end_input.text())
            t_range = [t_start, t_end]
            x0 = float(self.param_input.x0_input.text())
            y0 = float(self.param_input.y0_input.text())
            z0 = float(self.param_input.z0_input.text())

            self.visualizer.update_plot(v, theta, azimuth, g, t_range, x0, y0, z0)

        except Exception as e:
            pass


    def reset_visualizer(self):
        self.visualizer.w.reset()
        self.visualizer.w.opts['distance'] = 40


