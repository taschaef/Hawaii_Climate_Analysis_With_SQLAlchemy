## SQLAlchemy Challenge - Weather in Hawaii

In this assignment we were asked to: use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

1. Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

2. Use the SQLAlchemy create_engine() function to connect to your SQLite database.

3. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

4. Link Python to the database by creating a SQLAlchemy session.

5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

# Section 1 - Precipitation Analysis
We were asked to query the last 12 months of data from the table and create a bar chart showcasing that data. 
![precip_bar](https://user-images.githubusercontent.com/124079708/235550355-77a61428-b9b2-4edb-9580-1c68addccb4e.png)

# Section 2 - Station Analysis
We were asked to find the most active station, then collect temperature data from that specific station for the last 12 months. Data is shown in a histogram. 
![temp_hist](https://user-images.githubusercontent.com/124079708/235550359-41fd8421-3b85-4b99-9cd6-db4c2e255b79.png)


# Section 3 - Climate App
We were asked to create a climate app that allowed users to interface with some of our quereies from the Jupyter Notebook in a Flask API. 
My app is called weather_app.py and can be found in the Surfs_Up folder in this repo. 

In that same folder you will find the Jupyter Notebook containing my code for the precipitation and temperature analysis. Additionally, there is a Resources folder in Surfs_Up that contains the sqlite database, and the CSV's used in this analysis. 
