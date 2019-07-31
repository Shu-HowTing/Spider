'''
Function:
	有道翻译小爬虫
'''
import sys
import time
import random
import hashlib
import requests
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton


'''
Function:
	有道翻译类
'''
class youdao():
	def __init__(self):
		self.headers = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
						'Referer': 'http://fanyi.youdao.com/',
						'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
					}
		self.data = {
						'i': None,
						'client': 'fanyideskweb',
						'keyfrom': 'fanyi.web',
						'salt': None,
						'sign': None
					}
		self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
	def translate(self, word):
		t = str(time.time()*1000 + random.randint(1, 10))
		self.data['i'] = word
		self.data['salt'] = t
		sign = 'fanyideskweb' + word + t + '6x(ZHw]mwzX#u0V7@yfwK'
		self.data['sign'] = hashlib.md5(sign.encode('utf-8')).hexdigest()
		res = requests.post(self.url, headers=self.headers, data=self.data)
		return res.json()['translateResult']


'''
Function:
	简单的Demo
'''
class Demo(QWidget):
	def __init__(self, parent=None):
		super().__init__()
		self.setWindowTitle('有道词典')
		self.Label1 = QLabel('原文')
		self.Label2 = QLabel('译文')
		self.LineEdit1 = QLineEdit()
		self.LineEdit2 = QLineEdit()
		self.translateButton = QPushButton()
		self.translateButton.setText('翻译')
		self.grid = QGridLayout()
		self.grid.setSpacing(12)
		self.grid.addWidget(self.Label1, 1, 0)
		self.grid.addWidget(self.LineEdit1, 1, 1)
		self.grid.addWidget(self.Label2, 2, 0)
		self.grid.addWidget(self.LineEdit2, 2, 1)
		self.grid.addWidget(self.translateButton, 2, 2)
		self.setLayout(self.grid)
		self.resize(600, 150)
		self.translateButton.clicked.connect(self.translate)
		self.yd_translate = youdao()
	def translate(self):
		word = self.LineEdit1.text()
		results = self.yd_translate.translate(word)
		for result in results:
			self.LineEdit2.setText(result)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())