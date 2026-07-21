-- Question 3 ● Problem Statement: Display all OrderID logs along with their corresponding user names where the order took more than 35 minutes to deliver. ● Tables to Use: Users, Orders, Deliveries 



SELECT O.OrderID, 
U.UserName FROM Orders O INNER JOIN Users U ON O.UserID = U.UserID INNER JOIN Deliveries D ON O.OrderID = D.OrderID WHERE D.DeliveryTimeMinutes > 35; 