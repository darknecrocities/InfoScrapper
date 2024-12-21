
# 🧰 A.I Web Scraper

Welcome to the **A.I Web Scraper** project! This project is a tool built using **Streamlit** to scrape web content, parse it using A.I, and export the results to an Excel file. It utilizes various web scraping techniques and AI-powered parsing to make data extraction efficient and easy.

## Features
- **Web Scraping**: Scrape any website for relevant content.
- **A.I Parsing**: Using A.I models to parse and summarize scraped content.
- **Database Integration**: Store scraped data in a SQLite database.
- **Export to Excel**: Export all scraped data to Excel for easy access.

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**: The programming language for the app.
- **Streamlit**: The framework for building the interactive web app.
- **pandas**: For managing and exporting data.
- **sqlite3**: For the database functionality.
- **openpyxl**: To export to Excel.

### Required Libraries

To run this project, you need to install the required libraries. You can do so using pip:

```bash
pip install streamlit pandas sqlite3 openpyxl
```

## How to Use

1. **Clone this repository**:
   - You can clone this repository to your local machine with:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   ```
   Replace `yourusername` and `repository-name` with your actual GitHub username and repo name.

2. **Run the Streamlit app**:
   Navigate to the project directory and run:
   ```bash
   streamlit run main.py
   ```

3. **Scrape a Website**:
   - Enter the URL of the website you wish to scrape and press "Scrape Site".
   - The tool will scrape the website and extract content from it.

4. **Parse the Content**:
   - Once the content is scraped, you can describe the type of data you want to extract.
   - For example, you can extract all headers, summaries, or specific sections.

5. **View Scraped Records**:
   - You can view the previously saved scraped records, which will display the **URL**, **Parsed Content**, and **Timestamp**.

6. **Export Data**:
   - Export all the scraped data to an **Excel** file using the "Export All Data to Excel" button.

## Database Integration
All scraped data is stored in a **SQLite database** called `scraper_data.db`. The database schema consists of:
- **id**: Primary key
- **url**: URL of the scraped website
- **parsed_content**: The parsed data/content
- **timestamp**: The time the data was scraped

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
If you would like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. We welcome suggestions and improvements!

## Acknowledgments
- **Streamlit**: For the framework.
- **OpenAI**: For AI-powered parsing.

## Contact
For any issues or suggestions, feel free to open an issue on this GitHub repository or contact me via email at `your-email@example.com`.

---
Made with 💚 using Streamlit and Python.

# 🧰 A.I Web Scraper

Welcome to the **A.I Web Scraper** project! This project is a tool built using **Streamlit** to scrape web content, parse it using A.I, and export the results to an Excel file. It utilizes various web scraping techniques and AI-powered parsing to make data extraction efficient and easy.

## Features
- **Web Scraping**: Scrape any website for relevant content.
- **A.I Parsing**: Using A.I models to parse and summarize scraped content.
- **Database Integration**: Store scraped data in a SQLite database.
- **Export to Excel**: Export all scraped data to Excel for easy access.

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**: The programming language for the app.
- **Streamlit**: The framework for building the interactive web app.
- **pandas**: For managing and exporting data.
- **sqlite3**: For the database functionality.
- **openpyxl**: To export to Excel.

### Required Libraries

To run this project, you need to install the required libraries. You can do so using pip:

```bash
pip install streamlit pandas sqlite3 openpyxl
```

## How to Use

1. **Clone this repository**:
   - You can clone this repository to your local machine with:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   ```
   Replace `yourusername` and `repository-name` with your actual GitHub username and repo name.

2. **Run the Streamlit app**:
   Navigate to the project directory and run:
   ```bash
   streamlit run main.py
   ```

3. **Scrape a Website**:
   - Enter the URL of the website you wish to scrape and press "Scrape Site".
   - The tool will scrape the website and extract content from it.

4. **Parse the Content**:
   - Once the content is scraped, you can describe the type of data you want to extract.
   - For example, you can extract all headers, summaries, or specific sections.

5. **View Scraped Records**:
   - You can view the previously saved scraped records, which will display the **URL**, **Parsed Content**, and **Timestamp**.

6. **Export Data**:
   - Export all the scraped data to an **Excel** file using the "Export All Data to Excel" button.

## Database Integration
All scraped data is stored in a **SQLite database** called `scraper_data.db`. The database schema consists of:
- **id**: Primary key
- **url**: URL of the scraped website
- **parsed_content**: The parsed data/content
- **timestamp**: The time the data was scraped

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
If you would like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. We welcome suggestions and improvements!

## Acknowledgments
- **Streamlit**: For the framework.
- **OpenAI**: For AI-powered parsing.

## Contact
For any issues or suggestions, feel free to open an issue on this GitHub repository or contact me via email at `your-email@example.com`.

---
Made with 💚 using Streamlit and Python.
