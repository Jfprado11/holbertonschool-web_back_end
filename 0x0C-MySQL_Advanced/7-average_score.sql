-- mysql advanced
-- creatinag a more advance procedure
delimiter $$

CREATE Procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE finalscore float;
    SET finalscore = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    UPDATE users SET average_score = finalscore WHERE id = user_id;
END $$
delimiter ;