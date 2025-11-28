from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QDir
from PySide6.QtGui import QDoubleValidator

from util.json_reader import JSONReader
from util.json_writer import JSONWriter
from util.params import Params
import json

class ParameterInput(QWidget):
    def __init__(self):
        super().__init__()

        graph_data = None

        self.file_name = None

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        current_graph_label = QLabel(alignment=Qt.AlignmentFlag.AlignLeft)
        current_graph_label.setText("Untitled Graph")

        self.reset_button = QPushButton()
        self.reset_button.setText("⌂")

        saved_graph_label = QLabel(alignment=Qt.AlignmentFlag.AlignRight)
        saved_graph_label.setText("⚠There are unsaved changes")

        label_layout = QHBoxLayout()
        label_layout.addWidget(QLabel(alignment=Qt.AlignmentFlag.AlignLeft, text = "Current Graph: "))
        label_layout.addWidget(current_graph_label)
        label_layout.addStretch(1)
        label_layout.addWidget(saved_graph_label)
        label_layout.addWidget(self.reset_button)
        
        main_layout.addLayout(label_layout)

        def new_changes():
            saved_graph_label.setText("⚠There are unsaved changes")

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
        self.v_input.textChanged.connect(new_changes) 

        self.theta_slider = QSlider(Qt.Horizontal)
        self.theta_slider.setRange(-90, 90)
        self.theta_slider.setValue(0)
        self.theta_label = add_row(f"Vertical launch angle θ (°): {self.theta_slider.value()}", self.theta_slider)
        self.theta_slider.valueChanged.connect(
            lambda val: self.theta_label.setText(f"Vertical launch angle θ (°): {val}")
        )
        self.theta_slider.valueChanged.connect(new_changes)

        self.azimuthal_slider = QSlider(Qt.Horizontal)
        self.azimuthal_slider.setRange(-180, 180)
        self.azimuthal_label = add_row(f"Azimuthal angle (°): {self.azimuthal_slider.value()}", self.azimuthal_slider)
        self.azimuthal_slider.valueChanged.connect(
            lambda val: self.azimuthal_label.setText(f"Azimuthal angle (°): {val}")
        )
        self.azimuthal_slider.valueChanged.connect(new_changes)

        self.g_input = QLineEdit(text="9.81")
        self.g_input.setValidator(float_validator)
        add_row("Gravitational acceleration g (m/s²):", self.g_input)
        self.g_input.textChanged.connect(new_changes)

        self.t_start_input = QLineEdit(text="0") 
        self.t_start_input.setValidator(float_validator)
        self.t_start_input.textChanged.connect(new_changes) 
        self.t_end_input = QLineEdit(text="3") 
        self.t_end_input.setValidator(float_validator) 
        self.t_end_input.textChanged.connect(new_changes) 
        t_layout = QHBoxLayout() 
        t_layout.addWidget(QLabel("Time array t [start, end] (s):")) 
        t_layout.addWidget(self.t_start_input) 
        t_layout.addWidget(QLabel("to")) 
        t_layout.addWidget(self.t_end_input) 
        main_layout.addLayout(t_layout)

        self.x0_input = QLineEdit()
        self.x0_input.setValidator(float_validator)
        self.x0_input.textChanged.connect(new_changes) 
        add_row("Initial X-coordinate x0:", self.x0_input)

        self.y0_input = QLineEdit()
        self.y0_input.setValidator(float_validator)
        self.y0_input.textChanged.connect(new_changes) 
        add_row("Initial Y-coordinate y0:", self.y0_input)

        self.z0_input = QLineEdit()
        self.z0_input.setValidator(float_validator)
        self.z0_input.textChanged.connect(new_changes) 
        add_row("Initial Z-coordinate z0:", self.z0_input)

        def get_json_file():
            file_name = None
            global graph_data
            dialog = QFileDialog()
            dialog.setDirectory("./params")
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setFilter(QDir.Files)
            dialog.setAcceptMode(QFileDialog.AcceptOpen)
            dialog.setNameFilter("JSON Files (*.json)")


            if dialog.exec_():
                file_name = dialog.selectedFiles()

                if file_name[0].endswith('.json'):
                    json_reader = JSONReader(file_name[0])
                    graph_data = json_reader.params
                    self.v_input.setText(str(graph_data.velocity))
                    self.theta_slider.setValue(graph_data.theta)
                    self.azimuthal_slider.setValue(graph_data.azimuthal_angle)
                    self.g_input.setText(str(graph_data.g))
                    self.t_start_input.setText(str(graph_data.t_start))
                    self.t_end_input.setText(str(graph_data.t_end))
                    self.x0_input.setText(str(graph_data.x0))
                    self.y0_input.setText(str(graph_data.y0))
                    self.z0_input.setText(str(graph_data.z0))



                else:
                    pass

            if file_name:
                self.file_name = file_name[0]
                current_graph_label.setText(self.file_name.split("/")[-1].split(".")[0])
                saved_graph_label.setText("✓Saved")

        def save_json_file():
            if self.v_input.text() and self.g_input.text() and self.t_start_input.text() and self.t_end_input.text() and self.x0_input.text() and self.y0_input.text() and self.z0_input.text():
                data = Params(
                        float(self.v_input.text()),
                        float(self.theta_slider.value()),
                        float(self.azimuthal_slider.value()),
                        float(self.g_input.text()),
                        float(self.t_start_input.text()),
                        float(self.t_end_input.text()),
                        float(self.x0_input.text()),
                        float(self.y0_input.text()),
                        float(self.z0_input.text())
                    )
                if not self.file_name:
                    save_json_file_as(data)
                else:
                    json_writer = JSONWriter(self.file_name, data)
                    saved_graph_label.setText("✓Saved")

        def save_json_file_as(data: Params):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "./params", "JSON Files(*.json)", options = options)
            if file_name:
                json_writer = JSONWriter(file_name, data)
                self.file_name = file_name
                current_graph_label.setText(self.file_name.split("/")[-1].split(".")[0])
                saved_graph_label.setText("✓Saved")


        def new_graph():
            self.file_name = None
            current_graph_label.setText("Untitled Graph")



        self.h_button_layout = QHBoxLayout()

        self.open_param_button = QPushButton()
        self.open_param_button.setText("Open Existing Param File")
        self.open_param_button.clicked.connect(get_json_file)


        self.save_param_button = QPushButton()
        self.save_param_button.setText("Save Param File")
        self.save_param_button.clicked.connect(save_json_file)

        self.new_graph_button = QPushButton()
        self.new_graph_button.setText("New Graph")
        self.new_graph_button.clicked.connect(new_graph)




        self.h_button_layout.addWidget(self.open_param_button)
        self.h_button_layout.addWidget(self.save_param_button)
        self.h_button_layout.addWidget(self.new_graph_button)
        
        main_layout.addLayout(self.h_button_layout)
        
