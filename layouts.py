from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Checkboxes yayy")
        self.resize(1280, 720)

        stacked = QStackedLayout()

        stacked.addWidget(QLabel("Stuff 1"))
        stacked.addWidget(QLabel("Stuff 2"))
        stacked.addWidget(QLabel("Stuff 3"))
        stacked.addWidget(QLabel("Stuff 4"))
# 1-2-3-4
        widget = QWidget()
        widget.setLayout(stacked)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
