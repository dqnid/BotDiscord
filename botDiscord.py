import requests
import sys
import datetime

url = "https://discord.com/api/webhooks/948910007146143784/KyCOCSsFdsFdzEWvp43dOK_qooHI5UDi358fwFQCPSyJM2F6_4903A5f-JRgT7heX3DJ"
dia = datetime.datetime.now()
if sys.argv[1] == '0':
    estado = "El sistema se ha arrancado: "
else:
    estado = "El sistema se ha apagado: "
mensaje = estado + str(dia)
data = {
    "content" : str(mensaje),

    "username" : "BotSystemdAS"
}


result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Mensaje entregado correctamente, cod {}.".format(result.status_code))
