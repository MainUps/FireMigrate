from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

# 🔑 .env 파일 로드
load_dotenv()

app = Flask(__name__)

# 환경변수에서 키 불러오기
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None

    if request.method == "POST":
        user_prompt = request.form.get("user_prompt")

        if user_prompt:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_prompt},
                ],
            )
            response_text = completion.choices[0].message.content

    return render_template("index.html", response_text=response_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
