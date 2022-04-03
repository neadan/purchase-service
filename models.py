from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.product_name} -- {self.product_price}"
