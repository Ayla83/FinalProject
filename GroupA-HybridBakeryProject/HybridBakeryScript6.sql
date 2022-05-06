USE hybrid_bakery;

select * from order_detail;

INSERT INTO order_detail(customer_id, order_value, order_date, order_status, delivery_address_id, delivery_recipient) VALUES (20, 23.40, '2022-04-30', 'despatched', 1, 'Pam Johnson'), (20, 34.95, '2021-04-19', 'delivered', 2, 'Dave Johnson');


INSERT INTO product(product_name, price, product_description) VALUES ('Cheeskie', 3.75, 'A Cookie with a cheesecake filling and flavour - these Cheeskie\'s are a real treat.'), ('Bruffin', '3.50', 'Is it a Brioche? Is it a Muffin? It\'s both! The Bruffin is a light fluffy muffin made from brioche pastry - perfect any time of the day.');