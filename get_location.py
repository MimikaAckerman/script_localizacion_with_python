import requests
import json

# Obtener la dirección IP pública
import re
import urllib.request

def get_public_ip():
    data = str(urllib.request.urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

public_ip = get_public_ip()
print(f"Tu dirección IP pública es: {public_ip}")

# Utilizar la API de ip-api.com para obtener la ubicación geográfica
url = f"http://ip-api.com/json/{public_ip}"

response = requests.get(url)
data = json.loads(response.text)

if data["status"] == "success":
    
    print(f"Ciudad: {data['city']}")
    print(f"RegiónName: {data['regionName']}")
    print(f"País: {data['country']}")
    print(f"zip: {data['zip']}")
    print(f"Coordenadas: {data['lat']}, {data['lon']}")
else:
    print("Error al obtener la ubicación geográfica.")