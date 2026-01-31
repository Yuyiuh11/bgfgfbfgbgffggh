from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ip")
def get_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return jsonify({"ip": ip})

if __name__ == "__main__":
    app.run()
