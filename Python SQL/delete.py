import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'python'

)

mycursor = mydb.cursor()

#### Deletando a tabela #####
print("###### DELETE CLIENTE #######")

sql = "DELETE FROM cliente WHERE idCliente = '7' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, ' record(s) deleted')

