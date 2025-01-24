# final-project-last-minute
# Topic idea:
How do social bots engage in public discussions about topics in the Los Angeles wildfire?
# Sources of data: 
## Reddit: 
Collection Method: Selenium
Justification: Reddit is one of the largest platforms where people engage in idea exchanges about a wide variety of topics. It is easy to keep track of discussions by focusing on several selected Reddit communities directly related to the event of interest. Reddit data can be scraped using Selenium, which was introduced in class.
## Bluesky:
Collection Method: Bluesky API(https://docs.bsky.app/)
Justification: The Bluesky API is free and publicly available without the need for applications and approval. The platform itself is emerging.
## YouTube:
Collection Method: YouTube API(https://developers.google.com/youtube/v3/getting-started)
Justification: YouTube’s API allows users to access the comment threads of videos in JSON structure. 
Note: We are actively considering other potential sources of data including X/Twitter(through web-scraping packages), Quora(web-scraping), Meta/Facebook(API), Instagram(API), etc.
# Responsibilities of each team member(alphabetical order):
Hugo He: Presentation slides, video, Bluesky data scraping, data processing
Moe Wu: Youtube data scraping, data processing, analysis, and visualization
Yilin Xu: Reddit data scraping, data processing, analysis, and visualization
# Repository:
Link: https://github.com/macs30122-winter25/final-project-last-minute
# Goals and approach:
Active participation of online social bots in political debates and discussions has been extensively researched and confirmed by previous studies. For instance, Hagen et al. (2020) examined the activity patterns of social bots in discussions surrounding the 2020 U.S. presidential election on Twitter through network analysis. However, despite the high politicization and widespread generation and dissemination of online misinformation about environmental issues, few studies have explored the influence of bots. Building on this body of work, we aim to explore the prevalence of social bots in public discussions about topics beyond U.S. politics.
To achieve this, we plan to gather textual data using Selenium for Reddit and the respective APIs for Bluesky and YouTube. Bot accounts will be identified using BotBuster, Botometer, and other reliable bot detection methods that have demonstrated high accuracy in prior research. Our focus will be on discussions about the recent Los Angeles wildfire. We hypothesize that the prevalence of bots in discussions about elections is largely due to the involvement of various stakeholders. Similarly, while the L.A. wildfires are not explicitly political, they naturally evoke discussions about state policies and governmental responses, making them a relevant event to study social bot behavior. (200 words! Yeah!)
# Expected Findings:
Based on past literature, we propose the following expected findings. On the pro-Democrats platform(Bluesky), we expect to observe a lower rate of use of bots. On more polarized platforms(Reddit), we expect to observe a greater rate of use of bots, a greater degree of polarization in attitudes of bots, and a higher level of disagreement in conversations for bots. On YouTube, we expect to observe lower levels of disagreement in conversations where bots are involved.
# Resources:
BotBuster: https://github.com/quarbby/BotBuster-Universe
Botometer X: https://botometer.osome.iu.edu/






