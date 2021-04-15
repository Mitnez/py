# traducido por m1t (creditos noob-hackers)

# modulos reequeridos
import argparse
import requests, json
import sys
from sys import argv
import os

# ni puta idea realmente, m1t del futuro sabe que onda

parser = argparse.ArgumentParser()

parser.add_argument ("-ip", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#banner of script

print ("         <===[[ coded by N17RO ]]===> \n")
print ("   <---(( search on youtube Noob Hackers ))--> \n"+clear)
print ("   <---(( Traducido por m1t xdxd ))--> \n")


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        print ("[Victima]:", data['query'])
        print("<--------------->")
        print ("[Proveedor]:", data['isp'])
        print("<--------------->")
        print ("[Organizacion]:", data['org'])
        print("<--------------->")
        print ("[Ciudad]:", data['city'])
        print("<--------------->")
        print ("[Region]:", data['region'])
        print("<--------------->")
        print ("[Longitud]:", data['lon'])
        print("<--------------->")
        print ("[Latitiud]:", data['lat'])
        print("<--------------->")
        print ("[Zona horaria]:", data['timezone'])
        print("<--------------->")
        print (a, "[Codigo postal]:", data['zip'])

except KeyboardInterrupt:
        print ('Adios, ten un buen dia :)')
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print ("[~]"+" No tengo internet, no sirvo")
sys.exit(1)