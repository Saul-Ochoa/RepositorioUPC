# Importar las librerias
import requests
import pandas as pd
import time
import os
import warnings
warnings.filterwarnings('ignore')

# Obtener la información de la API
def get_exchange_rate():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "Fecha": data['fecha'],
            "Compra": data['compra'],
            "Venta": data['venta'],
            "Origen": data['origen'],
            "Moneda": data['moneda']
        }
    else:
        print('Error al obtener los datos')
        return None

# Guardar la información en CSV
def save_to_csv(data, filename='tipo_cambio.csv'):
    if not os.path.exists(filename):
        df = pd.DataFrame([data])
        df.to_csv(filename, index=False)
    else:
        df = pd.read_csv(filename)
        
        # Verificar si la última entrada es diferente antes de guardar
        if df.iloc[-1]['Fecha'] != data['Fecha']:
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)  # Cambio aquí
            df.to_csv(filename, index=False)  # Asegurar que se guarde el archivo
            print('Nuevo tipo de cambio guardado')
        else:
            print('No hay cambios en el tipo de cambio')

# Llamar a las funciones para obtener el precio del dólar
exchange_rate = get_exchange_rate()
if exchange_rate:
    save_to_csv(exchange_rate)
