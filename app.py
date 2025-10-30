from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔧 여기서 고정 시스템 역할 정의
SYSTEM_PROMPT = (
    "너는 지금 방화벽 엔지니어로서의 역할을 수행중이야. "
    "사용자가 보낸 방화벽 설정(config) 내용에서 username의 리스트를 읽고 "
    "username:password 형태로만 응답해야 해. "
    "불필요한 설명이나 문장은 절대 포함하지 마."
)


@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None

    if request.method == "POST":
        user_input = request.form.get("user_prompt")

        if user_input:
            # 실제 요청 시 system 프롬프트 + user 데이터 조합
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input},
                ],
            )
            response_text = completion.choices[0].message.content

    return render_template("index.html", response_text=response_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
