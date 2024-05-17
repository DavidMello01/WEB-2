from flask import g, current_app
from sqlalchemy import event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import MetaData

from models import db

# Função para definir o esquema baseado no tenant
def get_tenant_schema():
    return g.tenant_id if hasattr(g, 'tenant_id') else 'public'

# Função para inicializar o esquema do tenant
def init_tenant_schema(app, tenant_id):
    with app.app_context():
        g.tenant_id = tenant_id
        db.create_all()

# Configurar evento dentro do contexto da aplicação
def setup_event_listeners():
    with current_app.app_context():
        @event.listens_for(db.engine, "before_cursor_execute")
        def set_search_path(conn, cursor, statement, parameters, context, executemany):
            schema = get_tenant_schema()
            cursor.execute(f"SET search_path TO {schema}")
