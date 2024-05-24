from Phramacy import Pharmacy
from Medicine import Medicine
from Location import Location

pharmacy1 = Pharmacy("pharmacy1", "Taiz University", "University Street")
pharmacy1.add_list_medicines(
    [
        Medicine("m1", 15.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m10", 28.2),
    ]
)

pharmacy2 = Pharmacy("pharmacy2", "Moath Mosque", "University Street")
pharmacy2.add_list_medicines(
    [
        Medicine("m1", 20.0),
        Medicine("m2", 10.5),
        Medicine("m3", 12.3),
        Medicine("m4", 20.7),
        Medicine("m5", 24.8),
        Medicine("m6", 25.4),
        Medicine("m7", 20.8),
        Medicine("m8", 30.5),
        Medicine("m9", 20.0),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m11", 28.2),
    ]
)

pharmacy3 = Pharmacy("pharmacy3", "University Hotel", "University Street")
pharmacy3.add_list_medicines(
    [
        Medicine("m1", 20.8),
        Medicine("m2", 12.2),
        Medicine("m3", 10.6),
        Medicine("m4", 19.0),
        Medicine("m5", 26.0),
        Medicine("m6", 22.4),
        Medicine("m7", 22.2),
        Medicine("m8", 30.5),
        Medicine("m9", 21.3),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m12", 28.2),
    ]
)

pharmacy4 = Pharmacy("pharmacy4", "Alshahid School", "University Street")
pharmacy4.add_list_medicines(
    [
        Medicine("m1", 21.0),
        Medicine("m2", 13.2),
        Medicine("m3", 11.6),
        Medicine("m4", 18.0),
        Medicine("m5", 24.0),
        Medicine("m6", 20.4),
        Medicine("m7", 21.5),
        Medicine("m8", 30.2),
        Medicine("m9", 20.5),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m13", 20.2),
    ]
)

pharmacy5 = Pharmacy("pharmacy5", "Yemen Supermarket", "Gamal Street")
pharmacy5.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 22.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m14", 28.2),
    ]
)

pharmacy6 = Pharmacy("pharmacy6", "Taiz Restaurant", "Gamal Street")
pharmacy6.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 21.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m15", 28.2),
    ]
)

pharmacy7 = Pharmacy("pharmacy7", "Alkuraimi Bank", "Gamal Street")
pharmacy7.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 20.5),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 39.0),
        Medicine("m23", 35.5),
        Medicine("m16", 28.2),
    ]
)

pharmacy8 = Pharmacy("pharmacy8", "Bus Station", "Al-Masbah Street")
pharmacy8.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 29.0),
        Medicine("m9", 20.9),
        Medicine("m22", 32.0),
        Medicine("m23", 35.0),
        Medicine("m17", 28.2),
    ]
)

pharmacy9 = Pharmacy("pharmacy9", "Taiz City Mall", "Al-Masbah Street")
pharmacy9.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 17.9),
        Medicine("m22", 34.0),
        Medicine("m23", 37.0),
        Medicine("m18", 28.2),
    ]
)

pharmacy10 = Pharmacy("pharmacy10", "Hadramout Restaurant", "Al-Masbah Street")
pharmacy10.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 30.0),
        Medicine("m23", 35.0),
        Medicine("m19", 28.2),
    ]
)

pharmacy11 = Pharmacy("pharmacy11", "Tadhamon Bank", "Al-Masbah Street")
pharmacy11.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 31.0),
        Medicine("m23", 33.0),
        Medicine("m20", 29.2),
    ]
)

pharmacy12 = Pharmacy("pharmacy12", "Yemen Cafa", "Al-Masbah Street")
pharmacy12.add_list_medicines(
    [
        Medicine("m1", 20.5),
        Medicine("m2", 12.2),
        Medicine("m3", 12.6),
        Medicine("m4", 20.0),
        Medicine("m5", 25.0),
        Medicine("m6", 24.4),
        Medicine("m7", 21.8),
        Medicine("m8", 30.0),
        Medicine("m9", 20.9),
        Medicine("m22", 32.0),
        Medicine("m23", 35.0),
        Medicine("m21", 26.2),
    ]
)

location1 = Location("University Street")
location1.add_list_pharmacies([pharmacy1, pharmacy2, pharmacy3, pharmacy4])

location2 = Location("Gamal Street")
location2.add_list_pharmacies([pharmacy5, pharmacy6, pharmacy7])

location3 = Location("Al-Masbah Street")
location3.add_list_pharmacies(
    [pharmacy8, pharmacy9, pharmacy10, pharmacy11, pharmacy12]
)


pharmacies = [
    pharmacy1,
    pharmacy2,
    pharmacy3,
    pharmacy4,
    pharmacy5,
    pharmacy6,
    pharmacy7,
    pharmacy8,
    pharmacy9,
    pharmacy10,
    pharmacy11,
    pharmacy12,
]


graph = {
    pharmacy1: [(pharmacy2, 3), (pharmacy3, 4)],
    pharmacy2: [(pharmacy1, 3), (pharmacy4, 5)],
    pharmacy3: [(pharmacy1, 4), (pharmacy4, 4), (pharmacy5, 12)],
    pharmacy4: [(pharmacy2, 5), (pharmacy3, 4)],
    pharmacy5: [(pharmacy3, 12), (pharmacy7, 5), (pharmacy6, 4)],
    pharmacy6: [(pharmacy5, 4), (pharmacy7, 3)],
    pharmacy7: [(pharmacy5, 5), (pharmacy6, 3), (pharmacy8, 15)],
    pharmacy8: [(pharmacy7, 15), (pharmacy9, 3)],
    pharmacy9: [(pharmacy8, 3), (pharmacy10, 4), (pharmacy11, 2), (pharmacy12, 4)],
    pharmacy10: [(pharmacy9, 4), (pharmacy11, 5)],
    pharmacy11: [(pharmacy9, 2), (pharmacy10, 5), (pharmacy12, 5)],
    pharmacy12: [(pharmacy9, 4), (pharmacy11, 5)],
}
