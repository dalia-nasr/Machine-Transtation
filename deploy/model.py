import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np
import pickle
import logging

eng_token = pickle.load(open('deploy/model_result/eng_tokenizer.pickle', 'rb'))
fr_token = pickle.load(open("deploy/model_result/fr_tokenizer.pickle", 'rb'))

class Translator:
    def __init__(self, model_path):
        logging.info("Translation class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")
        
    
    def predict(self, input):
        test_tokenized = eng_token.texts_to_sequences([input])
        test_padded = pad_sequences(test_tokenized, maxlen=15, padding='post')

        predictions = self.model.predict(test_padded)[0]

        index_to_words = {id: word for word, id in fr_token.word_index.items()}
        index_to_words[0] = ''
        return ' '.join([index_to_words[prediction] for prediction in np.argmax(predictions, 1)])

def main():
	model = Translator('deploy/model_result/translation_model.h5') 

	predicted_class = model.predict("she is driving the truck")
	logging.info("Translated sentence: {}".format(predicted_class)) 


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
