# BC Tourism Analytics

_An end-to-end data science project powered by open data from the British Columbia government._

---

## 🧑‍💻 Author

**Fatih**

---

## 📦 Overview

This project explores British Columbia's tourism sector using publicly available data from the BC Government Open Data Catalogue. It includes:

- Jupyter-based data cleaning and preprocessing
- A Plotly Dash dashboard with interactive analytics
- Advanced visualizations and multi-metric comparisons
- A foundation for future machine learning modeling

All components are neatly organized to support collaboration, transparency, and reproducibility.

---

## 📁 Project Structure

bc_tourism_analytics/ ├── data-cleaning/ # Jupyter notebook & cleaned CSV dataset ├── dash-app/ # Dash dashboard files: app.py, assets/, README ├── ml-models/ # (optional) future ML notebooks ├── LICENSE.md # Open Government Licence – BC └── README.md # This file


---

## 🧪 Technologies Used

- Python: pandas, plotly, dash  
- Jupyter Notebook  
- Git & GitHub  
- Open Government Data BC  

---

## 📊 Dash Dashboard (in `dash-app/`)

A full-featured dashboard offering:

- Compare Years mode with dual legends (colors for metrics, patterns for years)  
- Date Range mode for flexible time-series analysis  
- Advanced analytics including horizon charts, stacked area plots, and event annotations

To run the dashboard locally:

```bash
cd dash-app
python app.py

Open your browser at http://127.0.0.1:8050

📥 Data Source & Licensing
Tourism data is sourced from the BC Government Open Data Catalogue, and is subject to:

Licence: Open Government Licence – British Columbia Full terms: included in LICENSE.md

Roadmap
[x] Cleaned and preprocessed BC tourism data

[x] Built interactive dashboard with advanced charts

[ ] Add machine learning forecasts and analytics in ml-models/

[ ] Make dashboard responsive across devices

[ ] Deploy dashboard online (e.g., Heroku, Azure)

[ ] Publish project highlights on LinkedIn and Kaggle

Contact
GitHub: [https://github.com/fohu44/bc_tourism_analytics]

LinkedIn: [https://www.linkedin.com/in/fatihozcelik/]

Feel free to connect or collaborate!