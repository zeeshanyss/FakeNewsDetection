from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

# Dummy function for Fake News detection (Replace with ML Model if needed)
def check_fake_news(text):
    confidence = round(random.uniform(60, 99), 2)
    result = "Real" if random.choice([True, False]) else "Fake"
    return result, confidence

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    url = request.form.get("url")
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.title.string if soup.title else "No Title Found"
        text = " ".join([p.get_text() for p in soup.find_all("p")])

        if not text.strip():
            return jsonify({"status": "error", "message": "Unable to extract content"})

        result, confidence = check_fake_news(text)
        return jsonify({"status": "success", "title": title, "result": result, "confidence": confidence, "url": url})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Unable to extract content: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
