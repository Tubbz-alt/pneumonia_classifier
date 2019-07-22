import numpy as np
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model 
from keras.applications import imagenet_utils
from keras import backend as K
import tensorflow as tf
from PIL import Image
import numpy as np
import Flask
import io
import pdb

# Define a flask app
app = flask.Flask(__name__)

model_path = 'models/cnn.h5'

def loaded_model():
    global model
    model = load_model(model_path)
    model._make_predict_function()
    graph = tf.reset_default_graph()
    print('Model loaded. Check http://127.0.0.1:5000/')


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode == "RGB":
        image = image.convert("L")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = image.reshape(-1,128,128,1) / 255.
    # return the processed image
    return image


@app.route('/', methods=['POST'])
    render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = {'success': False}
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image = flask.request.files['image'].read()
            image = Image.open(io.BytesIO(image))
            model = load_model(model_path)
            image = prepare_image(image, target=(128,128))
            prediction = model.predict(image)
            class_predicted = np.argmax(prediction)
            data['prediction'] = []
            data['prediction'].append(class_predicted) 
            data['success'] = True
    return flask.jsonify(str(data))


if __name__ == '__main__':
    loaded_model()
    app.run(debug=True)