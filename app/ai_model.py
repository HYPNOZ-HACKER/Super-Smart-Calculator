# app/ai_model.py
import tensorflow as tf

class AIModel:
    def __init__(self):
        self.model = tf.keras.models.load_model('path_to_your_trained_model')

    def predict(self, expression):
        # Preprocess the expression if needed
        result = self.model.predict(expression)
        return result
