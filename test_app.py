from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_products():
    client = app.test_client()

    response = client.get("/products")

    assert response.status_code == 200

    products = response.get_json()

    assert len(products) == 3
    assert products[0]["name"] == "Laptop"
    assert products[1]["name"] == "Phone"
    assert products[2]["name"] == "Headphones"