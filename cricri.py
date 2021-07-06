import urllib.request
import json
import argparse

parser =  argparse.ArgumentParser()
parser.add_argument("-ip","--ip", help="Inserta la IP de la persona a localizar :D")
parser =  parser.parse_args()

server1 = 'http://soporteweb.com'
consulta =  urllib.request.build_opener()
consulta.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]

#################################################
def geolocalizacion(sacada):
    ip = sacada
    url = "https://ipinfo.io/" + ip + "/json"
    abrirURL = urllib.request.urlopen(url)
    cargarURL = json.load(abrirURL)
    for i in cargarURL:
        print( i + ": " + cargarURL[i])
##################################################

print('''
 _____      _ _____      _     __   _____ 
/  __ \    (_)  __ \    (_)   /  | |  _  |
| /  \/_ __ _| /  \/_ __ _    `| | | |/' |
| |   | '__| | |   | '__| |    | | |  /| |
| \__/\ |  | | \__/\ |  | |   _| |_\ |_/ /
 \____/_|  |_|\____/_|  |_|   \___(_)___/ 
\n
''')

if parser.ip:
    ip = parser.ip
    localizacion = geolocalizacion(ip)
else:
    print("No hay ningun argumento, te dare tu info\n ")
    try:
        url =  consulta.open(server1, timeout=17)
        respuesta =  url.read()
        respuesta =  respuesta.decode('UTF-8')
        print("Tu ip es: " + respuesta)
    except:
        print("Hubo un error lol")
    localizacion = geolocalizacion(respuesta)