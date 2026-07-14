# email_spam_detection
# 📧 Email Spam Detection using Machine Learning and Django

## Overview

This project is a web-based **Email Spam Detection System** built using **Django** as the backend framework and a **Machine Learning** model trained with **Scikit-learn**. The application classifies email messages as **Spam** or **Not Spam** based on their content.

The machine learning model was trained in **Jupyter Notebook** and integrated into a Django web application using **Joblib**.

---

## Features

* Detects whether an email is Spam or Not Spam.
* Simple and user-friendly web interface.
* Machine Learning model integrated with Django.
* Real-time predictions.
* TF-IDF text vectorization.
* Support Vector Machine (SVM) classifier.

---

## Tech Stack

* Python
* Django
* Scikit-learn
* Pandas
* NumPy
* NLTK
* Joblib
* HTML
* CSS

---

## Machine Learning Pipeline

1. Load the email dataset.
2. Clean and preprocess the text.
3. Remove punctuation and special characters.
4. Convert text to lowercase.
5. Remove stopwords.
6. Transform text using TF-IDF Vectorizer.
7. Train an SVM classifier.
8. Save the trained model and vectorizer using Joblib.
9. Load the model into the Django application for prediction.

---

## Project Structure

```text
email-spam-detection/
│
├── detector/
│   ├── views.py
│   ├── spam_model.joblib
│   ├── tfidf_vectorizer.joblib
│   └── ...
│
├── spam_detector/
│
├── templates/
│   └── home.html
│
├── static/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/email-spam-detection.git
```

Move into the project directory:

```bash
cd email-spam-detection
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Django server:

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Dataset

The model was trained on an email dataset containing spam and legitimate (ham) emails. Text preprocessing and TF-IDF feature extraction were applied before training the classifier.

---

## Future Improvements

* Add probability/confidence scores.
* Support multiple machine learning models.
* Improve the user interface with Bootstrap.
* Add user authentication.
* Store prediction history.
* Deploy using Render or Railway.

---

## Author

**Aniket Kumar Singh**

---

## License

This project is intended for educational and learning purposes.
