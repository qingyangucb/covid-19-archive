# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getData/<date>/<counties>")
def getData(date, counties):


    results = [date, counties, 'this is your results']  
    
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
