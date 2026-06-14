# 🧠 AmberMind

AmberMind is a multi-document conversational RAG (Retrieval-Augmented Generation) chatbot built with **FastAPI**, **ChromaDB**, **Sentence Transformers**, and **Groq**. It allows users to upload PDF documents and ask natural language questions grounded in the uploaded content, complete with source citations.

## 🚀 Live Demo

**Live Application:**
https://krish-2-ambermind.hf.space/

---

## ✨ Features

* 📄 Upload and process PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 💬 Conversational question answering
* 🔄 Query rewriting for better context handling
* 📚 Source citations with page numbers
* 🗂 Multi-document support
* ⚡ Fast inference using Groq
* 🌐 Live deployment on Hugging Face Spaces

---

## 🏗 Tech Stack

### Backend

* FastAPI
* Python

### Vector Database

* ChromaDB

### Embeddings

* Sentence Transformers
* Model: `paraphrase-MiniLM-L3-v2`

### LLM

* Groq
* Llama 3.3 70B

### PDF Processing

* PyPDF

### Deployment

* Docker
* Hugging Face Spaces

---

## 📂 Project Structure

```text
AmberMind
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── models
│   │   └── services
│
├── frontend
│   └── index.html
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/krishpatel2-prog/AmberMind.git

cd AmberMind
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

```bash
uvicorn backend.app.main:app --reload
```

API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Example Workflow

1. Upload one or more PDF documents.
2. Ask questions in natural language.
3. AmberMind retrieves relevant chunks from the documents.
4. Groq generates answers grounded in the retrieved context.
5. Source documents and page numbers are displayed.

---

## Example Questions

* What skills does Krish Patel have?
* What was Apple's revenue in 2025?
* Compare NASA and ISRO.
* Who has more employees, Amazon or NASA?
* Compare Apple, NASA, and Krish Patel in terms of leadership and focus.

---

## Future Improvements

* Streaming responses
* Chat history persistence
* Session-based conversations
* Delete documents from vector database
* OpenAI embedding support
* GitHub auto-deployment
* User authentication

---

## Repository

https://github.com/krishpatel2-prog/AmberMind

---

## Author

**Krish Patel**

Built as an AI-powered RAG system to demonstrate semantic search, vector databases, and document-grounded conversational AI.
