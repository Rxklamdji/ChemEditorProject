from flask import Flask, redirect, url_for, render_template, request
from flask import Request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        search = ""
        return redirect(url_for())
    else:
        return render_template('index.html')

@app.route("/<src>")
def search(src):
    return ""



if __name__ == "__main__":
    app.run(debug=True)


