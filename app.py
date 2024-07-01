from flask import Flask, request, render_template
from transformers import TFDistilBertForSequenceClassification, DistilBertTokenizer
import tensorflow as tf

app = Flask(__name__)

# Load the model and tokenizer
model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input', '')
    
    inputs = tokenizer(user_input, return_tensors='tf')
    outputs = model(inputs)
    
    predictions = tf.nn.softmax(outputs.logits, axis=-1)
    result = 'positive' if predictions[0][1] > predictions[0][0] else 'negative'
    
    return render_template('result.html', result=result, user_input=user_input)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
