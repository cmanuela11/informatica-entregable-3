# view.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QSlider, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class HospitalView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Componentes de la interfaz gráfica
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.slider = QSlider()
        self.info_label = QLabel()
        self.logout_button = QPushButton("Logout")

        # Componentes de Matplotlib
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        login_layout = QVBoxLayout()
        login_layout.addWidget(QLabel("Username:"))
        login_layout.addWidget(self.username_input)
        login_layout.addWidget(QLabel("Password:"))
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(self.login_button)

        image_layout = QVBoxLayout()
        image_layout.addWidget(self.canvas)
        image_layout.addWidget(self.slider)
        image_layout.addWidget(self.info_label)
        image_layout.addWidget(self.logout_button)

        layout.addLayout(login_layout)
        layout.addLayout(image_layout)

        self.setLayout(layout)

        # Conecta los eventos a los métodos del controlador
        self.login_button.clicked.connect(self.controller.login)
        self.slider.valueChanged.connect(self.controller.change_image)
        self.logout_button.clicked.connect(self.controller.logout)
