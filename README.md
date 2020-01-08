# Exploring dynamics of Bird e-scooters.

## Synopsis: 
Exploring the usage of scooters around Washington D.C. region by geo-clustering and visualizing movements through different time periods. This unsupervised learning problem is set with over 8M observations of scooters which were converted to trips data for capturing movement. We consider various models for clustering, and visulaize the movements and clusters through geoplots. 

## Project motivation:
I was looking for interesting ideas to do a project on as a part of my mentorship program at SharpestMinds with Renkoh Kato who is a Senior Machine learning engineer at J.P. Morgan Chase. After exploring different ideas, I decided upon doing a project on this fast trending mode of transportation, e-scooters. I set out with these questions in mind:
-	What is the spread of e-scooters throughout the D.C. region?
-	Scooters seem for recreational purposes and so should mostly be used on the weekends. Right?
- Is it possible to visualize their movements through time?
-	If so, can I use that to optimize placement of scooters? 

## About Bird scooters:

Wikipedia gives a good short introduction:

> Bird is a micromobility company based in Santa Monica, California. Founded in September 2017 Bird operated shared electric scooters in over 100 cities in Europe, the Middle East, and North America with 10 million rides in its first year of operation.

<img src="https://media.giphy.com/media/jTfkkLVpDC9Et91mkj/giphy.gif" width="285" > <img src="https://media.giphy.com/media/3o6ozzX4mAcwkkgzG8/giphy.gif" width="285" > <img src="https://media.giphy.com/media/88iJ0OpxFHbd09sFOU/giphy.gif" width="285" > 


## Getting started:
### Installation
The code was written in Python 3 and uses the following packages: pandas, numpy, matplotlib, datetime, uuid, descartes, geopandas, shapely, sklearn, folium, hdbscan.

### Data collection & preparation:
- In order to capture movements, I needed to collect scooter data at frequent intervals. Developed a script that pinged the API every 5 mins for multiple coordinate points for 45 days straight resulting in about ~8M observations.  
API: https://github.com/ubahnverleih/WoBike/blob/master/Bird.md
- Data was initially collected as CSVs, but managing numerous CSVs became really cumbersome. So I improved upon the above script to start exporting the collected data to a PostgreSQL database using the sqlalchemy package.
- The data collected required extensive cleaning and preparation that I wouldnt go into too much detail here, but you can find an in-depth explanation of my whole project here (link to my blogpost)

### Analysis:
After collection and preparation of data, I performed some exploratory data analysis to answer my initial basic questions. As you might guess, there were quite a good number of scooters in the D.C. region, so in order to understand their concentrations and movements, I clustered them based on their coordinate points using K-Means and HDBSCAN and then visualized it on a geomap using folium in Python.

In depth description of my analysis can be found on my blogpost. (link to my blog post)

### Interesting conclusion:
While I go over all my conclusions in my blog, I want to point out to one that really suprised me. 
##### " Scooters seem for recreational purposes and so should mostly be used on the weekends. Right?" #####
<img src="https://github.com/himanshu20792/BirdProject/blob/master/StationaryScooters/Images/Weekend_weekday_1.png" width="600" >

<img src="https://github.com/himanshu20792/BirdProject/blob/master/StationaryScooters/Images/Weekend_weekday_2.png" width="600" >




**Visualization of select scooters movements:**

<img src="https://github.com/himanshu20792/BirdProject/blob/master/StationaryScooters/Images/Individual_Scooter_Movement.png" width="600" >

<p>&nbsp;</p>

**Heatmap of scooters and Cluster centers:**

<img src="https://github.com/himanshu20792/BirdProject/blob/master/StationaryScooters/Images/Stationary_Scooters_Cluster.png" width="600" >
