-- mysql advanced
-- Using a trigger in sql
CREATE trigger update_items
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
