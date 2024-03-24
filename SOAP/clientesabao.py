from zeep import Client

client = Client('http://www.dneonline.com/calculator.asmx?WSDL')

def add(a, b):
    result = client.service.Add(a, b)
    return result

def subtract(a, b):
    result = client.service.Subtract(a, b)
    return result

def multiply(a, b):
    result = client.service.Multiply(a, b)
    return result

def divide(a, b):
    result = client.service.Divide(a, b)
    return result

print("Soma: ", add(10, 5))
print("Subtração: ", subtract(10, 5))
print("Multiplicação: ", multiply(10, 5))
print("Divisão: ", divide(10, 5))
