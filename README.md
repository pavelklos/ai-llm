# AI - LLM

## 01. Models

- **OpenAI (gpt, website)** (openai, gpt, summarize website)<br>`model-gpt-website.ipynb`
- **Ollama (llama)** (ollama, llama)<br>`model-ollama-llama.ipynb`
- **Ollama (llama, deepseek)** (ollama, llama, deepseek)<br>`model-ollama-llama-deepseek.ipynb`
- **Ollama (llama, website)** (ollama, llama, summarize website)<br>`model-ollama-llama-website-1.ipynb`
- **Ollama (llama, website)** (ollama, llama, summarize website)<br>`model-ollama-llama-website-2.ipynb`
- **OpenAI (gpt, website, brochure)** (openai, gpt, summarize website, create brochure)<br>`model-gpt-website-brochure-1.ipynb`
- **OpenAI (gpt, website, brochure)** (openai, gpt, summarize website, create brochure)<br>`model-gpt-website-brochure-2.ipynb`
- **OpenAI + Ollama (gpt, llama, code)** (openai, gpt, ollama, llama, explain code)<br>`model-gpt-ollama-llama-1.ipynb`
- **OpenAI + Ollama (gpt, llama, code)** (openai, gpt, ollama, llama, explain code)<br>`model-gpt-ollama-llama-2.ipynb`

## 02. Models with GUI (Gradio)

- **Models** (gpt, claude, gemini)<br>`w2d1-1.ipynb`
- **Models** (gpt, claude, gemini, deepseek)<br>`w2d1-2.ipynb`
- **Models + Gradio** (gpt, claude, summarize website, create brochure)<br>`w2d2-1.ipynb`
- **Models + Gradio** (gpt, claude, summarize website, create brochure)<br>`w2d2-2.ipynb`
- **Models + Gradio** (gpt, conversation history)<br>`w2d3-1.ipynb`
- **Models + Gradio** (gpt, conversation history)<br>`w2d3-2.ipynb`
- **Models + Gradio** (gpt, tools)<br>`w2d4-1.ipynb`
- **Models + Gradio** (gpt, tools)<br>`w2d4-1-updated.ipynb`
- **Models + Gradio** (gpt, ollama, llama, tools)<br>`w2d4-2.ipynb`
- **Models + Gradio** (gpt, tools, multi-modal, history)<br>`w2d5-1.ipynb`
- **Models + Gradio** (gpt, tools, multi-modal, history)<br>`w2d5-2.ipynb`

## 03. HuggingFace (by [Google Colab](https://colab.research.google.com/))

- **Colab** `Week_3_Day_1_Colab.ipynb`
- **Pipelines** `Week_3_Day_2_Pipelines.ipynb`
- **Tokenizers** `Week_3_Day_3_Tokenizers.ipynb`
- **Models** `Week_3_Day_4_Models.ipynb`
- **Meeting Minutes product** `Week_3_Day_5_Meeting_Minutes_product.ipynb`

## 04. Code Generation
- Generate high performance C++ code from Python code
  - **Code Generator 1** `w4d3-1.ipynb` `w4d3-2.ipynb`

## LangChain

- [README](LangChain/README.md)

## Streamlit (GUI)

- **Basic Streamlit by GitHub Copilot** (controls, data, chart, file uploader, csv)<br>`000-streamlit-basic-copilot.py`
- **Re-write your text** (openai, prompt template)<br>`001-streamlit-redaction-improver.py`
- **Blog Post Generator** (openai, prompt template)<br>`002-streamlit-blog-post-generator.py`
- **AI Long Text Summarizer** (openai, upload file, recursive character text splitter, summarize chain)<br>`003-streamlit-split-and-summarize.py`
- **Writing Text Summarization** (openai, character text splitter, summarize chain)<br>`004-streamlit-text-summarization.py`
- **Extract Key Information from Product Reviews** (openai, prompt template, format output)<br>`005-streamlit-extract-json-from-review.py`
- **Evaluate a RAG App** (openai, upload file, rag with faiss, qa eval chain)<br>`009-streamlit-evaluate-QandA-from-long-document.py`

## 30 Days of Streamlit
- [Get started with Streamlit](https://docs.streamlit.io/get-started)<br>
  [30 Days of Streamlit](https://30days.streamlit.app/)

- **Install conda**<br>
  [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)
- **Terminal**
  ```
  conda create -n stenv python=3.9
  conda activate stenv
  pip install streamlit
  streamlit hello
  ```
  ```
  conda create --name myenv
  conda create --name myenv python=3.8 numpy
  conda activate myenv
  conda install --file requirements.txt
  conda deactivate

  conda info --envs
  conda env list
  conda env remove --name myenv
  ```
  ```
  python -m venv venv
  .\venv\Scripts\activate  # Windows
  source venv/bin/activate  # macOS
  pip install -r requirements.txt
  ```
- `streamlit_app.py`<br>`streamlit_app_layout.py`<br>`streamlit_app_dashboard.py`<br>`streamlit_app_shap.py`<br>`streamlit_app_zero_shot_classifier.py`<br>`streamlit_app_art.py`
  ```
  streamlit run streamlit_app.py
  ```
