-- mysql advanced
-- creating the first procedure

delimiter $$

CREATE Procedure AddBonus(IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
    DECLARE idsprojects INT;
    DECLARE project_exits INT;
    SET project_exits = EXISTS(SELECT name FROM projects WHERE name = project_name);
    IF project_exits = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SET idsprojects = (SELECT id FROM projects WHERE name = project_name);
    INSERT INTO corrections VALUES(user_id, idsprojects, score);
END$$
delimiter ;
