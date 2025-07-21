import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

curr_dir = Path(__file__).resolve().parent

# Observing run baseline in days (How long we observe the same star)
baseline = 150

# Cadence in days (How frequently we observe the planet)
cadence = 0.02

# Period of the planet, in days
period = 30

# Transit depth
depth = 0.0003

# Width of the transit, in days
width = 0.1

# Noise level (Set very small, because the instruments in this utopia are perfect)
noise_level = 0.001

# Time array, and normalised flux of the star
time = np.arange(0, baseline, cadence)
flux = np.ones_like(time)

# Add transits
for t0 in np.arange(0, baseline, period):
    transit = np.exp(-0.5 * ((time - t0) / (width/2.355))**2)
    flux -= depth * transit

# Add noise
flux += np.random.normal(0, noise_level, size = time.size)

# Save the data as a .csv file
df = pd.DataFrame({
    'time': time,
    'flux': flux,
    'flux_err': np.full_like(time, noise_level)
})
df.to_csv(curr_dir / "Planet 5.csv")

# Plot the transits
plt.figure(figsize=(10,4))
plt.plot(time, flux, 'k.', markersize = 2)
plt.xlabel("Time [days]")
plt.ylabel("Relative Flux")
plt.show()