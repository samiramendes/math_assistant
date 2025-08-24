# Math Assistent Chat using LangChain Agents, Groq and Chainlit

## Overview
This repository contains the code for an AI assistant capable of handling both math calculations and general knowledge questions. The backend is built using LangChain agents and tools, and the interactive interface is powered by Chainlit.

## Features

- **Math calculations:** Solve math expressions, including functions like `sqrt`, `log`, `sin`, `cos`, etc.
- **Knowledge search::** Retrieve general information using the Wikipedia API.


## Getting Started
### Prerequisites
- Python 3.8 or later
- A Grok API key for LLM

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/samiramendes/math_assistant.git
   cd math-assistant
   ```
  
2. **Set Up a Virtual Environment (Recommended)**
* Create a virtual environment:

   ```bash
   python -m venv
   ```
* Activate the environment on Linux/macOS:

   ```bash
   source venv/bin/activate
   ```
* Activate the environment on Windows:

   ```bash
   .\venv\Scripts\activate
   ```
   

3. **Install Dependencies**
* Install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your Groq API Key**
* Create a .env file in the root directory of the project.
* Add your Groq API key to the `.env` file:

   ```bash
   GROQ_API_KEY='Your-Groq-API-Key-Here'
   ```

### Usage
To run the Math Assistent, execute the `app.py` script using:
   ```bash
   chainlit run app.py -w --port 8000
```

This will run the application at  http://localhost:8000# math_assistant

### Project Structure

```
math_assistant/
│
├── app.py
├── tools/
│   ├── calculator.py
│   └── web_searcher.py
├── chainlit.md
├── requirements.txt
├── .env
└── README.md
```

### Author

Developed by Samira Mendes.
