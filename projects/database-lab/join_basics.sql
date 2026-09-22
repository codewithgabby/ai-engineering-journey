SELECT
    products.name,
    categories.name
FROM products
JOIN categories
    ON products.category_id = categories.id;