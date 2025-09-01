# Pandas - Data Analysis & Manipulation Course Materials

This folder contains comprehensive materials for learning pandas, Python's powerful data analysis library. The course focuses on practical data manipulation, financial data analysis, and real-world applications using Indian stock market data.

## 📚 File Overview

### 1. `pandas1.ipynb` - Pandas Fundamentals & Series Operations
**🎯 What is taught:**
- **Pandas Configuration**: Setting up pandas and numpy for data analysis
- **Series Creation**: Building pandas Series with different index types
- **Indexing & Selection**: Accessing data using labels and positions
- **Date Handling**: Working with datetime indices and date ranges
- **Data Alignment**: Combining multiple Series with automatic index alignment
- **CSV Data Loading**: Reading financial data from CSV files
- **Data Type Conversion**: Converting string dates to datetime objects
- **Basic Visualization**: Creating simple plots of financial time series data
- **Data Manipulation**: Adding calculated columns and handling missing data

**📖 Learning Approach:**
- Step-by-step introduction to pandas Series
- Practical examples using temperature data and financial data
- Hands-on exercises with real CSV files
- Progressive complexity from basic operations to data analysis

**🔧 Key Projects:**
- Temperature comparison between cities (Chennai vs Mumbai)
- Stock price data loading and preprocessing
- Time series data manipulation and visualization
- Monthly and yearly return calculations

**📊 Sample Data Used:**
- Temperature data for multiple cities
- INFY (Infosys) stock price data with OHLCV information

---

### 2. `pandas2.ipynb` - Advanced DataFrame Operations & Financial Analysis
**🎯 What is taught:**
- **DataFrame Creation**: Building DataFrames from CSV files and custom data
- **Data Inspection**: Understanding data structure, shape, and types
- **Column Operations**: Renaming, reordering, adding, and deleting columns
- **Data Concatenation**: Combining DataFrames using concat and append
- **Row Operations**: Adding, replacing, and manipulating rows
- **Data Joins**: Merging and joining DataFrames on common keys
- **GroupBy Operations**: Aggregating data by categories (industry, sector)
- **Advanced Filtering**: Complex boolean indexing and conditional selection
- **Financial Calculations**: Percentage changes, returns, and market analysis
- **Data Visualization**: Creating bar charts and custom visualizations

**📖 Learning Approach:**
- Advanced DataFrame manipulation techniques
- Real-world financial data analysis scenarios
- Industry-level data aggregation and analysis
- Performance optimization and best practices

**🔧 Key Projects:**
- Nifty 50 stock market data analysis
- Industry-wise performance analysis
- Market advances/declines classification
- Custom color-coded visualizations
- Sector-wise performance comparisons

**📊 Sample Data Used:**
- Nifty 50 index data with 50+ stocks
- Company information with industry classifications
- Stock price data with technical indicators

---

### 3. `ind_nifty50list.csv` - Nifty 50 Company Information
**📋 Data Structure:**
- **Company Name**: Full company names
- **Industry**: Sector classification (Financial Services, IT, Healthcare, etc.)
- **Symbol**: Stock exchange symbols
- **Series**: Equity series (EQ)
- **ISIN Code**: International Securities Identification Number

**🎯 Purpose:**
- Reference data for company identification
- Industry classification for sector analysis
- Mapping between company names and stock symbols
- Data validation and cross-referencing

---

### 4. `nifty50.csv` - Nifty 50 Market Data
**📋 Data Structure:**
- **Price Data**: Open, High, Low, Previous Close, LTP (Last Traded Price)
- **Technical Indicators**: 52-week High/Low, 30-day and 365-day percentage changes
- **Volume & Value**: Trading volume and transaction value in crores
- **Market Movement**: Change and percentage change from previous close


---

### 5. `INFY.csv` - Infosys Stock Data
**📋 Data Structure:**
- **Time Series Data**: Daily stock prices over extended period
- **OHLCV Data**: Open, High, Low, Close, Volume
- **Date Index**: Chronological order for time series analysis
- **Historical Data**: Sufficient data for trend analysis and backtesting



---

## 🎓 Learning Path

### For Beginners:
1. Start with **`pandas1.ipynb`** - Master pandas Series and basic operations
2. Practice with the temperature data examples
3. Move to stock data loading and basic manipulation

### For Intermediate Users:
1. Complete **`pandas1.ipynb`** for foundation
2. Advance to **`pandas2.ipynb`** for complex DataFrame operations
3. Practice with real financial data analysis


### Recommended Order:
```
pandas1.ipynb → pandas2.ipynb
```

## 🛠️ Prerequisites

- **Python Knowledge**: Basic Python programming skills
- **Pandas Installation**: `pip install pandas numpy matplotlib`
- **Data Understanding**: Basic knowledge of financial markets (helpful)
- **CSV Files**: Understanding of comma-separated values format
- **Jupyter Environment**: Notebook or similar interactive environment


## 📊 Data Analysis Skills Covered

### **Basic Operations:**
- Series and DataFrame creation
- Indexing and selection
- Data type handling
- Missing data management

### **Advanced Operations:**
- Data concatenation and merging
- GroupBy operations
- Custom aggregations
- Performance optimization


### **Visualization:**
- Line charts for time series
- Bar charts for comparisons
- Custom color coding
- Multi-panel displays

## 🔧 Technical Skills

- **Pandas API**: Mastery of Series and DataFrame methods
- **Data Cleaning**: Handling messy real-world data
- **Performance Tuning**: Efficient data operations
- **Memory Management**: Working with large datasets
- **Error Handling**: Robust data processing pipelines

