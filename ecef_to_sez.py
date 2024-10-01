# ecef_to_sez.py
#
# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
# Converts ECEF coordinates to SEZ coordinates 
#
# Parameters:
# o_x_km: ECEF x-coordinate of the SEZ frame 
# o_y_km: ECEF y-coordinate of the SEZ frame 
# o_z_km: ECEF z-coordinate of the SEZ frame 
# x_km: ECEF x-coordinate in km 
# y_km: ECEF y-coordinate in km
# z_km: ECEF z-coordinate in km
#
# Output:
# s_km: South coordinate in SEZ in km
# e_km: East coordinate in SEZ in km
# z_km: Zenith coordinate in the SEZ in km
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # argv
import math  # math module 

# Helper functions

## Convert ECEF to SEZ coordinates
def ecef_to_sez(o_x, o_y, o_z, x, y, z):
    # Calculate the difference between the origin and the point in ECEF
    dx = x - o_x
    dy = y - o_y
    dz = z - o_z

    # Calculate observer's lat and long
    r_o = math.sqrt(o_x**2 + o_y**2)
    lat_o = math.atan2(o_z, r_o)
    lon_o = math.atan2(o_y, o_x)

    # Calculate transformation matrix 
    sin_lat = math.sin(lat_o)
    cos_lat = math.cos(lat_o)
    sin_lon = math.sin(lon_o)
    cos_lon = math.cos(lon_o)

    # Transformation from ECEF to SEZ 
    s_km = -cos_lat * cos_lon * dx - cos_lat * sin_lon * dy + sin_lat * dz  # South
    e_km = -sin_lon * dx + cos_lon * dy  # East
    z_km = sin_lat * cos_lon * dx + sin_lat * sin_lon * dy + cos_lat * dz  # Zenith (fixed to point upwards)

    return s_km, e_km, z_km

# Initialize script arguments
o_x_km = 0  # ECEF x-coordinate of SEZ fram origin
o_y_km = 0  # ECEF y-coordinate of SEZ origin
o_z_km = 0  # ECEF z-coordinate of SEZ origin
x_km = 0    # ECEF x-coordinate
y_km = 0    # ECEF y-coordinate 
z_km = 0    # ECEF z-coordinate o

# Parse script arguments
if len(sys.argv) == 7:
    o_x_km = float(sys.argv[1])
    o_y_km = float(sys.argv[2])
    o_z_km = float(sys.argv[3])
    x_km = float(sys.argv[4])
    y_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print('Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km')
    exit()

# Convert ECEF to SEZ
s_km, e_km, z_km = ecef_to_sez(o_x_km, o_y_km, o_z_km, x_km, y_km, z_km)

# Print the SEZ coordinates
print(s_km)
print(e_km)
print(z_km)

