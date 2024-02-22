# Import the necessary modules
from astropy import units as u
from astropy.coordinates import SkyCoord, get_constellation

# Define the coordinates of Betelgeuse and Rigel
betelgeuse = SkyCoord(ra=88.7929*u.deg, dec=7.4071*u.deg)
rigel = SkyCoord(ra=78.6345*u.deg, dec=-8.2016*u.deg)

# Define the reference frame and origin
frame = 'icrs'
origin = betelgeuse

# Define a list of stars in Orion
stars = ['Betelgeuse', 'Rigel', 'Bellatrix', 'Mintaka', 'Alnilam', 'Alnitak', 'Saiph']

# Loop over the stars and print their coordinates
for star in stars:
    # Get the coordinate object of the star
    coord = SkyCoord.from_name(star)

    # Get the constellation of the star
    constellation = get_constellation(coord)

    # Calculate the relative coordinates to the origin
    dx = (coord.ra - origin.ra).to(u.deg).value
    dy = (coord.dec - origin.dec).to(u.deg).value

    # Print the star name, constellation, and coordinates
    print(f"{star} is in {constellation} and has coordinates ({dx:.2f}, {dy:.2f})")
