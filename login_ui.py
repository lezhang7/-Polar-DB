
import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import *
from main_window import Ui_Form
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt
class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.Password_root= "admin"
        self.UserName_root= "admin"
        self.login_status=""
        self.initUI()

    def initUI(self):
        """
        初始化UI
        :return:
        """
        self.setObjectName("loginWindow")
        self.setStyleSheet('#loginWindow{background-color:white}')
        self.setFixedSize(650, 400)
        self.setWindowTitle("教学信息管理系统登录")
        self.setWindowIcon(QIcon('static/logo_title.png'))

        self.text = "教学管理系统"

        # 添加顶部logo图片
        pixmap = QPixmap("2.jpg")
        scaredPixmap = pixmap.scaled(650, 140)
        label = QLabel(self)
        label.setPixmap(scaredPixmap)

        # 绘制顶部文字
        lbl_logo = QLabel(self)
        lbl_logo.setText(self.text)
        lbl_logo.setStyleSheet("QWidget{color:white;font-weight:600;background: transparent;font-size:30px;}")
        lbl_logo.setFont(QFont("Microsoft YaHei"))
        lbl_logo.move(250, 50)
        lbl_logo.setAlignment(Qt.AlignCenter)
        lbl_logo.raise_()

        # 登录表单内容部分
        login_widget = QWidget(self)
        login_widget.move(0, 140)
        login_widget.setGeometry(0, 140, 650, 260)

        hbox = QHBoxLayout()
        # 添加左侧logo
        logolb = QLabel(self)
        logopix = QPixmap("fudan.jpg")
        logopix_scared = logopix.scaled(150, 150)
        logolb.setPixmap(logopix_scared)
        logolb.setAlignment(Qt.AlignCenter)
        hbox.addWidget(logolb, 1)
        # 添加右侧表单
        fmlayout = QFormLayout()
        self.lbl_workerid = QLabel("用户名")
        self.lbl_workerid.setFont(QFont("Microsoft YaHei"))
        self.led_workerid = QLineEdit()
        self.led_workerid.setFixedWidth(270)
        self.led_workerid.setFixedHeight(38)

        self.lbl_pwd = QLabel("密码")
        self.lbl_pwd.setFont(QFont("Microsoft YaHei"))
        self.led_pwd = QLineEdit()
        self.led_pwd.setEchoMode(QLineEdit.Password)
        self.led_pwd.setFixedWidth(270)
        self.led_pwd.setFixedHeight(38)

        btn_login = QPushButton("登录")
        btn_login.setFixedWidth(270)
        btn_login.setFixedHeight(40)
        btn_login.setFont(QFont("Microsoft YaHei"))
        btn_login.setObjectName("login_btn")
        btn_login.setStyleSheet("#login_btn{background-color:#2c7adf;color:#fff;border:none;border-radius:4px;}")
        btn_login.clicked.connect(self.Login)

        fmlayout.addRow(self.lbl_workerid, self.led_workerid)
        fmlayout.addRow(self.lbl_pwd, self.led_pwd)
        fmlayout.addWidget(btn_login)
        hbox.setAlignment(Qt.AlignCenter)
        # 调整间距
        fmlayout.setHorizontalSpacing(20)
        fmlayout.setVerticalSpacing(12)

        hbox.addLayout(fmlayout, 2)

        login_widget.setLayout(hbox)
        self.setWindowTitle('登录')
        self.setWindowIcon(QIcon('1.png'))
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def messageDialog_fail(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '登陆失败', '账号或密码错误')
        msg_box.exec_()
    def messageDialog_success(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '登录成功', '进入教师系统，全部功能开放')
        my.settitle_teacher()

        my.show()
        self.close()
        msg_box.exec_()
    def messageDialog_success_t(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '登录成功', '进入学生系统,部分功能受限')
        my.settitle_student()
        my.show()
        self.close()
        msg_box.exec_()
    def Login(self):
        if (self.led_workerid.text() == self.UserName_root and self.led_pwd.text() == self.Password_root):
            self.login_status="admin"
            self.messageDialog_success()

        elif (self.led_workerid.text() == "" and self.led_pwd.text() == ""):
            self.led_workerid.setText("")
            self.led_pwd.setText("")
            self.login_status="teacher"
            self.messageDialog_success_t()
        else :
            self.led_workerid.setText("")
            self.led_pwd.setText("")
            self.login_status=""
            self.messageDialog_fail()
import matplotlib.pyplot as plt
#coding:utf-8
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

class Mywindow(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model='s'
        self.printfall('学生')
        #美化窗口
        self.setWindowIcon(QIcon('fudan.jpg'))



        #设置堆叠布局
        self.qsl=QStackedLayout(self.frame_2)
        self.teacher=Teacher()
        self.courses=xuanke()
        self.student=Student()

        self.qsl.addWidget(self.student)
        self.qsl.addWidget(self.teacher)
        self.qsl.addWidget(self.courses)

        #设置信号
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.pushButton_11.clicked.connect(self.btnPress11_Clicked)
        self.pushButton_12.clicked.connect(self.btnPress12_Clicked)
        self.pushButton_13.clicked.connect(self.btnPress13_Clicked)
        self.pushButton_14.clicked.connect(self.quit)
        self.courses.shuru_text1.editingFinished.connect(self.printfall3)
        self.courses.btn1.clicked.connect(self.printfall2) #选课系统中点选课或者退课时对左边的框进行刷新
        self.courses.btn2.clicked.connect(self.printfall2)
    def checkinlist(self,i,id):
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')
        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                if i== 'cid':
                    sql = "SELECT * FROM `c`"
                elif i == 'sid':
                    sql = "SELECT * FROM `s`"
                elif i == 'tid':
                    sql = "SELECT * FROM `t`"
                cursor.execute(sql)
                list=[]
                for result in cursor:
                    # 输出查询结果
                    #print(result[0])
                    list.append(result[0])
                #print('含有如下id：',list)
                if id in list:
                    f=1
                else:
                    f=0
        finally:
            connection.close()
            if f==1:
                return True
            else:
                return False
    def quit(self):
        self.close()
        ex.show()
    def btnPress11_Clicked(self):
        self.textBrowser.clear()
        self.printfall('学生')
        self.qsl.setCurrentIndex(0) #student
    def btnPress12_Clicked(self):#点到教师信息左边显示为教师
        self.textBrowser.clear()
        self.printfall('教师')
        self.qsl.setCurrentIndex(1) #teacher
    def btnPress13_Clicked(self): #点到选课系统，使左边框显示为S
        self.textBrowser.clear()
        self.printfall('学生')
        self.qsl.setCurrentIndex(2) #courses
    def settitle_student(self):
        self.setWindowTitle('学生界面')
        self.pushButton_12.setEnabled(False)
        self.student.btn2.setEnabled(False)
        self.student.btn3.setEnabled(False)
    def settitle_teacher(self):
        self.setWindowTitle('教师界面')
        self.pushButton_12.setEnabled(True)
        self.student.btn2.setEnabled(True)
        self.student.btn3.setEnabled(True)
    def selectionchange(self, i):
        # 标签用来显示选中的文本
        # currentText()：返回选中选项的文本
        #print('Items in the list are:')
        # 输出选项集合中每个选项的索引与对应的内容
        # count()：返回选项集合中的数目
        self.textBrowser.clear()
        self.printfall(self.comboBox.currentText())
    def printfall2(self):
        self.textBrowser.clear()
        self.printfall('学生成绩')
    def printfall1(self):
        self.textBrowser.clear()
        self.printfall('学生成绩')
    def printfall3(self):
        self.textBrowser.clear()
        self.printfall('学生')
    def printfall(self,i):
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')

        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                if i == '课程':
                    sql = "SELECT * FROM `c`"
                    title = "%-14s%-14s%-14s%-14s" % ('课程号', '课程名名', '教师','课程类型')
                    self.printf(title)
                elif i == '学生':
                    sql = "SELECT * FROM `s`"
                    title = "%-14s%-14s%-14s"%('学号','姓名','性别')
                    self.printf(title)
                elif i == '教师':
                    sql = "SELECT * FROM `t`"
                    title = "%-15s%-15s%-15s" % ('教师号', '教职', '教师名')
                    self.printf(title)
                elif i == '学生成绩':
                    sql = "SELECT * FROM `sc`"
                    title = "%-12s%-12s%-12s" % ('学生号', '课程号', '成绩')
                    self.printf(title)


                cursor.execute(sql)
                for result in cursor:
                    # 输出查询结果
                    r = [self.pro_str(s) for s in result]
                    self.printf(' '.join(r))
        finally:
            connection.close()
    def pro_str(self,s):
        s = str(s)
        return "%-15s" % s

    def printf(self, mypstr):
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        #self.cursor = self.tetxBrowser.textCursor()
        #self.tetxBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
class Student(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.shuru=QtWidgets.QLabel("输入学号")
        self.shuru_text=QtWidgets.QLineEdit()
        self.shuru_text.setPlaceholderText('学号全为数字')
        self.btn1=QtWidgets.QPushButton("查询成绩信息")
        self.btn2=QtWidgets.QPushButton("添加学生信息")
        self.btn3=QtWidgets.QPushButton("删除学生信息")
        self.textBrowser = QtWidgets.QTextBrowser()
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.shuru)
        self.hbox.addWidget(self.shuru_text)
        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.btn1)
        self.hbox1.addWidget(self.btn2)
        self.hbox1.addWidget(self.btn3)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addWidget(self.textBrowser)
        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.btn1.clicked.connect(self.printfall)
        self.btn2.clicked.connect(self.addstudent)
        self.btn3.clicked.connect(self.dropstudent)
        self.show()
    def checkinlist(self,i,id):
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')
        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                if i== 'cid':
                    sql = "SELECT * FROM `c`"
                elif i == 'sid':
                    sql = "SELECT * FROM `s`"
                elif i == 'tid':
                    sql = "SELECT * FROM `t`"
                cursor.execute(sql)
                list=[]
                for result in cursor:
                    # 输出查询结果
                    #print(result[0])
                    list.append(result[0])
                #print('含有如下id：',list)
                if id in list:
                    f=1
                else:
                    f=0
        finally:
            connection.close()
            if f==1:
                return True
            else:
                return False
    def ceshi(self):
        print(int(self.shuru_text.text()))
    def dropstudent(self):
        try:
            sid, ok1 = QInputDialog.getText(self, '删除学生', '输入4数字学号')
            sid = int(sid)
            if not self.checkinlist('sid',sid):
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '系统中不存在该学号')
                msg_box.exec_()
                return
        except Exception:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '学号格式不正确请重新输入')
            msg_box.exec_()
            return
        if ok1:
            connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                         port=3306,
                                         user='lab_1506359621',
                                         passwd='19152398ed17_#@Aa',
                                         db='final_pj')
            try:
                with connection.cursor() as cursor:
                    # 以查询courses表为例
                    sql = "DELETE FROM `final_pj`.`s` WHERE `sid`=%d;" % sid
                    cursor.execute(sql)
                    connection.commit()
                    msg_box = QMessageBox(QMessageBox.Warning, '成功', '删除成功！刷新学生名单后可见')
                    msg_box.exec_()
            except Exception:
                # print(Exception)
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '添加失败')
                msg_box.exec_()
                connection.rollback()
                return
            finally:
                connection.close()
    def addstudent(self):
        items=('F','M')
        try:
            sid, ok1 = QInputDialog.getText(self, '添加学生', '输入4数字学号')
            sid=int(sid)
        except Exception:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '学号格式不正确请重新输入')
            msg_box.exec_()
            return
        sname,ok2= QInputDialog.getText(self, '添加学生', '输入学生姓名')
        sex, ok3 = QInputDialog.getItem(self, '添加学生', '选择性别',items,0,False)
        sex=str(sex)
        print(sid,sname,sex,type(sid),type(sname),type(sex))
        if ok1 and ok2 and ok3:
            connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                         port=3306,
                                         user='lab_1506359621',
                                         passwd='19152398ed17_#@Aa',
                                         db='final_pj')
            try:
                with connection.cursor() as cursor:
                    # 以查询courses表为例

                    sql = "INSERT INTO `final_pj`.`s` (`sid`,`sname`,`sex`) VALUES (%d,'%s','%s')" %(sid,sname,sex)
                    cursor.execute(sql)
                    connection.commit()
                    msg_box = QMessageBox(QMessageBox.Warning, '成功', '成功添加！刷新学生名单后可见')
                    msg_box.exec_()
            except Exception:
                #print(Exception)
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '添加失败')
                msg_box.exec_()
                connection.rollback()
                return
            finally:
                connection.close()
    def printfall(self):

        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')

        try:
            self.textBrowser.clear()
            with connection.cursor() as cursor:
                # 以查询courses表为例
                try:
                    id = int(self.shuru_text.text())
                except Exception:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '请先输入学号')
                    msg_box.exec_()
                    return
                if not self.checkinlist('sid',id):
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '系统中不存在该学号')
                    msg_box.exec_()
                    return
                #print(id)
                sql = "SELECT * FROM `sc` WHERE sid=%d"%id
                cursor.execute(sql)
                title = "%-8s%-11s%-14s" % ('学生号', '课程号', '成绩')
                self.printf(title)
                for result in cursor:
                    # 输出查询结果
                    r = [self.pro_str(s) for s in result]
                    self.printf(' '.join(r))
        except Exception:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '学号格式不正确请重新输入')
            msg_box.exec_()
            return
        finally:
            connection.close()
    def pro_str(self, s):
        s=str(s)
        return "%-12s"%s
    def printf(self, mypstr):
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        # self.cursor = self.tetxBrowser.textCursor()
        # self.tetxBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
class Teacher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.shuru=QtWidgets.QLabel("输入工号")
        self.shuru_text=QtWidgets.QLineEdit()
        self.btn1=QtWidgets.QPushButton("教师开课信息")
        self.btn2=QtWidgets.QPushButton("修改职称")
        self.btn3=QtWidgets.QPushButton("教师开课成绩分析")
        self.textBrowser = QtWidgets.QTextBrowser()

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.shuru)
        self.hbox.addWidget(self.shuru_text)
        self.hbox1=QHBoxLayout()
        self.hbox1.addWidget(self.btn1)
        self.hbox1.addWidget(self.btn3)
        self.hbox1.addWidget(self.btn2)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addWidget(self.textBrowser)


        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.btn1.clicked.connect(self.printfall_openclass)
        self.btn2.clicked.connect(self.changetitle)
        self.btn3.clicked.connect(self.classanalysis)
        self.show()
    def checkinlist(self,i,id):
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')
        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                if i== 'cid':
                    sql = "SELECT * FROM `c`"
                elif i == 'sid':
                    sql = "SELECT * FROM `s`"
                elif i == 'tid':
                    sql = "SELECT * FROM `t`"
                cursor.execute(sql)
                list=[]
                for result in cursor:
                    # 输出查询结果
                    #print(result[0])
                    list.append(result[0])
                #print('含有如下id：',list)
                if id in list:
                    f=1
                else:
                    f=0
        finally:
            connection.close()
            if f==1:
                return True
            else:
                return False
    def changetitle(self):
        items = ('教授', '副教授','研究员','讲师')
        try:
            tid, ok1 = QInputDialog.getText(self, '修改职称', '输入教师工号号')
            tid = int(tid)
            if not self.checkinlist('tid',tid):
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '该工号不在系统中')
                msg_box.exec_()
                return
        except Exception:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '工号格式不正确请重新输入')
            msg_box.exec_()
            return
        new, ok3 = QInputDialog.getItem(self, '修改职称', '选择修改后的职称', items, 0, False)
        print(tid, new, type(tid), type(new))
        if ok1  and ok3:
            connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                         port=3306,
                                         user='lab_1506359621',
                                         passwd='19152398ed17_#@Aa',
                                         db='final_pj')
            try:
                with connection.cursor() as cursor:
                    # 以查询courses表为例

                    sql = "UPDATE `final_pj`.`t` SET `title`='%s' WHERE `tid`=%d;" % (new,tid)
                    cursor.execute(sql)
                    connection.commit()
                    msg_box = QMessageBox(QMessageBox.Warning, '成功', '成功修改！刷新教师名单后可见')
                    msg_box.exec_()
            except Exception:
                # print(Exception)
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '修改职称失败')
                msg_box.exec_()
                connection.rollback()
                return
            finally:
                connection.close()
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % int(height))
    def classanalysis(self):
        """
        先链接查询该教师开课的课程名和平均分，然后通过matplotlib柱状图绘制出来
        :return:
        """
        cname=[]
        avg_score=[]
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')

        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                try:
                    id = int(self.shuru_text.text())
                except Exception:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '请先输入教师号')
                    msg_box.exec_()
                    return
                if not self.checkinlist('tid', id):
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '系统中没有该教师号')
                    msg_box.exec_()
                    return
                # print(id,type(id))

                sql = "SELECT c.cname,AVG(sc.score) FROM `c`,`sc` WHERE tid=%d AND c.cid=sc.cid GROUP BY sc.cid" % id
                cursor.execute(sql)

                for result in cursor:
                    # 输出查询结果
                    cname.append(result[0])
                    avg_score.append(result[1])
                #name_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                #num_list = [33, 44, 53, 16, 11, 17, 17, 10]
                if len(cname)==0:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有教师开设课程成绩记录')
                    msg_box.exec_()
                    return
                plt.close('all')
                plt.bar(cname,avg_score,fc='y')
                plt.ylim((0,100))
                for a, b in zip(cname, avg_score):
                    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
                plt.title('教师开设课程成绩分析')
                plt.show()
                print(cname,avg_score)

        finally:
            connection.close()
    def printfall_openclass(self):

        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')

        try:
            self.textBrowser.clear()
            with connection.cursor() as cursor:
                # 以查询courses表为例
                try:
                    id = int(self.shuru_text.text())
                except Exception:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '请先输入教师号')
                    msg_box.exec_()
                    return
                if id<200000 or id>300000:
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '教师号格式出错')
                    msg_box.exec_()
                    return
                if not self.checkinlist('tid',id):
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '系统中没有该教师号')
                    msg_box.exec_()
                    return
                #print(id,type(id))

                sql = "SELECT * FROM `c` WHERE tid=%d"%id
                cursor.execute(sql)
                title = "%-14s%-14s%-14s%-14s" % ('课程号', '课程名', '教师号','课程类型')
                self.printf(title)
                for result in cursor:
                    # 输出查询结果
                    r = [self.pro_str(s) for s in result]
                    self.printf(' '.join(r))
                    '''
        except Exception:
            print(Exception)
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '教师号格式不正确请重新输入')
            msg_box.exec_()
            return'''
        finally:
            connection.close()
    def pro_str(self, s):
        s = str(s)
        return "%-15s" % s
    def printf(self, mypstr):
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        #self.cursor = self.tetxBrowser.textCursor()
        #self.tetxBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
class xuanke(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.shuru1=QtWidgets.QLabel("学号")
        self.shuru_text1=QtWidgets.QLineEdit()
        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.shuru1)
        self.hbox1.addWidget(self.shuru_text1)

        self.shuru2 = QtWidgets.QLabel("课程号")
        self.shuru_text2 = QtWidgets.QLineEdit()
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.shuru2)
        self.hbox2.addWidget(self.shuru_text2)

        self.btn1=QtWidgets.QPushButton("选课")
        self.btn2 = QtWidgets.QPushButton("退课")
        self.btn3= QtWidgets.QPushButton("查看所有课程成绩统计情况")
        self.hbox3=QHBoxLayout()
        self.hbox3.addWidget(self.btn1)
        self.hbox3.addWidget(self.btn2)
        self.textBrowser = QtWidgets.QTextBrowser()
        self.vbox=QVBoxLayout()
        self.vbox.addWidget(self.btn3)
        self.vbox.addWidget(self.textBrowser)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.printfall('课程')
        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.btn1.clicked.connect(self.xuanke)
        self.btn2.clicked.connect(self.tuike)
        self.btn3.clicked.connect(self.analysis)
        self.show()
    def printfall(self,i):
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')


        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                if i == '课程':
                    sql = "SELECT * FROM `c`"
                    title = "%-14s%-14s%-14s%-14s" % ('课程号', '课程名名', '教师','课程类型')
                    self.printf(title)
                elif i == '学生':
                    sql = "SELECT * FROM `s`"
                    title = "%-14s%-14s%-14s"%('学号','姓名','性别')
                    self.printf(title)
                elif i == '教师':
                    sql = "SELECT * FROM `t`"
                    title = "%-15s%-15s%-15s" % ('教师号', '教职', '教师名')
                    self.printf(title)
                elif i == '学生成绩':
                    sql = "SELECT * FROM `sc`"
                    title = "%-12s%-12s%-12s" % ('学生号', '课程号', '成绩')
                    self.printf(title)


                cursor.execute(sql)
                for result in cursor:
                    # 输出查询结果
                    r = [self.pro_str(s) for s in result]
                    self.printf(' '.join(r))
        finally:
            connection.close()
    def pro_str(self,s):
        s = str(s)
        return "%-15s" % s
    def printf(self, mypstr):
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        #self.cursor = self.tetxBrowser.textCursor()
        #self.tetxBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
    def checkinlist(self,i,id):
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')
        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                if i== 'cid':
                    sql = "SELECT * FROM `c`"
                elif i == 'sid':
                    sql = "SELECT * FROM `s`"
                elif i == 'tid':
                    sql = "SELECT * FROM `t`"
                cursor.execute(sql)
                list=[]
                for result in cursor:
                    # 输出查询结果
                    #print(result[0])
                    list.append(result[0])
                #print('含有如下id：',list)
                if id in list:
                    f=1
                else:
                    f=0
        finally:
            connection.close()
            if f==1:
                return True
            else:
                return False
    def xuanke(self):
        try:
            sid=self.shuru_text1.text()
            cid=self.shuru_text2.text()
            sid = int(sid)
            cid=int(cid)
            if not self.checkinlist('sid', sid):
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '该学号不在系统中')
                msg_box.exec_()
                return
            if not self.checkinlist('cid', cid):
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '课程号不在系统中')
                msg_box.exec_()
                return
            '''
            if sid < 1000 or sid > 9999:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '学号位数不对请重新输入')
                msg_box.exec_()
                return
            if cid<0 or cid >100:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '课程号位数不对请重新输入')
                msg_box.exec_()
                return
            '''
        except Exception:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '格式不正确请重新输入')
            msg_box.exec_()
            return
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')
        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例

                sql = "INSERT INTO `final_pj`.`sc` (`sid`,`cid`) VALUES (%d,'%d')" % (sid, cid)
                cursor.execute(sql)
                connection.commit()
                msg_box = QMessageBox(QMessageBox.Warning, '成功', '成功添加！刷新选课名单后可见')
                msg_box.exec_()
        except Exception:
            # print(Exception)
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '选课失败,该学生已经选该课程！')
            msg_box.exec_()
            connection.rollback()
            return
        finally:
            connection.close()
    def tuike(self):
        try:
            sid=self.shuru_text1.text()
            cid=self.shuru_text2.text()
            sid = int(sid)
            cid=int(cid)
            if not self.checkinlist('sid',sid):
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '该学号不在系统中')
                msg_box.exec_()
                return
            if not self.checkinlist('cid',cid):
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '课程号不在系统中')
                msg_box.exec_()
                return
            '''
            if sid < 1000 or sid > 9999:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '学号位数不对请重新输入')
                msg_box.exec_()
                return
            if cid<0 or cid >100:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '课程号位数不对请重新输入')
                msg_box.exec_()
                return
            '''
        except Exception:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '格式不正确请重新输入')
            msg_box.exec_()
            return
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')
        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例
                #DELETE FROM `final_pj`.`sc` WHERE `sid`=1001 AND `cid`=10;
                sql = "DELETE FROM `final_pj`.`sc` WHERE `sid`=%d AND `cid`=%d" % (sid, cid)
                cursor.execute(sql)
                connection.commit()
                msg_box = QMessageBox(QMessageBox.Warning, '成功', '退课成功！刷新选课名单后可见')
                msg_box.exec_()
        except Exception:
            # print(Exception)
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '退课失败')
            msg_box.exec_()
            connection.rollback()
            return
        finally:
            connection.close()
    def analysis(self):
        cname = []
        avg_score = []
        connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                                     port=3306,
                                     user='lab_1506359621',
                                     passwd='19152398ed17_#@Aa',
                                     db='final_pj')

        try:
            with connection.cursor() as cursor:
                # 以查询courses表为例

                # print(id,type(id))

                sql = "SELECT c.cname,AVG(sc.score) FROM `c`,`sc` WHERE c.cid=sc.cid GROUP BY c.cname"
                cursor.execute(sql)

                for result in cursor:
                    # 输出查询结果
                    cname.append(result[0])
                    score=round(result[1],2)
                    avg_score.append(score)
                # name_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                # num_list = [33, 44, 53, 16, 11, 17, 17, 10]
                plt.close('all')
                plt.bar(cname, avg_score, fc='y')
                plt.ylim((0, 100))
                for a, b in zip(cname, avg_score):
                    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
                plt.title('所有开设课程平均成绩统计情况')
                plt.show()

                print(cname, avg_score)

        finally:
            connection.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginForm()
    my = Mywindow()
    ex.show()

    #my.show()
    sys.exit(app.exec_())