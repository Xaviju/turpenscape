from flask import Flask, render_template, request, redirect, url_for, send_file
from io import BytesIO
from palette_gen import generate_palette

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            palette = generate_palette(file)
            palette_name = request.form['palette_name']
            template = render_template('palette.gpl', palette=palette, palette_name=palette_name)

            # import ipdb; ipdb.set_trace()
            palette_file = BytesIO()
            palette_file.write(bytes(template, encoding="utf-8"))
            palette_file.seek(0)

            return send_file(palette_file, mimetype="application/octet-stream", as_attachment=True, attachment_filename="{palette_name}.gpl".format(palette_name=palette_name))

            # return redirect(url_for('upload'))
            # return redirect(url_for('uploaded_file', filename=filename))
    return render_template('home.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

# url_for('static', filename='style.css')
# url_for('static', filename='script.js')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
