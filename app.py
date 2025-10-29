from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "✅ FireMigrate Flask is running."

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    # 개발용 실행(참고): python app.py
    app.run(host="0.0.0.0", port=8000, debug=True)
