from entities.wlan_class import Wlan
from services.wlan_scanner import WLANScanner
from repository.wlan_repository import WlanSqlManagement

ws = WLANScanner()

def run():
    ssid_list = ws.get_ssid_profiles_list()
    for wlan in ssid_list:
        pssw = ws.get_ssid_password(wlan)
        new_wlan = Wlan(ssid=wlan, password=pssw)    

        WlanSqlManagement(new_wlan).post_wlan()

if __name__ == '__main__':
    run()