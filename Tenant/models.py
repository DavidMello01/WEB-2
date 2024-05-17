from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tenant_id = db.Column(db.String(80), nullable=False)

    def __init__(self, username, tenant_id):
        self.username = username
        self.tenant_id = tenant_id
