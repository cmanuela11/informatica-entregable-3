# main.py
from PyQt5.QtWidgets import QApplication
from model import HospitalModel
from view import HospitalView
from controller import HospitalController

def main():
    app = QApplication([])
    model = HospitalModel()
    view = HospitalView()
    controller = HospitalController(model, view)

    # Asigna la vista al controlador y viceversa
    view.controller = controller
    controller.view = view

    # Inicia la aplicación
    controller.start_application()

    app.exec_()

if __name__ == "__main__":
    main()
