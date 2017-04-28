import sys
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Intenta descubri mediante fuerza bruto los servicios REST expuestos')
parser.add_argument('--url', dest='Url')
parser.add_argument('--file',dest='Diccionario')

args = parser.parse_args()
servicios = open(args.Diccionario)
for s in servicios:
    try:
       api = args.Url + s
       response = requests.get(api.strip(), verify=True)
       if (response.ok):
           print('{}[0;93m {}-[OK] {}[0m'.format(chr(27),args.Url, chr(27)))
       else:
           print('{}[0;91m {}-Failed {}[0m'.format(chr(27),args.Url, chr(27)))
    except Exception as ex:
           print(chr(27) + '[0;31m' +ex + chr(27)+'[0m')
           pass




