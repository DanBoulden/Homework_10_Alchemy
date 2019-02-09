import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Avalable routes:<br/>"
        f"Avalable pathes = /api/v1.0<br/>"
        f"                  /api/v1.0/Measurement<br/>"
        f"                  /api/v1.0/Station<br/>"
        f"                  /api/v1.0/precipitation<br/>"        
        f"                  /api/v1.0/stations<br/>"
        f"                  /api/v1.0/tob<br/>"
    )


@app.route("/")
def home():
    return (
        f"Hi, this is the Hawaii climate site<br/>"
        f"Avalable routes:<br/>"
        f"Avalable pathes = /api/v1.0<br/>"
        f"                  /api/v1.0/Measurement<br/>"
        f"                  /api/v1.0/Station<br/>"
        f"                  /api/v1.0/precipitation<br/>"        
        f"                  /api/v1.0/stations<br/>"
        f"                  /api/v1.0/tob<br/>"
     )


@app.route("/v1.0")
def ver():
    return (
        f"This is the Hawaii climate site, version 1.0<br/>"
        f"Avalable routes:<br/>"
        f"Avalable pathes for v1.0<br/>"
        f"                        /api/v1.0/Measurement<br/>"
        f"                        /api/v1.0/Station<br/>"
        f"                        /api/v1.0/precipitation<br/>"
        f"                        /api/v1.0/stations<br/>"
        f"                        /api/v1.0/tobs<br/>"
    )

@app.route("/v1.0/Measurement")
def Measurement():
    return jsonify(Measurement)

@app.route("/v1.0/Station")
def Station():
    return jsonify(Station)

@app.route("/v1.0/precipitation")
def precipitation():
    return(
    f"This is the Hawaii climate site, version 1.0: precipitation<br/>"
    f"This is still under construction<br/>"
    )

@app.route("/v1.0/stations")
def station():
    """Return a list of stations"""
    # Query all stations
    results = session.query(Station).all()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station in results:
        station_dict = {}
        station_dict["station"] = hawaii_stations.station
        station_dict["name"] = station.name
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/v1.0/tobs")
def tobs():
    return(
    f"This is the Hawaii climate site, version 1.0: tobs<br/>"
    f"This is still under construction<br/>"
    )




if __name__ == '__main__':
    app.run(debug=True)
