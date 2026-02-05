# 🌍 GenAI Language Translator

A Streamlit-based language translation web application built using Hugging Face pretrained multilingual models. The app runs models locally (no paid APIs) and provides real-time text translation with a clean UI.

---

## 🚀 Features

* Automatic source language detection
* Translate text into multiple target languages
* Uses Hugging Face transformers locally (free)
* Streamlit-based interactive web UI
* Model caching for faster subsequent runs
* No external paid API dependency

---

## 🛠 Tech Stack

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* SentencePiece

---

## 📂 Project Structure

```
Language-Translator/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/language-translator.git
cd language-translator
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux / Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🔐 Hugging Face Token (Optional but Recommended)

To avoid rate limits and warnings, set your Hugging Face access token:

```bash
setx HF_TOKEN "your_huggingface_token"   # Windows
# export HF_TOKEN="your_huggingface_token"  # Linux / Mac
```

Restart your terminal after setting the token.

---

## 🌐 Supported Languages

* Hindi
* French
* Spanish
* German
* Japanese
* English (auto-detected source)

*(More languages can be added easily)*

---

## ⚠️ Notes

* The model downloads only once and is cached locally.
* First run may take time depending on model size.
* Some low-resource languages may have minor translation inaccuracies.

---

## 📌 Future Improvements

* Add language auto-detection display
* Add more multilingual models
* Deploy on Streamlit Cloud / Hugging Face Spaces
* Add speech-to-text translation

---

## 👨‍💻 Author

**Abhisek Mishra**
Aspiring Data Scientist & LLM Application Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
