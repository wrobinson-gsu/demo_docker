from __future__ import print_function
import os
from flask import Flask, render_template, request
from pypmml import Model

app = Flask(__name__)
global model, params
model = None


@app.route('/hello')
def hello():
    '''
    Used for testing to check if server is alive (without running model).
    :return:
    '''
    return "Hello from model server"


@app.route('/', methods=['POST', 'GET'])
@app.route('/model', methods=['POST', 'GET'])
def model_update():
    '''
    Generates HTML using the model parameters, prediction label name, and model name.
    :return: the HTML template for the model.
    '''
    global model, params
    model, params = get_model()
    score = 0.0
    if request.method == 'POST':
        params = request.form
        prediction = model.predict(params)
        score = prediction["prediction"]
    param_pairs = zip(params.keys(), params.values())
    return render_template("model.html", parameters=param_pairs, score=score,
                           label=model.targetName, model=model.functionName)


def get_model():
    '''
    Read PMML model from file, and read the input parameter names for the model.
    :return: model and its parameter names
    '''
    global model, params
    if model is None:
        # On Windows, path to the file (used for debugging, when not running in a container)
        if os.name == 'nt':
            model_path = os.path.join("//U:/Users/wnr/OneDrive/Profile/Documents/dev/docker/flask-pmml/flask_app/",
                                      "model.pmml")
            print("loading model from ", model_path)
            model = Model.fromFile(model_path)
        # In Docker, python runs in the app directory
        else:
            model = Model.fromFile("model.pmml")
        params = {fn: 0.0 for fn in model.dataDictionary.fieldNames}
    return model, params


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
