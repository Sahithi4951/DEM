## Digital Elevation Model (DEM) from a Grayscale Moon Image
## Overview

This project reconstructs a Digital Elevation Model (DEM) from a single grayscale image of the Moon using classical computer vision and numerical methods.

Pixel brightness is not treated as height. Instead, brightness variations are interpreted as surface orientation, from which surface slopes are estimated and then globally integrated to recover terrain height.

The final output is a relative elevation map highlighting craters, slopes, and flat regions.

---

## Method Summary

Gaussian Smoothing
Reduces noise, compression artifacts, and unstable brightness variations.

Image Gradients (Sobel Operator)
Estimates brightness changes along x and y directions, which relate to surface tilt.

Surface Normals
Gradients are converted into 3D surface normals representing local surface orientation.

Surface Slopes
Normals are transformed into slope fields (∂z/∂x, ∂z/∂y).

Divergence of Slopes
Captures global inconsistency in slope estimates.

Poisson Surface Integration
Solves for the height surface whose gradients best match the estimated slopes, using an FFT-based solution.

---

## Key Idea

The height surface 𝑧(𝑥,𝑦)
z(x,y) is recovered by solving a Poisson equation, which provides a globally consistent integration of local slope measurements.

This avoids error accumulation that occurs with direct path-wise integration.

---

## Output

A normalized Digital Elevation Model (DEM)

Relative height representation (not absolute elevation)

Terrain features such as craters and ridges are clearly visible

Assumptions

Lambertian surface reflectance

Single distant light source

Orthographic projection

Relative height reconstruction

---

## Limitations

Absolute height scale cannot be recovered

Sensitive to illumination direction

Boundary effects due to FFT-based solution

---

## Tools & Libraries

Python

NumPy

SciPy

Matplotlib

Applications

Shape-from-shading

Planetary surface analysis

Computer vision and graphics

Remote sensing fundamentals

---

## Result

The project demonstrates how local brightness changes can be converted into global terrain structure using principled mathematical modeling.

---

## Author

Sahithi Bashetty
bashettysahithi@gmail.com