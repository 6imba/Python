import mysql.connector

def create_tables():
    create_meta_data_table = """CREATE TABLE if not exists meta_data (
            M_Id              int AUTO_INCREMENT PRIMARY KEY,
            CopyRight         varchar(255),
            FullName          varchar(255)
        );"""
    db_cursor.execute(create_meta_data_table)
    create_site_url_table = """
    CREATE TABLE if not exists site_url (
        SiteUrlID               int AUTO_INCREMENT PRIMARY KEY,
        RequestUrl              varchar(255),
        UrlType                 int,
        MetaDataID              int
    );"""
    db_cursor.execute(create_site_url_table)

def save_in_metadata(dataList):
        insert_meta_data_value = "INSERT INTO meta_data (CopyRight,FullName) VALUES (%s,%s);"
        db_cursor.execute(insert_meta_data_value,(dataList[0],dataList[1]))

def save_in_site_url():
    insert_create_site_url_value = "INSERT INTO site_url (RequestUrl,UrlType,MetaDataID) VALUES (%s,%s,%s);"
    db_cursor.execute(insert_create_site_url_value,('http_6', 1, 0))
    db_cursor.execute(insert_create_site_url_value,('http_7', 1, db_cursor.lastrowid))


# Main:
try:
    db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='lesson_db',auth_plugin='mysql_native_password')
    db_cursor = db_connection.cursor()
    create_tables()
    save_in_metadata()
    save_in_site_url()
    db_connection.commit() # when working with table data.
    db_connection.close()
except Exception as e:
    print("Exception caught ==> ", e)

       