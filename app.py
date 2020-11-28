from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products/<int:product_price_menor>&<int:product_price_mayor>')
def getProductByPrice(product_price_menor, product_price_mayor):
    productsFounds = [product for product in products if product['price'] != "AGOTADO" if (int(product['price']) >= product_price_menor) and (int(product['price'] <= product_price_mayor))]
    if(len(productsFounds) > 0):
        return jsonify({"product": productsFounds})
    return jsonify({"message": "Products by prices not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "description": request.json['description'],
        "price": request.json['price'],
    }
    products.append(new_product)
    return jsonify(({"message": "Product Added Succesfully", "products": products}))

if __name__ == '__main__':
    app.run(debug=True, port=3030)