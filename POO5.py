#Crie uma classe chamada Fatura , a classe Fatura deve incluir
#os seguintes atributos o nome do item; o preço unitário do item;
#quantidade de item a ser faturado; valor total da fatura; Sua
#classe deve ter um construtor que inicialize todos os atributos
#menos o valor total da fatura. Forneça um método chamado
#gerar_fatura que calcula o valor da fatura (isto é, multiplicar a
#quantidade pelo preço por item).

class Invoice:
    def __init__(self, name_item, price_item, quantity_item):
        self.name_item = name_item
        self.price_item = price_item
        self.quantity_item = quantity_item
        self.total_item = 0  # Inicializado como zero, será calculado no método generate_invoice

    def generate_invoice(self):
        self.total_item = self.price_item * self.quantity_item
        return self.total_item

# Criando uma instância da classe Invoice
item_name = input("Enter a name of item: ")
item_price = float(input("Enter a price of item: "))
item_quantity = int(input("Enter a quantity of item: "))

invoice = Invoice(item_name, item_price, item_quantity)

# Chamando o método generate_invoice
total_invoice = invoice.generate_invoice()

print(f"Total Invoice Value: {total_invoice}")
    
    


        
    
