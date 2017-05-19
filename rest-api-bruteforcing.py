import os
import sys
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Intenta descubri mediante fuerza bruto los servicios REST expuestos')
parser.add_argument('-u','--url',  help='Direccion del dominio de destino')
parser.add_argument('-f','--file',help='Ubicacion del diccionario con los posibles verbos')

print("""
                 _   _____  ______  _____ _______ 
     /\         (_) |  __ \|  ____|/ ____|__   __|
    /  \   _ __  _  | |__) | |__  | (___    | |   
   / /\ \ | '_ \| | |  _  /|  __|  \___ \   | |   
  / ____ \| |_) | | | | \ \| |____ ____) |  | |   
 /_/    \_\ .__/|_| |_|  \_\______|_____/   |_|   
          | |                                     
          |_|                                     

""")
print('')
os.system('clear')
args = parser.parse_args()
servicios = open(args.Diccionario)
for s in servicios:
    if s:
        try:
           api = args.Url + s
           response = requests.get(api.strip(), verify=True)

           if (response.ok):
              print('{}[0;93m {}-[OK] {}[0m'.format(chr(27),api, chr(27)))
           else:
              print('{}[0;91m {}-[failed] {}[0m'.format(chr(27),api.strip(), chr(27)))
              print('{}[0;93m {}'.format(chr(27),response.json()))
        except Exception as ex:
              print(chr(27) + '[0;31m' +ex + chr(27)+'[0m')
              print(response)
              pass





