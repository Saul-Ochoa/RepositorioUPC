# Importar las librerias
import requests
import pandas as pd
import time
import os
import warnings
warnings.filterwarnings('ignore')

# obtener la información de la api
def get_exchange_rate():
    url='https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return{
            "Fecha": data['fecha'],
            "Compra": data['compra'],
            "Venta": data['venta'],
            "Origen": data['origen'],
            "Moneda": data['moneda']
        }
    else:
        print('Error obtener los datos')
        return None
    
# Guardar la información en el save_to_csv
def save_to_csv(data,filename='tipo_cambio.csv'):
    if not os.path.exists(filename):
        df=pd.DataFrame([data])
        df.to_csv(filename,index=False)
    else:
        df=pd.read_csv(filename)
        
        # Verificar si la ultima entrada es diferente antes de guardar
        if df.iloc[-1]['Fecha']!=data['Fecha']:
            df=df.append(data,ignore_index=True)
            print('Nuevo tipo de cambio guardado')
        else:
            print('No hay cambios en el tipo de cambio')
            
            
# llamar a la funciones para obtener el precio del dolar
exchange_rate=get_exchange_rate()
save_to_csv(exchange_rate)