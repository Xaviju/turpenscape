from flask import Flask, render_template, request, redirect
import base64
from utils.palette_gen import generate_palette
from utils.slug import slugify

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/palettes')
def palettes():
    return render_template('palettes.html')

@app.route('/', methods=['GET', 'POST'])
def home():
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

            palette = generate_palette(file)
            palette_name = slugify(request.form['palette_name'])

            template = render_template(
                'palette.gpl',
                palette=palette,
                palette_name=palette_name
            )

            file.seek(0)
            image = base64.b64encode(file.read())
            image = image.decode("utf-8")

            return render_template(
                'palette.html',
                palette=palette,
                palette_name=palette_name,
                template=template,
                image=image
            )

    return render_template('create.html')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
