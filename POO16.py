#Desenvolva uma classe Produto em python que contenha
#atributos privados, como nome, preço e quantidade em
#estoque. Forneça métodos públicos para acessar e
#modificar esses atributos e garantir que o preço e a
#quantidade não sejam definidos como valores negativos.


#CLASSE COM OS ATRIBÚTOS PROPOSTOS:
class Product:
    def __init__(self, name, price, quantity_stock):
        self.__name = name
        self.__price = price
        self.__quantity_stock = quantity_stock
#METODOS GET:
    def get_name_product(self):
        return self.__name
    def get_price_product(self):
        return self.__price
    def get_quantity_product(self):
        return self.__quantity_stock
#METODOS SET:
    def set_name_product(self, name):
        self.__name = name

    def set_price_product(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("This number is negative. This not exist, try again.")
    def set_quantity_product(self, quantity_stock):
        if quantity_stock >= 0:
            self.__quantity_stock = quantity_stock
        else:
            raise ValueError("This number is negative. This not exist, try again.")

product1 = Product('Mesa', 20000.00, 12)
#ANTES DE MODIFICAR OS ITENS:
product1.get_name_product()
product1.get_price_product()
product1.get_quantity_product()
#acessando os atributos através do método get:
print("\nMetohods with gets. Before Modifications:")
print(f"Name of Product: {product1.get_name_product()}")
print(f"Price of Product: {product1.get_price_product()}")
print(f"Quantity of Stock: {product1.get_quantity_product()}")

#DEPOIS DE MODIFICAR OS ITENS:
#Utilizando os métodos setts para modificação dos atribútos:
print("\nMetohods with sets:")
product1.set_name_product('Sofa')
print(f"Name of Product: {product1.get_name_product()}")
product1.set_price_product(30000.00)
print(f"Price of Product: {product1.get_price_product()}")
product1.set_quantity_product(6)
print(f"Quantity of Stock:{product1.get_quantity_product()}")