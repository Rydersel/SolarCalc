<h1 align="center">
  <br>
  <a href="https://github.com/Rydersel"><img src="https://cdn.discordapp.com/attachments/722227948157141023/929897255283073034/Solar-Plant-PNG.png"></a>
  <br>
  SolarCalc
  <br>
</h1>



**The Problem:**

Current solar power residential price calculators are crude and rely a-lot on rough estimation. They also fail to take into account deviation in the Sun's energy output due to variables such as cloud cover, location and local weather patterns. I plan to code a more comprehensive solar price calculator that takes these factors into account in order to better educate possible solar power consumers on the pros and cons of a given system. 

**Creating an Initial Prototype:**

Before we can create a better calculation system, we must first create a mockup of an existing system. Since no open source examples seem to be available I started by quickly writing one up in C++.I later converted this to python to better handle large data set management further down the line.

**Calculating the Sun's irradiation output:** 

The first characteristic that is going to make our calculator unique is its ability to take into account the suns irradiance. To do this there are a couple characteristics we must take into account. 
-Global Radiation (GR) (This is what we want to calculate and is the total amount of radiation from the sun reaching a given area)
-Direct Radiation (DIR) (Non-Difused Radation)
-Difuse Radiation (DR) (Solar Radiation Difused as it enters the atmosphere)

These values relate to each other through the formula: `GR = DIR + DR`. 

**Calculating Direct Radiation:**

The direct insolation from the sun map sector (Dirθ,α) with a centroid at zenith angle (θ) and azimuth angle (α) is calculated using the following equation:

` Dirθ,α = SConst * βm(θ) * SunDurθ,α * SunGapθ,α * cos(AngInθ,α)`

Variables Used:

SConst — The solar flux outside the atmosphere at the mean earth-sun distance, known as solar constant. The solar constant used in the analysis is 1367 W/m2. This is consistent with the World Radiation Center (WRC) solar constant.

`β` — The transmissivity of the atmosphere (averaged over all wavelengths) for the shortest path (in the direction of the zenith).

`m(θ)` — The relative optical path length, measured as a proportion relative to the zenith path length (see equation 3 below).

`SunDurθ,α` — The time duration represented by the sky sector. For most sectors, it is equal to the day interval (for example, a month) 
multiplied by the hour interval (for example, a half hour). For partial sectors (near the horizon), the duration is calculated using spherical geometry.

`SunGapθ,α` — The gap fraction for the sun map sector.

`AngInθ,α` — The angle of incidence between the centroid of the sky sector and the axis normal to the surface (see equation 4 below).


**Calculating Difused Radiation:*

For each sky sector, the diffuse radiation at its centroid (Dif) is calculated, integrated over the time interval, and corrected by the gap fraction and angle of incidence using the following equation:


` Difθ,α = Rglb * Pdif * Dur * SkyGapθ,α * Weightθ,α * cos(AngInθ,α)`

Variables:

`Rglb` — The global normal radiation (` Rglb = (SConst Σ(βm(θ))) / (1 - Pdif)`).

`Pdif` — The proportion of global normal radiation flux that is diffused. Typically it is approximately 0.2 for very clear sky conditions and 0.7 for very cloudy sky conditions.

`Dur` — The time interval for analysis.

`SkyGapθ,α` — The gap fraction (proportion of visible sky) for the sky sector.

`Weightθ,α` — The proportion of diffuse radiation originating in a given sky sector relative to all sectors (see equations 7 and 8 below).

`AngInθ,α` — The angle of incidence between the centroid of the sky sector and the intercepting surface.


It is then as simple as adding both equations together to create a final formula for global radiation we can then implement in our code.

`(Dirθ,α = SConst * βm(θ) * SunDurθ,α * SunGapθ,α * cos(AngInθ,α)) + (Dirθ,α = SConst * βm(θ) * SunDurθ,α * SunGapθ,α * cos(AngInθ,α)) = GR`

Luckily our code can be drastically simplified with the help of the [PySolar](https://pysolar.readthedocs.io/en/latest/#) Python Lib. Using this we can turn hundreds of lines of code into the following:



**Calculate Sun's Altitude:**

`
latitude = YOUR_LATITUDE_GOES_HERE
longitude = YOUR_LONGITUDE_GOES_HERE
date = datetime.datetime.now(datetime.timezone.utc)
print(get_altitude(latitude, longitude, date))
`

**Calculate Sun's Azimuth:**
`
latitude = 42.206
longitude = -71.382
`
`
date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)
print(get_azimuth(latitude, longitude, date))
`

**Calculate Suns Irradiation (using results of code above:)**
`
latitude_deg = 42.206
longitude_deg = -71.382
date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)
altitude_deg = get_altitude(latitude_deg, longitude_deg, date)
print (radiation.get_radiation_direct(date, altitude_deg))
`









**What we can do with this info:**

using this information we can now calculate exact solar array size required for a given person's energy needs at a given time of the year and location. We can also now estimate the amount of energy produced by said array at different points throughout the year. Combining these characteristics we can now calculate the total solar array size required for a given person to satisfy their energy need for a given section of time. For example we can not only calculate how large of a solar array a specific consumer needs for their individual energy needs, we can also verify that said rig will be sufficient for every day of the year for the next 50 years. 

An Implementation of this can be seen in this project.
