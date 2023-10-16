import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=anies-baswedan&apiKey=e390520d248a47b4a1902e94153003be"
request = requests.get(url)
content = request.json()

body = " "
for article in content["articles"]:
    body = body + article["title"] + '\n' + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)