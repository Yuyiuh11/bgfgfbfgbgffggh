from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # (opcional) guardar IPs
    with open("ips.txt", "a", encoding="utf-8") as f:
        f.write(f"{time} | {ip}\n")

    return render_template("index.html", ip=ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
