class Vehicle:
    vid = ''
    model = ''
    year = 0
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year
    def __str__(self):
        return "(Vehicle ID : " + str(self.vid) + ", Model : " + str(self.model) + ", Year : " + str(self.year) + ")"
    def __eq__(self, other):
        return self.vid == other.vid
    def is_new(self, n):
        return self.year >= 2026 - n
class Car(Vehicle):
    fuel_type = ''
    doors = 0
    def __init__(self, vid, model, year,fuel_type, doors):
        Vehicle.__init__(self, vid, model, year)
        self.fuel_type = fuel_type
        self.doors =int(doors)

    def __str__(self):
        return "(Car ID : " + str(self.vid) + ", Model : " + str(self.model) + ", Year : " + str(self.year) + ", Fuel Type : "+ self.fuel_type + ", Doors : " + str(self.doors) + ")"


class Truck(Vehicle):
    max_load = 0
    axles = 0
    def __init__(self, vid, model, year,max_load,axles):
        Vehicle.__init__(self, vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return "(Truck ID : " +str(self.vid) + ", Model : " +str(self.model) +", Year : " + str(self.year) + ", Max Load : "+ str(self.max_load) +", Axles : "+ str(self.axles) + ")"
class Motorcycle(Vehicle):
    engine_cc = 0
    type = ''
    def __init__(self, vid, model, year,engine_cc,type ):
        Vehicle.__init__(self, vid, model, year)
        self.type = type
        self.engine_cc = int(engine_cc)
    def __str__(self):
        return "(Motorcycle ID : " + str(self.vid) + ", Model : " + str(self.model) + ", Year : " +str(self.year) + ", Engine CC : "+str(self.engine_cc) + ", Type : " + str(self.type) +")"


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as file:
        for v in vehicles:
            if isinstance(v, Car):
                file.write(f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}\n")
            elif isinstance(v, Truck):
                file.write(f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}\n")
            elif isinstance(v, Motorcycle):
                file.write(f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.type}\n")


def load_fleet_from_file(filename):
    loaded_vehicles = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            v_type = data[0]

            vid = data[1]
            model = data[2]
            year = int(data[3])


            if v_type == "Car":
                loaded_vehicles.append(Car(vid, model, year, data[4], int(data[5])))
            elif v_type == "Truck":
                loaded_vehicles.append(Truck(vid, model, year, int(data[4]), int(data[5])))
            elif v_type == "Motorcycle":
                loaded_vehicles.append(Motorcycle(vid, model, year, int(data[4]), data[5]))

    return loaded_vehicles

v1 = Car("V001", "Tesla Model 3", 2023, "Electric", 4)
v2 = Car("V002", "Toyota Corolla", 2018, "Petrol", 4)
t1 = Truck("T101", "Volvo FH16", 2019, 25000, 6)
t2 = Truck("T102", "Mercedes Actros", 2021, 18000, 4)
m1 = Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport")
m2 = Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")

fleet = [v1, v2, t1, t2, m1, m2]

save_fleet_to_file(fleet, "fleet.txt")

print("Loading fleet data from 'fleet.txt'...")
loaded_fleet = load_fleet_from_file("fleet.txt")
print(f"{len(loaded_fleet)} vehicles loaded successfully.\n")

print("--- All Vehicles ---")
for v in loaded_fleet:
    print(v)

print("\n--- Recent Vehicles (Last 4 Years) ---")
for v in loaded_fleet:
    if v.is_new(4):
        print(v)

print("\n--- Electric Cars Only ---")
for v in loaded_fleet:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)