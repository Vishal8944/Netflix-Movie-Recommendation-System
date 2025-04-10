## 🎬 Movie Recommendation System

This is a simple **Content-Based Movie Recommendation System** built using **Streamlit**, **pandas**, and **scikit-learn**. It suggests movies based on genre similarity using TF-IDF Vectorization and Cosine Similarity.
---

### 🚀 Features

- 📂 Loads movie dataset (`net.csv`) with movie titles and genres.
- 📈 Calculates **cosine similarity** using **TF-IDF** on genres.
- 🔍 Recommends the top 5 most similar movies based on the selected title.
- 🎨 Styled with a custom dark theme for better UI.

---

### 🛠️ Technologies Used

- Python
- Streamlit
- pandas
- scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

### 📁 Files Overview

| File                | Description                                      |
|---------------------|--------------------------------------------------|
| `RSapp.py`          | Main Streamlit app code                         |
| `Movie_Recommendation.ipynb` | Jupyter Notebook version (exploratory)     |
| `net.csv`           | Dataset containing movie titles and genres      |
| `requirements.txt`  | List of dependencies for running the app        |

---

### 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
```

---

### ▶️ Running the App

```bash
streamlit run RSapp.py
```

---

### 📊 Dataset Info

- `net.csv` contains two main columns:
  - `title`: Movie title
  - `genres`: Pipe-separated genres (e.g., `"Action|Adventure|Sci-Fi"`)

---

### 📌 How it Works

1. **TF-IDF Vectorizer** is used to convert genres into numerical vectors.
2. **Cosine Similarity** is computed to find similarities between movies.
3. Given a movie, the top 5 most similar ones are returned.

---

### ✨ Example

Select `"The Matrix"` in the app, and it might recommend:
- Terminator 2: Judgment Day  
- Inception  
- Blade Runner  
- Equilibrium  
- Minority Report  

---

### 🧑‍💻 Author

- [Vishal S]

---

