import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Manoj@3197'    

     )

cursorObject=dataBase.cursor()

cursorObject.execute('CREATE DATABASE dcrm')

print('All done')