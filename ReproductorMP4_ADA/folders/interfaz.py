import sys
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QPushButton, QListWidgetItem, QLabel, \
    QSlider, QVBoxLayout
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import Qt, QUrl


class Reproductor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reproductor de Video")
        self.setWindowIcon(QIcon("sonido.gif"))
        self.setGeometry(100, 100, 800, 600)

        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self)

        self.archivoFolder = QListWidget(self)
        self.archivoFolder.setGeometry(10, 40, 300, 260)
        self.archivoFolder.itemDoubleClicked.connect(self.agregar_a_lista_reproduccion)

        self.listaReprod = QListWidget(self)
        self.listaReprod.setGeometry(10, 330, 300, 260)

        self.init_ui()

    def init_ui(self):
        self.SalidaVideo = QLabel(self)
        self.SalidaVideo.setGeometry(320, 40, 450, 260)
        self.SalidaVideo.setStyleSheet("border: 1px solid black;")

        self.btn_seleccionar_folder = QPushButton(self)
        self.btn_seleccionar_folder.setGeometry(10, 5, 30, 30)
        self.btn_seleccionar_folder.setIcon(QIcon("iconos/folder.png"))
        self.btn_seleccionar_folder.clicked.connect(self.abrir_carpeta)

        self.label_archivo_mp4 = QLabel(self)
        self.label_archivo_mp4.setGeometry(80, -22, 90, 80)
        self.label_archivo_mp4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_archivo_mp4.setText("ARCHIVOS MP4")

        self.btn_lista_reproduccion = QPushButton(self)
        self.btn_lista_reproduccion.setGeometry(10, 300, 30, 30)
        self.btn_lista_reproduccion.setIcon(QIcon("iconos/listaReproduccion.png"))

        self.label_lista_reproduccion = QLabel(self)
        self.label_lista_reproduccion.setGeometry(-100, 275, 500, 80)
        self.label_lista_reproduccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_lista_reproduccion.setText("LISTA DE REPRODUCCIÓN")

        self.btn_play = QPushButton(self)
        self.btn_play.setIcon(QIcon("iconos/play.png"))
        self.btn_play.setGeometry(470, 370, 100, 30)
        self.btn_play.clicked.connect(self.reproducir_video)

        self.btn_retroceder = QPushButton(self)
        self.btn_retroceder.setIcon(QIcon("iconos/retroceder.png"))
        self.btn_retroceder.setGeometry(350, 370, 100, 30)
        self.btn_retroceder.clicked.connect(self.retroceder_video)

        self.btn_adelantar = QPushButton(self)
        self.btn_adelantar.setIcon(QIcon("iconos/adelantar.png"))
        self.btn_adelantar.setGeometry(590, 370, 100, 30)
        self.btn_adelantar.clicked.connect(self.adelantar_video)

        self.btn_volumen = QPushButton(self)
        self.btn_volumen.setIcon(QIcon("iconos/volumen.png"))
        self.btn_volumen.setGeometry(350, 310, 30, 30)

        self.volumen_slider = QSlider()
        self.volumen_slider.setMinimum(0)
        self.volumen_slider.setMaximum(100)
        self.volumen_slider.setValue(50)
        layout = QVBoxLayout()
        layout.addWidget(self.volumen_slider)
        self.volumen_slider.setOrientation(Qt.Orientation.Horizontal)
        self.volumen_slider.setGeometry(550, 410, 100, 100)



    def abrir_carpeta(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Videos (*.mp4)")
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            for file_path in file_paths:
                item = QListWidgetItem(file_path)
                self.archivoFolder.addItem(item)

    def agregar_a_lista_reproduccion(self, item):
        self.listaReprod.addItem(item.text())

    def reproducir_video(self):
        current_item = self.listaReprod.currentItem()
        if current_item:
            video_path = current_item.text()
            video_url = QUrl.fromLocalFile(video_path)


    def retroceder_video(self):
        self.media_player.setPosition(self.media_player.position() - 5000)  # Retrocede 5 segundos

    def adelantar_video(self):
        self.media_player.setPosition(self.media_player.position() + 5000)  # Adelanta 5 segundos


def main():
    app = QApplication(sys.argv)
    player = Reproductor()
    player.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
