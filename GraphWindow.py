from PySide6.QtWidgets import QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class GraphWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Temperature Graphs')
        self.setGeometry(150, 150, 750, 520)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(20, 65, 710, 435)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(20, 15, 710, 40)

    def update_graph(self, times, temps1, temps2):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.plot(times, temps1, color='#dc2626', linewidth=2, label='Body 1')
        ax.plot(times, temps2, color='#2563eb', linewidth=2, label='Body 2')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_title('Body Temperatures Over Time')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Temperature (°C)')
        ax.legend(frameon=False)

        self.figure.tight_layout(pad=0.8)
        self.canvas.draw()