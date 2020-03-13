# add alpha (transparency) to a colormap
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
wd = cm.winter._segmentdata # only has r,g,b  
wd['alpha'] =  ((0.0, 0.0, 0.3), 
               (0.3, 0.3, 1.0),
               (1.0, 1.0, 1.0))

# modified colormap with changing alpha
al_winter = LinearSegmentedColormap('AlphaWinter', wd) 

# get the map image as an array so we can plot it 
import matplotlib.image as mpimg 
map_img = mpimg.imread('isavia_map.png') 

# making and plotting heatmap 
import numpy.random as random 
heatmap_data = random.rand(10,12) 

import seaborn as sns; sns.set()

hmax = sns.heatmap(heatmap_data,
            #cmap = al_winter, # this worked but I didn't like it
            cmap = cm.winter,
            alpha = 0.15, # whole heatmap is translucent
            annot = True,
            zorder = 2,
            )

# heatmap uses pcolormesh instead of imshow, so we can't pass through 
# extent as a kwarg, so we can't mmatch the heatmap to the map. Instead, 
# match the map to the heatmap:

hmax.imshow(map_img,
          aspect = hmax.get_aspect(),
          extent = hmax.get_xlim() + hmax.get_ylim(),
          zorder = 1) #put the map under the heatmap

from matplotlib.pyplot import show 
show()