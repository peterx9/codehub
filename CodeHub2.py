from werkzeug.utils import secure_filename
import os

# Define upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif', 'bmp'}

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected image file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        category = request.form.get('category')
        title = request.form.get('title')

        insert_image(category, title, filename)

        return jsonify({'success': 'Image uploaded successfully'})

    return jsonify({'error': 'Invalid file format'})

def insert_image(category, title, filename):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO images (category, title, url) VALUES (?, ?, ?)''', (category, title, filename))
    connection.commit()
    connection.close()
