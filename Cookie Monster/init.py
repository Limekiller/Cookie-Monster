from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import os
import time, threading

thread_loop = True
cwd = os.getcwd()
splash = QUrl.fromLocalFile(cwd+'\Splash\index.html')
app = QApplication([])
view = QWebEngineView()
QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

def clear_cookies():
    global thread_loop
    while thread_loop == True:
        time.sleep(5)
        view.page().profile().cookieStore().deleteAllCookies()

threading.Thread(target=clear_cookies).start()
view.setWindowTitle("Cookie Monster")
view.setWindowIcon(QIcon("./icon.jpg"))
view.page().profile().setPersistentCookiesPolicy(False)

view.load(QUrl(splash))
#view.load(QUrl("https://youtube.com"))

view.show()
app.exec_()
thread_loop = False