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
                                        'DUP','OP_CARRIER_FL_NUM','OP_UNIQUE_CARRIER','CANCELLATION_CODE',"ARR_DELAY_NEW"])
all_airports = all_airports.drop(columns=["tbl",'Geocoded_City','tbl2pk'])

#Now we will convert the date time to regular pandas dates.
all_flights['FL_DATE'] = pd.to_datetime(all_flights['FL_DATE'])
print(all_flights.head())