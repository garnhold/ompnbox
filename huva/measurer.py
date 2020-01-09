import huva

import helpers


def fetch_measurer(dpi=72.0):
	return helpers.get_or_create_by_key(fetch_measurer.measurers, dpi, lambda k: Measurer(dpi))
fetch_measurer.measurers = {}


class Measurer(huva.UnitSystemEX):
	def __init__(self, dpi):
		super(Measurer, self).__init__()

		self.pixels = self.add_internal("Pixel", "Pixels", ["px", "pxs"])
		
		self.ratio = self.add_ratio_of_world("Ratio", "Ratio", [])
		self.percent = self.add_that_is_n_this("Percent", "Percent", ["%"], 100.0, self.ratio)
		
		self.inches = self.add_this_is_n_that("Inch", "Inches", ["in", "''", '"'], dpi, self.pixels)
		self.feet = self.add_this_is_n_that("Foot", "Feet", ["ft", "'"], 12.0, self.inches)
		self.yards = self.add_this_is_n_that("Yard", "Yards", ["yd"], 3.0, self.feet)
		self.miles = self.add_this_is_n_that("Mile", "Miles", ["mi"], 5280.0, self.feet)
		
		self.points = self.add_that_is_n_this("Point", "Points", ["pt", "pts"], 72.0, self.inches)
		self.picas = self.add_this_is_n_that("Pica", "Picas", ["p"], 12.0, self.points)
		
		self.centimeters = self.add_that_is_n_this("Centimeter", "Centimeters", ["cm"], 2.54, self.inches)
		self.millimeters = self.add_that_is_n_this("Millimeter", "Millimeters", ["mm"], 10.0, self.centimeters)
		self.meters = self.add_this_is_n_that("Meter", "Meters", ["m"], 100.0, self.centimeters)
		self.kilometers = self.add_this_is_n_that("Kilometer", "Kilometers", ["km"], 1000.0, self.meters)
		
		self.chains = self.add_this_is_n_that("Chain", "Chains", [], 66.0, self.feet)
		self.links = self.add_that_is_n_this("Link", "Links", [], 100.0, self.chains)
		self.furlongs = self.add_this_is_n_that("Furlong", "Furlongs", [], 10.0, self.chains)
		
		self.rods = self.add_that_is_n_this("Rod", "Rods", [], 4.0, self.chains)
		self.perches = self.add_that_is_n_this("Perch", "Perches", [], 4.0, self.chains)
		self.poles = self.add_that_is_n_this("Pole", "Poles", [], 4.0, self.chains)
		
		self.horse_lengths = self.add_this_is_n_that("Horse Length", "Horse Lengths", [], 8.0, self.feet)