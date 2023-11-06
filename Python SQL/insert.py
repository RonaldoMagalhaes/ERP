import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='root',
    database = 'python'
)

mycursor = mydb.cursor()


########### Insert Tabela ################

print("##### INSERT TABELA ###########")

sql = "INSERT INTO cliente (Nome, Telefone, Cidade) VALUES(%s, %s,%s)"
val = ("Rebeca", "99999999", "Londrina")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, ' record(s) inserted')








