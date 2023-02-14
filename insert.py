import mysql.connector

def insertProduct():
    connection = mysql.connector.connect(host="localhost", user = "root", password = "17257117enes.", database = "node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = ("Samsung S5", 1000, "1.jpg", "iyi telefon")
    cursor.execute(sql, values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")