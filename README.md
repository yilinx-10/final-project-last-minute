# final-project-Last-Minute

This repository houses the code, presentation materials, and final project report for Team Last Minute’s MACS 30122 Group Project, which explores the involvement of social bots in online discussions surrounding the 2025 Los Angeles Wildfire.

Below is an overview of the README's contents:
| Section          | Description                                   |
|------------------|-----------------------------------------------|
| [Team Members](#team-members-and-division-of-labor) | Details about the contributors and their respective roles |
| [Project Description](#project-description) | 	Overview of research questions, motivation, data visualization, analysis strategies, and key findings |
| [Github Repo Navigation](#github-repo-navigation) | Guide to navigating this repository |
| [Process](#process) | Instructions on running the code to replicate the results |
| [Usage of AI](#usage-of-ai-assistance) | 	Explanation of how AI tools were utilized in this project |
| [In-Class Presentation Slides, Updated Presentation Slide, and Video Presentation](#in-class-presentation-slides-updated-presentation-slide-and-video-presentation) | Links to in-class presentation slides, updated slides, and video presentation |

## Team Members and Division of Labor
| Contributors(Alphabetical Order)  | Description                                   |
|------------------|-----------------------------------------------|
| Hugo He  | Bluesky Scraper, Manual Topic Assignment, Slides(Data Scraping), Video| 
| Moe Wu  | Bot/Human Labelling, Data Visualization(Plotting Post-Specific Graphs, Aesthetics), Data Analysis, Slides(Data Visualization & Anlysis)| 
| Yilin Xu  | Reddit Scraper, Bluesky BERTopic, Data Cleaning & Wrangling, Data Visualization(Prepate Nodes & Edge Lists, Batch Produce Visualizations, Cross-Post Network Visualization, Layouts, Aesthetics), Slides(Data Cleaning & Wrangling, Aesthetics), README| 

## Project Description

### Research Questions
- Q1: How important are bots in wildfire discussions?
- Q2.1: What sub-topics do social bots prefer in wildfire discussion?
- Q2.2: How do social bots and humans differ in sub-topic preference?
- Q3: How does the popularity of bots differ across platforms?

### Social Science Relevance  
Active participation of online social bots in political debates and discussions has been extensively researched and confirmed by previous studies. For instance, Hagen et al. (2020) examined the activity patterns of social bots in discussions surrounding the 2020 U.S. presidential election on Twitter through network analysis. However, despite the high politicization and widespread generation and dissemination of online misinformation about environmental issues, few studies have explored the influence of bots. Building on this body of work, we aim to explore the prevalence of social bots in public discussions about topics beyond U.S. politics. We hypothesize that the prevalence of bots in discussions about elections is largely due to the involvement of various stakeholders. Similarly, while the L.A. wildfires are not explicitly political, they naturally evoke discussions about state policies and governmental responses, making them a relevant event to study social bot behavior. 

### Data Source
- Bluesky
  - Time Frame: January 7, 2025 to January 31, 2025
  - Data Size: 4896 threads with their comments

- Reddit
  - Time Frame: January 5, 2025 onward
  - Data Size: 164 Posts and 44,107 Comments

### Bot Identification
We used [BotBuster-Universe](https://github.com/quarbby/BotBuster-Universe) to compute the bot probability of each Reddit comment we collected. Refer to BotBuster-Universe's Github Repository(linked) for more information. 

### Main Objectives
- Understanding Social Bots in LA Wildfire Discussions: Investigate how social bots engage in public discourse about the Los Angeles Wildfire in 2025, analyzing their role in shaping conversations.
- Sub-Topic Preference Analysis: Identify the specific wildfire-related topics that social bots focus on and compare them to the topics preferred by human users.
- Network Analysis: Utilize network analysis to determine the importance of social bots in online wildfire discussions by measuring engagement metrics like degree centrality and discussion tree structures.

### Method & Key Packages We Used(Non-exhaustive)
- Network Analysis with [NetworkX](https://networkx.org/documentation/stable/reference/index.html)
- Topic Modeling with [BERTopic](https://maartengr.github.io/BERTopic/api/bertopic.html)
- Reddit Scraping with [PRAW](https://praw.readthedocs.io/en/stable/index.html)
- Pandas
- Numpy
- json
- csv
- matplotlib
- seaborn

### Key Findings
- Humans are more likely to be Major Information Brokers
  - The overall standalized betweenness centrality distribution shows most users (both bots and humans) clustering between -0.5-0.5.
  - However, some users stand out with exceptionally high betweenness, indicating their role as a key influence in information exchange. These users are typically human.
- Bots do exhibit high engagement in certain kinds of posts
 - Among the 10 hottest posts, 5 have bots in the top five for betweenness centrality
 - Three out of the ten hottest posts are mostly related to Topic0, which focuses on President Trump and California’s electricity and water supply policies.
 - All of these three posts have bots ranking in the top five for betweenness centrality, implying that bot accounts may be particularly active in highly politicized discussions.
- Cross-Post Influence
 - Our visualization and analysis suggests the social bots follow an infiltration pattern of engagement.

## Github Repo Navigation
    .
    ├── bluesky/
      ├── bluesky_posts_0131.json
      ├── bluesky_posts_0309.json
      ├── bluesky BERTopic.ipynb # BERTopic topic modeling for Bluesky Data
      ├── bluesky_scrape_CleanCode.ipynb
    ├── reddit/    
      ├── networkdata/ #folder for 'reply_to' json file for network construction
      ├── networkviz/ #folder of network visualization results
      reddit_scraper.py # Reddit scraper
      reddit_post_data.json
      reddit_posts_cleaned.json # cleaned reddit post data
      reddit_topic.xlsx # reddit post manual topic assignment
      reddit_comment_data.json
      reddit_comments_cleaned.json # cleaned reddit comment data
      reddit_cleaning_wrangling.ipynb # Jupyter Notebook for Data Cleaning & Wrangling
      reddit_comments_bot_prob.csv # Output from BotBuster Model
      reddit_averaged_bot_prob.csv # Processed Bot Probability Results
      reddit_visualization.ipynb # Jupyter Notebook for Visualization and Analysis
    ├── slides/    
      ├── Last_Minute # In-Class Presentation Slide
      ├── Last_Minute_Updated # Updated Presentation Slide
    ├── Progress_Report_1.pdf     
    ├── Progress_Report_2.pdf                 
    └── README.md


## Process

This section outlines the (recommended) sequential order by which the users can reproduce the results with the code:  
1. Scraping Data from [Bluesky](bluesky/bluesky_scrape_CleanCode.ipynb) and [Reddit](reddit/reddit_scraper.py) (TIME CONSUMING! NOT RECOMMENDED TO RUN)  
2. Topic Modeling: run [bluesky BERTopic.ipynb](https://github.com/macs30122-winter25/final-project-last-minute/blob/a533acd35440098d1f25ecec618b7ea936941858/bluesky/bluesky%20BERTopic.ipynb)  
3. Data Cleaning and Wrangling: download reddit data for [post](reddit/reddit_post_data.json), [comment](reddit/reddit_comment_data.json), [cleaning and wrangling notebook](reddit/reddit_cleaning_wrangling.ipynb). Put in one folder. Create empty folder `networkdata` inside main folder. Run Jupyter Notebook.  
4. Data Visualization: download [visualization notebook](reddit/reddit_visualization_final.ipynb) in the same main folder. Create empty folder `networkviz` inside main folder. Run Jupyter Notebook. Note 'Descriptive Metrics' section of this notebook takes a long time to run(compute betweenness centrality.)  


## Usage of AI Assistance

| Aspect                      | Description                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------|
| Bluesky Scraper  | Design Parse Date Function                                      |
| Network Visualization  | Improve Visualization Parameters                                      |


## In-Class Presentation Slides, Updated Presentation Slide, and Video Presentation
Below are the materials related to our team's presentation as well as the final report:

|  materials               | Link                                                                                           |
|------------------------------|------------------------------------------------------------------------------------------------|
| In-Class Presentation Slide  | [View Slide](https://drive.google.com/file/d/1l__2GNCp4-6oQd9xErsNj648UF1IXLJM/view?usp=drive_link) |
| Updated Presentation Slide   | [View Slide](https://docs.google.com/presentation/d/1ZBmHigzorOr59d_jzhNyYkBCHIX91uLrL6bLp3pvZ5k/edit?usp=sharing)  |
| Video Presentation           | [Watch Video]()                                                                               |
