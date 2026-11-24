from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Me')
        self.setGeometry(200, 200, 350, 510)
        self.setStyleSheet("background-color: #f4f6f9; font-family: Arial;")

        self.name_label = QLabel('Name: Roi Harris', self)
        self.name_label.setGeometry(25, 20, 300, 35)
        self.name_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")

        self.email_label = QLabel('Email: RoiHarris94@gmail.com', self)
        self.email_label.setGeometry(25, 60, 300, 25)
        self.email_label.setStyleSheet("font-size: 13px; color: #555555;")

        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/in/roi-harris-63805b265">My LinkedIn Profile</a>', self)
        self.linkedin_label.setGeometry(25, 90, 300, 25)
        self.linkedin_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.linkedin_label.setOpenExternalLinks(True)

        self.github_label = QLabel('<a href="https://github.com/roi-dyna/exercise4_grades">My GitHub Repository</a>', self)        
        self.github_label.setGeometry(25, 120, 300, 25)
        self.github_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.github_label.setOpenExternalLinks(True)

        self.pic_label = QLabel(self)
        self.pic_label.setGeometry(25, 160, 300, 300)
        self.pic_label.setStyleSheet("border: 2px solid #bdc3c7;")
        image = QPixmap('image.jpg').scaled(300, 300)
        self.pic_label.setPixmap(image)


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()