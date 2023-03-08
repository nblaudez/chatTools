import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
from chatgpt import ChatGPT


class ChatGPTWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.chatbot = ChatGPT()
        self.initUI()

    def initUI(self):
        # Création des widgets
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.text_input = QLineEdit()
        self.text_input.returnPressed.connect(self.generate_response)

        self.submit_button = QPushButton('Envoyer')
        self.submit_button.clicked.connect(self.generate_response)

        # Création du layout vertical et ajout des widgets
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.text_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setGeometry(100, 100, 900, 500)
        self.setWindowTitle('ChatGPT')

    def generate_response(self):
        question = self.text_input.text()
        response = self.chatbot.generate_response(question)
        self.text_edit.append(f"Vous : {question}\nChatbot : {response}\n\n")
        self.text_input.clear()


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        self.setToolTip('ChatGPT')
        self.setIcon(QIcon('icon.png'))
        self.activated.connect(self.on_tray_activated)

    def on_tray_activated(self, reason):
        if reason == self.Trigger:
            if not hasattr(self, 'chat_gpt_window') or not self.chat_gpt_window.isVisible():
                self.chat_gpt_window = ChatGPTWindow()
                self.chat_gpt_window.show()
            else:
                self.chat_gpt_window.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tray_icon = SystemTrayIcon()
    tray_icon.show()
    sys.exit(app.exec_())

