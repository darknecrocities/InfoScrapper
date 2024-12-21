import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from scrape import (
    scrape_website, 
    split_dom_content,
    clean_body_content,
    extract_body_content,
)
from parse import parse_with_ollama

# Set Streamlit Page Configurations
st.set_page_config(
    page_title="A.I Web Scraper",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Database setup
def init_db():
    conn = sqlite3.connect("scraper_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ScraperData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            parsed_content TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Export data to Excel
def export_to_excel():
    # Fetch data from the database
    conn = sqlite3.connect("scraper_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url, parsed_content, timestamp FROM ScraperData")
    records = cursor.fetchall()
    conn.close()

    # Create a DataFrame from the fetched records
    df = pd.DataFrame(records, columns=["URL", "Parsed Content", "Timestamp"])

    # Export the DataFrame to an Excel file
    file_path = "scraper_data.xlsx"
    try:
        df.to_excel(file_path, index=False, engine="openpyxl")
        st.success(f"Data has been successfully exported to {file_path}")
    except Exception as e:
        st.error(f"Error exporting data: {e}")

init_db()

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #e09, #d0e);
        font-family: 'Roboto', sans-serif;
        color: #333;
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .stTextArea textarea {
        border-radius: 8px;
        transition: border-color 0.3s;
        border: 2px solid #ccc;
    }
    .stTextArea textarea:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 8px rgba(76, 175, 80, 0.3);
    }
    .stExpander {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 10px;
        background-color: #f9f9f9;
        transition: transform 0.3s;
    }
    .stExpander:hover {
        transform: scale(1.02);
    }
    footer {
        text-align: center;
        padding: 10px;
        background-color: #333;
        color: white;
        margin-top: 20px;
        border-radius: 8px;
        animation: slideUp 1s ease-out;
    }
    @keyframes slideUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title(
    "🧰 A.I Web Scraper",
    help="An interactive tool to scrape and parse web content using AI."
)

# Input URL
url = st.text_input(
    "Enter a Website URL:", 
    placeholder="https://example.com",
    help="Paste the URL of the website you want to scrape.",
)

# Scraping Section
if st.button("Scrape Site", help="Click to scrape the website for data"):
    if url:
        with st.spinner("Scraping the website... 🔄"):
            try:
                result = scrape_website(url)
                body_content = extract_body_content(result)
                cleaned_content = clean_body_content(body_content)

                # Save scraped content in session state
                st.session_state.dom_content = cleaned_content

                # Display DOM Content
                with st.expander("View Scraped DOM Content", expanded=False):
                    st.text_area("DOM Content", cleaned_content, height=300)
            except Exception as e:
                st.error(f"Error scraping the website: {e}")
    else:
        st.error("Please enter a valid URL before scraping.")

# Parsing Section
if "dom_content" in st.session_state:
    st.subheader("🔄 Parse the Content")

    # Input for parsing description
    parse_description = st.text_area(
        "Describe what you want to parse:",
        placeholder="E.g., Extract all the headers or summarize the content",
        help="Provide a description of what you want the scraper to do."
    )

    # Parse Content Button
    if st.button("Parse Content", help="Click to parse the scraped content"):
        if parse_description:
            with st.spinner("Parsing the content... 🧰"):
                try:
                    # Process the parsing request
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    result = parse_with_ollama(dom_chunks, parse_description)

                    # Save parsed content to database
                    conn = sqlite3.connect("scraper_data.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO ScraperData (url, parsed_content, timestamp) VALUES (?, ?, ?)",
                        (url, result, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    )
                    conn.commit()
                    conn.close()

                    # Display parsed results
                    st.success("Parsing complete!")
                    st.markdown(
                        f"**Parsed Results:**\n\n{result}",
                        unsafe_allow_html=False,
                    )
                except Exception as e:
                    st.error(f"Error parsing the content: {e}")
        else:
            st.error("Please describe what you want to parse.")

# View Saved Records
st.subheader("📜 View Scraped Records")
if st.button("Show Records", help="View all saved scraped records"):
    conn = sqlite3.connect("scraper_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url, parsed_content, timestamp FROM ScraperData")
    records = cursor.fetchall()
    conn.close()

    if records:
        for record in records:
            st.markdown(f"- **URL**: {record[0]}\n- **Parsed Content**: {record[1]}\n- **Timestamp**: {record[2]}\n---")
    else:
        st.info("No records found.")

# Export to Excel Button
st.subheader("📤 Export to Excel")
if st.button("Export All Data to Excel", help="Click to export all records to an Excel file"):
    export_to_excel()

# Footer Section
st.markdown(
    """
    --- 
    <footer>
    **Developed with 💚 using Streamlit**<br>
    Visit [Streamlit Docs](https://docs.streamlit.io) for more information.
    </footer>
    """,
    unsafe_allow_html=True,
)
