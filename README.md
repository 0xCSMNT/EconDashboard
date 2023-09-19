# EconDashboard

## Links
#### [WebSite](https://econ-dash-production.up.railway.app/)
#### [YouTube Demo](https://youtu.be/XXtdK6Ncq4w)

## About
EconDash is a simple vizualization tool using economic data taken from the Federal Reserve Economic Database (FRED). It's a culmination of the skills and knowledge I've acquired throughout the CS50x course. Data is sourced from the FRED API, and stored in a cloud-based MongoDB database to reduce calls to the FRED and provide snappier response to the user. A GitHub Action runs every 12 hours to refresh the data in the database.

I chose this project because I am interested in financial & economic data, and I wanted to gain experience working with APIs, noSQL databases, hosting, caching and automating data actions from a cloud server.

Future versions should include more data sources and customizable charts.

## Technologies Used:
- Flask - Backend
- MongoDB - Database
- Bootstrap - Frontend Layout & Styling
- Chart.js - Data Vizualization
- Railway.app - Hosting

## Specific Files & Development Process

- app.py - The backend is built with Flask. The core functions of the app is to pull down the data hosted in the database and process it and make it available to the front end. I found it helpful to continue to work with Flask, but now that I am done I think my next project will use node.js so I can get familiar with that technology.

- dashboard.html - This is the main fronted page that contains all of the data vizualisations. I layed it out with Bootstrap 5. I spent a lot of time researching CSS and Tailwaind, but specifically decided to go with Bootstrap because of the simple grid system and the dynamic scaling to fit different size screens. Towards the end, I decided that I did not really like the look or restrictive design of Bootstrap, and would probably take the extra time to learn Tailwind for my next project.

- makeChart.js - This is where the chart.js function lives. I have a total of twelve charts in the dashboard, and the dashboard.html file was already extremely long, so I decided to use a charting function to help with readability and maintenance. This did create some limitations though, and made it difficult to specify how I wanted different charts to behave. I also considered D3.js, but ultimatey went with chart.js as it was simpler and I thought I could learn it faster.

- update_db.py - This hosts the function that pings the FRED API and updates the data in the database. I originally had another file called get_data.py that actually created a local json object that I used as my db while developing. One of the most painful parts (8 hours) was uploading the data from my local json to the db. I found the documentation to be lacking, and ended up trying many, many variations on the same command before I figured out the solution.

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







