-- mysql advanced
-- creatinag funbction in sql

delimiter $$

CREATE Function SafeDiv(a INT, b INT)
RETURNS float
BEGIN
    IF b = 0 THEN
        RETURN (0);
    END IF;
    RETURN (a / b);
END;
$$
delimiter ;