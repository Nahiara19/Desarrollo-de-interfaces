# EJERCICIOS DIA 27/09/2024

### Ejercicio 1. Añade componentes diferentes a los widget y muestrame la pantalla

``` python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button = QPushButton("Presioname")
        layout.addWidget(button)

        button2 = QPushButton("Pulsa aquí")
        layout.addWidget(button2)

        button3 = QPushButton("Botón")
        layout.addWidget(button3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

```

### Ejercicio 2. Pon un  Qlabel y un QLineEdit

``` python

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QHBoxLayout()
        label = QLabel()
        label.setText("HOLA")
        layout.addWidget(label)
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)


        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Pon tu nombre")
        layout.addWidget(line_edit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

#### Ejercicio 3. Modifica el nested layout a otra configuración con los colores.

``` python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QHBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))

        layout3.addWidget(Color('purple'))
        layout3.addWidget(Color('green'))

        layout4.addLayout(layout2)
        layout4.addLayout(layout3)

        layout1.addLayout(layout4)
        layout1.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

```


#### Ejercicio 4. Añade widgets a esta configuración y luego cambia la configuración con otra estructura.

``` python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        # Cambiamos a un QVBoxLayout
        layout = QVBoxLayout()

        # Añadimos colores como antes
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        
        # Añadimos un nuevo color (azul)
        layout.addWidget(Color('blue'))

        # Añadimos un QLabel
        label = QLabel("Este es un label")
        layout.addWidget(label)

        # Añadimos un QPushButton
        button = QPushButton("Click me")
        layout.addWidget(button)

        # Creamos un widget central y lo configuramos
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

#### Ejercicio 5. Crea un Vertical Layout y un Horizontal Layout Añade 3 botones QButtons en la primera línea y en la otra crea un widget de color.
``` python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Layout vertical
        v_layout = QVBoxLayout()

        # Layout horizontal para los botones
        h_layout = QHBoxLayout()
        h_layout.addWidget(QPushButton("Botón 1"))
        h_layout.addWidget(QPushButton("Botón 2"))
        h_layout.addWidget(QPushButton("Botón 3"))

        # Añadir el layout horizontal al layout vertical
        v_layout.addLayout(h_layout)

        # Añadir un widget de color al layout vertical
        color_widget = Color('lightblue')  # Cambia el color 
        v_layout.addWidget(color_widget)

        # Crear un widget central y establecer el layout
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

```

#### Ejercicio 5-1. Vertical layout:

``` python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Layout vertical
        v_layout = QVBoxLayout()

        v_layout.addWidget(QPushButton("Botón 1"))
        # Añadir un widget de color al layout vertical
        color_widget = Color('lightblue')  # Cambia el color 
        v_layout.addWidget(color_widget)
        v_layout.addWidget(QPushButton("Botón 2"))
        v_layout.addWidget(QLabel("Hola"))
        v_layout.addWidget(QPushButton("Botón 3"))


        # Crear un widget central y establecer el layout
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

```
#### Ejercicio 5-2. Horizontal layout:

``` python

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Layout horizontal
        h_layout = QHBoxLayout()

        h_layout.addWidget(QPushButton("Botón 1"))
        # Añadir un widget de color al layout horizontal
        color_widget = Color('lightblue')  # Cambia el color 
        h_layout.addWidget(color_widget)
        h_layout.addWidget(QPushButton("Botón 2"))
        h_layout.addWidget(QLabel("Hola"))
        h_layout.addWidget(QPushButton("Botón 3"))


        # Crear un widget central y establecer el layout
        widget = QWidget()
        widget.setLayout(h_layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

```
