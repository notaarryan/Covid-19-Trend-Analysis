# COVID-19 Trend Analysis

## Overview
The **Covid19TrendAnalysis** project provides visual insights into the spread of COVID-19 across different countries. It processes global COVID-19 data, generating time series plots to display the number of confirmed cases, deaths, and recoveries for each country. The goal of the project is to offer an easy-to-understand visualization of how the pandemic evolved over time in various regions.

## Features
- **Data Cleaning and Preprocessing**: The script handles missing data and aggregates it to generate meaningful summaries.
- **Trend Visualization**: Plots for confirmed cases, deaths, and recoveries are generated for each country.
- **Country-Specific Analysis**: Automatically loops through all available countries and generates individual plots.
- **Interactive Exploration**: View trends for each country in a clear, graphical format.

## Data
The project uses COVID-19 data in CSV format. The dataset includes:
- Date of observation
- Country/Region
- Confirmed cases, deaths, and recovered cases

You can update the dataset to analyze the latest trends, or use historical data to view past trends.

## Requirements
To run the project, you need to have Python and the following libraries installed:
- `pandas` (for data manipulation)
- `numpy` (for numerical operations)
- `matplotlib` (for data visualization)

Install them using:
```bash
pip install pandas numpy matplotlib
```

How to Run

1.	Clone this repository:
```bash
git clone https://github.com/notaarryan/Covid-19-Trend-Analysis.git cd Covid-19-Trend-Analysis
```
2.	Place your updated COVID-19 data file (covid_19_data.csv) in the root directory.
3.	Run the script:
```bash
python main.py
```
4.	The script will display time series plots for confirmed cases, deaths, and recoveries for each country in the dataset.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
