import os
import json

class Writer:    
    WORKING_PATH = os.getcwd()
    FILE_NAME = "localStorage.json"
    STORAGE_FILE = os.path.join(WORKING_PATH, FILE_NAME)
    
    def __init__(self):
        self.check_local_storage()

    def check_local_storage(self):
        try:
            if not os.path.exists(self.STORAGE_FILE):
                with open(self.STORAGE_FILE, "w") as file:
                    json.dump([], file)
        except OSError as e:
            pass
        
    def read_local_storage(self) -> list[dict[str, str]]:
        try:
            with open(self.STORAGE_FILE, "r") as file:
                current_data = json.load(file)
                return current_data
        except OSError as e:
            return []
    
    def __check_duplicity_data(self, incoming: dict[str, str]) -> list[dict[str, str]]:
        current_data = self.read_local_storage()
        key_chain = "ssid"
        for index, wlan in enumerate(current_data):
            if incoming[key_chain] == wlan.get(key_chain):
               current_data[index] = incoming
               break
        else:
            current_data.append(incoming)
        return current_data
     
    def save_data_in_file(self, new_data: dict[str, str]):
        updated_data = self.__check_duplicity_data(new_data)
        try:
            with open(self.STORAGE_FILE, "w") as file:
                json.dump(updated_data, file, indent=4)
        except OSError as e:
            print(e)
    