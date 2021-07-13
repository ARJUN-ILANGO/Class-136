from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "data":data,
        "message":"success"
    }),200

@app.route("/planet")
def pl():
    name = request.args.get("name")
    planet_info = next(item for item in data if item["name"] == name)
    return jsonify({
        "data":planet_info,
        "message":"success"
    }),200

if __name__ == "__main__":
    app.run()
