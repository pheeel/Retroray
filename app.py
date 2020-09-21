import os, imghdr
from flask import Flask, render_template, send_from_directory, request, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".gif"]
app.config["UPLOAD_PATH"] = "static/uploads"
app.config["RESULT_PATH"] = "static/result"


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    file_format = imghdr.what(None, header)
    if not file_format:
        return None
    return "." + (file_format if file_format != "jpeg" else "jpg")


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/editor", methods=["POST", "GET"])
def upload():
    # Create a target folder for the uploaded image
    target = os.path.join(APP_ROOT, app.config["UPLOAD_PATH"])
    if not os.path.isdir(target):
        os.mkdir(target)

    # Handle image
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    destination = "/".join([target, filename])

    # Image file validation
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config[
            "UPLOAD_EXTENSIONS"
        ] or file_ext != validate_image(uploaded_file.stream):
            abort(400)
        #  Save image into the Target and render the template
        uploaded_file.save(destination)
    return render_template("editor.html", image_name=filename)


@app.route("/editor", methods=["POST"])
def on_submit(filename):
    target = os.path.join(APP_ROOT, app.config["RESULT_PATH"])
    if not os.path.isdir(target):
        os.mkdir(target)

    return send_from_directory("static/result", filename)
    # if request.form.get("submit_button") == "See result" and request.method == "POST":
    #     return render_template("editor.html", image_name=filename)


@app.route("/edit/<filename>")
def show_original_image(filename):
    print(filename)
    return send_from_directory(app.config["UPLOAD_PATH"], filename)


@app.route("/edit/<filename>")
def show_edited_image(filename):
    print(filename)
    return send_from_directory(app.config["RESULT_PATH"], filename)


if __name__ == "__main__":
    app.run(debug=True)
