from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Deta Space!</h1><p>This app is online 24/7 🎉</p>"

if __name__ == "__main__":
    # Deta Space gebruikt standaard poort 8080
    app.run(host="0.0.0.0", port=8080)
