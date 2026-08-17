from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "application": "ShopFast",
        "version": "1.0",
        "message": "ShopFast application is running"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.get("/products")
def products():
    return jsonify([
        {
            "id": 1,
            "name": "Laptop",
            "price": 75000
        },
        {
            "id": 2,
            "name": "Phone",
            "price": 35000
        },
        {
            "id": 3,
            "name": "Headphones",
            "price": 5000
        }
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
