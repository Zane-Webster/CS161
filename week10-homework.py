"""
1. Create class SolarObject with attr distance from sun (au), spin type, and average time to orbit.
2. Create method estimated_potential_population(), which returns 6 billion / distance from sun. Round to nearest billion
3. Create method spin(), which is a pass (placeholder)
4. Create class Planet which inherits SolarObject using polymorphism. The planets always spin "slightly elliptical", and orbit time is measured in days. Create objects Earth and Mars
5. Create class Comet which inherits SolarObject using polymorphism. The comets always spin "like crazy", and orbit time is measured in years. Create objects Halley and Hale-Bopp.
6. Print all objects, listing attributes then estimated potential population
"""

class SolarObject:
    """
    Class containing attributes of a solar object

    :param name = name of the solar object
    :param distance_from_sun = the distance of the solar object from the sun in au
    :param spin_type = the way the solar object spins
    :param orbit_time = the time it takes the solar object to orbit
    :param orbit_unit = days or years depending on the length of orbit
    """
    def __init__(self, name, distance_from_sun, spin_type, orbit_time, orbit_unit):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.spin_type = spin_type
        self.orbit_time = orbit_time
        self.orbit_unit = orbit_unit

    def estimated_potential_population(self):
        return round(6/self.distance_from_sun)

    def spin(self):
        pass

    def list_attributes(self):
        print(f"{self.name} is "
              f"{self.distance_from_sun} au from the sun, "
              f"spins {self.spin_type}, "
              f"has an orbit taking {self.orbit_time} {self.orbit_unit} and "
              f"can support a population of: {self.estimated_potential_population()} billion")

class Planet(SolarObject):
    """
    Class containing attributes of a planet. Supersets SolarObject. Always has spin type of 'slightly elliptical', and orbit time measured in days.

    :param name = name of the planet
    :param distance_from_sun = the distance of the planet from the sun in au
    :param orbit_time = the time it takes the planet to orbit
    """
    def __init__(self, name, distance_from_sun, orbit_time):
        super().__init__(name, distance_from_sun, "slightly elliptical", orbit_time, "days")

class Comet(SolarObject):
    """
    Class containing attributes of a comet. Supersets SolarObject. Always has spin type of 'like crazy', and orbit time measured in years.

    :param name = name of the comet
    :param distance_from_sun = the distance of the comet from the sun in au
    :param orbit_time = the time it takes the comet to orbit
    """
    def __init__(self, name, distance_from_sun, orbit_time):
        super().__init__(name, distance_from_sun, "like crazy", orbit_time, "years")

earth = Planet("Earth", 1, 365)
mars = Planet("Mars", 1.4, 687)
halley = Comet("Halley", 35, 76.95)
hale_bopp = Comet("Hale-Bopp", 354, 2397.29)

solar_objects = [earth, mars, halley, hale_bopp]

for solar_object in solar_objects:
    solar_object.list_attributes()