class Vehicle:


    def __init__(self, name, type_of_a_vehicle, source_of_energy, average_speed_of_movement):
        self.name = name
        self.type_of_a_vehicle = type_of_a_vehicle
        self.source_of_energy = source_of_energy
        self.average_speed_of_movement = average_speed_of_movement


    def print_info(self):
        print('\nName of a vehicle: %s' % self.name)
        print('Type of a vehicle: %s' % self.type_of_a_vehicle)
        print('Source of energy for a vehicle: %s' % self.source_of_energy)
        print('Average speed of a vehicle: %s' % self.average_speed_of_movement)

    def delivery_time_by_distance(self, distance=0):
        delivery_time_h = (((distance / self.average_speed_of_movement) * 60) // 60)
        delivery_time_m = (((distance / self.average_speed_of_movement) * 60) % 60)
        print('Delivery time by distance %d km: %d hour(s) %d min.' % (distance, delivery_time_h, delivery_time_m))


class Train(Vehicle):


    def __init__(self, name, type_of_a_vehicle, source_of_energy, average_speed_of_movement, number_of_seats_for_passengers):
        super().__init__(name, type_of_a_vehicle, source_of_energy, average_speed_of_movement)
        self.number_of_seats_for_passengers = number_of_seats_for_passengers


    def print_info(self):
        super().print_info()
        print('Number of seats for passengers %d' % self.number_of_seats_for_passengers)


class Airplane(Vehicle):


    def __init__(self, name, type_of_a_vehicle, source_of_energy, average_speed_of_movement, maximum_flight_altitude):
        super().__init__(name, type_of_a_vehicle, source_of_energy, average_speed_of_movement)
        self.maximum_flight_altitude = maximum_flight_altitude

    def print_info(self):
        super().print_info()
        print('Maximum flight altitude: %d m.' % self.maximum_flight_altitude)


train1 = Train('Train123', 'land vehicle', 'electricity', 80, 700,)
train1.print_info()
train1.delivery_time_by_distance(120)

airplane1 = Airplane('Boing','air vihicle','fuel', 850, 9000)
airplane1.print_info()
airplane1.delivery_time_by_distance(450)