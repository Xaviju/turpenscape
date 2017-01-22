import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, after_this_request
from werkzeug.utils import secure_filename
from palette_gen import generate_palette

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = '/static/uploads'
UPLOAD_FOLDER = '/home/xaviju/Projects/2017/turpenscape/static/uploads'

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/palette', methods=['GET', 'POST'])
def palette():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            palette = generate_palette(file)
            palette_name = request.form['palette_name']

            template = render_template('palette.gpl', palette=palette, palette_name=palette_name)

            # @after_this_request
            # def remove_file(response):
            #      os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # filename = secure_filename(file.filename)
            # palette_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # palette_file_edit = open(palette_file, "w")
            # palette_To_File = raw_input(template)
            # palette_file_edit.write(palette_To_File)
            # palette_file_edit.close()
            #
            # with open("{}.gpl".format(filename), "r+") as palette_file:
            #     palette_file.write(template)
            #     palette_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # send_file(palette_file, mimetype="application/octet-stream", as_attachment=True, attachment_filename="{palette_name}.gpl".format(palette_name=palette_name))

            return render_template('palette.html', palette=palette, palette_name=palette_name, template=template, filename=filename)

    return render_template('create.html')

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
