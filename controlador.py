from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pydicom

class HospitalController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_application(self):
        if self.view is not None:
            self.view.show()

    def login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        if self.model.authenticate(username, password):
            folder_path = QFileDialog.getExistingDirectory(self.view, "Select Folder", "")
            if folder_path:
                self.model.load_dcm_files(folder_path)
                self.update_image()
                self.view.login_button.setEnabled(False)
                self.view.username_input.setEnabled(False)
                self.view.password_input.setEnabled(False)
        else:
            self.show_error("Invalid credentials")

    def logout(self):
        self.view.login_button.setEnabled(True)
        self.view.username_input.setEnabled(True)
        self.view.password_input.setEnabled(True)
        self.view.username_input.clear()
        self.view.password_input.clear()
        self.view.info_label.clear()
        self.view.slider.setValue(0)

    def change_image(self):
        self.model.current_image_index = self.view.slider.value()
        self.update_image()

    def update_image(self):
        current_image_info = self.model.get_current_image_info()
        self.view.info_label.setText(current_image_info)

        if self.model.current_images:
            current_image_path = self.model.current_images[self.model.current_image_index]
            dcm_data = pydicom.dcmread(current_image_path)

            # Limpia la figura antes de mostrar una nueva imagen
            self.view.ax.clear()

            # Muestra la imagen utilizando matplotlib
            self.view.ax.imshow(dcm_data.pixel_array, cmap="gray")
            self.view.ax.set_title(f"Image {self.model.current_image_index + 1}/{len(self.model.current_images)}")

            # Actualiza el canvas
            self.view.canvas.draw()
