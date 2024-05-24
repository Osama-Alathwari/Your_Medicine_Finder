from Medicine import Medicine
from typing import List


class Pharmacy:
    id = 1

    def __init__(self, nameOfPharmacy, locationOfPharmacy, streetName):
        self.__ID = Pharmacy.id
        self.__nameOfPharmacy = nameOfPharmacy
        self.__locationOfPharmacy = locationOfPharmacy
        self.__streetName = streetName
        self.__medicines: List[Medicine] = []
        Pharmacy.id += 1

    def get_ID(self):
        return self.__ID

    def set_nameOfPharmacy(self, nameOfPharmacy):
        self.__nameOfPharmacy = nameOfPharmacy

    def set_locationOfPharmacy(self, locationOfPharmacy):
        self.__locationOfPharmacy = locationOfPharmacy

    def set_streetName(self, streetName):
        self.__streetName = streetName

    def add_medicine(self, medicine):
        if type(medicine) == Medicine:
            self.__medicines.append(medicine)
        else:
            raise ValueError("You Input Error Value")

    def add_list_medicines(self, listOfMedicines: List[Medicine]):
        for medicine in listOfMedicines:
            # self.__medicines.append(medicine)
            self.add_medicine(medicine)

    def get_nameOfPharmacy(self):
        return self.__nameOfPharmacy

    def get_locationOfPharmacy(self):
        return self.__locationOfPharmacy

    def get_streetName(self):
        return self.__streetName

    def get_medicines(self):
        return self.__medicines

    def search_medicine(self, nameOfMedicine):
        for medicine in self.__medicines:
            if nameOfMedicine == medicine.get_nameOfMedicine():
                return medicine

    def __str__(self):
        return self.get_nameOfPharmacy()
