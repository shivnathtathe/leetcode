# Write your MySQL query statement below
# Table_name = Signups
# Column Names = user_id,time_stamp
# confirmation_rate = confirmed / total number of requested confirmation
# Round the confirmation rate to two decimal places.
SELECT
    S.user_id,
    CASE
        WHEN COUNT(C.action) = 0 THEN 0.00
        ELSE ROUND(SUM(C.action = 'confirmed') / COUNT(C.action), 2)
    END AS confirmation_rate
FROM Signups AS S
LEFT JOIN Confirmations AS C
ON S.user_id = C.user_id
GROUP BY S.user_id;
