from blobmodel import Model, Blob

bm = Model(Nx=200, Ny=100, Lx=10, Ly=10, dt=0.1, T=10, blob_shape='gauss', t_drain=2)

#bm.sample_blobs(num_blobs=1000, A_dist='deg',W_dist='deg', vx_dist='deg',vy_dist='zeros')

bm.sample_blobs(num_blobs=100)

#bm.integrate(file_name='2d_blobs.nc' ,speed_up=False, truncation_Lx = 1)

bm.show_model(interval=100)#), save = False)