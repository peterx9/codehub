from PIL import Image
import numpy as np
import tensorflow as tf

# Load pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))

def predict_image_category(image_path):
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image_path))
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions.numpy())

    # Assuming the top prediction is the category
    category = decoded_predictions[0][0][1]
    return category

def insert_image(category, title, filename):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Predict category using neural network
    predicted_category = predict_image_category(filename)

    cursor.execute('''INSERT INTO images (category, title, url, predicted_category) VALUES (?, ?, ?, ?)''', (category, title, filename, predicted_category))
    connection.commit()
    connection.close()
