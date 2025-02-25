# WebScraperAI

## Overview
WebScraperAI is a web-based tool that allows users to perform question-answering on a given website URL. It supports multiple LLMs and has two modes of operation:

## Preview
![Screenshot 2025-02-23 130842](https://github.com/user-attachments/assets/23cbc98f-d875-43db-9d2f-9601d7e94ebb)


![Screenshot 2025-02-23 132439](https://github.com/user-attachments/assets/cbd001ba-8ef5-4b04-9aaf-ddd67b875199)


![Screenshot 2025-02-23 134013](https://github.com/user-attachments/assets/e6ea68dc-1b6b-4775-8510-6c65ec8b6c1f)


![Screenshot 2025-02-25 092021](https://github.com/user-attachments/assets/7fdb742c-36f3-4cbc-a231-6571876edd31)


![Screenshot 2025-02-25 092727](https://github.com/user-attachments/assets/f18e034f-77fe-4537-a535-fb3e9ea66526)


![Screenshot 2025-02-25 093013](https://github.com/user-attachments/assets/1595c817-6e5f-49b6-962d-2273593c87bc)



1. **Page-Specific Q&A**: Extracts information only from the given webpage.
2. **Deep Analysis Q&A**: Extracts information from the given page and all its linked pages (use cautiously, as it may take a long time for large websites).

The project uses **BeautifulSoup** for web scraping and a **RAG pipeline in LlamaIndex and HuggingFace** to enhance response accuracy. Supported LLMs include:

- OpenAI GPT-3.5
- OpenAI GPT-4
- Gemini Pro
- Gemini Ultra
- DeepSeek
- Groq

## Features
- Extracts and analyzes website content for Q&A.
- Offers two modes: specific page analysis and deep analysis.
- Supports multiple LLMs for flexibility.
- Built with Streamlit for an interactive UI.

## Installation
Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```sh
git clone https://github.com/tejas-130704/WebScraperAI.git
cd WebScraperAI
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### 1. Run the Streamlit App
```sh
streamlit run app.py
```

### 2. Enter Details
- **Select Model**: Choose an LLM for processing.
- **Enter API Key**: Provide the API key for the selected LLM.
- **Enter Website URL**: Input the URL to analyze.
- **Choose Deep Analysis (Optional)**: Check this box if you want to analyze linked pages.

### 3. Click **Load Website & LLM** to start the process.
- After processing, enter a question related to the webpage and click **Ask Question**.

## Caution ⚠️
- **Use Deep Analysis Only for Limited Scope Websites**: Avoid using it on large websites like Wikipedia, as the high number of linked pages may cause extreme delays or failures.
- **Respect Website Policies**: Some sites may have anti-scraping policies. Always ensure compliance.
- **API Limits**: LLM responses are subject to API limits and costs depending on the provider.

## Future Enhancements
- Implement caching to improve deep analysis speed.
- Add support for multi-threaded scraping.
- Introduce a ranking system for LLM performance comparison.

## Contributing
Pull requests are welcome! If you find any issues, feel free to open an issue in the repository.



