# Google Dorking Tool

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

## 📄Description
A Python Script for performing advanced Google searches (Google Dorking using the Google Custom Search API).
It enables you to search for specific information on the web through advanced search queries and retrieve multiple results efficiently.

## ⚙️Features
- Supports **Python 3.x** only.
- Uses the **Google Custom Search API** for searching.
- Allows you to specify the number of results or fetch all available results.
- Option to save the output to a text file.
- Displays URLs fetched from the search query.
- Graceful handling of interruptions and errors.

## 🚀Installation
1. Clone the repository or download the script:
    ```bash
    https://github.com/mahaveer-choudhary/DorkXplorer.git
    cd DorkXplorer
    ```

2. Install required dependencies : 
    ```bash
    pip install requests
    ```

## 🛠️Usage

### Run the script

for windows :
```bash
python dork.py
```

for linux :
```bash
python3 dork.py
```

# 💡Example Execution : 

![Example](https://github.com/mahaveer-choudhary/DorkXplorer/blob/main/images/image%202.png)

# ✅Output
- URLs matching your dorking query will be displayed. 
- If you choose to save the output, it will be stored in the specific text file. 

## ⚠️Requirements 
- **Python 3.x**
- **requests** library

# 🔥Important Notes
- The script uses **Google Custom Search API** credentials. Replace the `api_key` and `search_engine_id` with your own valid credentials.
- To avoid rate-limiting issues, the script includes a **1-second delay** between requests.

##  📸 Screenshots
### 🔹Example Output
![output image](https://github.com/mahaveer-choudhary/DorkXplorer/blob/main/images/image%201.png)
