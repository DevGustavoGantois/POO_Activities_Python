#Faça um programa completo utilizando classes e métodos que:
#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: i.tipoCombustivel.ii.valorLitroiii.quantidadeCombustivel
#Possua no mínimo esses métodos:i.abastecerPorValor() método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#ii.abastecerPorLitro() método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#iii. alterarValor()altera o valor do litro do combustível.iv. alterarCombustivel()
#altera o tipo do combustível.v.alterarQuantidadeCombustivel() altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class FuelPump:
    def __init__(self, fuel_type, liter_price, fuel_quantity):
        self.fuel_type = fuel_type
        self.liter_price = liter_price
        self.fuel_quantity = fuel_quantity

    def refuel_by_value(self, value):
        liters_refueled = value / self.liter_price
        if liters_refueled <= self.fuel_quantity:
            self.fuel_quantity -= liters_refueled
            return f"Refueled {liters_refueled:.2f} liters. Total cost: $ {value:.2f}"
        else:
            return "Insufficient fuel quantity in the pump."

    def refuel_by_liter(self, liters):
        total_cost = liters * self.liter_price
        if liters <= self.fuel_quantity:
            self.fuel_quantity -= liters
            return f"Refueled {liters:.2f} liters. Total cost: $ {total_cost:.2f}"
        else:
            return "Insufficient fuel quantity in the pump."

    def change_price_per_liter(self, new_price):
        self.liter_price = new_price
        return f"Price per liter changed to $ {new_price:.2f}"

    def change_fuel_type(self, new_fuel_type):
        self.fuel_type = new_fuel_type
        return f"Fuel type changed to {new_fuel_type}"

    def change_fuel_quantity(self, new_quantity):
        self.fuel_quantity = new_quantity
        return f"Fuel quantity in the pump changed to {new_quantity:.2f} liters"

# Example usage
fuel_pump = FuelPump("Gasoline", 5.50, 100.0)

print(fuel_pump.refuel_by_value(50)) 
print(fuel_pump.refuel_by_liter(10))  
print(fuel_pump.change_price_per_liter(6.0)) 
print(fuel_pump.change_fuel_type("Ethanol"))  
print(fuel_pump.change_fuel_quantity(150))  

