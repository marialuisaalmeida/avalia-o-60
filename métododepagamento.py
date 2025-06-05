class MetodoPagamento:
    def pagar(self, valor):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class CartaoCredito(MetodoPagamento):
    def __init__(self, numero_cartao, nome_titular, validade):
        self.numero_cartao = numero_cartao
        self.nome_titular = nome_titular
        self.validade = validade

        
    def pagar(self, valor):
        print(f"Pagamento de R${valor:.2f} realizado com cartão de crédito {self.numero_cartao}.")

class Boleto(MetodoPagamento):
    def pagar(self, valor):
        print(f"Boleto gerado para pagamemto de R${valor:.2f}.")
        
class Pix(MetodoPagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix
        
        
    def pagar(self, valor):
        print(f"Pagamento via pix (chave {self.chave_pix} no valor de R${valor:.2f} realizado.")
            

#RESTO DO CÓDIGO

def processar_pagamento(metodo, valor):
    metodo.pagar(valor)
    
cartao = CartaoCredito("1234 5678 9876 5432", "João Silva", "12/25")
boleto = Boleto()
pix = Pix("joao.silva@gmail.com")

processar_pagamento(cartao, 150.0)
processar_pagamento(boleto, 250.0)
processar_pagamento(pix, 300.0)
