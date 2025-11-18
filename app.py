from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])

def index():
   if request.method == "POST":
       return redirect(url_for("gato"))
   
   return render_template("index.html")



@app.route("/gato")
def gato():   
    return render_template("gato.html")

if __name__ == "__main__":
    app.run(debug=True)