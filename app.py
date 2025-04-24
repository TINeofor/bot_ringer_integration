
from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/mensagem", methods=["POST"])
def receber_mensagem():
    dados = request.json
    msg = dados.get("mensagem", "").lower()
    numero = dados.get("numero", "")

    # Aqui estariam as chamadas para salvar em planilha e responder com IA
    if "falar com atendente" in msg or "marcar consulta" in msg:
        resposta = "Tudo certo! Encaminhando você para um atendente agora mesmo. 😊"
    else:
        resposta = "Resposta automatizada via IA aqui..."

    requests.post("https://api.ringer.com.br/whatsapp/send", json={
        "numero": numero,
        "mensagem": resposta
    }, headers={"Authorization": f"Bearer {os.getenv('RINGER_TOKEN', 'SEU_TOKEN_AQUI')}"})

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
