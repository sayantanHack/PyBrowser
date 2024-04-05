
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()

        # Create a tab widget to hold multiple tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.switch_tab)

        # Create a URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)

        # Create navigation buttons
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.go_forward)
        self.refresh_button = QPushButton("⟳")
        self.refresh_button.clicked.connect(self.refresh_page)

        #youtube ADD Skipper
        self.skip_ad = QPushButton("Skip Ad")
        self.skip_ad.clicked.connect(self.yt_skip_ad)
        #google & youtube
        self.google_button = QPushButton("Google")
        self.google_button.clicked.connect(self.google_search)
        self.yt_button = QPushButton("Youtube")
        self.yt_button.clicked.connect(self.yt_search)
        
        
        # Create a layout for the navigation bar
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.back_button)
        navigation_layout.addWidget(self.forward_button)
        navigation_layout.addWidget(self.refresh_button)
        navigation_layout.addWidget(self.skip_ad)
        
        navigation_layout.addWidget(self.url_bar)
        navigation_layout.addWidget(self.google_button)
        navigation_layout.addWidget(self.yt_button)

        # Create a layout for the browser window
        layout = QVBoxLayout()
        layout.addLayout(navigation_layout)
        layout.addWidget(self.tabs)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Add initial tab
        self.add_new_tab()

    def add_new_tab(self):
        # Create a new web view widget
        web_view = QWebEngineView()
        web_view.urlChanged.connect(self.update_url)

        # Add the web view to a new tab
        index = self.tabs.addTab(web_view, "New Tab")
        self.tabs.setCurrentIndex(index)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def switch_tab(self, index):
        web_view = self.tabs.widget(index)
        url = web_view.url().toString()
        self.url_bar.setText(url)

    def load_url(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        url = self.url_bar.text()
        web_view.load(QUrl(url))

    def go_back(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        web_view.back()

    def go_forward(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        web_view.forward()

    def refresh_page(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        web_view.reload()

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    
    def google_search(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        web_view.load(QUrl("https://google.com/"))

    def yt_search(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        web_view.load(QUrl("https://youtube.com/"))
        

    def yt_skip_ad(self):
        current_index = self.tabs.currentIndex()
        web_view = self.tabs.widget(current_index)
        web_view.load(QUrl("javascript:(function(){let x=document.querySelector('video');x.playbackRate=15;})();"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser_window = BrowserWindow()
    browser_window.show()
    app.exec_()
