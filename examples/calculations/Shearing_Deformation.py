# Copyright (c) 2022 MetPy Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""
====================
Shearing Deformation
====================

Use `metpy.calc.shearing_deformation`.

This example demonstrates the calculation of shearing deformation using the example xarray
Dataset and plotting using Matplotlib.
"""
import matplotlib.pyplot as plt

import metpy.calc as mpcalc
from metpy.cbook import example_data

# load example data
ds = example_data()

# Calculate the shearing deformation of the flow
shr_def = mpcalc.shearing_deformation(ds.uwind, ds.vwind)

# start figure and set axis
fig, ax = plt.subplots(figsize=(5, 5))

# plot shearing deformation and scale by 1e5
cf = ax.contourf(ds.lon, ds.lat, shr_def * 1e5, range(-80, 81, 1), cmap=plt.cm.PuOr_r)
plt.colorbar(cf, pad=0, aspect=50)
ax.barbs(ds.lon.values, ds.lat.values, ds.uwind, ds.vwind, color='black', length=5, alpha=0.5)
ax.set(xlim=(260, 270), ylim=(30, 40))
ax.set_title('Shearing Deformation Calculation')

plt.show()