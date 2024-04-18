
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return '<Order %r>' % self.name

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        orders = Order.query.all()
        return jsonify([order.to_dict() for order in orders])
    elif request.method == 'POST':
        data = request.get_json()
        order = Order(name=data['name'], description=data['description'])
        db.session.add(order)
        db.session.commit()
        return jsonify(order.to_dict())

@app.route('/api/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order(order_id):
    order = Order.query.get_or_404(order_id)
    if request.method == 'GET':
        return jsonify(order.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        order.name = data['name']
        order.description = data['description']
        db.session.commit()
        return jsonify(order.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
        return jsonify({'success': True})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
