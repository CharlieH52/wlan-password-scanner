
from entities.wlan_class import Wlan
from dotenv import load_dotenv
import psycopg2
import sqlite3
import os

class WlanSqlManagement:
    load_dotenv()
    LOCAL = os.getenv("dblocal")
    # LocalStorage
    DATABASE = os.path.join(os.getcwd(),f'{LOCAL}')
    db_conector = sqlite3.connect(DATABASE)
    cursor = db_conector.cursor()

    # Remote
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    def __init__(self, wlan_obj: Wlan) -> None:
        self.wlanObj = wlan_obj
        self.remoteDB = psycopg2.connect(
            user=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
            dbname=self.DBNAME
        )
        
    def post_wlan(self):
        data = self.wlanObj.to_dict()
        try:
            self.cursor.execute("INSERT INTO wlan (ssid, password) VALUES(?, ?) ON CONFLICT(ssid) DO UPDATE SET password = excluded.password", (data.get("ssid"),data.get("password")))
        except sqlite3.IntegrityError as e:
            print(e)
        self.db_conector.commit() 
        
    def send_to_remote(self): 
        data = self.wlanObj.to_dict()
        cursor = self.remoteDB.cursor()
        cursor.execute("INSERT INTO wlan (ssid, password) VALUES(%s, %s) ON CONFLICT(ssid) DO UPDATE SET password = excluded.password;", (data.get("ssid"),data.get("password")))
        self.remoteDB.commit()
        cursor.close()
        self.remoteDB.close()