from blobmodel import Model, BlobFactory, Blob
import numpy as np


class CustomBlobFactoryVy0(BlobFactory):
    def __init__(self) -> None:
        pass

    def sample_blobs(
        self, Ly: float, T: float, num_blobs: int, blob_shape: str, t_drain: float
    ) -> list[Blob]:

        # set custom parameter distributions
        __amp = np.ones(num_blobs)
        __width = np.ones(num_blobs)
        __vx = np.ones(num_blobs)
        __vy = np.zeros(num_blobs)

        __posx = np.zeros(num_blobs)
        __posy = np.ones(num_blobs) * Ly / 2
        __t_init = np.ones(num_blobs) * 0

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


class CustomBlobFactoryVx0(BlobFactory):
    def __init__(self) -> None:
        pass

    def sample_blobs(
        self, Ly: float, T: float, num_blobs: int, blob_shape: str, t_drain: float
    ) -> list[Blob]:

        # set custom parameter distributions
        __amp = np.ones(num_blobs)
        __width = np.ones(num_blobs)
        __vx = np.zeros(num_blobs)
        __vy = np.ones(num_blobs)

        __posx = np.zeros(num_blobs)
        __posy = np.ones(num_blobs) * Ly / 2
        __t_init = np.ones(num_blobs) * 0

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


bf_vy_0 = CustomBlobFactoryVy0()

bm_vy_0 = Model(
    Nx=10,
    Ny=10,
    Lx=10,
    Ly=10,
    dt=1,
    T=1,
    periodic_y=True,
    blob_shape="exp",
    num_blobs=1,
    blob_factory=bf_vy_0,
    t_drain=1e10,
)

bf_vx_0 = CustomBlobFactoryVx0()

bm_vx_0 = Model(
    Nx=10,
    Ny=10,
    Lx=10,
    Ly=10,
    dt=1,
    T=1,
    periodic_y=True,
    blob_shape="exp",
    num_blobs=1,
    blob_factory=bf_vx_0,
    t_drain=1e10,
)


def test_vy_0():
    assert bm_vy_0.make_realization(speed_up=True, error=1e-2)


def test_vx_0():
    assert bm_vx_0.make_realization(speed_up=True, error=1e-2)


test_vx_0()
test_vy_0()
