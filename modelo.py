# model.py
import os
import pydicom

class HospitalModel:
    def __init__(self):
        self.logged_in = False
        self.current_folder_path = ""
        self.current_images = []
        self.current_image_index = 0

    def authenticate(self, username, password):
        return username == "medicoAnalitico" and password == "bio12345"

    def load_dcm_files(self, folder_path):
        self.current_folder_path = folder_path
        self.current_images = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.dcm')]
        self.current_image_index = 0

    def get_current_image_info(self):
        if not self.current_images:
            return ""
        current_image_path = self.current_images[self.current_image_index]
        dcm_data = pydicom.dcmread(current_image_path)
        return f"Image {self.current_image_index + 1}/{len(self.current_images)} - {current_image_path}"
