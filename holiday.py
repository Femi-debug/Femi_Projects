# Getting User Inputs
city_list = ["New York","Boston","Chicago","Atlanta", "Houston"]
print(city_list)
city_flight = (input("Enter the city they will be flying to: ")).lower()
num_nights = int(input("The number of nights you will be staying at the hotel: ")) 
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Function for hotel cost
def hotel_cost (num_nights):
    price_per_night = 130
    return num_nights * price_per_night

# Function for plane cost
def plane_cost(city_flight):
    if city_flight == "new york":
        return 1200
    elif city_flight == "boston":
        return 1100
    elif city_flight == "chicago":
        return 1050
    elif city_flight == "atlanta":
        return 900
    elif city_flight == "houston":
        return 800
    else:
        return 0   

# Function for car rental
def car_rental (rental_days):
    daily_rental_cost = 60
    return rental_days * daily_rental_cost

# Function for holiday cost
def holiday_cost(num_nights,city_flight,rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)


print(f"Hotel cost of trip is: {hotel_cost (num_nights)}")
print(f"Plane cost of trip is: {plane_cost(city_flight)}")
print(f"Car Rental cost of trip is: {car_rental (rental_days)}")
print(f"Hotel cost of trip is: {holiday_cost(num_nights,city_flight,rental_days)}")