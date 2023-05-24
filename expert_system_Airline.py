class Flight:
    def __init__(self, flight_number, departure, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time


class Cargo:
    def __init__(self, cargo_id, description, weight):
        self.cargo_id = cargo_id
        self.description = description
        self.weight = weight


class AirlineSystem:
    def __init__(self):
        self.flights = []
        self.cargos = []

    def add_flight(self, flight_number, departure, destination, departure_time, arrival_time):
        flight = Flight(flight_number, departure, destination, departure_time, arrival_time)
        self.flights.append(flight)
        print("Flight added successfully.")

    def add_cargo(self, cargo_id, description, weight):
        cargo = Cargo(cargo_id, description, weight)
        self.cargos.append(cargo)
        print("Cargo added successfully.")

    def view_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            print("Flight Schedule:")
            for flight in self.flights:
                print(f"Flight Number: {flight.flight_number}")
                print(f"Departure: {flight.departure}")
                print(f"Destination: {flight.destination}")
                print(f"Departure Time: {flight.departure_time}")
                print(f"Arrival Time: {flight.arrival_time}")
                print("-------------------------")

    def view_cargos(self):
        if not self.cargos:
            print("No cargos available.")
        else:
            print("Cargo Schedule:")
            for cargo in self.cargos:
                print(f"Cargo ID: {cargo.cargo_id}")
                print(f"Description: {cargo.description}")
                print(f"Weight: {cargo.weight} kg")
                print("-------------------------")


def menu():
    airline_system = AirlineSystem()
    while True:
        print("\n--- Airline Scheduling and Cargo Schedules System ---")
        print("1. Add a flight")
        print("2. Add a cargo")
        print("3. View flight schedule")
        print("4. View cargo schedule")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure location: ")
            destination = input("Enter destination location: ")
            departure_time = input("Enter departure time: ")
            arrival_time = input("Enter arrival time: ")
            airline_system.add_flight(flight_number, departure, destination, departure_time, arrival_time)

        elif choice == "2":
            cargo_id = input("Enter cargo ID: ")
            description = input("Enter cargo description: ")
            weight = float(input("Enter cargo weight (in kg): "))
            airline_system.add_cargo(cargo_id, description, weight)

        elif choice == "3":
            airline_system.view_flights()

        elif choice == "4":
            airline_system.view_cargos()

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
menu()