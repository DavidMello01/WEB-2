from zeep import Client

client = Client('algo.wsdl')

# Chamar o método do servidor para calcular o GCD
x = 1920  # largura da imagem
y = 1080  # altura da imagem
gcd = client.service.CalculateMDC(x, y)

# Calcular o Aspect Ratio
aspect_ratio_x = x / gcd
aspect_ratio_y = y / gcd

print("MDC:", gcd)
print("Aspect Ratio:", aspect_ratio_x, ":", aspect_ratio_y)
