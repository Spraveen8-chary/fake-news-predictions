# Fake News Prediction App
## Overview
This Flask-based web application is designed to predict whether a given news article is fake or genuine. It utilizes a machine learning model trained on a labeled dataset of news articles. Users can input a news article, and the application will provide a prediction based on the trained model.

# Prerequisites
Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- scikit-learn
- pandas

# Dataset
download the news.csv by following url.
```bash
https://drive.google.com/file/d/1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q/view
```
You can install these dependencies using pip:
```bash
  pip install Flask scikit-learn pandas
```

# Getting Started
1. Clone the repository to your local machine:
```bash
    git clone https://github.com/Spraveen8-chary/fake-news-prediction-app.git
```
2. Run the Flask application:
```bash
  python app.py
```

The application will start locally, and you can access it in your web browser at `http://localhost:5000`.

# Usage
1. Visit the home page of the web application.

2. Enter a news article into the provided text input field.

3. Click the "Predict" button to submit the article for prediction.

4. The application will use the trained model to predict whether the input news article is fake or genuine.

# Model Training
The machine learning model used in this application was trained on a dataset of news articles. The training code and dataset are not included in this repository, but you can replace the `model.pkl` file with your own trained model if you have one.

# Data
The training data for the model is stored in a CSV file named `news.csv`. This dataset contains both the text of news articles and their corresponding labels (fake or genuine). You can replace this dataset with your own if needed.

# Customization
You can customize the application by modifying the following components:

- `Model`: Replace the `model.pkl` file with your own trained model or retrain the model using your data.

- `Data`: Replace the `news.csv` file with your own dataset if you want to train the model on different data.

- `Text Vectorization`: Modify the vectorization settings in the `app.py` file to change how the text is transformed before prediction.

- `Styling`: You can customize the HTML templates and CSS to change the look and feel of the web application.

# Acknowledgments
This project is for educational purposes and was created as a demonstration of building a fake news prediction application using Flask and machine learning.

# Output 
![WhatsApp Image 2023-10-02 at 21 05 32_236595c0](https://github.com/Spraveen8-chary/fake-news-predictions/assets/108536707/66a47c60-b48e-4d9e-b548-be2b17e321a3)
