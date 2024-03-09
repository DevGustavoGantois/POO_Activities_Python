#Desenvolva uma aplicação de loja online em. Crie as
#classes Cliente e Pedido com uma associação
#bidirecional. Os clientes podem fazer pedidos, e os
#pedidos devem estar associados aos clientes que os
#fizeram. Implemente a capacidade de listar todos os
#pedidos de um cliente específico.

class Client:
    def __init__(self, name):
        self.orders = []
        self.name = name
    
    def make_orders(self, products, order_id):
        order = Order(products, order_id, self)
        self.orders.append(order)

    def list_orders(self):
        print(f"Orders for {self.name}:")
        for order in self.orders:
            print(order)
    def set_client(self, client):
        self.client = client
       
class Order:
    def __init__(self, products, order_id, client):
        self.products = products 
        self.order_id = order_id
        self.client = client

    def set_client(self, client):
        self.client = client

    def __str__(self):
        return f"The Order Id:{self.order_id}: Products: {','.join(self.products)}"
    
client1 = Client('Gustavo Gantois')
client1.make_orders(["Sofa", "Cadeira"], 1)
client1.make_orders(["Computador", "TV"], 2)

client1.list_orders()




        
