# Surfs Up!

![surfs-up-mikey.jpeg](Images/surfs-up-mikey.jpeg)

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! The scripts in this file will help with your trip planning by providing some climate analysis on the area. This script provides the following:

## Climate Analysis and Exploration

Using Python and SQLAlchemy, basic climate analysis and data exploration of the climate database is provided. 


* A spring date is used in script, but feel free to update it with your own! Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.



### Precipitation Analysis

* The script provides a query to retrieve the last 12 months of precipitation data.

* A plot the preciption results is provided using the DataFrame.

  ![precipitation](Images/precipitation.png)



### Station Analysis

* The script provides a query to calculate the total number of temperature stations.

* The script provides a query to retrieve the last 12 months of temperature observation data (tobs).

  * The results are filtered by the station with the highest number of observations.

  * A histogram plot of the results is provided.

    ![station-histogram](Images/station-histogram.png)

### Temperature Analysis (Optional)

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.

* The `calc_temps` function is provided and will return the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* A bar plot is provided with the min, avg, and max temperature from your previous query as a bar chart.

    ![temperature](Images/temperature.png)

- - -

## Step 2 - Climate App

Secondly a Flask API is provided based on the queries provided above.

### Routes

* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

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