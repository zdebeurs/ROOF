import os
from astropy.io import fits

class Data:
	'''
	A simple class to hold data
	'''

	def __init__(self, filepath, **kwargs):
		# Assign the filepath to the data
		self.filepath = filepath

		# Load the data from the filepath
		self.load_data(filepath)


	def load_data(self, filepath):
		'''
		Function to load JWST pipeline data prior to ramp fitting
		'''
		# Check if filepath is actually a file
		if not os.path.isfile(filepath):
			raise ValueError('File path not recognised as a file.')

		# Open FITS file
		with fits.open(filepath) as hdul:
			self.phead = hdul[0].header
			self.sci = hdul['SCI'].data
			self.pixdq = hdul['PIXELDQ'].data
			self.grpdq = hdul['GROUPDQ'].data
			self.err = hdul['ERR'].data

		return

	# Power spectrum

	# ABC method

	# Median method

	# Polynomial fit method