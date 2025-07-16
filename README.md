# 📊 FinanceProfileAnalyzer

A Python-based data analysis tool designed to explore and visualize income and expenditure trends across different regions. This project performs data cleaning, statistical review, and duplication analysis while delivering visual insights using Matplotlib.

---

## 📌 Features

* ✅ Cleans and preprocesses tabular financial data (e.g., missing values, duplicates)
* ✅ Visualizes income vs. expenditure using overlapping histograms
* ✅ Breaks down data by regions and flags duplicated entries
* ✅ Provides statistical summaries using `describe()`
* ✅ Easy to extend with more regions or financial indicators

---

## 🧠 How It Works

1. Loads CSV data (`Book1.csv`)
2. Cleans the data (removes duplicates and null values)
3. Displays statistical summaries
4. Generates comparative histograms of Income vs Expenditure
5. Analyzes each region for duplicated income/expenditure entries
6. Prints insights by region

---

## 📁 Project Structure

```
FinanceProfileAnalyzer/
├── data/
│   └── Book1.csv                # Input dataset
├── analyzer.py                  # Main logic for analysis
├── README.md                    # Project documentation
```

---

## 📊 Sample Output

* Income vs Expenditure histogram:

  * Income bars shown in pink
  * Expenditure bars shown in green
* Console output:

  * Summary statistics (mean, min, max, etc.)
  * Duplicates per region
  * Region-wise cleaned data display

---

## 🛠 Dependencies

* Python 3.6+
* pandas
* matplotlib
* numpy

> Install them via:

```bash
pip install pandas matplotlib numpy
```

---

## 🚀 Getting Started

1. Clone the repo

   ```bash
   git clone https://github.com/yourusername/FinanceProfileAnalyzer.git
   cd FinanceProfileAnalyzer
   ```

2. Place your CSV file inside the `data/` folder (named `Book1.csv` or adjust the path in code)

3. Run the analysis

   ```bash
   python analyzer.py
   ```

---

## 📌 Use Case Ideas

* Regional financial pattern analysis
* Budget planning tools
* Market segmentation research
* Education and occupation correlation (future feature)

---

## 🔒 License

This project is licensed under the MIT License.

---
