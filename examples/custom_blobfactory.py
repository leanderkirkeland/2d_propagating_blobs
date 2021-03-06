from blobmodel import Model, BlobFactory, Blob, show_model
import numpy as np

# create custom class that inherits from BlobFactory
# here you can define your custom parameter distributions
class CustomBlobFactory(BlobFactory):
    def __init__(self) -> None:
        pass

    def sample_blobs(
        self, Ly: float, T: float, num_blobs: int, blob_shape: str, t_drain: float
    ) -> list[Blob]:

        # set custom parameter distributions
        __amp = np.linspace(0.01, 1, num=num_blobs)
        __width = np.linspace(0.01, 1, num=num_blobs)
        __vx = np.linspace(0.01, 1, num=num_blobs)
        __vy = np.linspace(0.01, 1, num=num_blobs)

        __posx = np.zeros(num_blobs)
        __posy = np.random.uniform(low=0.0, high=Ly, size=num_blobs)
        __t_init = np.random.uniform(low=0, high=T, size=num_blobs)

        # sort blobs by __t_init
        __t_init = np.sort(__t_init)

        return [
            Blob(
                id=i,
                blob_shape=blob_shape,
                amplitude=__amp[i],
                width_prop=__width[i],
                width_perp=__width[i],
                v_x=__vx[i],
                v_y=__vy[i],
                pos_x=__posx[i],
                pos_y=__posy[i],
                t_init=__t_init[i],
                t_drain=t_drain,
            )
            for i in range(num_blobs)
        ]


bf = CustomBlobFactory()
tmp = Model(
    Nx=100,
    Ny=100,
    Lx=2,
    Ly=2,
    dt=0.1,
    T=10,
    blob_shape="gauss",
    t_drain=2,
    periodic_y=True,
    num_blobs=1000,
    blob_factory=bf,
)

ds = tmp.make_realization(speed_up=True, error=1e-1)
show_model(ds=ds)
