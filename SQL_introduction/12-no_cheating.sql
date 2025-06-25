-- Updates the score of Bob to 10 in the table `second_table`.
UPDATE second_table
JOIN (
    SELECT score FROM second_table WHERE name = 'John'
) AS temp
SET second_table.score = temp.score
WHERE second_table.name = 'Bob';
