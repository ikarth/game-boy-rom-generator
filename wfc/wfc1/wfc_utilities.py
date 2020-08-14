# In[4]:

import collections
import numpy as np
import math
import logging

CoordXY = collections.namedtuple("coords_xy", ["x", "y"])
CoordRC = collections.namedtuple("coords_rc", ["row", "column"])

WFC_PARTIAL_BLANK = -3
WFC_NULL_VALUE = -9


def hash_downto(a, rank, seed=0):
    state = np.random.RandomState(seed)
    assert rank < len(a.shape)
    u = a.reshape((np.prod(a.shape[:rank]), -1))
    v = state.randint(1 - (1 << 63), 1 << 63, np.prod(a.shape[rank:]), dtype="int64")
    return np.inner(u, v).reshape(a.shape[:rank]).astype("int64")


# In[5]:


try:
    import google.colab

    IN_COLAB = True
except:
    IN_COLAB = False


# In[6]:


# get_ipython().run_line_magic('pylab', 'inline')
def load_visualizer(wfc_ns):
    if IN_COLAB:
        from google.colab import files

        uploaded = files.upload()
        for fn in uploaded.keys():
            print(
                'User uploaded file "{name}" with length {length} bytes'.format(
                    name=fn, length=len(uploaded[fn])
                )
            )
    else:
        import matplotlib
        import matplotlib.pylab
        from matplotlib.pyplot import figure
        from matplotlib.pyplot import subplot
        from matplotlib.pyplot import title
        from matplotlib.pyplot import matshow

    wfc_ns.img_filename = f"images/{wfc_ns.img_filename}"
    return wfc_ns


def find_pattern_center(wfc_ns):
    # wfc_ns.pattern_center = (math.floor((wfc_ns.pattern_width - 1) / 2), math.floor((wfc_ns.pattern_width - 1) / 2))
    wfc_ns.pattern_center = (0, 0)
    return wfc_ns
