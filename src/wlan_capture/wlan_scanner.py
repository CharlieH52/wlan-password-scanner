import os
import re
from datetime import date
from src.wlan_capture.command_processor import CommandProcessor

workingPath = os.getcwd()
storageFile = os.path.join(workingPath, 'localStorage.json')

class WLANScanner:
    SEARCH_LINE = r'(?<=: ).*'
    CLEAN_LINE = r'(.*\s:\s)'

    CMD_SSID = ["netsh", "wlan", "show", "profiles"]
    CMD_PASSWORD = ["netsh", "wlan", "show", "profiles", "", "KEY=CLEAR"]
    
    def __init__(self):
        self.today = date.strftime(date.today(),'%d-%m-%Y')

    def __parse_ssid_output(self, command_output: list[str]) -> list[str]:
        ssid_list = []
        for line in command_output:
            ssid = re.search(self.SEARCH_LINE, line)
            if ssid:
                ssid_name = re.sub(self.CLEAN_LINE, '', line)
                ssid_list.append(ssid_name)
        return ssid_list

    def get_ssid_profiles_list(self) -> list[str]:
        to_parse = CommandProcessor(command=self.CMD_SSID).stdout_to_list()
        return self.__parse_ssid_output(to_parse)

    def __parse_password_output(self, command_output: list[str]) -> str:
        pssw = ""
        for line in command_output:
            if 'Contenido' in line:
                pssw = re.sub(self.CLEAN_LINE, '', line)
        return pssw 

    def get_ssid_password(self, ssid: str) -> str:
        CMD_LINE = self.CMD_PASSWORD
        CMD_LINE[4] = f'name={ssid}'
        to_parse = CommandProcessor(CMD_LINE).stdout_to_list()
        return self.__parse_password_output(to_parse)