# API_request.py
import requests

CHANNEL_ID = "2943258"
READ_API_KEY = "G3BDQS6I5PRGFEWR"
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=15"

def requisicao():
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            feeds = data.get("feeds", [])

            labels = []
            temperaturas = []
            umidades = []

            for feed in feeds:
                hora = feed.get("created_at", "N/A")
                temperatura = feed.get("field1")
                umidade = feed.get("field2")

                # Conversão segura para float
                try:
                    temperatura = float(temperatura) if temperatura is not None else None
                except ValueError:
                    temperatura = None

                try:
                    umidade = float(umidade) if umidade is not None else None
                except ValueError:
                    umidade = None

                labels.append(hora)
                temperaturas.append(temperatura)
                umidades.append(umidade)

            # Valores atuais (últimos valores)
            temperatura_atual = temperaturas[-1] if temperaturas else None
            umidade_atual = umidades[-1] if umidades else None
            
            return {
                "labels": labels, 
                "temperaturas": temperaturas, 
                "umidades": umidades,
                "temperatura_atual": temperatura_atual,
                "umidade_atual": umidade_atual
            }

        else:
            print(f"Erro na requisição: {response.status_code}")
            return {
                "labels": [], 
                "temperaturas": [], 
                "umidades": [],
                "temperatura_atual": None,
                "umidade_atual": None
            }

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return {
            "labels": [], 
            "temperaturas": [], 
            "umidades": [],
            "temperatura_atual": None,
            "umidade_atual": None
        }
