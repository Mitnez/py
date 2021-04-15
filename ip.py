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

print (lgreen+bold+"         <===[[ coded by N17RO ]]===> \n"+clear)
print (yellow+bold+"   <---(( search on youtube Noob Hackers ))--> \n"+clear)
print (yellow+bold+"   <---(( Traducido por m1t xdxd ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victima]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[Proveedor]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organizacion]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[Ciudad]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitud]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitiud]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Zona horaria]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Codigo postal]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Adios, ten un buen dia :)'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" No tengo internet, no sirvo"+clear)
sys.exit(1)