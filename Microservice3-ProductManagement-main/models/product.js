const mongoose = require('mongoose');

// Definir el esquema del producto
const productSchema = new mongoose.Schema({
    product_id: { type: String, required: true, unique: true },
    product_name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    stock: { type: Number, required: true }
});

// Crear el modelo basado en el esquema
const Product = mongoose.model('Product', productSchema);

module.exports = Product;
