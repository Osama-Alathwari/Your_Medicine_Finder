from Phramacy import Pharmacy
from typing import List


class Location:
    id = 1

    def __init__(self, nameOfLocation):
        self.__ID = Location.id
        self.__nameOfLocation = nameOfLocation
        self.__pharmacies: List[Pharmacy] = []
        Location.id += 1

    def get_ID(self):
        return self.__ID

    def get_nameOfLocation(self):
        return self.__nameOfLocation

    def set_nameOfLocation(self, nameOfLocation):
        self.__nameOfLocation = nameOfLocation

    def add_pharmacy(self, pharmacy):
        if type(pharmacy) == Pharmacy:
            self.__pharmacies.append(pharmacy)
        else:
            raise ValueError("You Input Error Value")

    def add_list_pharmacies(self, listOfPharmacies: List[Pharmacy]):
        for pharmacy in listOfPharmacies:
            self.add_pharmacy(pharmacy)

    def get_pharmacies(self):
        return self.__pharmacies

    def search_pharmacy(self, nameOfPharmacy):
        for ph in self.__pharmacies:
            if nameOfPharmacy == ph.get_nameOfPharmacy():
                return ph

    def sreach_pharmacy_by_place(self, place):
        for ph in self.__pharmacies:
            if ph.get_locationOfPharmacy() == place:
                return ph

    def search_pharmacy_by_ID(self, id):
        for ph in self.__pharmacies:
            if ph.get_ID() == id:
                return ph
