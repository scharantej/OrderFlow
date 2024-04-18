## Flask Application Design for an Order System using Angular

### HTML Files

- **index.html**: This will be the entry point of the application. It will contain the Angular application code and serve as the interface for user interaction.

### Routes

- **@app.route('/')**: This route will handle the initial request and serve the 'index.html' file.

- **@app.route('/api/orders', methods=['GET', 'POST'])**: This route will handle API requests for creating and retrieving orders. A GET request will return a list of all orders, while a POST request will create a new order.

- **@app.route('/api/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])**: This route will handle API requests for specific orders based on their ID. A GET request will return the order details, a PUT request will update the order, and a DELETE request will remove the order.