import os

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from models import Purchase, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:" \
                                            f"{os.environ['POSTGRES_PASSWORD']}" \
                                            f"@purchase-db/{os.environ['POSTGRES_DB']}"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app()


@app.route('/api/v1/purchase_form', methods=['GET', 'POST'])
def purchase_form():
    if request.method == 'POST':
        new_purchase = Purchase(product_name=request.form['p_name'], product_price=request.form['p_price'])
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for('list_purchases'))
    else:
        return render_template('purchase_form.html')


@app.route('/api/v1/list')
def list_purchases():
    purchases = Purchase.query.all()
    return render_template('list_purchases.html', purchases=purchases)


if __name__ == '__main__':
    app.run()
