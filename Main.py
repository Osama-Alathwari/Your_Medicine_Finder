import PharmacyMap
from Phramacy import Pharmacy
from Location import Location
from typing import List
import Algorithms, ACO

locations: List[Location] = [
    PharmacyMap.location1,
    PharmacyMap.location2,
    PharmacyMap.location3,
]

start: Pharmacy = None


def search_location(id):
    for loc in locations:
        if loc.get_ID() == id:
            return loc


def __main__():
    while True:
        print("#" * 50)
        loc: Location
        for loc in locations:
            print(f"{loc.get_ID()} - {loc.get_nameOfLocation()}")
        print("#" * 50)
        numberOfLocation = int(
            input("Enter the number of location that you are living: ").strip()
        )
        print("#" * 50)
        user_location = search_location(numberOfLocation)
        if user_location != None:
            for ph in user_location.get_pharmacies():
                print(ph.get_ID(), ".", ph.get_locationOfPharmacy())

            num_pharmacy = int(
                input("Write the number of the nearest place from you : ").strip()
            )
            start = user_location.search_pharmacy_by_ID(num_pharmacy)
            if start is None:
                print(
                    f"You enter place that is not found in {user_location.get_nameOfLocation()}"
                )
                continue
            else:
                break

        else:
            print("You enter error place")
            continue

    print("#" * 50)
    goal = input("Write the name of your medicine : ").strip()
    while True:
        print("#" * 50)
        print(
            """
Choose Your Preference:
    1) The Nearest Place
    2) The Best Price
"""
        )
        choice = input("Enter The Number Of Your Choice : ").strip()
        if choice == "1":
            goal_path = Algorithms.__main__(PharmacyMap.graph, start=start, goal=goal)
            pharmacyGoal: Pharmacy
            if goal_path is not None:
                pharmacyGoal = goal_path[-1][0]
                print(f"You can find the medicine {goal} by follow the under path :")
                streets = []
                places = []
                # counter = 0
                for node, cost in goal_path:
                    if streets == []:
                        counter = 0
                        streets.append(node.get_streetName())
                        places.append(node.get_locationOfPharmacy())
                        counter -= 1
                        print(f"You are in {node.get_streetName()} so :")
                    elif node.get_streetName() not in streets:
                        counter = 0
                        streets.append(node.get_streetName())
                        places.append(node.get_locationOfPharmacy())
                        counter -= 1
                        print(f"Go to {node.get_streetName()}", end=", ")
                    else:
                        places.append(node.get_locationOfPharmacy())
                        counter -= 1

                print("and Pass by ", end=" ")
                for p in places[counter:-1]:
                    print(f"{p} ", end=" , ")
                print(
                    f"and {places[-1]}\nThe medicine {goal}, you can find it after :",
                    Algorithms.path_cost(goal_path) / 10,
                    f"KM in {pharmacyGoal.get_nameOfPharmacy()} that is next to {pharmacyGoal.get_locationOfPharmacy()}",
                )
            else:
                print(f"The medicine {goal} ('The goal') is not found")

            break

        elif choice == "2":
            ACO.__main__(goal)
            break


__main__()
