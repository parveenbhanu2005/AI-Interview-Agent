# 🤖 AI Interview Agent

An AI-powered Interview Agent built with **Flask** and **Groq LLM** that generates role-based interview questions, evaluates candidate answers, and provides instant AI-driven feedback with performance analysis.

---

## 📌 Features

- 🎯 Role-based interview question generation
- 🤖 AI-powered answer evaluation
- 📊 Automatic scoring and feedback
- 📈 Overall performance analysis
- ⏱️ Interview timer
- 💻 Responsive and modern user interface
- 🔒 Secure API key management using `.env`
- 🌐 Built with Flask and Python

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- Groq API (Llama 3.1)
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- dotenv

---

## 📂 Project Structure

```
AI-Interview-Agent/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── templates/
│   ├── index.html
│   ├── interview.html
│   └── result.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── utils/
│   ├── ai.py
│   └── evaluator.py
│
├── prompts/
│
└── data/
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Interview-Agent.git
```

### 2. Navigate to the Project

```bash
cd AI-Interview-Agent
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

### 7. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🎯 How It Works

1. Enter your name and job role.
2. The AI generates interview questions.
3. Answer each question.
4. The AI evaluates your responses.
5. Receive detailed feedback, scores, and overall performance.

---

## 📸 Screenshots

You can add screenshots of:

- Home Page
- Interview Page
- Result Dashboard

inside the `screenshots/` folder.

---

## 📈 Future Enhancements

- 🎤 Voice-based interviews
- 📄 Resume analysis
- 📥 PDF interview reports
- 🔐 User authentication
- 📊 Interview history dashboard
- 🌍 Multi-language support
- 📱 Mobile-friendly UI

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 👨‍💻 Author

**B. Parveen Bhanu**

- B.Tech (Computer Science Engineering – Cyber Security)
- Rajeev Gandhi Memorial College of Engineering and Technology
- Python Developer | AI & Cybersecurity Enthusiast

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, don't forget to **Star ⭐ the repository**.