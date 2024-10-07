from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoints de los microservicios
USER_MANAGEMENT_URL = "http://localhost:5001/users"
ORDER_MANAGEMENT_URL = "http://localhost:5002/orders"
PRODUCT_MANAGEMENT_URL = "http://localhost:5003/products"


# Endpoint para crear un nuevo usuario
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    # Enviar los datos al microservicio de gestión de usuarios
    response = requests.post(f"{USER_MANAGEMENT_URL}/create", json=data)
    return jsonify(response.json()), response.status_code


# Endpoint para crear un nuevo pedido y verificar el usuario
@app.route('/create_order', methods=['POST'])
def create_order():
    order_data = request.json

    # Verificar si el usuario existe en UserManagement
    user_id = order_data.get('user_id')
    user_response = requests.get(f"{USER_MANAGEMENT_URL}/{user_id}")

    if user_response.status_code == 200:
        # Crear el pedido en OrderManagement si el usuario es válido
        order_response = requests.post(f"{ORDER_MANAGEMENT_URL}/create", json=order_data)
        return jsonify(order_response.json()), order_response.status_code
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


# Endpoint para obtener información de un producto
@app.route('/get_product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product_response = requests.get(f"{PRODUCT_MANAGEMENT_URL}/{product_id}")

    if product_response.status_code == 200:
        return jsonify(product_response.json()), 200
    else:
        return jsonify({"error": "Producto no encontrado"}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
