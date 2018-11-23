# Import dependecies 

from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
import datetime as dt
from datetime import date

# SQL setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# Description of file rountines
"""
* Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

"""

# Flask setup
app = Flask(__name__)

# Flask routes
@app.route("/")
def welcome():
    return(
        f"Thank you for visiting Precipitation API! <br>"
          "Get precipitation, temperature, elevation and a host of other data!<br>"
          "Planning a trip? Use this API for smart trip planning<br>"
          "Surfs Up, Brudha! <br>"
          "<br> Here are the available API Routess:<br>"
          "/api/v1.0/stations <br>"
          "/api/v1.0/tobs<br>"
          "/api/v1.0/<start>/<end>"
          
    )

@app.route("/api/v1.0/stations")
def stations ():
    """ Returns json list of all stations"""
    stations = session.query(Station.station)\
        .all()

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temperatures ():
    """  * query for the dates and temperature observations from a year from the last data point.
         * Return a JSON list of Temperature Observations (tobs) for the previous year. """

    # Find lastest temp in dataset:
    lastest_dt = session.query(Measurement.date).order_by(
    Measurement.date.desc()).first()[0]

    # Find previous year date
    prev_year = (dt.datetime.strptime(lastest_dt, '%Y-%m-%d')
             .date() - dt.timedelta(365)
             ).strftime('%Y-%m-%d')
   
    

    # Use most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(
    Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]

    # Query for date and temperature observations
    tobs = session.query(Measurement.date, Measurement.tobs) .\
    filter(Measurement.date.between(prev_year, lastest_dt)).\
    filter(Measurement.station == most_active_station).all()

    # Convert tobs to a dict
    tobs_dict = {}

    for temp in tobs:
        tobs_dict[temp[0]] = temp[1]
    
    # Return date, temperatures in .json
    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>/<end>")
def temperatures_by_date(start_date, end_date):
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
         filter(Measurement.date >= start_date).filter(
         Measurement.date <= end_date).all()


if __name__ == "__main__":
    app.run(debug=True)