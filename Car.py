class Car:
    __fuel_level = 100  # percentage of fuel

    def __init__(self, brand, model, year, color, noise, autonomy):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.color = color
        self.noise = noise
        self.__autonomy = autonomy  # kms
        self.__current_autonomy = autonomy

    def __repr__(self):
        return f'This is a {self.color} {self.__brand} {self.__model} from {self.__year}'

    def fill_gas(self, amount):
        if amount + self.__fuel_level <= 100:
            self.__fuel_level += amount
            print('Car is filled!')
        else:
            raise ValueError(f'amount exceeds maximum capacity -- amount: {amount}')

    def drive(self, distance):
        required_fuel = self.__fuel_level * (distance / self.__current_autonomy)
        if required_fuel <= self.__fuel_level:
            self.__fuel_level -= required_fuel
            self.__current_autonomy -= distance
            print(f'Driving... {self.noise}')
        else:
            print('Not enough fuel :(\n'
                  f'Required fuel: {int(required_fuel)}\n'
                  f'Autonomy left: {self.__current_autonomy} kms')
            raise ValueError(f'Not enough fuel -- required fuel: {required_fuel}')

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def autonomy(self):
        return self.__autonomy

    @property
    def fuel_level(self):
        return self.__fuel_level


