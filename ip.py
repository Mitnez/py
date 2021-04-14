# Codigo por m1t (basdo en noob-hackers)

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-ip", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()
 
 # banner que el mit se diseño 
 print("                   ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀          Hecho por m1t ")
                
                ip= args.target
                api = "http://ip-api.com/json/"
                try
                data = requests.get(api+ip).json()
                sys.stdout.flush()
                rint (a, "[Victim]:", data['query'])
                        print(red+"<--------------->"+red)
                        print (b, "[ISP]:", data['isp'])
                        print(red+"<--------------->"+red)
                        print (a, "[Organisation]:", data['org'])
                        print(red+"<--------------->"+red)
                        print (b, "[City]:", data['city'])
                        print(red+"<--------------->"+red)
                        print (a, "[Region]:", data['region'])
                        print(red+"<--------------->"+red)
                        print (b, "[Longitude]:", data['lon'])
                        print(red+"<--------------->"+red)
                        print (a, "[Latitude]:", data['lat'])
                        print(red+"<--------------->"+red)
                        print (b, "[Time zone]:", data['timezone'])
                        print(red+"<--------------->"+red)
                        print (a, "[Zip code]:", data['zip'])
                        print (" "+yellow)
                        
                       except KeyboardInterrupt:
                        print ("Acabando programa adios")
                        sys.exit(0)
                       except requests.exceptions.ConnectionError as e:
                        print ("Checa la conexion a internet porque si no no sirvo")
                       sys.exit(1)                        
                
                
                