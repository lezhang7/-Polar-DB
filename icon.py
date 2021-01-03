import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Communicate(QObject):
    closeApp = pyqtSignal()
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI() #界面绘制交给这个方法
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.btn1=QPushButton('按钮1',self)
        self.btn1.setToolTip('这是一个按钮')
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(50,50)

        self.btn2 = QPushButton('按钮2', self)
        self.btn2.setToolTip('这是一个按钮')
        self.btn2.resize(self.btn1.sizeHint())
        self.btn2.move(750, 50)


        self.le = QLineEdit(self) #文本框
        self.le.move(130, 22)

        self.btn1.clicked.connect(self.showDialog)
        #btn2.clicked.connect(self.buttonClicked)



        self.center()
        self.resize(1500,1000)#窗口位置和大小

        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('27.png'))
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

    def showDialog(self):

        text1, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        text2, ok = QInputDialog.getText(self, 'Input Dialog',
                                         'Enter your name:')
        if ok:
            self.le.setText(str(text1))
    def center(self):

        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "确定退出教师管理数据库系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=='__main__':
    """
    这个例子是OOP风格
    每个界面都要有两个必须的实例，一是QApplication的实例，二是QWidget的实例
    对于窗口的参数设定，在QWidget实例中修改
    可以创建一个继承了QWidget的子类，所有参数修改都在该类实例创建的初始化函数中实现
    """
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

