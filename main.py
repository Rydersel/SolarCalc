import requests
import time

from pysolar.solar import *
import datetime
State = 0
UserState = 0
User_KW_Use = 11


latitude = 42.206
longitude = -71.382
#Calculate Azimuth
date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)
print(get_azimuth(latitude, longitude, date))



#Calculate Sun's irradiation (not taking into account cloud cover)
latitude_deg = 42.206
longitude_deg = -71.382
date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)
altitude_deg = get_altitude(latitude_deg, longitude_deg, date)
print (radiation.get_radiation_direct(date, altitude_deg))


"""
1 = Arizona
2 = California
3 = Florida
4 = Massachusetts
5 = Maryland
6 = Minnesota
7 = New Hampshire
8 = New Mexico
9 = Oregon
10 = Texas
11 = Illinois

"""





#Calc PPW depending on State
def PPW(State):
    switcher={
      1: 3.61,
      2: 4.31,
      3: 3.45,
      4: 4.18,
      5: 3.93,
      6: 4.61,
      7: 3.72,
      8: 4.82,
      9: 3.79,
      10: 3.83,
      11: 0
    }
    return switcher.get(State)
def Energy_Production_Score(Score):
    switcher={
      1: 2100,
      2: 1900,
      3: 1700,
      4: 1600,
      5: 1600,
      6: 1700,
      7: 1600,
      8: 2000,
      9: 1500,
      10: 1600,
      11: 1550
    }
    return switcher.get(Score)

UserState = 1
PPWVAL = PPW(UserState)
int(PPWVAL * 1000) == PPWVAL

PPWVAL = (PPWVAL * 1000)  #convert to from Watts To KillaWatts
Total_Price = (PPWVAL * User_KW_Use)


KWH_Produced = (Energy_Production_Score(UserState) * User_KW_Use * 0.78) #18% energy loss which is the universally agreed ammount

"""
    Formula:
   (PPWVAL * 1000) = (Energy_Production_Score * User_KW_Use * 0.78)
   Total_Price = PPWVAL * User_KW_Use 
   
"""
