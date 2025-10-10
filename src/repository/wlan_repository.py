from entities.wlan_class import Wlan
import sqlite3
import os

class WlanSqlManagement:
    DATABASE = os.path.join(os.getcwd(),'db\\wlan_backup.db')
    db_conector = sqlite3.connect(DATABASE)
    cursor = db_conector.cursor()

    def __init__(self, wlan_obj: Wlan) -> None:
        self.wlanObj = wlan_obj
        
    def post_wlan(self):
        data = self.wlanObj.to_dict()
        try:
            self.cursor.execute("INSERT INTO wlan (ssid, password) VALUES(?, ?) ON CONFLICT(ssid) DO UPDATE SET password = excluded.password", (data.get("ssid"),data.get("password")))
        except sqlite3.IntegrityError as e:
            print(e)
        self.db_conector.commit()