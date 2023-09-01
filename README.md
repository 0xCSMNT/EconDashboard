# EconDashboard

EconDashboard is a simple, single-page application designed to pull and visualize key economic indicators. The project is under active development and aims to become a useful tool for personal research and possibly more. I'm using GPT4 as a collaborative tool to help scope, plan, and troubleshoot various aspects of the project. 



## Project Timeline and Tasks

#### Week 1: Initial Setup and Data Source Research
- [x] **Day 1:** Setup the initial GitHub repository and local development environment.
- [x] **Day 2-3:** Research APIs for Federal Reserve, ~~OECD, etc~~. Understand rate limits and data structures.
- [x] **Day 4:** Finalize list of indicators and data sources to be displayed on the dashboard.

#### Week 2: Backend Development and Data Retrieval
- [x] **Day 5-6:** Write Python scripts to pull data from finalized APIs.
- [x] **Day 7:** Create JSON object for cache ~~SQLite database schema~~.
- [ ] **Day 8:** Implement caching logic to update JSON every 12 hours using Github Actions ~~store API data in SQLite database~~.

#### Week 3: Front-end Development
- [ ] **Day 9:** Design the front-end layout with HTML and CSS.
- [ ] **Day 10-11:** Learn basic D3.js for data visualization.
- [ ] **Day 12:** Implement D3.js charts and graphs based on the data in SQLite database.

#### Week 4: Full-Stack Integration and Testing
- [ ] **Day 13:** Integrate the Flask backend with the front-end.
- [ ] **Day 14:** Test the complete application locally for bugs and performance issues.
- [ ] **Day 15:** Make any necessary adjustments based on testing.

#### Final Days: Deployment and Documentation
- [ ] **Day 16:** Secure your API key. Decide on hosting (Heroku or GitHub Pages) and deploy the project. 
- [ ] **Day 17:** Write final documentation in README, including how to run the project locally and how to use the deployed application.



## Project Information

### Target Audience
Primarily for personal use, though the project may evolve into a portfolio piece in the future.

### Data Sources
V1 will focus entirely on US economic data available on the FRED database: https://fred.stlouisfed.org/docs/api/fred/. 

Future versions will include more diverse data sources.

### Dashboard Features
The focus is on a simple dashboard showcasing various economic indicators such as GDP, CPI etc.

### Caching
The cache will use a JSON object due to the small size and simplicity of the data. 

~~SQLite3 is the database being considered for caching, with JSON as an alternative.~~

### Hosting
Hosting will be on GitHub pages, and the backend requirements will be minimized to enable that.

~~Undecided between GitHub Pages and Heroku; dependent on back-end resource needs.~~

### Technology Stack
HTML, CSS, Python, Flask, ~~SQLite3~~, JavaScript, Chart.js, ~~D3.js~~, ~~Pandas~~

### Time Frame
The project is estimated to be completed in 10-15 days.



## Recommendations by GPT4

### Finalize Data Sources
Determine the APIs or data sources as early as possible to plan for rate limits and data structures.

### Prototyping
Prioritize creating small prototypes for testing various aspects of the project like data retrieval and visualization.

### Iterative Development
Start with an MVP (Minimum Viable Product) and evolve from there.

### Iterate
Build upon the MVP based on new learnings and potential user feedback.

### Hosting & Backend
Given the tech stack of Python and Flask, Heroku could be a more fitting choice for hosting as it also supports SQLite.

### Resource Allocation
Ensure ample time is allocated for each segment of the project, and be prepared to make adjustments based on initial findings.

### Divide and Conquer
Break the project into smaller tasks and prioritize them.

### Identify Dependencies
Understand dependencies between tasks to avoid future roadblocks.

### Version Control
Use Git effectively to manage the project versions.

### Test
Allocate time for testing, especially integration tests between different components.

### Documentation
Keep comprehensive notes for long-term maintenance and scalability.
