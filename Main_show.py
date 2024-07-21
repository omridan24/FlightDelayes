import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Holding all the CSV's as pandas data frame
all_flights = pd.read_csv("Data/T_ONTIME_MARKETING.csv")
all_airports = pd.read_csv("Data/Consumer_Airfare_Report__Table_2_-_Top_1_000_City-Pair_Markets_20240710.csv")
all_airlines = pd.read_csv("Data/Bansard-airlines-codes-IATA-ICAO.csv")

#clening all the columns that are not relevent to us
all_flights = all_flights.drop(columns=['DIV5_TAIL_NUM', 'DIV5_WHEELS_OFF', 'DIV5_WHEELS_ON', 'DIV5_AIRPORT',
                                        'DIV4_TAIL_NUM', 'DIV4_WHEELS_OFF', 'DIV4_TOTAL_GTIME', 'DIV4_WHEELS_ON', 'DIV4_AIRPORT',
                                        'DIV3_TAIL_NUM', 'DIV3_WHEELS_OFF', 'DIV3_TOTAL_GTIME', 'DIV3_WHEELS_ON', 'DIV3_AIRPORT',
                                        'DIV2_TAIL_NUM', 'DIV2_WHEELS_OFF', 'DIV2_TOTAL_GTIME', 'DIV2_WHEELS_ON', 'DIV2_AIRPORT',
                                        'DIV1_TAIL_NUM', 'DIV1_WHEELS_OFF', 'DIV1_TOTAL_GTIME', 'DIV1_WHEELS_ON', 'DIV1_AIRPORT',
                                        'DIV_ACTUAL_ELAPSED_TIME','DIV_AIRPORT_LANDINGS','TOTAL_ADD_GTIME','FIRST_DEP_TIME',
                                        'LATE_AIRCRAFT_DELAY','SECURITY_DELAY',"NAS_DELAY",'WEATHER_DELAY','CARRIER_DELAY',
                                        'DUP','OP_CARRIER_FL_NUM','OP_UNIQUE_CARRIER','CANCELLATION_CODE',"ARR_DELAY_NEW","TAIL_NUM","ORIGIN_STATE_ABR",
                                        "ARR_TIME","TAXI_IN","WHEELS_ON","WHEELS_OFF","TAXI_OUT","CRS_DEP_TIME","DEP_TIME","DIVERTED","CANCELLED"])
all_airports = all_airports.drop(columns=["tbl",'Geocoded_City','tbl2pk'])


#Now we will convert the date time to regular pandas dates.
all_flights['FL_DATE'] = pd.to_datetime(all_flights['FL_DATE'])
#Here we will switch the mkt_unique_carrier in the name of the company, using the second table
IATA_dict_for_names = all_airlines.set_index('IATA Designator')['Airline Name'].to_dict()
all_flights['Airline']=all_flights['MKT_UNIQUE_CARRIER'].map(IATA_dict_for_names)
#now we can drop the MKT_UNIQUE_CARRIER column
all_flights = all_flights.drop(columns="MKT_UNIQUE_CARRIER")
#The first graph will be the relation between the distance of the flight, to the arrival delay
plt.figure(figsize=(10, 6))
plt.scatter(all_flights['DISTANCE'], all_flights['ARR_DELAY'])  # Assuming your data is in a DataFrame called 'df'
plt.xlabel('Distance')
plt.ylabel('Arrival Delay')
plt.title('Arrival Delay vs. Distance')
plt.grid(alpha=0.4)
plt.savefig("Output/Dist-Delay")
plt.show()
#Now we will see the graph of the connection between the airline and the delay
airline_groups = all_flights.groupby('Airline')
#grouping the mean delayes of each airline
mean_delays = airline_groups['ARR_DELAY'].mean() 
#getting it sorted to pull the top deleys
mean_delays_sorted = mean_delays.sort_values(ascending=False)
#holding the top delayers
top_delayers_airlines = mean_delays_sorted.head(10)
plt.figure(figsize=(10, 6))
top_delayers_airlines.plot(kind='bar')
plt.xlabel('Airline')
plt.ylabel('Mean Arrival Delay')
plt.title('Mean Arrival Delay by Airline')
plt.xticks(rotation=45)
plt.show()

