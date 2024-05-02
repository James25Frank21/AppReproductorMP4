from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider, QWidget
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider Example")

        # Crear el slider
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.valueChanged.connect(self.value_changed)

        # Crear el layout y agregar el slider
        layout = QVBoxLayout()
        layout.addWidget(self.slider)

        # Establecer el layout central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def value_changed(self, value):
        print(f"Valor del slider: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
