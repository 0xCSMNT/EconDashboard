# EconDashboard

# Links
#### [WebSite](https://econ-dash-production.up.railway.app/)
#### [YouTube Demo](https://youtu.be/XXtdK6Ncq4w)

# About
EconDash is a simple vizualization tool using economic data taken from the Federal Reserve Economic Database (FRED). It's a culmination of the skills and knowledge I've acquired throughout the CS50x course. Data is sourced from the FRED API, and stored in a cloud-based MongoDB database to reduce calls to the FRED and provide snappier response to the user. A GitHub Action runs every 12 hours to refresh the data in the database.

I chose this project because I am interested in financial & economic data, and I wanted to gain experience working with APIs, noSQL databases, hosting, caching and automating data actions from a cloud server.

Future versions should include more data sources and customizable charts.

# Technologies Used:
- Flask - Backend
- MongoDB - Database
- Bootstrap - Frontend Layout & Styling
- Chart.js - Data Vizualization
- Railway.app - Hosting

## Project Timeline and Tasks

#### Week 1: Initial Setup and Data Source Research
- [x] **Day 1:** Setup the initial GitHub repository and local development environment.
- [x] **Day 2-3:** Research APIs for Federal Reserve, ~~OECD, etc~~. Understand rate limits and data structures.
- [x] **Day 4:** Finalize list of indicators and data sources to be displayed on the dashboard.

#### Week 2: Backend Development and Data Retrieval
- [x] **Day 5-6:** Write Python scripts to pull data from finalized APIs.
- [x] **Day 7:** Create JSON object for cache ~~SQLite database schema~~.
- [x] **Day 8:** Secure your API key. ~~store API data in SQLite database~~.

#### Week 3: Front-end Development
- [x] **Day 9:** Create the front-end layout with HTML and CSS.
- [x] **Day 10-11:** Learn basic Chart.js ~~D3.js~~ for data visualization.
- [x] **Day 12:** Implement ~~D3.js~~ charts and graphs based on the data in JSON object ~~SQLite database~~.

#### Week 4: Full-Stack Integration and Testing
- [x] **Day 13:** Integrate the Flask backend with the front-end. Migrate api logic from ipynb to .py
- [x] **Day 14:** Style the front end
- [x] **Day 15:** Get database & frontend hosted on Railway

#### Final Days: Deployment and Documentation
- [x] **Day 16:** Implement caching logic to update DB every 12 hours. ~~Decide on hosting (Heroku or GitHub Pages)~~. 
- [x] **Day 17:** Write final documentation in README, including how to run the project locally and how to use the deployed application.







