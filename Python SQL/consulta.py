import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'python'
)

mycursor = mydb.cursor()

### Consulta Tablea ####


print("######  CNSULTA TABELA CLIENTE #######")
print()

mycursor.execute("SELECT * FROM cliente ")

myresult = mycursor.fetchall()

for line in myresult:
    print(f"line: {line}")