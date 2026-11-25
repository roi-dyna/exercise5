from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDoubleSpinBox, QSlider
from PySide6.QtCore import Qt
import os
from About import AboutWindow
from GraphWindow import GraphWindow


class HeatTransfer(QWidget):
    def __init__(self):
        super().__init__()
        self.about_window = AboutWindow()
        self.graph_window = GraphWindow()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Heat Transfer Simulation')
        self.setGeometry(100, 100, 800, 440)

        self.start_button = QPushButton('Start', self)
        self.start_button.setGeometry(20, 20, 120, 35)
        self.start_button.setCheckable(True)
        self.start_button.setObjectName('primaryBtn')

        self.graphs_button = QPushButton('Graphs', self)
        self.graphs_button.setGeometry(155, 20, 120, 35)
        self.graphs_button.setObjectName('secondaryBtn')
        self.graphs_button.clicked.connect(self.show_graphs)

        self.about_button = QPushButton('About', self)
        self.about_button.setGeometry(660, 20, 120, 35)
        self.about_button.setObjectName('secondaryBtn')
        self.about_button.clicked.connect(self.show_about)

        self.body1_title = QLabel('Body 1', self)
        self.body1_title.setGeometry(90, 75, 140, 25)
        self.body1_title.setAlignment(Qt.AlignCenter)

        self.body1_box = QLabel('', self)
        self.body1_box.setGeometry(90, 105, 140, 150)
        self.body1_box.setObjectName('bodyBox')

        self.left_slider = QSlider(Qt.Vertical, self)
        self.left_slider.setGeometry(250, 105, 30, 150)
        self.left_slider.setRange(0, 200)
        self.left_slider.setValue(200)

        self.temp1_label = QLabel('Temp:', self)
        self.temp1_label.setGeometry(60, 275, 85, 30)
        self.left_temp_spin = QDoubleSpinBox(self)
        self.left_temp_spin.setGeometry(150, 275, 130, 30)
        self.left_temp_spin.setRange(0, 200)
        self.left_temp_spin.setValue(200)
        self.left_temp_spin.setSuffix(' °C')
        self.left_temp_spin.setReadOnly(True)

        self.mass1_label = QLabel('Mass:', self)
        self.mass1_label.setGeometry(60, 315, 85, 30)
        self.left_mass_spin = QDoubleSpinBox(self)
        self.left_mass_spin.setGeometry(150, 315, 130, 30)
        self.left_mass_spin.setRange(0.01, 100000)
        self.left_mass_spin.setValue(100)
        self.left_mass_spin.setSuffix(' kg')

        self.cap1_label = QLabel('Heat Cap:', self)
        self.cap1_label.setGeometry(60, 355, 85, 30)
        self.left_cap_spin = QDoubleSpinBox(self)
        self.left_cap_spin.setGeometry(150, 355, 130, 30)
        self.left_cap_spin.setRange(0.01, 100000)
        self.left_cap_spin.setValue(0.5)
        self.left_cap_spin.setSuffix(' J/kg*°C')


        self.k_label = QLabel('Conductivity (k):', self)
        self.k_label.setGeometry(325, 145, 150, 25)
        self.k_label.setAlignment(Qt.AlignCenter)

        self.k_spin = QDoubleSpinBox(self)
        self.k_spin.setGeometry(330, 175, 140, 30)
        self.k_spin.setRange(0.01, 100000)
        self.k_spin.setValue(5.0)
        self.k_spin.setSuffix(' J/s*°C')

        self.body2_title = QLabel('Body 2', self)
        self.body2_title.setGeometry(560, 75, 140, 25)
        self.body2_title.setAlignment(Qt.AlignCenter)

        self.body2_box = QLabel('', self)
        self.body2_box.setGeometry(560, 105, 140, 150)
        self.body2_box.setObjectName('bodyBox')

        self.right_slider = QSlider(Qt.Vertical, self)
        self.right_slider.setGeometry(515, 105, 30, 150)
        self.right_slider.setRange(0, 200)
        self.right_slider.setValue(20)

        self.temp2_label = QLabel('Temp:', self)
        self.temp2_label.setGeometry(515, 275, 85, 30)
        self.right_temp_spin = QDoubleSpinBox(self)
        self.right_temp_spin.setGeometry(605, 275, 135, 30)
        self.right_temp_spin.setRange(0, 200)
        self.right_temp_spin.setValue(20)
        self.right_temp_spin.setSuffix(' °C')
        self.right_temp_spin.setReadOnly(True)

        self.mass2_label = QLabel('Mass:', self)
        self.mass2_label.setGeometry(515, 315, 85, 30)
        self.right_mass_spin = QDoubleSpinBox(self)
        self.right_mass_spin.setGeometry(605, 315, 135, 30)
        self.right_mass_spin.setRange(0.01, 100000)
        self.right_mass_spin.setValue(100)
        self.right_mass_spin.setSuffix(' kg')

        self.cap2_label = QLabel('Heat Cap:', self)
        self.cap2_label.setGeometry(515, 355, 85, 30)
        self.right_cap_spin = QDoubleSpinBox(self)
        self.right_cap_spin.setGeometry(605, 355, 135, 30)
        self.right_cap_spin.setRange(0.01, 100000)
        self.right_cap_spin.setValue(0.5)
        self.right_cap_spin.setSuffix(' J/kg*°C')

        qss_path = os.path.join(os.path.dirname(__file__), 'style.qss')

        with open(qss_path, 'r') as f:
            self.setStyleSheet(f.read())

        self.left_slider.valueChanged.connect(self.left_temperature_changed)
        self.right_slider.valueChanged.connect(self.right_temperature_changed)

        self.left_temperature_changed()
        self.right_temperature_changed()

    def show_about(self):
        self.about_window.show()

    def show_graphs(self):
        self.graph_window.show()

    def update_body_color(self, box, temp):
        red = int((temp / 200) * 255)
        red = max(0, min(255, red))
        box.setStyleSheet(f'background-color: rgb({red}, 0, 0); border-radius: 12px; border: 2px solid #1e293b;')
        
    def left_temperature_changed(self):
        temp = self.left_slider.value()
        self.left_temp_spin.setValue(temp)
        self.update_body_color(self.body1_box, temp)

    def right_temperature_changed(self):
        temp = self.right_slider.value()
        self.right_temp_spin.setValue(temp)
        self.update_body_color(self.body2_box, temp)


if __name__ == '__main__':
    app = QApplication()
    window = HeatTransfer()
    window.show()
    app.exec()