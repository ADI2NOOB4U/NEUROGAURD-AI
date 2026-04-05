# 🧠 NeuroGuard AI

### Real-Time AI-Based System Monitoring & Threat Detection

NeuroGuard is an intelligent cybersecurity project that uses Machine Learning to monitor system processes in real-time and detect anomalies that may indicate malicious activity or potential cyber threats.

---

## 🚀 Features

* 🔍 Real-time system process monitoring using `psutil`
* 🤖 AI-based anomaly detection using Isolation Forest
* 📊 Interactive dashboard built with Streamlit
* ⚡ Fast and lightweight execution
* 🛡️ Identifies suspicious or abnormal processes
* 📈 Displays CPU, memory, and process behavior insights

---

## 🧠 How It Works

1. The system continuously collects process data (CPU usage, memory, PID, etc.)
2. Data is passed into a trained Machine Learning model
3. The model predicts whether the process is:

   * ✅ Normal
   * ⚠️ Suspicious / Anomalous
4. Results are displayed in a live dashboard

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – for dashboard UI
* **Scikit-learn** – for ML model (Isolation Forest)
* **psutil** – for system monitoring
* **Pandas** – data handling

---

## 📂 Project Structure

```
NeuroGuard-AI/
│── src/
│   ├── dashboard.py        # Streamlit UI
│   ├── detector.py         # ML prediction logic
│   ├── model.pkl           # Trained ML model
│
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/NeuroGuard-AI.git
cd NeuroGuard-AI
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the project

```
streamlit run src/dashboard.py
```

---

## 📸 Demo

* Live process monitoring
* AI detection results
* Interactive dashboard

<img width="1900" height="865" alt="image" src="https://github.com/user-attachments/assets/7a884905-15ec-4d55-be4d-55777d4be105" />

---

## 🎯 Use Cases

* Detect suspicious background processes
* Basic malware/anomaly detection
* Learning project for AI + Cybersecurity
* Hackathons & portfolio projects

---

## ⚠️ Limitations

* Model accuracy depends on training data
* Not a full antivirus replacement
* Requires manual improvement for advanced threats

---

## 🔮 Future Improvements

* 🔥 Deep Learning integration
* 🌐 Network traffic monitoring
* ☁️ Cloud-based threat intelligence
* 📱 Alerts & notifications system

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Aditya Kumar Sharma**
Cybersecurity & AI Enthusiast 🚀

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
