# Data Collection - Web Scraping & Data Extraction Course Materials

This folder contains comprehensive web scraping examples that demonstrate various techniques for collecting data from different sources. Each scraper showcases different approaches to data extraction, from simple RSS feeds to complex AJAX requests and parallel processing.

## 📚 File Overview

### 1. `rss_feed_scraper.py` - RSS Feed Data Extraction
**🎯 What is taught:**
- **RSS Feed Parsing**: Extracting news articles from RSS feeds
- **Feedparser Library**: Using the `feedparser` library for RSS/XML parsing
- **JSON Data Structure**: Converting RSS data to structured JSON format
- **Simple Data Extraction**: Basic text extraction from feed entries

**📖 Learning Approach:**
- Introduction to RSS feed structure and parsing
- Simple data extraction without complex web scraping
- Converting unstructured feed data to structured format
- Working with news data from NDTV RSS feed

**🔧 Key Features:**
- Extracts article titles, links, descriptions, and content
- Converts RSS feed to JSON format
- Handles multiple feed entries efficiently
- Demonstrates feed data structure exploration

**📊 Sample Output:**
```json
{
    "articles": [
        {
            "title": "Article Title",
            "link": "https://example.com/article",
            "description": "Article summary",
            "detail": "Full article content"
        }
    ]
}
```

---

### 2. `scraper_sulekha.py` - Basic GET Request Web Scraping
**🎯 What is taught:**
- **HTTP GET Requests**: Making basic web requests using `requests` library
- **HTML Parsing**: Using BeautifulSoup for HTML content extraction
- **CSS Selectors**: Finding elements using class names and attributes
- **Data Extraction**: Extracting structured data from HTML elements
- **File Operations**: Saving HTML content and extracted data to files

**📖 Learning Approach:**
- Step-by-step HTML parsing and data extraction
- Working with real business listing websites
- Handling complex HTML structures
- Converting scraped data to CSV format

**🔧 Key Features:**
- Extracts business information from Sulekha.com
- Handles business IDs, names, locations, ratings
- Extracts services, response times, and scores
- Saves data to both HTML and CSV formats

**📊 Data Extracted:**
- Business ID and name
- Location (locality, latitude, longitude)
- Ratings and reviews
- Services offered
- Response time and Sulekha score

---

### 3. `nse_scraper2.py` - AJAX GET Request with Session Management
**🎯 What is taught:**
- **Session Management**: Maintaining cookies and session state
- **AJAX GET Requests**: Handling dynamic content loaded via AJAX
- **Headers Management**: Setting proper User-Agent and request headers
- **Rate Limiting**: Implementing delays between requests
- **Error Handling**: Managing timeouts and request failures
- **JSON Data Processing**: Working with API responses

**📖 Learning Approach:**
- Advanced session-based scraping techniques
- Working with financial APIs and historical data
- Handling authentication and session cookies
- Processing large datasets with proper error handling

**🔧 Key Features:**
- Establishes session with NSE website
- Extracts historical Nifty 50 index data
- Handles multiple years of data collection
- Implements proper delays and error handling
- Converts data to pandas DataFrame

**📊 Data Extracted:**
- Historical Nifty 50 index data
- Date-wise closing prices and volumes
- Multiple years of financial data
- Structured CSV output

---

### 4. `nseindices_scraper.py` - AJAX POST Request with JSON Payload
**🎯 What is taught:**
- **POST Requests**: Making POST requests with JSON payloads
- **Request Headers**: Setting proper headers for AJAX requests
- **JSON Payload Construction**: Building complex request payloads
- **Response Processing**: Handling JSON responses from APIs
- **Data Aggregation**: Combining data from multiple requests

**📖 Learning Approach:**
- Advanced AJAX request handling
- Working with POST APIs that require specific payloads
- Processing JSON responses and data aggregation
- Handling large-scale data collection

**🔧 Key Features:**
- Makes POST requests to Nifty Indices API
- Extracts historical Nifty 100 data
- Handles JSON payload construction
- Aggregates data across multiple years
- Implements proper error handling and delays

**📊 Data Extracted:**
- Historical Nifty 100 index data
- Date-wise index values and changes
- Multiple years of historical data
- Structured CSV output

---

### 5. `nseindices_scraper_parallel.py` - Parallel Processing with Proxy Support
**🎯 What is taught:**
- **Parallel Processing**: Using ThreadPoolExecutor for concurrent requests
- **Proxy Management**: Implementing proxy rotation for request distribution
- **Rate Limiting**: Advanced rate limiting with random delays
- **Error Handling**: Robust error handling for parallel requests
- **Resource Management**: Managing concurrent connections efficiently

**📖 Learning Approach:**
- Advanced scraping techniques for high-volume data collection
- Implementing proxy rotation to avoid IP blocking
- Parallel processing for improved performance
- Production-ready scraping with proper resource management

**🔧 Key Features:**
- Parallel processing of multiple indices
- Proxy rotation and management
- Random delays to avoid detection
- Robust error handling and retry logic
- Efficient resource utilization

**📊 Advanced Features:**
- Proxy discovery and validation
- Concurrent data collection from multiple sources
- Automatic proxy rotation on failures
- Scalable architecture for large datasets

---

## 🎓 Learning Path

### For Beginners:
1. Start with **`rss_feed_scraper.py`** - Learn basic data extraction
2. Move to **`scraper_sulekha.py`** - Master HTML parsing and GET requests
3. Practice with real websites and data extraction

### For Intermediate Users:
1. Complete basic scrapers for foundation
2. Advance to **`nse_scraper2.py`** - Learn session management and AJAX
3. Practice with **`nseindices_scraper.py`** - Master POST requests

### For Advanced Users:
1. Master all basic and intermediate techniques
2. Study **`nseindices_scraper_parallel.py`** - Learn parallel processing
3. Implement production-ready scraping solutions

### Recommended Order:
```
rss_feed_scraper.py → scraper_sulekha.py → nse_scraper2.py → nseindices_scraper.py → nseindices_scraper_parallel.py
```

## 🛠️ Prerequisites

- **Python Knowledge**: Basic Python programming skills
- **Web Scraping Libraries**: `pip install requests beautifulsoup4 feedparser pandas lxml`
- **HTTP Understanding**: Basic knowledge of HTTP methods (GET, POST)
- **HTML/CSS**: Understanding of HTML structure and CSS selectors
- **JSON**: Familiarity with JSON data format

## 💡 Key Learning Outcomes

After completing these materials, you will be able to:

✅ **Data Extraction**: Extract data from various web sources  
✅ **RSS Feed Processing**: Parse and structure RSS feed data  
✅ **HTML Parsing**: Navigate and extract data from HTML documents  
✅ **AJAX Handling**: Work with dynamic content and JavaScript-loaded data  
✅ **Session Management**: Maintain sessions and handle authentication  
✅ **Parallel Processing**: Implement concurrent data collection  
✅ **Proxy Management**: Use proxies for distributed scraping  
✅ **Error Handling**: Build robust scraping solutions  
✅ **Data Storage**: Save extracted data in various formats  

## 🎯 Practical Applications

These materials prepare you for:

- **News Aggregation**: Collecting news from multiple RSS feeds
- **Business Intelligence**: Extracting business listings and information
- **Financial Data Collection**: Gathering stock market and financial data
- **Market Research**: Collecting competitive intelligence
- **Academic Research**: Data collection for research projects
- **E-commerce**: Product information and pricing data extraction

## 🔧 Technical Skills Covered

### **Basic Scraping:**
- HTTP requests (GET/POST)
- HTML parsing with BeautifulSoup
- CSS selector usage
- Data extraction and cleaning

### **Advanced Techniques:**
- Session management and cookies
- AJAX request handling
- JSON payload construction
- Rate limiting and delays

### **Production Features:**
- Parallel processing
- Proxy rotation
- Error handling and retry logic
- Resource management

### **Data Processing:**
- JSON data handling
- CSV file generation
- Pandas DataFrame operations
- Data aggregation and cleaning

## ⚠️ Important Considerations

### **Legal and Ethical:**
- Always check website's robots.txt file
- Respect rate limits and terms of service
- Use scraping responsibly and ethically
- Consider using official APIs when available

### **Technical Best Practices:**
- Implement proper delays between requests
- Use appropriate User-Agent headers
- Handle errors gracefully
- Monitor and log scraping activities

### **Performance Optimization:**
- Use session objects for multiple requests
- Implement parallel processing when appropriate
- Cache data to avoid redundant requests
- Monitor memory usage with large datasets
