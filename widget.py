import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget ,QPushButton ,QVBoxLayout , QMainWindow
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
import psutil


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.myLayout = QVBoxLayout()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.initLabelCloc()
        #self.initButton()
        self.initLabelProcessorUse()
        self.initLabelRamUse()
        self.initLabelDiskUse()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()
        self.setGeometry(100, 100, 300, 300) 

        

        #widget = QWidget()
        #widget.setLayout(self.myLayout)
        #self.setCentralWidget(widget)

    def update_time(self):
        self.labelClocl.setText(QTime.currentTime().toString("HH:mm:ss"))
        self.labelPUse.setText("CPU :"  + str(psutil.cpu_percent()) + "%")
        self.labelRUse.setText("RAM :" + str(psutil.virtual_memory().percent) +"%" )
        self.labelDUse.setText("DISK:" + str(psutil.disk_usage('/').percent) +"%")

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.old_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()


    def clickButton(self, event):
        #self.labelClocl.setFont(QFont("Arial", 20, QFont.Bold))
        print("psutil.cpu_count()" + str(psutil.cpu_count()))
        print("psutil.cpu_percent() " + str(psutil.cpu_percent()))
        print("psutil.virtual_memory()" + str(psutil.virtual_memory().percent))        
        print("psutil.disk_usage('/')" + str(psutil.disk_usage('/').percent))

    def initButton(self):
        self.button = QPushButton(' try button ' , self)
        self.button.clicked.connect(self.clickButton)
        self.button.setGeometry(50,50,100,20)

    def initLabelCloc(self):
        self.labelClocl = QLabel(self)
        self.labelClocl.setFont(QFont("Arial", 40, QFont.Bold))
        self.labelClocl.setStyleSheet("color: white;")
        self.labelClocl.setAlignment(Qt.AlignCenter)

    def initLabelProcessorUse(self):
        self.labelPUse = QLabel(self)
        self.labelPUse.setFont(QFont("Arial", 20, QFont.Bold))
        self.labelPUse.setStyleSheet("color: white;")
        self.labelPUse.setAlignment(Qt.AlignCenter)
        self.labelPUse.setGeometry(0,100,200,30)
        self.labelPUse.setText("CPU : 50" )

    def initLabelRamUse(self):
        self.labelRUse = QLabel(self)
        self.labelRUse.setFont(QFont("Arial", 20, QFont.Bold))
        self.labelRUse.setStyleSheet("color: white;")
        self.labelRUse.setAlignment(Qt.AlignCenter)
        self.labelRUse.setGeometry(0,150,200,30)
        self.labelRUse.setText("RAM :" )

    def initLabelNetUse(self):
        self.labelNUse = QLabel(self)
        self.labelNUse.setFont(QFont("Arial", 20, QFont.Bold))
        self.labelNUse.setStyleSheet("color: white;")
        self.labelNUse.setAlignment(Qt.AlignCenter)
        self.labelNUse.setGeometry(0,150,200,30)
        self.labelNUse.setText("RAM :" )

    def initLabelDiskUse(self):
        self.labelDUse = QLabel(self)
        self.labelDUse.setFont(QFont("Arial", 20, QFont.Bold))
        self.labelDUse.setStyleSheet("color: white;")
        self.labelDUse.setAlignment(Qt.AlignCenter)
        self.labelDUse.setGeometry(0,200,200,30)
        self.labelDUse.setText("DISK:" )

if __name__ == "__main__":
    print("main if")
    app = QApplication(sys.argv)
    appWidget = Widget()
    appWidget.show()
    sys.exit(app.exec_())
