#======================================================================
# physconsts.py
# Physical Constants — St. Xavier's College (Autonomous), Kolkata
# B.Sc. Physics Lab — 2025
#======================================================================

"""
Physical Constants in SI Units (CODATA recommended values)
Usage:
    import physconsts
    or
    exec(open("physconsts.py").read())
"""

G        = 6.67430e-11       # m^3 kg^-1 s^-2
c        = 299792458.0       # m s^-1
h        = 6.62607015e-34    # J s
hbar     = h / (2 * 3.141592653589793)
e        = 1.602176634e-19   # C
me       = 9.1093837015e-31  # kg
mp       = 1.67262192369e-27 # kg
NA       = 6.02214076e23     # mol^-1
kB       = 1.380649e-23      # J K^-1
R        = NA * kB           # J mol^-1 K^-1
epsilon0 = 8.8541878128e-12  # F m^-1
mu0      = 1.25663706212e-6  # N A^-2
sigma    = 5.670374419e-8    # W m^-2 K^-4
g        = 9.80665           # m s^-2

M_earth  = 5.972e24          # kg
R_earth  = 6.371e6           # m
M_sun    = 1.9885e30         # kg

micro = 1e-6
milli = 1e-3
kilo  = 1e3
mega  = 1e6
giga  = 1e9

# No print statements — completely safe for exec(open(...).read())