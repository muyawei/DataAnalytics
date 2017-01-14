# object-oriented plot

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
    (0., 0.),
    (0., 1.),
    (0.5, 1.5),
    (1., 1.),
    (1., 0.),
    (0., 0.),
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

patch = patches.PathPatch(path, facecolor='coral')
ax.add_patch(patch)
ax.set_xlim(-0.5, 2)
ax.set_ylim(-0.5, 2)

canvas.print_figure('oo.png')