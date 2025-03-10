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