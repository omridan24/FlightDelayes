import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Holding all the CSV's as pandas data frame
all_flights = pd.read_csv("Data/T_ONTIME_MARKETING.csv")
all_airports = pd.read_csv("Data/Consumer_Airfare_Report__Table_2_-_Top_1_000_City-Pair_Markets_20240710.csv")
all_airlines = pd.read_csv("Data/Bansard-airlines-codes-IATA-ICAO.csv")


print(all_flights.head())