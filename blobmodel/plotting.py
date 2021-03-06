import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import xarray as xr


def show_model(
    ds: xr.Dataset,
    interval: int = 100,
    save: bool = False,
    gif_name: str = "2d_blobs.gif",
    fps: int = 10,
) -> None:
    """Show animation of Model output.

    Parameters
    ----------
    ds: xarray Dataset,
        Model data
    interval: int, optional
        time interval between frames in ms
    save: bool, optional
        if True save animation as gif
    gif_name: str, optional
        set name for gif
    fps: int, optional
        set fps for gif
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    div = make_axes_locatable(ax)
    cax = div.append_axes("right", "5%", "5%")

    frames = []

    for timestep in ds.t.values:
        frame = ds["n"].sel(t=timestep).values
        frames.append(frame)

    cv0 = frames[0]
    im = ax.imshow(cv0, origin="lower")
    fig.colorbar(im, cax=cax)
    tx = ax.set_title("t = 0")

    dt = ds.t.values[1] - ds.t.values[0]

    def animate(i: int) -> None:
        arr = frames[i]
        vmax = np.max(arr)
        vmin = np.min(arr)
        im.set_data(arr)
        im.set_clim(vmin, vmax)
        tx.set_text(f"t = {i*dt:.2f}")

    ani = FuncAnimation(fig, animate, frames=ds["t"].values.size, interval=interval)
    if save:
        ani.save(gif_name, writer="ffmpeg", fps=fps)
    plt.show()
