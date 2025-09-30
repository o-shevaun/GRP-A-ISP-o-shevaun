# DigestWell — Personalized Nutrition for Digestive Health

**DigestWell** is a safety-first recipe recommendation API for people with **digestive conditions** (e.g., IBS, GERD, IBD).
It ranks real recipes using a machine-learning model trained on **per-serving nutrients** and **ingredient-derived safety flags** (spicy, acidic, high-FODMAP, lactose, gluten).
Recipes are sourced at runtime from **Edamam Recipe Search v2** (USDA optional for enrichment). The system applies **hard safety rules** (condition + allergies) and then **ML scoring** to prioritize gentler options. It is designed to learn from user feedback later (accept / swap / ban) to become more personalized over time.

---

## 🚀 Quickstart

### Prerequisites

* Python 3.11+ (3.12 OK)
* Git
* (Dev DB) SQLite by default; PostgreSQL optional

### 1) Clone & create a virtual environment

```bash
git clone <your-repo-url> Digestwell
cd Digestwell
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
# source venv/bin/activate
```

### 2) Install backend dependencies

```bash
pip install django djangorestframework pandas scikit-learn==1.6.1 joblib
# If using PostgreSQL later: pip install psycopg2-binary
```

### 3) Configure Django

* Ensure your Django app (e.g., `nutrition`) is added to `INSTALLED_APPS`.
* Use SQLite for quick dev, then:

```bash
cd backend
python manage.py migrate
```

### 4) Add the trained model

Place your trained file `digestwell_model.pkl` at:

```
backend/<your_app>/ml/digestwell_model.pkl
```

(Where `<your_app>` is typically `nutrition` or `core`.)

### 5) Run the server

```bash
python manage.py runserver
```

You should see the server at `http://127.0.0.1:8000/`.

### 6) Call the API (one example)

POST to:

```
http://127.0.0.1:8000/api/score/
```

Body (JSON) should include candidate recipes with the same feature fields used in training; the API returns the **ranked** list with a suitability score.

---
