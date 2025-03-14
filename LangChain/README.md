# LangChain

## Docs (Resources)

- [Introduction](https://python.langchain.com/docs/introduction/)
- [Conceptual guide](https://python.langchain.com/docs/concepts/)
- [Tutorials](https://python.langchain.com/docs/tutorials/)
- [How-to guides](https://python.langchain.com/docs/how_to/)
- [Integrations](https://python.langchain.com/docs/integrations/providers/)
- [Security](https://python.langchain.com/docs/security/)
- [LangServe](https://python.langchain.com/docs/langserve/)
- [LangSmith](https://docs.smith.langchain.com/)
- [v0.3](https://python.langchain.com/docs/versions/v0_3/)
- [Chat models](https://python.langchain.com/docs/integrations/chat/)
   ([OpenAI](https://python.langchain.com/docs/integrations/chat/openai/),
   [Anthropic](https://python.langchain.com/docs/integrations/chat/anthropic/),
   [Ollama](https://python.langchain.com/docs/integrations/chat/ollama/),
   [DeepSeek](https://python.langchain.com/docs/integrations/chat/deepseek/))
- [Indexing API](https://python.langchain.com/docs/how_to/indexing/)

## Links

- [Chatbot](https://chat.langchain.com/) (...answer questions about langchain)
- [LangSmith](https://smith.langchain.com/)
- [Hub (Prompts)](https://smith.langchain.com/hub)

## 01. Basic

- **Basic LangChain in 15 minutes** (openai, connect, prompt template, chain, conversation chain memory)<br>`basic-langchain-in-15-mins.ipynb`
- **Tools & Agents (1) [TODO]** (openai, tools, agents)<br>`tools-agents-1.ipynb`
- **Tools & Agents (2) [TODO]** (openai, tools, agents)<br>`tools-agents-2.ipynb`
- **Models (OpenAI)** (openai, messages)<br>`models.ipynb`
- **Models (Replicate + Llama)** (replicate, llama)<br>`models-replicate-llama.ipynb`
- **Prompts** (openai, prompt template, messages, chat prompt template)<br>`prompts.ipynb`
- **Few Shot Prompts** (openai, prompt template, few shot prompt template)<br>`few-shot-template.ipynb`
- **Output Parsers** (openai, prompt template, pydantic output parser)<br>`output-parsers.ipynb`
- **Memory** (openai, conversation buffer memories)<br>`memory.ipynb`
- **Chains** (openai, chain, sequential chain, router chain)<br>`chains.ipynb`
- **Document Loaders** (openai, loaders - pdf, audio, website)<br>`document-loaders.ipynb`
- **Splitters** (text splitters - character, recursive character, markdown header)<br>`splitters.ipynb`
- **Callbacks** (openai, callback handlers - stdout, base, openai costs & usage)<br>`callbacks.ipynb`
- **OpenAI functions** (openai, solution by langchain, openai api)<br>`openai-functions.ipynb`
- **Connect with FastAPI** (openai, basic rag, rag with fastapi)<br>`basic-rag-app-qa-to-fastapi.ipynb`
- **Agents** (openai, basic rag, agents - simple, custom)<br>`agents.ipynb`
- **Indexing API** (openai, basic rag with deeplake, similarity search, indexing api)<br>`indexing-api.ipynb`

## 02. Groq (alternative to OpenAI)

- **How to use Groq** (chat groq with llama3, mixtral)<br>`groq-llama3-mixtral.ipynb`

## 03. LCEL (LangChain Expression Language)

- **Chains** (openai, old-new way, llm chain, pipe)<br>`LCEL-chains.ipynb`
- **Output Parsers** (openai, old-new way, str output parser)<br>`LCEL-output-parsers.ipynb`
- **Arguments** (openai, old-new way, llm.bind)<br>`LCEL-kargs-arguments.ipynb`
- **OpenAI functions** (openai, old-new way, json output functions parser, functions, llm.bind)<br>`LCEL-openai-functions.ipynb`
- **RAG Applications** (openai, old-new way, basic rag, runnable passthrough)<br>`LCEL-basic-rag-app-qa.ipynb`

## 04. Advanced Components

- **[LangSmith](https://docs.smith.langchain.com/)** (openai, tracer, tags, groups, client, metadata, filters, evaluating with dataset)<br>`langchain-langsmith.ipynb`
- **[LangServe](https://python.langchain.com/docs/langserve/)** (openai, fastapi, routes, uvicorn, server)<br>`langserve.ipynb`
- **[Templates](https://templates.langchain.com/)** (**[v0.1](https://python.langchain.com/v0.1/docs/templates/)**) (by terminal & langserve, rag-conversation template, etc.)<br>`langchain-templates.ipynb`
- **[Chatbot](https://chat.langchain.com/)** (...answer questions about langchain)

## 05. Level 1 Apps: "Toy Demos"

- **Summarization** (openai, tokens, text splitter, chunks, chain, summarize chain)<br>`basic-app-summarization.ipynb`
- **RAG: Document QA (Question-Answering)** (openai, basic rag)<br>`basic-rag-app-qa.ipynb`
- **Extraction of structured data** (openai, response schema, structured output parser)<br>`basic-app-text-extraction.ipynb`
- **Evaluation of QA App** (openai, basic rag, questions, answers, predictions, evaluation manual-automatic)<br>`basic-app-evaluation.ipynb`
- **Querying database** (openai, sqlite, sql database chain)<br>`basic-app-querying-tabular-data.ipynb`
- **Asking GitHub repo** (openai, text loader, basic rag)<br>`basic-app-qa-a-github-repo.ipynb`
- **Asking API & LangGraph** (openai, api chain, langgraph)<br>`basic-app-interacting-with-api.ipynb`
- **Chatbot with personality & memory** (openai, role template, conversation buffer memory)<br>`basic-app-chatbot.ipynb`
- **RAG with DeepLake** (openai, documents, basic rag, deeplake, add documents)<br>`basic-rag-with-deeplake.ipynb`
- **Basic Agent** (openai, google search, tools with functions, search.run, requests.get, agent)<br>`basic-app-simple-agent.ipynb`
- **Advanced Output Parser** (openai, pydantic output parser)<br>`basic-app-with-pydantic-output-parser.ipynb`

## 06. Level 2 Apps: "Toy Demos" + "Toy UIs" with Streamlit
moved to [**Streamlit**] directory in root

## 07. LangChain v0.2

- **Connecting with LLMs** (openai, llm-chat model, stream, prompt templates, chain, output parsers, pydantic)<br>`connect-llms.ipynb`
- **Loading Data** (openai, loaders txt-csv-html-pdf-wiki, rag, splitter, embeddings, vector store, retriever, indexing)<br>`load-data.ipynb`
- **Chaining Actions** (openai, chain)
 [Legacy Chains](https://python.langchain.com/v0.1/docs/modules/chains/),
 [LCEL chain runnables](https://python.langchain.com/docs/how_to/sequence/)
 <br>`chain-actions.ipynb`
- **Memory** (openai, conversation buffer memory, chat message history)<br>`memory.ipynb`

## 08. LangChain v0.2 (LCEL in Depth)

- **LCEL in 06/2024** (openai, legacy chain vs. lcel chain runnables)<br>`intro-lcel-0724.ipynb`
- **Runnable Execution Order** (openai, runnables, pipe, execution order, invoke, stream, batch)<br>`runnable-order.ipynb`
- **Built-In Runnables** (openai, runnable passthrough - lambda - parallel, lambda function, itemgetter)<br>`builtin-runnables.ipynb`
- **Built-In Functions for Runnables** (openai, bind, assign)<br>`builtin-functions-runnable.ipynb`
- **Main Operations** (openai, chaining runnables, coercion, chains multiple - nested - fallback)<br>`main-ops-chains.ipynb`
- **Basic RAG App** (openai, webbase loader, rag)<br>`lcel-chains-at-work.ipynb`

## 09. Top 10 Apps with LangChain v0.2

- **Simple Translator** (openai, chain with fastapi & routes, langserve)<br>`simpleTranslator.py`
- **LLM App deployed with LangServe** (openai, chain with fastapi & routes, langserve, remote runnable)<br>`simple-llm-app.ipynb`
- **Simple Chatbot** (openai, conversation buffer memory, file chat message history, memory in .json file)<br>`simple-chatbot.ipynb`
- **Advanced Chatbot** (openai, chat message history, runnable with message history, memory in python dict)<br>`advanced-chatbot.ipynb`
- **Retriever App with Vector Database** (openai, vector store, retriever, similarity search)<br>`retriever-app.ipynb`
- **Tool-Using Agent with LangGraph** (openai, tools, search tool by tavily search, agent)<br>`simple-agent.ipynb`
- **RAG App with Vector Database** (openai, text loader, predefined prompt, rag with chroma vector store)<br>`simple-rag.ipynb`
- **Conversational RAG App** (openai, text loader, rag with chroma vector store, chat message history)<br>`conversational-rag.ipynb`
- **QA App from SQL Data** (openai, sqlite, sql query chain, query sql database tool)<br>`qa-from-sql.ipynb`
- **QA App from PDF File** (openai, pdf loader, rag with chroma vector store)<br>`qa-from-pdf.ipynb`
- **Key Data Extraction App** (openai, structured output by pydantic schema, chain)<br>`key-data-extraction.ipynb`
- **Sentiment Analysis App** (openai, structured output by pydantic schema, enum, chain)<br>`sentiment-analysis.ipynb`

## [Chatbot](https://chat.langchain.com/) (QA about LangChain) generated code by Chatbot

- **RAG App** (openai, pdf, rag, faiss, save-load vectore store)<br>`chatbot-rag-pdf-faiss.py`<br>`chatbot-rag-pdf-faiss.ipynb` + `faiss_index` vectore store
- **Querying database** (openai, sqlite, sql database chain)<br>`chatbot-database.py`<br>`chatbot-database.ipynb` + `street_tree_db.sqlite` `Chinook.sqlite` databases
- **Asking GitHub repo** (openai, git loader, rag)<br>`chatbot-github.py`<br>`chatbot-github.ipynb`
- **Web Search (DuckDuckGo & Google Search API) with Agent** (openai, search api, tools, agent)<br>`chatbot-google-search.py`<br>`chatbot-google-search.ipynb`