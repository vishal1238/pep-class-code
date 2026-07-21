SELECT
    U.UserName,
    COUNT(O.OrderID) AS TotalOrders
FROM Users U
LEFT JOIN Orders O
    ON U.UserID = O.UserID
GROUP BY U.UserID, U.UserName;


SELECT
    R.RestaurantName,
    SUM(O.BillAmount) AS TotalRevenue
FROM Restaurants R
JOIN Orders O
    ON R.RestaurantID = O.RestaurantID
JOIN Users U
    ON O.UserID = U.UserID
WHERE U.City = 'Delhi'
GROUP BY R.RestaurantID, R.RestaurantName
HAVING SUM(O.BillAmount) > 5000;



SELECT
    R.RestaurantName,
    COUNT(D.DeliveryID) AS CancelledOrders
FROM Restaurants R
JOIN Orders O
    ON R.RestaurantID = O.RestaurantID
JOIN Deliveries D
    ON O.OrderID = D.OrderID
WHERE D.DeliveryStatus = 'Cancelled'
GROUP BY R.RestaurantID, R.RestaurantName;