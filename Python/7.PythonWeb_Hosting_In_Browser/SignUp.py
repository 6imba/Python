#!F:/Software/Python/Python_Files/python.exe

print("Content-Type: text/html\n") #help to run html code
print() # use ??



print("<h1>Welcome Python_File (SignUp.py) </h1>")
print("</hr>")

print("<body bgcolor='green'>")
print("<hr color=blue>")

import cgi
form = cgi.FieldStorage()
name = form.getvalue("name")
address = form.getvalue("address") 
gender = form.getvalue("gender")
password = form.getvalue("password")
country = form.getvalue("country")

print([password])

import mysql.connector
connection = mysql.connector.connect(user='root',password='',host='localhost', database='database_4')
print('jbfwefbewfbfiweifb')
if connection:
    print('Connection success')
else:
    print('Connection failed')


db_cursor = connection.cursor()
db_cursor.execute ("CREATE TABLE IF NOT EXISTS table1 (id int(103) auto_increment,name varchar(255),address varchar(255),gender varchar(255),country varchar(255))")
db_cursor.execute ("INSERT INTO table1 values (%s,%s,%s,%s,%s)" , (name,address,gender,password,country))
db_cursor.commit()
db_cursor.close()
connection.close()


print("<h3>Congrats, ",name,"</h3>")
print("<a herf='http://localhost/PythonWeb_Hosting_In_Browser/Form.php'> Home</a>")




