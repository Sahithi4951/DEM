import scipy.fft
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy.ndimage import gaussian_filter,sobel
import numpy as np
from scipy.fft import ifft2,fft2,fftfreq

testImage = img.imread("C:/Users/bashe/Downloads/moon.png")

y_gauss = gaussian_filter(testImage,sigma=2)

grad_x = sobel(y_gauss,axis = 1)
grad_y = sobel(y_gauss,axis = 0)

magnitude = np.sqrt(grad_x**2 + grad_y**2)

Nx = -grad_x
Ny = -grad_y
Nz = np.ones((1100,1100))

length = np.sqrt((Nx**2) + (Ny**2) + (Nz**2))

Normalized_vec = [Nx/length,Ny/length,Nz/length]

slope_x = -Nx/Nz
slope_y = -Ny/Nz

p = gaussian_filter(slope_x,sigma=2)
q = gaussian_filter(slope_y,sigma=2)

div = sobel(p,axis = 1) + sobel(q,axis = 0)
DIV_F = np.float32(fft2(div))

W = DIV_F.shape[1]
H = DIV_F.shape[0]

kx = fftfreq(W)
ky = fftfreq(H)

kx_grid, ky_grid = np.meshgrid(kx,ky, indexing = 'xy')

L = -(kx_grid**2 + ky_grid**2)
L[0,0] = 1

height = DIV_F / L

HEIGHT_F = ifft2(height).real

HEIGHT_F = (HEIGHT_F - HEIGHT_F.min()) / (HEIGHT_F.max() - HEIGHT_F.min())

plt.imshow(HEIGHT_F,cmap='viridis')
plt.title("Digital Elevation Model(DEM)")
plt.axis('off')
plt.show()