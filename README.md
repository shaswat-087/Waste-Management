
#  Smart Waste Management System

## 📖 Overview
This project is a **web-based Waste Management System** built with **Flask (Python)**, **HTML**, **CSS**, and **Pandas**. It promotes sustainable practices by gamifying waste management — users can register, earn points for eco-friendly actions, and track their progress on a leaderboard. The system also integrates an interactive map of waste facilities across India using **Folium**.

---




## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, FontAwesome
- **Data Handling**: Pandas, CSV
- **Mapping**: Folium (interactive maps)

---

## 📂 Project Structure
```
Waste-Management/
│
├── app.py                # Main Flask application
├── show.py               # Additional script for data display
├── users.csv             # User data storage (generated at runtime)
├── static/               # CSS and static assets
│   ├── shop-style.css
│   ├── game-style.css
│   └── style.css
├── templates/            # HTML templates
│   ├── shop.html
│   ├── game.html
│   ├── module.html
│   ├── training.html
│   ├── map.html
│   └── sign-in.html
├── images/               # Project images
└── video.mp4             # Demo video
```

---

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/shaswat-087/Waste-Management.git
   cd Waste-Management
   ```
2. Install dependencies:
   ```bash
   pip install flask pandas folium 
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🚀 Future Improvements
- Replace CSV with a proper database (SQLite/PostgreSQL).
- Implement password hashing for security.
- Add search and filter functionality for users.
- Enhance gamification with badges and rewards.
- Deploy on cloud (Heroku, AWS, etc.).

---

---
