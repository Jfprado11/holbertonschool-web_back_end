-- mysql advanced
-- creatinag funbction in sql

delimiter $$

CREATE Function SafeDiv(a INT, b INT)
RETURNS float
BEGIN

    IF b = 0 THEN
        SET valuereturn = 0;
    ELSE
        SET valuereturn = (a / b);
    END IF;
    RETURN valuereturn;
END$$
delimiter ;
