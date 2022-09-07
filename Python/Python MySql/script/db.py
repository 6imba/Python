import mysql.connector

def save_in_metadata(fontData):
    try:
        db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='test_db',auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor()

        create_meta_data_table = """CREATE TABLE if not exists meta_data (
            M_ID              int AUTO_INCREMENT PRIMARY KEY,
            CopyRight               varchar(255),
            FullName                varchar(255)
        );"""
        insert_meta_data_value = "INSERT INTO meta_data (CopyRight,FullName) VALUES (%s,%s);"
        datas = (fontData[1], fontData[5])
        db_cursor.execute(create_meta_data_table)
        db_cursor.execute(insert_meta_data_value,datas)
        print("MetaData inserted !!!")

        fk = db_cursor.lastrowid

        db_connection.commit() # when working with table data.
        db_connection.close()

        return fk

    except Exception as e:
        print("Exception caught ==> ", e)


def save_in_site_url(urlDetail):
    try:
        db_connection = mysql.connector.connect(host="localhost",user="simba",passwd="1234",database='test_db',auth_plugin='mysql_native_password')
        db_cursor = db_connection.cursor()

        create_site_url_table = """
        SET FOREIGN_KEY_CHECKS=0
        CREATE TABLE if not exists site_url (
            SiteUrlID               int AUTO_INCREMENT PRIMARY KEY,
            RequestUrl              varchar(255),
            UrlType                 int,
            MetaDataID              int,
            FOREIGN KEY(MetaDataID) REFERENCES meta_data(M_ID)
        );"""
        insert_create_site_url_value = "INSERT INTO site_url (RequestUrl,UrlType,MetaDataID) VALUES (%s,%s,%s);"
        datas = (urlDetail[0], urlDetail[1], urlDetail[2])
        db_cursor.execute(create_site_url_table)
        db_cursor.execute(insert_create_site_url_value,datas)
        print("url inserted !!!")

        db_connection.commit() # when working with table data.
        db_connection.close()

    except Exception as e:
        print("Exception caught ==> ", e)












        # create_site_url_table = """CREATE TABLE if not exists site_url (
        #     SiteUrlID               int AUTO_INCREMENT PRIMARY KEY,
        #     RequestUrl              varchar(255),
        #     UrlType                 int(1),
        #     MetaDataID              FOREIGN KEY MetaDataID REFERENCES meta_data(MetaDataID)
                                #     FOREIGN KEY(Writer_id) REFERENCES Writers(Id)
        # );"""