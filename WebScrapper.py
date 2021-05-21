from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://mexico.as.com/resultados/futbol/mexico_clausura/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Equipos
eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()

count = 0
for i in eq:
    if count<20:
        equipos.append(i.text)
    else:
        break
    count+=1


# PUNTOS
pt = soup.find_all('td', class_='destacado')

puntos = list()

count = 0
for i in pt:
    if count<20:
        puntos.append(i.text)
    else:
        break
    count+=1


df = pd.DataFrame({'Nombre': equipos, 'Puntos':puntos}, index=list(range(1,21)))
print(df)

print("¿Quieres crear un archivo?[y/n]")
decision= input()
if (decision =='y'):
    df.to_csv('Clasificacion.csv', index=False)
    print("Archivo creado, hasta la próxima")
else:
    print("Hasta luego")

