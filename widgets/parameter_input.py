from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator

class ParameterInput(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        float_validator = QDoubleValidator()
        float_validator.setNotation(QDoubleValidator.StandardNotation)

        def add_row(label_text, widget):
            row = QHBoxLayout()
            label = QLabel(label_text)
            label.setFixedWidth(220)
            row.addWidget(label)
            row.addWidget(widget, 1)
            main_layout.addLayout(row)
            return label

        self.v_input = QLineEdit()
        self.v_input.setValidator(float_validator)
        add_row("Initial velocity v (m/s):", self.v_input)

        self.theta_slider = QSlider(Qt.Horizontal)
        self.theta_slider.setRange(-90, 90)
        self.theta_slider.setValue(0)
        self.theta_label = add_row(f"Vertical launch angle θ (°): {self.theta_slider.value()}", self.theta_slider)
        self.theta_slider.valueChanged.connect(
            lambda val: self.theta_label.setText(f"Vertical launch angle θ (°): {val}")
        )

        self.azimuthal_slider = QSlider(Qt.Horizontal)
        self.azimuthal_slider.setRange(-180, 180)
        self.azimuthal_label = add_row(f"Azimuthal angle (°): {self.azimuthal_slider.value()}", self.azimuthal_slider)
        self.azimuthal_slider.valueChanged.connect(
            lambda val: self.azimuthal_label.setText(f"Azimuthal angle (°): {val}")
        )

        self.g_input = QLineEdit(text="9.81")
        self.g_input.setValidator(float_validator)
        add_row("Gravitational acceleration g (m/s²):", self.g_input)

        self.t_start_input = QLineEdit(text="0") 
        self.t_start_input.setValidator(float_validator) 
        self.t_end_input = QLineEdit(text="3") 
        self.t_end_input.setValidator(float_validator) 
        t_layout = QHBoxLayout() 
        t_layout.addWidget(QLabel("Time array t [start, end] (s):")) 
        t_layout.addWidget(self.t_start_input) 
        t_layout.addWidget(QLabel("to")) 
        t_layout.addWidget(self.t_end_input) 
        main_layout.addLayout(t_layout)

        self.x0_input = QLineEdit()
        self.x0_input.setValidator(float_validator)
        add_row("Initial X-coordinate x0:", self.x0_input)

        self.y0_input = QLineEdit()
        self.y0_input.setValidator(float_validator)
        add_row("Initial Y-coordinate y0:", self.y0_input)

        self.z0_input = QLineEdit()
        self.z0_input.setValidator(float_validator)
        add_row("Initial Z-coordinate z0:", self.z0_input)

