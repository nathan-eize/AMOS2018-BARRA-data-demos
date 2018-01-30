#!/usr/bin/env python
"""
 Creates an animation of the pressure-level wind data from BARRA-TA and BARRA-R sample data.
 Wind vectors over 37 pressure levels.

 Codes written for illustrating BARRA pressure-level data.

 Chun-Hsu Su, 19 January 2018
 The Bureau of Meteorology
"""
import os, sys
import numpy as np
from netCDF4 import Dataset, num2date, date2num
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cartopy.crs as ccrs
from matplotlib import cm
from mpl_toolkits.basemap import Basemap

#--------------------------
# Methods
#--------------------------
def get_uv(j):
	"""
	Returns the lon,lat,pres,u,v values for a given pressure level
	identified by index j.
	"""
	_,a,b = modwind['uwind'].shape
	c = max(a,b)
	ivl = int(c/20)
	x = modwind['lon'][::ivl]
	y = modwind['lat'][::ivl]
	u = modwind['uwind'][j,::ivl,::ivl]
	v = modwind['vwind'][j,::ivl,::ivl]
	p = modwind['prs'][j]
	return x,y,p,u,v

def update_quiver(j,ax,fig):
	"""
	Update the figure with the wind field at pressure level j.
	"""
	print "Plotting pressure level {:}".format(j)
	x,y,p,u,v = get_uv(j)
	Q.set_UVC(u,v)
	ax.set_title('Pressure level: %3.3f hPa' % p,fontsize=14)
	return Q

def init_quiver():
	"""
	Initialise the figure with the wind field at pressure level j = 0.
	"""
	global Q
	x,y,p,u,v = get_uv(0)
	Q = ax.quiver(x,y,u,v)
	ax.set_title('Pressure level: %3.3f hPa' % p,fontsize=14)
	#ax.set_xlabel('Longitude')
	#ax.set_ylabel('Latitude')
	return Q

if __name__ != "__main__":
	sys.exit(0)

#-------------------------------
# Main
#-------------------------------
# Specify the data inputs
t = datetime(2015,2,7,12,0)
model = 'BARRA_R'
forecast_h = 6
# basetime
bt = t - timedelta(hours=forecast_h)

datadir = '/g/data/ma05/sample/%s/v1' % model
tfmt = '%Y%m%dT%H%MZ'
if model == 'BARRA_TA':
	# Plotting domain extent: lonmin, lonmax, latmin, latmax
	domain = [143, 149, -44.185, -39.55]
	resolution = 'f'
	# Input filenames for zonal and meridional wind and topography
	u_filename = os.path.join(datadir,'forecast/prs/wnd_ucmp/%04d/%02d/wnd_ucmp-fc-prs-PT1H-BARRA_TA-v1-%s.nc' % (bt.year,bt.month,bt.strftime(tfmt)))
	v_filename = os.path.join(datadir,'forecast/prs/wnd_vcmp/%04d/%02d/wnd_vcmp-fc-prs-PT1H-BARRA_TA-v1-%s.nc' % (bt.year,bt.month,bt.strftime(tfmt)))
	topo_filename = os.path.join(datadir,'forecast/slv/topog/%04d/%02d/topog-fc-slv-PT1H-BARRA_TA-v1-%s.nc' % (bt.year,bt.month,bt.strftime(tfmt)))
elif model == 'BARRA_R':
	# Plot over Australia
	domain = [110.8, 158, -45.6, -10.5]
	resolution = 'c'
	u_filename = os.path.join(datadir,'forecast/prs/wnd_ucmp/%04d/%02d/wnd_ucmp-fc-prs-PT1H-BARRA_R-v1-%s.nc' % (bt.year,bt.month,bt.strftime(tfmt)))
	v_filename = os.path.join(datadir,'forecast/prs/wnd_vcmp/%04d/%02d/wnd_vcmp-fc-prs-PT1H-BARRA_R-v1-%s.nc' % (bt.year,bt.month,bt.strftime(tfmt)))
	topo_filename = os.path.join(datadir,'analysis/slv/topog/%04d/%02d/topog-an-slv-PT0H-BARRA_R-v1-%s.nc' % (bt.year,bt.month,bt.strftime(tfmt)))

#--------------------------------
# Open the file and read the data
#--------------------------------
u_fid = Dataset(u_filename,'r')
v_fid = Dataset(v_filename,'r')
z_fid = Dataset(topo_filename,'r')
lat = u_fid.variables['latitude'][:]
lon = u_fid.variables['longitude'][:]
time = num2date(u_fid.variables['time'][:], u_fid.variables['time'].units)

#-----------------------------------------
# Truncate the data based on domain and t
#-----------------------------------------
if domain == None:
	domain = [lon.min(), lon.max(), lat.min(), lat.max()]

aa = np.logical_and(lon>=domain[0], lon<=domain[1])
bb = np.logical_and(lat>=domain[2], lat<=domain[3])
tind = np.argwhere(time == t).ravel()[0]

uwnd = u_fid.variables['wnd_ucmp'][tind,:,bb,aa]
vwnd = v_fid.variables['wnd_vcmp'][tind,:,bb,aa]
prs = u_fid.variables['pressure'][:]
latc = lat[bb]
lonc = lon[aa]
nprs = len(prs)
modwind = {'lon':lonc, 'lat':latc, 'uwind':uwnd, 'vwind':vwnd, 'prs':prs}
dx = (domain[1]-domain[0])/8
dy = (domain[3]-domain[2])/10
if dx == 0:
	dx = 0.5
if dy == 0:
	dy = 0.5

#-----------------------
# Plotting 
#-----------------------
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
m = Basemap(llcrnrlon=domain[0], \
		llcrnrlat=domain[2], \
		urcrnrlon=domain[1], \
		urcrnrlat=domain[3], \
		projection='cyl', \
		fix_aspect=False, \
		resolution=resolution)
m.drawcoastlines()
m.drawparallels(np.arange(np.floor(domain[2]), np.ceil(domain[3]), dy), \
		labels=[1,0,0,0], linewidth=0.75, color='gray') #20
m.drawmeridians(np.arange(np.floor(domain[0]), np.ceil(domain[1]), dx), \
		labels=[0,0,0,1], linewidth=0.75,color='gray')

# Plot the topography
top = ax.pcolorfast(z_fid.variables['longitude'][:], \
		z_fid.variables['latitude'][:], \
		z_fid.variables['topog'][:], \
		vmin=0, \
		vmax=1000, \
		cmap=cm.Blues)
colorbar_frame = fig.add_axes([0.82,0.12,0.01,0.3])
plt.colorbar(top,label='Elevation [m]',cax=colorbar_frame)

# Plot the wind vector as frames
anim = FuncAnimation(fig, \
		update_quiver, \
		frames=np.arange(0,nprs), \
		init_func=init_quiver, \
		interval=400, \
		fargs=(ax,fig), \
		repeat = False, \
		repeat_delay = 1000)

# Save the animation of the wind fields
anim.save('prs_wnd.%s.%s.gif' % (model,t.strftime("%Y%m%d%H")), dpi=80, writer='imagemagick')

# Done!
print "SUCCESS!"
sys.exit(0)

