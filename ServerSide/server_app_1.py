# Using flask to make an api
# import necessary libraries and functions
import file_reader_writer as file_reader
from flask import Flask, jsonify, request, render_template, redirect, url_for
import json

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route("/resources", methods=["GET", "POST"])
def home():
    response = {"data": ""}

    if request.method == "GET":
        response["data"] = file_reader.get_file_contents_as_json("RES")
        return response


# Write Resources data to CSV
@app.route("/update_resources", methods=["POST"])
def update_resources():
    form_data = ""
    headers = "image_url,name,designation,description\n"

    form_data = (
        form_data
        + request.form["image_url"]
        + ","
        + request.form["name"]
        + ","
        + request.form["designation"]
        + ","
        + request.form["description"]
    )

    file_reader.write_to_file(headers, form_data, "RES")

    return render_template("Config_Page.html")


# Contact Us CTA
@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():

    if request.method == "POST":
        form_data = ""
        headers = "Name,Email,Subject,Comment\n"

        form_data = (
            form_data
            + request.form["Name"]
            + ","
            + request.form["Email"]
            + ","
            + request.form["Subject"]
            + ","
            + request.form["Comment"]
        )

        file_reader.write_to_file(headers, form_data, "CON")

        return render_template("SAMP_Architecture_1.html")

    if "GET" == request.method:
        response = {"data": ""}
        
        response["data"] = file_reader.get_file_contents_as_json("CON")
        return response


@app.route("/", methods=["GET"])
def homepage():
    return render_template("SAMP_Architecture_1.html")


@app.route("/config", methods=["GET"])
def config_page():
    return render_template("Config_Page.html")


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
