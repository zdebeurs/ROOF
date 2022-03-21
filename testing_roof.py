import roof
import matplotlib.pyplot as plt

filepath = '/Users/megan/Documents/Code/ROOF/ROOF_data/NIRSpec/jwdata0010010_11010_0001_NRS1_uncal_updatedHDR_10INTS_ramp_STOPAFTERBIAS.fits'

data = roof.Data(filepath)

# print(data.sci)

spec_window=3

removef_simple = data.roof_median(spec_window)

plt.figure()
plt.imshow(data.sci[0,0,:,:],aspect=10)
plt.show()

plt.figure()
plt.imshow(removef_simple,aspect=10)
plt.show()