import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QLabel, QWidget, QPushButton

class login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("login ejemplo")
        self.setGeometry(500, 500, 300, 200)

        layout = QGridLayout()

        # Crear etiquetas y campos de entrada
        etiqueta_usuario = QLabel("Nombre de usuario:")
        etiqueta_contraseña = QLabel("Contraseña:")

        self.usuario = QLineEdit()
        self.contraseña = QLineEdit()
        self.contraseña.setEchoMode(QLineEdit.EchoMode.Password)

        # Agregar componentes al diseño
        layout.addWidget(etiqueta_usuario, 0, 0)
        layout.addWidget(self.usuario, 0, 1)
        layout.addWidget(etiqueta_contraseña, 1, 0)
        layout.addWidget(self.contraseña, 1, 1)

        # Crear botón de inicio de sesión
        botonLogin = QPushButton("Iniciar sesión")
        botonLogin.clicked.connect(self.verificar)

        layout.addWidget(botonLogin, 2, 0)

        # Crear botón de cancelar
        botonCancelar = QPushButton("Cancelar")
        botonCancelar.clicked.connect(self.cancelar)
        layout.addWidget(botonCancelar, 2,1)

        self.setLayout(layout)

    def verificar(self):
        usuario = self.usuario.text()
        contraseña = self.contraseña.text()

        # TO DO: Implementar la lógica de inicio de sesión aquí
        # Por motivos de demostración, solo imprimiré las credenciales
        print(f"Nombre de usuario: {usuario}, Contraseña: {contraseña}")
    
    def cancelar(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo_login = login()
    dialogo_login.show()
    sys.exit(app.exec())
