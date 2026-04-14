# 🚑 AI Smart Ambulance Routing using Endee

## 📌 Overview

This project implements an **AI-powered ambulance routing system** that intelligently identifies the most relevant hospital based on input queries using **vector embeddings and semantic search**.

Traditional systems rely on simple distance calculations, but this project enhances decision-making using **AI similarity search** powered by **Endee vector database**.

---

## ❗ Problem Statement

In emergency situations, selecting the right hospital quickly is critical.
However, traditional systems:

* Do not consider hospital specialization
* Lack intelligent matching
* Use only basic filtering

This can lead to delays in providing the right treatment.

---

## 💡 Solution

This project uses **semantic search and vector similarity** to:

1. Convert hospital data into embeddings
2. Store them in **Endee vector database**
3. Accept user queries (e.g., "cardiac emergency", "trauma care")
4. Retrieve the most relevant hospital using similarity search

---

## ⚙️ How It Works

```
User Query
   ↓
Convert to Embedding
   ↓
Search in Endee Vector DB
   ↓
Return Best Matching Hospital
```

---

## 🧠 Use of Endee (MANDATORY)

This project uses **Endee** as the core vector database.

* Stores hospital embeddings
* Performs fast similarity search
* Retrieves top matching results

Endee enables efficient **semantic understanding** instead of keyword-based search.

---

## 🛠️ Tech Stack

* Python
* Endee (Vector Database)
* Sentence Transformers (for embeddings)
* Pandas (data handling)

---

## 📂 Project Structure

```
my_project/
 ├── main.py
 ├── hospital_data.csv
 └── README.md
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the project:

```bash
python main.py
```

---

## 📊 Example Output

```
Input: "heart attack emergency"

Output:
Best Match: City Cardiac Hospital
Distance: 2.1 km
Specialization: Cardiology
```

---

## 🚀 Features

* Semantic hospital search
* AI-based decision support
* Fast vector similarity search using Endee
* Easy to extend for real-world applications

---

## 🔮 Future Improvements

* Real-time traffic integration
* GPS-based live ambulance tracking
* Integration with maps API
* Web-based dashboard

---

## 📌 Conclusion

This project demonstrates how **AI + Vector Databases (Endee)** can improve emergency response systems by providing **intelligent and fast hospital recommendations**.

---

## ⭐ Acknowledgment

Built using the Endee vector database framework.
