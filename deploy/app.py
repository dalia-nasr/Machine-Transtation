import logging
import os
from flask import Flask, render_template, request
from model import Translator

app = Flask(__name__)  
model_path = 'deploy/model_result/translation_model.h5'

# create instance
model = Translator(model_path)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Translate',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        logging.info("Predict request received!")
        sentence = (request.form['sentence'])
        res = model.predict(sentence)
    
    logging.info("prediction from model= {}".format(res))
    return render_template('index.html',result=res)

def main():
    """Run the Flask app."""
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port = port) 


if __name__ == "__main__":
    main()
