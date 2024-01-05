class Cars:
    def __init__(self, model, color, year, transmission, is_electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.is_electric = is_electric

    def print_cars(self):
        print(f"car_model ={self.model}\nColor = {self.color}")
        print(f"Year ={self.year}\nTransmission = {self.transmission}\nElectric = {self.is_electric}\n")


class Ford(Cars):
    def __init__(self, model, color, year, transmission, is_electric):
        super().__init__(model, color, year, transmission, is_electric)



class BMW(Cars):
    def __init__(self, model, color, year, transmission, is_electric):
        super().__init__(model, color, year, transmission, is_electric)


class Telsa(Cars):
    def __init__(self, model, color, year, transmission, is_electric):
        super().__init__(model, color, year, transmission, is_electric)



# Creating instances for each car brand
bmw1 = BMW(model="X6", color="Silver", year=2018, transmission="Auto", is_electric=False)
tesla1 = Telsa(model="S", color="Beige", year=2017, transmission="Auto", is_electric=True)
ford1 = Ford(model="Focus", color="White", year=2020, transmission="Auto", is_electric=False)

bmw1.print_cars()
tesla1.print_cars()
ford1.print_cars()


