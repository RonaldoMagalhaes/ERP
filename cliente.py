# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#FAZ este importe manual abaixo
from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog,QTableWidget,QTableWidgetItem

# Libs diversas
import mysql.connector
import pandas as pd

# import de telas
from dadosCliente import Ui_form_dadosCliente

### import variaveis de controle
import variaveisControle

### conexao com o banco de dados
host = variaveisControle.host
user = variaveisControle.user
password = variaveisControle.password
database = variaveisControle.database
     

class Ui_formCliente(object):
    def setupUi(self, formCliente):
        formCliente.setObjectName("formCliente")
        formCliente.resize(545, 410)
        self.bt_adicionar = QtWidgets.QPushButton(formCliente)
        self.bt_adicionar.setGeometry(QtCore.QRect(10, 0, 81, 81))
        self.bt_adicionar.setText("")
        self.bt_adicionar.setObjectName("bt_adicionar")
        self.bt_alterar = QtWidgets.QPushButton(formCliente)
        self.bt_alterar.setGeometry(QtCore.QRect(90, 0, 81, 81))
        self.bt_alterar.setText("")
        self.bt_alterar.setObjectName("bt_alterar")
        self.bt_consultar = QtWidgets.QPushButton(formCliente)
        self.bt_consultar.setGeometry(QtCore.QRect(170, 0, 81, 81))
        self.bt_consultar.setText("")
        self.bt_consultar.setObjectName("bt_consultar")
        self.bt_excluir = QtWidgets.QPushButton(formCliente)
        self.bt_excluir.setGeometry(QtCore.QRect(250, 0, 81, 81))
        self.bt_excluir.setText("")
        self.bt_excluir.setObjectName("bt_excluir")
        self.bt_retornar = QtWidgets.QPushButton(formCliente)
        self.bt_retornar.setGeometry(QtCore.QRect(450, 0, 81, 81))
        self.bt_retornar.setText("")
        self.bt_retornar.setObjectName("bt_retornar")
        self.bt_pesquisarGeral = QtWidgets.QPushButton(formCliente)
        self.bt_pesquisarGeral.setGeometry(QtCore.QRect(450, 120, 31, 31))
        self.bt_pesquisarGeral.setStyleSheet("image:url(:/icon_geral/icons/filtro.png)")
        self.bt_pesquisarGeral.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_geral/icons/filtro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_pesquisarGeral.setIcon(icon)
        self.bt_pesquisarGeral.setObjectName("bt_pesquisarGeral")
        self.bt_pesquisar = QtWidgets.QPushButton(formCliente)
        self.bt_pesquisar.setGeometry(QtCore.QRect(410, 120, 31, 31))
        self.bt_pesquisar.setStyleSheet("image:url(:/icon_pesquisar/icons/pesquisar.png)")
        self.bt_pesquisar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon_pesquisar/icons/pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_pesquisar.setIcon(icon1)
        self.bt_pesquisar.setObjectName("bt_pesquisar")
        self.tb_cliente = QtWidgets.QTableWidget(formCliente)
        self.tb_cliente.setGeometry(QtCore.QRect(10, 210, 531, 192))
        self.tb_cliente.setObjectName("tb_cliente")
        self.tb_cliente.setColumnCount(4)
        self.tb_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_cliente.setHorizontalHeaderItem(3, item)
        self.nome_cliente = QtWidgets.QLabel(formCliente)
        self.nome_cliente.setGeometry(QtCore.QRect(10, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nome_cliente.setFont(font)
        self.nome_cliente.setObjectName("nome_cliente")
        self.lineEdit = QtWidgets.QLineEdit(formCliente)
        self.lineEdit.setGeometry(QtCore.QRect(100, 130, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(formCliente)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.label_2.setStyleSheet("image:url(:/icon_adicionar/icons/adicionar.png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(formCliente)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 61, 51))
        self.label_3.setStyleSheet("image:url(:/icon_alterar/icons/alterar.png)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(formCliente)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 61, 51))
        self.label_4.setStyleSheet("image:url(:/icon_consultar/icons/consultar.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(formCliente)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 61, 51))
        self.label_5.setStyleSheet("image:url(:/icon_excluir/icons/excluir.png)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(formCliente)
        self.label_6.setGeometry(QtCore.QRect(460, 10, 61, 51))
        self.label_6.setStyleSheet("image:url(:/icon_retornar/icons/retornar.png)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(formCliente)
        QtCore.QMetaObject.connectSlotsByName(formCliente)

    def retranslateUi(self, formCliente):
        _translate = QtCore.QCoreApplication.translate
        formCliente.setWindowTitle(_translate("formCliente", "Form"))
        item = self.tb_cliente.horizontalHeaderItem(0)
        item.setText(_translate("formCliente", "Id"))
        item = self.tb_cliente.horizontalHeaderItem(1)
        item.setText(_translate("formCliente", "Nome"))
        item = self.tb_cliente.horizontalHeaderItem(2)
        item.setText(_translate("formCliente", "Telefone"))
        item = self.tb_cliente.horizontalHeaderItem(3)
        item.setText(_translate("formCliente", "Cidade"))
        self.nome_cliente.setText(_translate("formCliente", "Nome Cliente:"))

##### BOTÕES SISTEMA #######
        self.bt_retornar.clicked.connect(lambda:self.sairTela(formCliente))
        self.bt_pesquisarGeral.clicked.connect(self.consultarGeral)
        self.bt_pesquisar.clicked.connect(self.pesquisarCliente)
        self.bt_adicionar.clicked.connect(self.cadastrarCliente)
        self.bt_consultar.clicked.connect(self.consultarCliente)
        self.bt_alterar.clicked.connect(self.alterarCliente)
        self.bt_excluir.clicked.connect(self.excluirCliente)


###### FUNÇÕES SISTEMA ######
## fechar tela cliente
    def sairTela(self, formCliente):        
        formCliente.close()

## consultar tabela Cliente geral
    def consultarGeral(self):
        mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
        mycursor = mydb.cursor()        
        mycursor.execute("SELECT * FROM cliente ")
        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=['ID','Nome','Telefone','Cidade'])
        self.all_data = df

        # carrega arquivo na tabela tb_cliente
        numRows =len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()

        mycursor.close() # Fecha conexao

 ## Pesquisar por nome cliente
    def pesquisarCliente(self):        
        mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
        mycursor = mydb.cursor()    
        nome_consulta = self.lineEdit.text()  
        consulta_sql = "SELECT * FROM cliente WHERE nome LIKE   '" + nome_consulta + "%'" 
        mycursor.execute(consulta_sql)
        myresult = mycursor.fetchall()
        df = pd.DataFrame(myresult, columns=['ID','Nome','Telefone','Cidade'])
        self.all_data = df

        # carrega arquivo na tabela tb_cliente
        numRows =len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()

        mycursor.close() # Fecha conexao


## Função cadastrar cliente
    def cadastrarCliente(self):
        variaveisControle.tipoTelaDadosCliente = "incluir"

        self.form_dadosCliente = QtWidgets.QWidget()
        self.ui = Ui_form_dadosCliente()
        self.ui.setupUi(self.form_dadosCliente)
        self.form_dadosCliente.show()

## Função consultar cliente
    def consultarCliente(self):
        #tipo tela dadosCliente
        variaveisControle.tipoTelaDadosCliente = "consultar"
        print('FormCliente: ', variaveisControle.tipoTelaDadosCliente)

        #ID para consulta

        line = self.tb_cliente.currentRow()
        item = self.tb_cliente.item(line,0)
        variaveisControle.idConsulta = item.text()
       # print('IdConsulta: ', variaveisControle.idConsulta)

        ##Abertura da tela cliente
        self.form_dadosCliente = QtWidgets.QWidget()
        self.ui = Ui_form_dadosCliente()
        self.ui.setupUi(self.form_dadosCliente)
        self.form_dadosCliente.show()


## Função Alterar cliente
    def alterarCliente(self):
        #tipo tela dadosCliente
        variaveisControle.tipoTelaDadosCliente = "alterar"
        print('FormCliente: ', variaveisControle.tipoTelaDadosCliente)

        #ID para consulta

        line = self.tb_cliente.currentRow()
        item = self.tb_cliente.item(line,0)
        variaveisControle.idConsulta = item.text()
       # print('IdConsulta: ', variaveisControle.idConsulta)

        ##Abertura da tela cliente
        self.form_dadosCliente = QtWidgets.QWidget()
        self.ui = Ui_form_dadosCliente()
        self.ui.setupUi(self.form_dadosCliente)
        self.form_dadosCliente.show()

## função excluir cliente

    def excluirCliente(self):
        
        line = self.tb_cliente.currentRow()
        item = self.tb_cliente.item(line,0)
        id_cliente = item.text()

        ##conexao com o bando de dadods

        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        mycursor = mydb.cursor()
        sql = "DELETE FROM cliente WHERE IdCliente = '" + id_cliente+ "'"  
        mycursor.execute(sql)
        mydb.commit()

        print(mycursor.rowcount, ' record(s) exclused')
        #atualizar a tabela

             
        mycursor.execute("SELECT * FROM cliente ")
        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=['ID','Nome','Telefone','Cidade'])
        self.all_data = df

        # carrega arquivo na tabela tb_cliente
        numRows =len(self.all_data.index)
        self.tb_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_cliente.setRowCount(numRows)
        self.tb_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_cliente.resizeColumnsToContents()
        self.tb_cliente.resizeRowsToContents()

        mycursor.close() # Fecha conexao

           



# IMAGENS DO SISTEMA ####
import icon_adicionar
import icon_alterar
import icon_consultar
import icon_excluir
import icon_geral
import icon_pesquisar
import icon_retornar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formCliente = QtWidgets.QWidget()
    ui = Ui_formCliente()
    ui.setupUi(formCliente)
    formCliente.show()
    sys.exit(app.exec_())
