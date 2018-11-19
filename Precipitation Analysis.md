____________________________________________________

Precipitation Analysis
____________________________________________________

1) Design a query to retrieve the last 12 months of precipitation data.

------------------------------------------------------
Need help querying for latest date and returning 12 months from latest date:
----------------------------------------------------------

	* Step 1a Find latest date in dataset:
	 lastest_dt = 
		max (session.query(Measurement.date) )


	* Find latest_dt minus 12 months:  
	lastest_12 = 
		latest_dt - 12 months


-------------------------------------------------------------------
2) Select only the date and prcp values.

-----------------------------------------------------------------

dt_prcp = 

	session.query(Measurement.date, Measurement.prcp) .\
    filter(Measurement.date >= lastest_12). \
    filter(Measurement.date <= lastest_dt).all()


-----------------------------------------------------------------

3) Load the query results into a Pandas DataFrame and set the index to the date column.

dt_prcp_df =

	 pd.DataFrame(results, columns=['Date', 'Precipitation'], 
	 	index='Date')

------------------------------------------------------------------
Drop nan values
-----------------------------------------------------------------

dt_prcp_df  = dt_prcp_df .dropna()

-----------------------------------------------------------------

Sort the DataFrame values by date.

------------------------------------------------------------------

dt_prcp_df  = dt_prcp_df.sort_values(by=['Date'])



-----------------------------------------------------------------

4) Plot the results using the DataFrame plot method.

----------------------------------------------------------------------

dt_prcp_df.plot.bar()
dt_prcp_df.tight_layout()
dt_prcp_df.show()