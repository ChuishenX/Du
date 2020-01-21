#This File's name is reader.py
import urllib3, sys, os, getToken
from urllib.parse import urlencode
from PySide2.QtWidgets import *
from ui_read import Ui_MainWindow

class Read(QMainWindow,Ui_MainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.file = None
                self.txt = None
                self.voice = 0
                self.save = None
                self.token = getToken.getToken()
                self.create.clicked.connect(self.generate)
                self.play.clicked.connect(self.musicPlay)
                self.open.clicked.connect(self.select_file)
                self.show()
        
        def select_file(self):
                self.file, _ = QFileDialog.getOpenFileName(self,'选择你要读取的文件',"C:/","Text files (*.log *.txt)")
                if self.file:
                        with open(self.file) as f:
                                self.txt = f.read()
                self.textEdit.setText(self.txt)
                

        def generate(self):
                if self.choser.currentText():
                        if self.choser.currentText() == "度逍遥":
                                self.voice = 3
                        elif self.choser.currentText() == "度小娇":
                                self.voice = 5
                        elif self.choser.currentText() == "度小宇":
                                self.voice = 1
                        elif self.choser.currentText() == "度小美":
                                self.voice = 0
                        elif self.choser.currentText() == "度博文":
                                self.voice = 106
                        elif self.choser.currentText() == "度小萌":
                                self.voice = 111
                        elif self.choser.currentText() == "度小童":
                                self.voice = 110
                self.txt = self.textEdit.toPlainText()
                self.save, _ = QFileDialog.getSaveFileName(self,"保存路径","C:/","(*.mp3)")
                if self.txt:
                        http = urllib3.PoolManager()
                        r = http.request('POST', "https://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=FE-1C-79-57-C2-60&tok=%s&tex=%s&per=%s" % (self.token, self.txt, self.voice))
                        result = r.data
                        if not isinstance(result, dict):
                                with open(self.save, 'wb') as f:
                                        f.write(result)
                                        QMessageBox.information(self,"生成声音成功","生成声音成功")
                        else:
                                QMessageBox.warning(self,"生成失败，请重试","生成失败，请重试")
                else:
                        QMessageBox.warning(self,"请先选择文件或输入内容！","请先选择文件或输入内容！")
        def musicPlay(self):
                os.system(self.save)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Read()
    win.show()
    sys.exit(app.exec_())
