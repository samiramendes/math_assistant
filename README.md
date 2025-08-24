# AI Math Assistent using LangChain Agents, Groq and Chainlit

## Overview
This repository contains the code for an AI assistant capable of handling both math calculations and general knowledge questions. The backend is built using LangChain agents and tools, and the interactive interface is powered by Chainlit.

## Features

- **Math calculations:** Solve math expressions, including functions like `sqrt`, `log`, `sin`, `cos`, etc.
- **Knowledge search::** Retrieve general information using the Wikipedia API.

## How It Works

The agent receives a custom prompt that defines its role and describes how and when to use the available tools.

For each user message, the agent decides whether to respond using its own knowledge or to invoke an external tool (calculator or Wikipedia search) for accurate answers.

Everything is integrated using Chainlit, which handles the chat interface and manages the user session state.

## Logic Flow

```mermaid 
flowchart TD
    A((User sends a question)) --> B[Chainlit receives the message and calls the agent]
    B --> C[Agent analyzes the question based on the prompt and available tools]
    C --> D{Is it a math-related question?}
    
    D -- Yes --> E[Use Calculator tool]
    D -- No --> F{"Is it a factual question? (Person, place, event...)"}

    F -- Yes --> G[Use Wikipedia Search tool]
    F -- No --> H[Respond using internal LLM knowledge]

    E --> I((Return response to user))
    G --> I
    H --> I
 ```

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

## Key Learnings

- LangChain’s core components: tools, agents, and their orchestration.

- How to build and register custom tools for mathematical operations and web-based searches.

- Prompt engineering techniques to improve tool-selection accuracy.

- Functional chatbot interface using Python and Chainlit.

## Future Improvements

- Integrate observability tooling such as LangSmith to monitor and analyze agent performance.

- Implement a pre-classifier agent to route questions based on their type (e.g., math vs. general knowledge).

- Create tests to measure the agent’s accuracy in solving math problems and choosing the correct tool.

- Consider migrating to LangGraph due to LangChain deprecations.


### Author

Developed by Samira Mendes.
