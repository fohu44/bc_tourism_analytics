## 👤 Author

Created by **Fatih**  
📧 Email: fatih.ozcelk@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/fatihozcelik/)  


BC Tourism Dashboard
A data‐driven dashboard showcasing key tourism metrics for British Columbia.

Author
Fatih

Overview
This interactive Dash application provides:

Year-over-year and custom date-range comparisons of tourism metrics

Core visualizations: line charts and grouped bar charts

Advanced analytics: horizon charts, stacked-area charts, and event annotation timelines

Flexible controls for selecting years, date ranges, and metrics

Features
Compare Years Select up to three years and one or more metrics to see side-by-side monthly bars (colored by metric, patterned by year) and overlaid lines.

Custom Date Range Pick any start/end period to analyze time-series behavior and aggregated totals.

Advanced Analytics

Horizon Chart: Condenses value intensities into color bands.

Stacked Area Chart: Shows evolution of visitor origin markets over time.

Event Annotations: Highlights major events (e.g., COVID-19, wildfires) on a timeline.

Installation
Clone this repository

git clone https://github.com/fohu44/bc-tourism-dashboard.git
cd bc-tourism-dashboard
Create and activate a Python environment

python3 -m venv venv
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Place your CSV data (monthly_tourism_cleaned.csv) in the project root.

Running the App
bash
python app.py
Then open your browser to http://127.0.0.1:8050/.

Data Source & Licensing
This dashboard uses tourism data sourced from the British Columbia Government’s Open Data Catalogue.

Data Licence: Open Government Licence – British Columbia

Last Updated: April 11, 2025

Full Terms: https://www2.gov.bc.ca/gov/content/data/open-data/open-government-licence-bc

Attribution
Contains information licensed under the Open Government Licence – British Columbia.

You are free to copy, modify, publish, translate, adapt, distribute or otherwise use the data for any lawful purpose, provided that you include the following attribution:

Contains information licensed under the Open Government Licence – British Columbia.

Disclaimer
The data is provided “as is” without warranty.

The Province of British Columbia is not liable for any errors or omissions.

This project does not imply endorsement by the Province of British Columbia.

Future Improvements
Add caching or background processing for faster performance

Enhance mobile responsiveness via Dash Bootstrap components

Integrate forecasting models (Prophet, ARIMA) with error-metric comparisons

Implement user authentication and role-based access

Contact
Fatih Email: fatih.ozcelk@gmail.com GitHub: https://github.com/fohu44

Feel free to open an issue or submit a pull request!