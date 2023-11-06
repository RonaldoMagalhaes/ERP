import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'python'
)

mycursor = mydb.cursor()

#### Variaveis #####

Cidade = 'Uberlândia'
IdCliente = '2'

### UPDATE #######

print("##### UPDATE #####")

sql = ("UPDATE cliente SET Cidade = %s WHERE IdCliente = %s ")
val = (Cidade, IdCliente)

mycursor.execute(sql, val)


mydb.commit()

print(mycursor.rowcount, ' record(s) updated')

