from flask import Flask, g, request
from config import Config
from models import db, User
from tenant import init_tenant_schema, setup_event_listeners

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Configurar ouvintes de eventos
setup_event_listeners()

@app.before_request
def set_tenant():
    g.tenant_id = request.headers.get('X-Tenant-ID')

@app.route('/init_tenant', methods=['POST'])
def create_tenant():
    tenant_id = request.headers.get('X-Tenant-ID')
    init_tenant_schema(app, tenant_id)
    return f"Tenant {tenant_id} schema created.", 201

@app.route('/users', methods=['POST'])
def create_user():
    tenant_id = request.headers.get('X-Tenant-ID')
    username = request.json.get('username')
    user = User(username=username, tenant_id=tenant_id)
    db.session.add(user)
    db.session.commit()
    return f"User {username} created for tenant {tenant_id}.", 201

if __name__ == '__main__':
    app.run(debug=True)
