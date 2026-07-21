-- Question 1 ● Problem Statement: Write a query to display the UserName of the customer, the RestaurantName they ordered from, and the BillAmount for all orders. ● Tables to Use: Users, Restaurants, Orders 

SELECT
    U.UserName,
    R.RestaurantName,
    O.BillAmount
FROM Orders O
INNER JOIN Users U ON O.UserID = U.UserID
INNER JOIN Restaurants R ON O.RestaurantID = R.RestaurantID;