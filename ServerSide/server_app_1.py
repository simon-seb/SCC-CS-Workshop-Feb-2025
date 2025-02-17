# Using flask to make an api
# import necessary libraries and functions
import read_data_file as file_reader
from flask import Flask, jsonify, request, render_template

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route("/resources", methods=["GET", "POST"])
def home():
    response = {"data": ""}

    if request.method == "GET":
        response["data"] = file_reader.get_file_contents_as_json()
        return response


@app.route("/", methods=["GET"])
def homepage():
    return render_template("SAMP_Architecture_1.html")


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route("/home/<int:num>", methods=["GET"])
def disp(num):

    return jsonify({"data": num**2})


# driver function
if __name__ == "__main__":

    app.run(debug=True)
