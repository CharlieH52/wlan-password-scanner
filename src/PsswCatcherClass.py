import os
import re
import json
import subprocess
from datetime import date
from src.WlanClass import Wlan

workingPath = os.getcwd()
storageFile = os.path.join(workingPath, 'localStorage.json')

# Profile output regular expressions
SEARCH_LINE = r'(?<=: ).*'
CLEAN_LINE = r'(.*\s:\s)'

class PasswordCatcher:
    def __init__(self):
        self.today_date = date.strftime(date.today(),'%d-%m-%Y')
        self.check_localstorage()
        self.saved_wlans = Wlan.load_from_json(storageFile)
        self.ssid_list = []
        self.get_ssid_profiles_list()
        self.device_wlans = self.get_wlan_data()
        self.save_passwords_onload()

    def check_localstorage(self):
        try:
            if not os.path.exists(storageFile):
                self.create_localstorage()
        except PermissionError as e:
            print(e)

        except OSError as e:
            print(e)

    def create_localstorage(self):
        try:
            with open(storageFile, "w") as jsonFile:
                json.dump([],jsonFile)
        except PermissionError as e:
            print(e)

        except OSError as e:
            print(e)

    def get_ssid_profiles_list(self):
        ssid_list = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for ssid in ssid_list:
            name = re.search(SEARCH_LINE, ssid)
            if name:
                ssid_name = re.sub(CLEAN_LINE, '', ssid)
                self.ssid_list.append(ssid_name)

    def get_ssid_password(self, ssid):
        command_out = subprocess.getoutput(f"netsh wlan show profiles name={ssid} KEY=CLEAR").split('\n')
        for pssw in command_out:
            if "clave" in pssw:
                clear_pssw = re.sub(CLEAN_LINE, '', pssw)
                return clear_pssw

    def get_wlan_data(self):
        new_list = []
        for ssidName in self.ssid_list:
            password = self.get_ssid_password(ssid=ssidName)
            wlan = Wlan(ssid=ssidName, password=password, upDate=self.today_date)
            new_list.append(wlan.to_dict())
        return new_list

    def json_to_object(self, json_data):
        return [Wlan(**wlan) for wlan in json_data]

    def save_passwords_onload(self):
        new_list = self.json_to_object(self.device_wlans)
        for new_wlan in new_list:
            if not any(saved_wlan.ssid == new_wlan.ssid for saved_wlan in self.saved_wlans):
                self.saved_wlans.append(new_wlan)
        self.add_to_localstorage()    

    def add_to_localstorage(self):
        with open(storageFile, "w") as jsonFile:
            update = []
            for i in self.saved_wlans:
                update.append(i.to_dict())
            json.dump(update, jsonFile, indent=4)