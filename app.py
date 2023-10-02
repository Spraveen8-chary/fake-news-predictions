# Flask application
from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the trained model
model_filename = 'model.pkl'
loaded_model = joblib.load(model_filename)
df = pd.read_csv('news.csv')
x_train,x_test,y_train,y_test=train_test_split(df['text'], df.label, test_size=0.2, random_state=7)

vectorizing = TfidfVectorizer(stop_words='english' , max_df=0.7)
vector_train = vectorizing.fit_transform(x_train)
vector_test = vectorizing.transform(x_test)
@app.route('/', methods=['GET', 'POST']) 
def predict():
    if request.method == 'POST':
        text = request.form['text']

        vectorized_text = vectorizing.transform([text])
        
        prediction = loaded_model.predict(vectorized_text)[0]

        return render_template('index.html', prediction=prediction)
    else:
        return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
