import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout, QListWidgetItem)


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 10-12_2024")

        lblNome = QLabel("Nome")
        lblApelido = QLabel("Apelido")
        lblTratamento = QLabel("Tratamento")
        lblUsuario = QLabel("Usuario")
        self.txtNome = QLineEdit()
        self.txtApelido = QLineEdit()
        self.txtTratamento = QLineEdit()
        txtUsuario = QLineEdit()
        lblFormato = QLabel("Formato")
        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(["Html", "Texto Plano", "Personalizado"])
        self.cmbFormato.currentTextChanged.connect(self.combochange)

        lblDireccionC = QLabel("Dirección de correo")
        self.txtDireccionC = QLineEdit()

        self.lstDireccionC = QListWidget()


        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.add_lista)
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.borrar_seleccionado)
        btnPorDefecto = QPushButton("Por Defecto")

        lblFormatodeCorreo = QLabel("Formato de correo:")
        self.rbtHtml = QRadioButton("HTML")
        self.rbtHtml.clicked.connect(self.radiochange)
        self.rbtTextoPlano = QRadioButton ("Texto Plano")
        self.rbtTextoPlano.clicked.connect(self.radiochange)
        self.rbtPersonalizado = QRadioButton ("Personalizado")
        self.rbtPersonalizado.clicked.connect(self.radiochange)

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        widget_principal = QWidget()
        self.setCentralWidget(widget_principal)

        layout_principal = QVBoxLayout()
        widget_principal.setLayout(layout_principal)

        # layout grid campos superiores
        layout1_grid = QGridLayout()
        layout1_grid.addWidget(lblNome, 0, 0)
        layout1_grid.addWidget(self.txtNome, 1, 0)
        layout1_grid.addWidget(lblTratamento, 0, 1)
        layout1_grid.addWidget(self.txtTratamento, 1, 1)
        layout1_grid.addWidget(lblApelido, 2, 0)
        layout1_grid.addWidget(self.txtApelido, 3, 0)
        layout1_grid.addWidget(lblUsuario, 2, 1)
        layout1_grid.addWidget(txtUsuario, 3, 1)
        layout_principal.addLayout(layout1_grid)

        # layout horizontal formato
        formato_lyt = QHBoxLayout()
        formato_lyt.addWidget(lblFormato)
        formato_lyt.addWidget(self.cmbFormato, stretch=1)
        layout_principal.addLayout(formato_lyt)

        # layout correo
        correo_lyt = QHBoxLayout() # sublayout horizontal
        correo_izq_lyt = QVBoxLayout() # layout de la izquierda
        dircorreo_lyt = QHBoxLayout() # subsublayout horizontal
        dircorreo_lyt.addWidget(lblDireccionC)
        dircorreo_lyt.addWidget(self.txtDireccionC)
        correo_izq_lyt.addLayout(dircorreo_lyt) # añadir layout horizontal
        correo_izq_lyt.addWidget(self.lstDireccionC)

        correo_izq_lyt.addWidget(lblFormatodeCorreo)
        radiobtn_lyt = QHBoxLayout() # layout horizontal para los radiobuttons
        radiobtn_lyt.addWidget(self.rbtHtml)
        radiobtn_lyt.addWidget(self.rbtTextoPlano)
        radiobtn_lyt.addWidget(self.rbtPersonalizado)
        correo_izq_lyt.addLayout(radiobtn_lyt)
        correo_lyt.addLayout(correo_izq_lyt)

        correo_der_lyt = QVBoxLayout() # layout vertical para los botones
        correo_der_lyt.setAlignment(Qt.AlignmentFlag.AlignTop)
        correo_der_lyt.addWidget(btnEngadir)
        correo_der_lyt.addWidget(btnEditar)
        correo_der_lyt.addWidget(btnBorrar)
        correo_der_lyt.addWidget(btnPorDefecto)

        correo_lyt.addLayout(correo_der_lyt)

        layout_principal.addLayout(correo_lyt)

        inferior_lyt = QGridLayout()
        inferior_lyt.setAlignment(Qt.AlignmentFlag.AlignRight)
        btnCancelar.setMaximumSize(60, 60)
        inferior_lyt.addWidget(btnCancelar, 0, 3)
        btnAceptar.setMaximumSize(60, 60)
        inferior_lyt.addWidget(btnAceptar, 0, 4)

        layout_principal.addLayout(inferior_lyt)

    def combochange(self):
        print(self.cmbFormato.currentText())

    def radiochange(self):
        if self.rbtHtml.isChecked():
            self.cmbFormato.setCurrentIndex(0)
        if self.rbtTextoPlano.isChecked():
            self.cmbFormato.setCurrentIndex(1)
        if self.rbtPersonalizado.isChecked():
            self.cmbFormato.setCurrentIndex(2)

    def add_lista(self):
        newItem = QListWidgetItem()
        newItem.setText(self.txtTratamento.text() + "," + self.txtNome.text() + "," + self.txtApelido.text() + "," + self.txtDireccionC.text())
        self.txtTratamento.clear()
        self.txtNome.clear()
        self.txtApelido.clear()
        self.txtDireccionC.clear()
        self.lstDireccionC.addItem(newItem)

    def borrar_seleccionado(self):
        print("borrando")
        itemSelected = self.lstDireccionC.selectedItems()
        print(itemSelected)
        for item in itemSelected:
            print(item.text())
            self.lstDireccionC.takeItem(self.lstDireccionC.row(item))
            self.lstDireccionC.update()



if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()

    aplicacion.exec()
