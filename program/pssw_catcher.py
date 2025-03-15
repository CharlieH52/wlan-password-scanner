import os
import re
import subprocess
from constants import *

class PasswordCatcher:
    def __init__(self):
        self.ssid_list = []

        # Pre-Process
        self._ssid_reader()

        self._catch_onload()
    
    def _catch_onload(self):
        for id in self.ssid_list:
            password = self._password_reader(ssid=id)
            self._write_ssid_file(ssid=id, pssw=password)

    def _ssid_reader(self):
        profiles = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for ssid in profiles:
            id = re.search(SEARCH_LINE, ssid)
            if id:
                cleared = re.sub(CLEAN_LINE, '', ssid)
                self.ssid_list.append(cleared)

    def _password_reader(self, ssid):
        command_out = subprocess.getoutput(f"netsh wlan show profiles name={ssid} KEY=CLEAR").split('\n')
        for pssw in command_out:
            if "clave" in pssw:
                clear_pssw = re.sub(CLEAN_LINE, '', pssw)
                return clear_pssw
            
    def _write_ssid_file(self, ssid, pssw):
        new_file = os.path.join(f'{PATHS["saves"]}\\{ssid}.txt')
        print(new_file)
        with open(new_file, 'w') as file:
            credentials = (
                f'SSID: {ssid}\n'
                f'PASS: {pssw}'
            )

            file.write(credentials)

    def _file_checker(self, ssid, pssw):
        # SSID Checker
        
        # PASSWORD Checker
        pass

ps = PasswordCatcher()
'''
Es necesario crear una función que rectifique la existencia de una carpeta llamada "saves" en la raiz, si esta no existe,
debe crearla.

Ademas la funcion file checker, debe listar los archivos dentro de la carpeta 'saves' con la lista de redes que acaba de crear
al cargar el programa, si los nombres SSID coinciden, debe comparar ahora la contrasena que contiene, si son identicos ambos,
la creacion del archivo se descarta, de lo contrario si la contrasena no coincide, crea el archivo con un parametro extra y la
contrasena nueva.

Se deben verificar estos dos puntos ANTES de que se cree algun archivo, para evitar la sobre escritura y la acumulacion.

Agregar un boton para borrar el archivo seleccionado en el dropdown.


'''