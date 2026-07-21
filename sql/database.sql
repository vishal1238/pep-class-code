CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50),
    City VARCHAR(50),
    AccountType VARCHAR(20)
);

CREATE TABLE Restaurants (
    RestaurantID INT PRIMARY KEY,
    RestaurantName VARCHAR(100),
    Cuisine VARCHAR(50),
    Rating DECIMAL(2,1)
);


INSERT INTO Users VALUES
(1, 'Aman Verma', 'Delhi', 'Premium'),
(2, 'Riya Sen', 'Mumbai', 'Regular');

INSERT INTO Restaurants VALUES
(101, 'Spice Symphony', 'North Indian', 4.5),
(102, 'Pizza Express', 'Italian', 3.9);


SELECT * FROM Users;

SELECT * FROM Restaurants;





CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    RestaurantID INT,
    BillAmount DECIMAL(10,2),
    OrderDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);



INSERT INTO Orders VALUES
(501, 1, 101, 1200.00, '2026-07-15'),
(502, 2, 102, 450.00, '2026-07-16');


SELECT * FROM Orders;