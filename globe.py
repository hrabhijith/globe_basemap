import matplotlib.pyplot as plt

import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

from mpl_toolkits.basemap import Basemap

fig, ax0 = plt.subplots(figsize=(10,6))

ax0.set_position([0,0,1,1])

galaxy_image = plt.imread('galaxy_image.png')

ax0.imshow(galaxy_image)

ax0.set_axis_off()

ax1 = fig.add_axes([0.09,0.1,0.8,0.8])

ax1.clear()

ax1.set_axis_off()

lat_pos=0
lon_pos=0

m = Basemap(projection='ortho', resolution = 'l', lat_0=lat_pos, lon_0 = lon_pos)

m.bluemarble()

def press(event):
    global lon_pos
    global lat_pos

    if event.key == 'w':
        lat_pos -=20
    
    if event.key == 'z':
        lat_pos +=20
    
    if event.key == 'a':
        lon_pos +=20
    
    if event.key == 'd':
        lon_pos -=20

    m = Basemap(projection='ortho',resolution='l',
            lat_0=lat_pos, lon_0=lon_pos)

    m.bluemarble()
    fig.canvas.draw()
    


fig.canvas.mpl_connect('key_press_event', press)

plt.show()