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
Nz = np.ones_like(Nx)

length = np.sqrt((Nx**2) + (Ny**2) + (Nz**2))

Normalized_vec = [Nx/length,Ny/length,Nz/length]

slope_x = -Nx/Nz
slope_y = -Ny/Nz

p = gaussian_filter(slope_x,sigma=2)
q = gaussian_filter(slope_y,sigma=2)

dq_dx = sobel(q, axis=1)  
dp_dy = sobel(p, axis=0)

curl_before = dq_dx - dp_dy
integrability_before = np.mean(np.abs(curl_before))
print("Integrability Error (Before Poisson):", integrability_before)

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

height_grad_x = sobel(HEIGHT_F, axis=1)
height_grad_y = sobel(HEIGHT_F, axis=0)

dq_dx_after = sobel(height_grad_y, axis=1)
dp_dy_after = sobel(height_grad_x, axis=0)

curl_after = dq_dx_after - dp_dy_after
integrability_after = np.mean(np.abs(curl_after))
print("Integrability Error (After Poisson):", integrability_after)

reduction = ((integrability_before - integrability_after) / integrability_before) * 100
print("Integrability Reduction (%):", reduction)

height_direct = np.cumsum(p, axis=1) + np.cumsum(q, axis=0)
height_direct = (height_direct - height_direct.min()) / (height_direct.max() - height_direct.min())

grad_direct_x = sobel(height_direct, axis=1)
grad_direct_y = sobel(height_direct, axis=0)
grad_poisson_x = sobel(HEIGHT_F, axis=1)
grad_poisson_y = sobel(HEIGHT_F, axis=0)

energy_direct = np.mean(grad_direct_x**2 + grad_direct_y**2)
energy_poisson = np.mean(grad_poisson_x**2 + grad_poisson_y**2)

print("Gradient Energy Direct:", energy_direct)
print("Gradient Energy Poisson:", energy_poisson)

reduction = ((energy_direct - energy_poisson) / energy_direct) * 100
print("Gradient Energy Reduction (%):", reduction)

plt.imshow(HEIGHT_F,cmap='viridis')
plt.title("Digital Elevation Model(DEM)")
plt.axis('off')
plt.savefig("DEM")
plt.show()
