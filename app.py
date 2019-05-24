import os

from flask import Flask, render_template, send_from_directory, request


app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def retroray_app():
    return render_template('home.html')


@app.route("/editor", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        destination = '/'.join([target, filename])
        print(destination)
        file.save(destination)
        return render_template('editor.html', image_name=filename)

@app.route('/edit/<filename>')
def show_original_image(filename):
    print(filename)
    return send_from_directory('static/images', filename)