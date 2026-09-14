from app.database import SessionLocal
from app.models import Product


def main():
    db = SessionLocal()

    try:
        products = {
            1: "RICE-001",
            2: "RICE-002",
            3: "BEANS-001",
            4: "OIL-001",
        }

        for product_id, sku in products.items():
            product = db.get(Product, product_id)

            if product is None:
                raise ValueError(f"Product {product_id} not found")

            product.sku = sku

        db.commit()

        print("SKU backfill completed successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()