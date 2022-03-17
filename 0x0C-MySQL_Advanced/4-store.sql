-- mysql advanced
-- Using a trigger in sql
CREATE trigger update_items
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - 1 WHERE name = NEW.item_name;
