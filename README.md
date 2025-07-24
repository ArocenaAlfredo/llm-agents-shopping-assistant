# LLM Agents – AI-Powered Shopping Assistant 

This project implements a conversational AI shopping assistant using Large Language Models (LLMs) and intelligent agents. It simulates a real-world e-commerce customer service system capable of understanding natural language, retrieving product information, managing shopping carts, and handling support requests.

---

##  Project Overview

A major e-commerce company needs to modernize its customer experience with AI. This assistant helps users:

- Search for products with natural queries
- Discover items using semantic understanding
- Add/remove items from their shopping cart
- Request refunds or report issues
- Escalate complex cases to human agents

The system supports **multi-turn conversations**, **context memory**, and combines **structured search** with **semantic search** over a grocery product catalog.

---

##  Dataset

The assistant uses a real-world grocery dataset including:

- 49,000+ product entries
- Product metadata (name, department, aisle, price)
- Historical purchase data

Used for:
- **Structured filtering** via Pandas
- **Semantic search** using vector embeddings

---

##  Tech Stack

- **Python 3.10+**
- **LangChain**: LLM agent management
- **LangGraph**: Multi-agent orchestration
- **OpenAI GPT models**: Natural language understanding
- **Chroma**: Vector database for semantic search
- **HuggingFace**: Text embeddings
- **Pandas**: Data filtering and manipulation
- **Pydantic**: Data validation and schemas
- **Streamlit**: Web-based user interface
- **Pytest**: Unit and integration testing

---

##  How to Run

1. **Install dependencies**:
```bash
pip install -r requirements.txt
Set OpenAI API key:

bash
Copiar
Editar
export OPENAI_API_KEY="your-api-key-here"
Build vector database
(see detailed steps in ASSIGNMENT.md or custom scripts)

Run assistant (CLI):

python
Copiar
Editar
from src.conversation_runner import run_single_turn
result = run_single_turn("Hi, I need some bananas", "test-thread-123")
print(result)
Run assistant (Web UI):

bash
Copiar
Editar
streamlit run app.py
 Testing
Run tests:

bash
Copiar
Editar
pytest tests/
 Project Structure
bash
Copiar
Editar
.
├── src/               # Agent logic and orchestration
├── data/              # Grocery dataset
├── vector_db/         # Local vector store (excluded from repo)
├── tests/             # Unit & integration tests
├── app.py             # Streamlit app
├── requirements.txt
└── README.md
 Code Style
The code follows Python best practices using black:

bash
Copiar
Editar
black --line-length=88 .
 Status
 Multi-agent architecture with LangGraph

 Memory, tool usage, and prompt templates

 Working CLI and web interface

 Embeddings and vector DB integration

 Full testing coverage with Pytest

This project showcases a modern, agent-based LLM system for intelligent automation in the e-commerce domain.
