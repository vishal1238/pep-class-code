SELECT
    U.UserName,
    R.RestaurantName,
    O.BillAmount
FROM Users U
JOIN Orders O
    ON U.UserID = O.UserID
JOIN Restaurants R
    ON O.RestaurantID = R.RestaurantID;




SELECT DISTINCT
    R.RestaurantName
FROM Restaurants R
JOIN Orders O
    ON R.RestaurantID = O.RestaurantID;



SELECT
    O.OrderID,
    U.UserName
FROM Users U
JOIN Orders O
    ON U.UserID = O.UserID
JOIN Deliveries D
    ON O.OrderID = D.OrderID
WHERE D.DeliveryTimeMinutes > 35;



SELECT
    U.UserName,
    SUM(O.BillAmount) AS TotalSpend
FROM Users U
JOIN Orders O
    ON U.UserID = O.UserID
GROUP BY U.UserName;



