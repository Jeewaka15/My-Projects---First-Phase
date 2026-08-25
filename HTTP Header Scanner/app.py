from flask import Flask, render_template, request
from scanner import scan_url

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    url = request.form.get("url")
    result = scan_url(url)

    if "error" in result:
        return render_template("result.html", error=result["error"])

    return render_template("result.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)