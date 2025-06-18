import json

class Wlan:
    def __init__(self, ssid, password, upDate):
        self.ssid = ssid
        self.password = password
        self.saveDate = upDate

    def to_dict(self):
        return {
            'ssid': self.ssid,
            'password': self.password,
            'upDate': self.saveDate
        }

    @staticmethod
    def load_from_json(file_path):
        with open(file_path, "r") as jsonFile:
            data = json.load(jsonFile)
            return [Wlan(**item) for item in data]
