 # Econ Dashboard

 # Scope and Planning
 
 ### Questions to Clarify

**Target Audience:** Who will be the end-users of your website? Is this dashboard for a specific industry, general public, or for personal use?
_It's more for personal use. Over time it might grow into some kind of portfolio piece, but that is less important_

**Data Sources:** What APIs will you be pulling data from? Have you checked their rate limits and data structures?
_I have not fully decided yet, some gov sources like Fed Reserve, OECD would be great if possible. I think this will be step one - clarifying what metrics and data sources I am going to use._

**Dashboard Features:** What specific features do you want your dashboard to have? (e.g., real-time updates, interactive graphs, user login, etc.)
_Nothing too sophisticated, just a single page with a bunch of indicators I find interesting_

**Caching:** What is the specific type of database you plan to use for caching? How frequently will you update it?
_I will try to use SQLite3 as I am familiar with it. I am also open to saving data in a JSON format if it is more suitable to the data, but that may add somewhat to learning time_

**Graph Types:** You mentioned using D3 for graphs; what types of graphs are you planning to include?
_Bar charts, line graphs mostly. I'm interested in correlations between assets and time series, so open to other suggestions_

**Hosting:** Do you have any preferences between GitHub Pages and Heroku based on your project's needs?
_It comes down to what resources I will need for my backed to operate correctly. I would like to rely on the simplest tool for the job._

**Technology Stack:** You've mentioned HTML, CSS, Python, Flask, SQL, JS, and D3. Any other technologies or libraries you're considering?
_Pandas, datareader, some API libraries for python. Anything else I might need for exploratory data analysis as I figure out what to include in the dashboards and any dataprocessing I will need to do_

**Time Frame:** What is the estimated time you're allocating for this project?
_10-15 days_

## General Tips

Start Small: Aim for a Minimum Viable Product (MVP) first. This will be the simplest version of your dashboard that still provides value.

Divide and Conquer: Break down the project into smaller tasks (e.g., API integration, database setup, front-end development, etc.) and prioritize them.

Identify Dependencies: Some tasks will depend on the completion of others. Make sure to identify these to avoid roadblocks later.

Iterate: Once the MVP is complete, you can iteratively add more features, guided by user feedback if possible.

Version Control: Since you're familiar with Git, make sure to use it effectively to manage different versions of your project.

Test: Don't forget to include time for testing, especially for integrations between different components like the API, caching layer, and front-end.

Documentation: Keep notes on your code, especially if you're planning to grow or maintain this project long-term.

## Specific Tips

APIs & Caching: Given that you aim to pull data from multiple APIs and use caching to reduce calls, plan how you'll sync data between your cache and the actual APIs. Decide on a caching strategy that aligns with the API rate limits.

JS & D3 Learning: As you mentioned learning JS and D3 for this project, allocate specific time for this. It might be beneficial to go through some quick tutorials to get a hang of the syntax and functionalities before diving into the project.

Full-Stack Goals: Since your objective is to get a grounding in full-stack development, pay attention to how each component (front-end, back-end, database) interacts with each other. This will be a crucial learning point for you.

