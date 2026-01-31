from flask import Flask, request
from datetime import datetime
import requests
import os

app = Flask(__name__)
LOG_FILE = "ips.txt"

def ip_info(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp")
        data = r.json()
        if data["status"] == "success":
            return f'{data["country"]}, {data["regionName"]}, {data["city"]}, {data["isp"]}'
    except:
        pass
    return "No disponible"

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info = ip_info(ip)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time} | {ip} | {info} | {ua}\n")

    return """
    <h1>Bienvenido</h1>
    <p>Este sitio registra IPs y ubicación aproximada con fines técnicos.</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
