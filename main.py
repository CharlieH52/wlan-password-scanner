from src.data_management import Writer
from src.wlan_class import Wlan
from src.wlan_scanner import WLANScanner

ws = WLANScanner()
wr = Writer()

def run():
    ssid_list = ws.get_ssid_profiles_list()
    for wlan in ssid_list:
        pssw = ws.get_ssid_password(wlan)
        new_wlan = Wlan(ssid=wlan, password=pssw, upDate=ws.today).to_dict()
        wr.save_data_in_file(new_wlan)    

if __name__ == '__main__':
    run()