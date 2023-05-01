# Import the dependencies.
import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///C:/Users/tsswi/OneDrive/Desktop/DU_Classwork/Module_10/Module_10_Starter_Code/Starter_Code/Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# Set up app
app = Flask(__name__)
end_year = '2016-08-23'

#################################################
# Flask Routes
#################################################

# Set up homepage
@app.route("/")
def home():
    return(
        f"Alohoa & welcome to Taylor's Hawaii Weather API<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

# /api/v1.0/precipitation
#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    precip_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > end_year).\
    group_by(Measurement.date).order_by(Measurement.date).all()

    # Jsonify the results
    precip_results = []
    for precip in precip_data:
        row = {}
        row["date"] = precip.date
        row["prcp"] = precip.prcp
        precip_results.append(row)
    return jsonify(precip_results)

# /api/v1.0/stations
#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    station_data = session.query(Station.station, Station.name).all()

    station_results = []
    for station in station_data:
        row = {}
        row["station"] = station.station
        row["name"] = station.name
        station_results.append(row)
    return jsonify(station_results)


# /api/v1.0/tobs
#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    most_active_data = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.station == "USC00519281").\
    filter(Measurement.date >= end_year).\
    order_by(Measurement.date).all()

    tobs_results = []
    for observation in most_active_data:
        row = {}
        row["station"] = observation[0]
        row["date"] = observation[1]
        row["tobs"] = observation[2]
        tobs_results.append(row)
    return jsonify(tobs_results)


# /api/v1.0/start
#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
@app.route("/api/v1.0/start")
def start_date(start):
    # Set up variables
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    last_year = dt.timedelta(days=365)
    start = start_date - last_year
    
    # Set up Query
    temp_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date <= end_year).\
    filter(Measurement.date >= start).all()
    temp_results = list(np.ravel(temp_data))
    return jsonify(temp_results)

# /api/v1.0/start/end
#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive. 
@app.route("/api/v1.0/start/end")
def start_end_date(start,end):
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    end = end_date-last_year
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    last_year = dt.timedelta(days=365)
    start = start_date - last_year


    total_temp_results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >=start).filter(Measurement.date <= end).all()
    total_temp = list(np.ravel(total_temp_results))
    return jsonify(total_temp)
    


if __name__ == "__main__":
    app.run(debug=True)