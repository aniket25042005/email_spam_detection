import joblib
import os
from django.conf import settings
from django.shortcuts import render

MODEL_PATH = os.path.join(settings.BASE_DIR, "detector", "spam_model.joblib")
VECT_PATH = os.path.join(settings.BASE_DIR, "detector", "tfidf_vectorizer.joblib")

print("Loading model from:", MODEL_PATH)
print("Loading vectorizer from:", VECT_PATH)

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECT_PATH)

print("Type:", type(tfidf))
print("Has vocabulary:", hasattr(tfidf, "vocabulary_"))
print("Has idf:", hasattr(tfidf, "idf_"))

# Test it immediately
try:
    tfidf.transform(["hello world"])
    print("✅ Vectorizer works")
except Exception as e:
    print("❌ Vectorizer failed:", e)

def home(request):
    result = None

    if request.method == "POST":
        message = request.POST.get("message")

        if not message:
            return render(request, "home.html", {"result": "Please enter text"})

        vec = tfidf.transform([message])   # ✅ tfidf is now defined
        pred = model.predict(vec)

        result = "Spam" if pred[0] == 1 else "Not Spam"

    return render(request, "home.html", {"result": result})