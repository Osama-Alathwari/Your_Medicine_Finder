class Medicine:
    def __init__(self, nameOfMedicine, priceOfMedicine):
        self.__nameOfMedicine = nameOfMedicine
        if (type(priceOfMedicine) == int) or type(priceOfMedicine) == float:
            self.__priceOfMedicine = priceOfMedicine
        else:
            raise ValueError("You Must Input Integer Or Float Value")

    def get_nameOfMedicine(self):
        return self.__nameOfMedicine

    def get_priceOfMedicine(self):
        return self.__priceOfMedicine

    def set_nameOfMedicine(self, nameOfMedicine):
        self.__nameOfMedicine = nameOfMedicine

    def set_priceOfMedicine(self, priceOfMedicine):
        if (type(priceOfMedicine) == int) or type(priceOfMedicine) == float:
            self.__priceOfMedicine = priceOfMedicine
        else:
            raise ValueError("You Must Input Integer Or Float Value")
