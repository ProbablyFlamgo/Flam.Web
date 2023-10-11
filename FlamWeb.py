from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):

    def __init__(self):
        super().__init__()

        icon_path = "Images/FlamWebIcon.png"
        
        self.window = QWidget()
        self.window.setWindowTitle("Flam.Web")
        self.window.setWindowIcon(QIcon(icon_path))
        

        self.layout = QVBoxLayout()

        self.url_bar1 = QLineEdit()
        self.url_bar1.setMaximumHeight(30)

        self.search_btn1 = QPushButton("Ent")
        self.search_btn1.setMinimumHeight(30)

        self.url_bar2 = QLineEdit()
        self.url_bar2.setMaximumHeight(30)

        self.search_btn2 = QPushButton("Ent")
        self.search_btn2.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.home_btn = QPushButton("HOME")
        self.home_btn.setMinimumHeight(30)

        self.toggle_browsers_btn = QPushButton("-")
        self.toggle_browsers_btn.setMinimumHeight(30)

        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.toggle_browsers_btn)
        self.horizontal.addWidget(self.url_bar1)
        self.horizontal.addWidget(self.search_btn1)
        self.horizontal.addWidget(self.url_bar2)
        self.horizontal.addWidget(self.search_btn2)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.home_btn)
        

        self.mainBrowser = QWebEngineView()
        self.DiscordBrowser = QWebEngineView()

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.DiscordBrowser)
        self.splitter.addWidget(self.mainBrowser)

        self.splitter.setSizes([500, 500])  # Initial sizes for the browsers

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.splitter)  # Add the splitter to the layout

        self.search_btn1.clicked.connect(lambda: self.navigate1(self.url_bar1.text()))
        self.search_btn2.clicked.connect(lambda: self.navigate2(self.url_bar2.text()))
        self.back_btn.clicked.connect(self.mainBrowser.back)
        self.forward_btn.clicked.connect(self.mainBrowser.forward)
        self.home_btn.clicked.connect(self.go_home)
        self.toggle_browsers_btn.clicked.connect(self.toggle_browser) 

        self.url_bar1.returnPressed.connect(self.search1)
        self.url_bar2.returnPressed.connect(self.search2)

        self.mainBrowser.setUrl(QUrl("https://google.com"))
        self.DiscordBrowser.setUrl(QUrl("https://discord.com"))

        self.DiscordBrowser.urlChanged.connect(self.update_url_bar1)
        self.mainBrowser.urlChanged.connect(self.update_url_bar2)

        self.window.setLayout(self.layout)
        self.window.show()

        self.left_browser_visible = True
    
    # Bar 1
    def navigate1(self, url):
        if not url.startswith("http"):
            url = "https://" + url
            self.url_bar1.setText(url)
        self.DiscordBrowser.setUrl(QUrl(url))

    def search1(self):
        text = self.url_bar1.text()
        self.navigate1(text)

    def clear_search_bar1(self, event):
        self.url_bar1.clear()

    def update_url_bar1(self, qurl):
        if qurl.toString() != "":
            self.url_bar1.setText(qurl.toString())

    # bar 2
    def navigate2(self, url):
        if not url.startswith("http"):
            url = "https://" + url
            self.url_bar2.setText(url)
        self.mainBrowser.setUrl(QUrl(url))

    def search2(self):
        text = self.url_bar2.text()
        self.navigate2(text)

    def clear_search_bar(self, event):
        self.url_bar2.clear()

    def update_url_bar2(self, qurl):
        if qurl.toString() != "":
            self.url_bar2.setText(qurl.toString())


    def go_home(self):
        self.mainBrowser.setUrl(QUrl("https://google.com"))

    def toggle_browser(self):
        if self.left_browser_visible:
            self.DiscordBrowser.setVisible(False)
            self.url_bar1.setVisible(False)
            self.search_btn1.setVisible(False)
            self.left_browser_visible = False
            self.toggle_browsers_btn.setText("+")
        else:
            self.DiscordBrowser.setVisible(True)
            self.left_browser_visible = True
            self.url_bar1.setVisible(True)
            self.search_btn1.setVisible(True)
            self.toggle_browsers_btn.setText("-")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWebBrowser()
    app.exec_()
