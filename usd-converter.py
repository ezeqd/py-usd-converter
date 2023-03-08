import argparse
import requests
from bs4 import BeautifulSoup

# Definir los argumentos que se esperan recibir desde la línea de comandos
parser = argparse.ArgumentParser(description='Conversión de moneda')
parser.add_argument('monto', type=float, help='Monto a convertir')
parser.add_argument('moneda', type=str, help='Moneda a convertir (ARS o cualquier otra)', choices=['ARS', 'Otra'])
args = parser.parse_args()

# Definir la URL de donde se obtendrá la cotización del USD
url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

try:
    # Obtener el contenido de la URL
    response = requests.get(url)
    # Convertir el contenido en formato HTML a un objeto de BeautifulSoup para poder manipularlo
    soup = BeautifulSoup(response.content, 'html.parser')
    # Buscar el valor del USD en la página
    usd = float(soup.find(string='Dolar Oficial').find_next('td').text.replace(',', '.'))
except:
    print('No se pudo obtener la cotización del USD')
    exit()

# Convertir el monto ingresado a USD
if args.moneda == 'ARS':
    resultado = args.monto / usd
else:
    resultado = args.monto

# Mostrar el resultado
print('Cotización del USD: ${}'.format(usd))
print('{} {} equivalen a ${} USD'.format(args.monto, args.moneda, resultado))
