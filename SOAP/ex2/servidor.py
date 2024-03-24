from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class GCDService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def CalculateMDC(ctx, x, y):
        while y != 0:
            x, y = y, x % y
        return x

application = Application([GCDService], 'urn:GCDService',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

# Rodar o servidor
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8000, wsgi_application)
    print("Servidor SOAP rodando na porta 8000...")
    server.serve_forever()
