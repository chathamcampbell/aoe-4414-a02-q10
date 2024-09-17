#llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg long_deg hae_km
#  Text explaining script usage
# Parameters:
#  lat_deg: Latitude in deg
#  lon_deg: Longitude in deg
#  hae_km : height above the elipsoid in km 
#  ...
# Output:
#  rx,ry,rz in km
#
# Written by Chatham Campbell


# import Python modules
import math
# e.g., import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456


# initialize script arguments
lat_deg = float('nan') # lat in deg
lon_deg = float('nan') # lon in deg
hae_km = float('nan') # height above ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print(\
     'Usage: '\
     'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
    )
    exit()

# write script below this line
lat_rad = lat_deg * math.pi/180.0
lon_rad = lon_deg * math.pi/180.0

denom = math.sqrt(1.0-(E_E**2)*(math.sin(lat_rad)**2))
C_E = R_E_KM/denom
S_E = (R_E_KM* (1-E_E**2.0))/denom
r_x_km = (C_E + hae_km)* math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (C_E + hae_km)* math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (S_E + hae_km) * math.sin(lat_rad)

print(r_x_km)
print(r_y_km)
print(r_z_km)