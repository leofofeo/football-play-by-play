# Objectives

This project aims to:
- take existing play-by-play nfl data and create an ELT pipeline that automatically ingests existing and new csv files
- use an NFL API to create dimensional tables about teams and players
- transform the raw data into modeled data that can be consumed for analytics via a tool like Preset, more easily accessed for data analysis via SQL and Python


# Extraction + Load

The data for the project as it stands was pulled from a couple of different sources. The main source of historical data was [the nflverse play by play data](https://github.com/nflverse/nflverse-data/releases/tag/pbp) hosted in a variety of different formats (though I used the CSVs). I also wrote a simple web scraper to get NFL roster data for every team dating back to 1999 - this will serve as a foundational piece of dimensional data to tie players to the other statistics.

My initial data setup included a couple of Python scripts. One script downloaded the nflverse csv files for years 1999-2023 and transferred them to an S3 bucket, and the other scraped [Pro Football Archives](https://www.profootballarchives.com/1999nflchib.html) for the requisite roster data, saving the data as one csv file and uploading it to a separate S3 bucket. Then, I modified both scripts and packaged them up as lambda functions. These are hosted on AWS and are scheduled to run twice a month from March-June, checking for new data in their respective domains and writing new csv files to their respective S3 buckets if the data doesn't already exist.

These two S3 buckets serve as the stores for the raw data that is then loaded into Snowflake. I setup two Airbyte connections that sync with the S3 buckets and load any new CSVs into a raw stream table in Snowflake.

# Transform

Transformations were applied via dbt. Though the goal is to eventually create a robust set of dimension fact tables to better analyze the existing data, I started with simple tables around drives and game summaries in order to test the data and validate the volume necessary for analysis. Basic tests were applied via sql tests stored under `/tests`. These transformations exist in the `/marts` directory.

# Analysis

One big table was created in the `/analytics` folder, and used in conjunction with Preset to create a dashboard with some charts looking at hisorical data for NFL plays. Within Preset, I used additional queries built on to pof the analytics table to create more targeted data for analysis.