from PySide6.QtWidgets import QWidget, QPushButton, QComboBox, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import os


class GraphWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle('Temperature Graphs')
        self.setGeometry(150, 150, 750, 520)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(20, 65, 550, 435)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(20, 15, 550, 40)

        self.body_combo = QComboBox(self)
        self.body_combo.setGeometry(585, 65, 145, 35)
        self.body_combo.addItems(['Body 1', 'Body 2'])

        self.draw_button = QPushButton('Draw', self)
        self.draw_button.setGeometry(585, 115, 145, 38)
        self.draw_button.setObjectName('primaryBtn')
        self.draw_button.clicked.connect(self.draw_graph)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setGeometry(585, 165, 145, 38)
        self.clear_button.setObjectName('secondaryBtn')
        self.clear_button.clicked.connect(self.clear_graph)

        self.export_button = QPushButton('Export to CSV', self)
        self.export_button.setGeometry(585, 215, 145, 38)
        self.export_button.setObjectName('secondaryBtn')
        self.export_button.clicked.connect(self.export_csv)

        qss_path = os.path.join(os.path.dirname(__file__), 'style.qss')
        with open(qss_path, 'r') as f:
            self.setStyleSheet(f.read())

        self.clear_graph()

    def draw_graph(self):
        times = self.main_window.time_history
        if len(times) == 0:
            return

        ax = self.ax
        if self.body_combo.currentText() == 'Body 1':
            ax.plot(times, self.main_window.body1_temp_history, color='#dc2626', linewidth=2, label='Body 1')
        else:
            ax.plot(times, self.main_window.body2_temp_history, color='#2563eb', linewidth=2, label='Body 2')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_title('Body Temperatures Over Time')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Temperature (°C)')
        ax.legend(frameon=False)

        self.figure.tight_layout(pad=0.8)
        self.canvas.draw()

    def clear_graph(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.set_title('Body Temperatures Over Time')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Temperature (°C)')
        self.figure.tight_layout(pad=0.8)
        self.canvas.draw()

    def export_csv(self):
        times = self.main_window.time_history
        if len(times) == 0:
            return

        filename, _ = QFileDialog.getSaveFileName(self, 'Export Results to CSV', 'heat_transfer_results.csv', 'CSV Files (*.csv)')
        if not filename:
            return

        t1_list = self.main_window.body1_temp_history
        t2_list = self.main_window.body2_temp_history

        with open(filename, 'w', encoding='utf-8-sig') as f:
            f.write('Time (s),Body 1 Temperature (°C),Body 2 Temperature (°C)\n')
            for i in range(len(times)):
                f.write(f'{times[i]:.2f},{t1_list[i]:.2f},{t2_list[i]:.2f}\n')

        os.startfile(filename)