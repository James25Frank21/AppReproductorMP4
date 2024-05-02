import sys
import os
import cv2
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, \
    QLineEdit, QMessageBox, QFileDialog, QInputDialog
from PIL import Image


class Reproductor_Video(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Reproductor de video")
        self.directorio = None  # para almacenar el directorio seleccionado

        self.lista_video = QListWidget()
        self.exportar_button = QPushButton("Exportar Imágenes")
        self.exportar_interv = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.lista_video)
        layout.addWidget(QLabel("Intervalo (segundos):"))
        layout.addWidget(self.exportar_interv)
        layout.addWidget(self.exportar_button)
        self.setLayout(layout)

        self.exportar_button.clicked.connect(self.exportar_imagenes)

        self.cargar_video()

    def cargar_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Utilizar el diálogo de selección de archivos de PyQt5
        directorio = QFileDialog.getExistingDirectory(self, "Seleccionar Directorio con Videos", options=options)
        if directorio:
            video_files = [file for file in os.listdir(directorio) if file.endswith('.mp4')]
            self.directorio = directorio  # Asignar el directorio seleccionado a la variable de instancia
            self.lista_video.addItems(video_files)

    def exportar_imagenes(self):
        selec_item = self.lista_video.currentItem()
        if not selec_item or not self.directorio:
            QMessageBox.warning(self, "Error", "Seleccione un video y un directorio válido.")
            return

        video_path = os.path.join(self.directorio, selec_item.text())

        interval, ok = QInputDialog.getInt(self, "Intervalo de Exportación",
                                           "Ingrese la duración del intervalo en segundos:")
        if not ok or interval <= 0:
            return

        directorio_export = QFileDialog.getExistingDirectory(self, "Seleccionar Directorio para Exportar Imágenes")
        if not directorio_export:
            return

        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Calcular el número total de cuadros a capturar dentro del intervalo de tiempo especificado
        num_fps = interval * fps
        count_fp = 0

        while count_fp < num_fps:
            success, image = cap.read()
            if not success:
                break

            count_fp += 1
            image_path = os.path.join(directorio_export, f"frame_{count_fp}.jpg")

        if image is not None:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            Image.fromarray((image_rgb)).save(image_path)

        cap.release()

        QMessageBox.information(self, "Exportación Exitosa", f"Se exportaron imágenes de {interval} segundos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = Reproductor_Video()
    player.show()
    sys.exit(app.exec())