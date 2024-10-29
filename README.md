# langchain-demo-translatinator-py

**LangChain Translator Server**
==========================

A simple API server using LangChain's Runnable interfaces to provide on-demand translations.

**Features**

* Uses the LLaMA 3.1 model for high-quality translations
* Utilizes a prompt template to ensure correct output formatting

**Getting Started**
-------------------

### Prerequisites

* Python 3.8+
* `fastapi` and `langchain_ollama` libraries installed (`pip install fastapi langchain_ollama`)

### Running the Server

1. Clone this repository: `git clone https://github.com/aligorithm/projekt.git`
2. Navigate to the project directory: `cd projekt`
3. Run the server: `python serve.py`

**Usage**
-----

Send a POST request to `http://localhost:8000/chain` with a JSON body containing:

```markdown
{
  "text": "Hello world!",
  "language": "es"
}
```

Replace `"Hello world!"` with the text you want to translate and `"es"` with the target language.

### Flutter Frontend
For a user-friendly frontend, check out the [Translatinator Flutter App](https://github.com/aligorithm/translatinator-flutter).
