-- Question 2 ● Problem Statement: Fetch a unique list of all restaurant names that have successfully had orders cooked and assigned to a delivery tracking record (even if the delivery was later cancelled). ● Tables to Use: Restaurants, Orders 

SELECT DISTINCT R.RestaurantName 
FROM Restaurants R INNER JOIN Orders O ON R.RestaurantID = O.RestaurantID; 