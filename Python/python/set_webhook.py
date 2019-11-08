from decouple import config
from pprint import pprint
import  requests




token = config('TOKEN') 
base_url = f'https://api.telegram.org/bot{token}'
#url =  "c89766cc.ngrok.io"
url="heesu40.pythonanywhere.com"
setweb_url =  f'/setWebhook?url={url}'

req = requests.get(base_url+setweb_url).json()
pprint(req)