-- Create Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    RestaurantID INT,
    BillAmount DECIMAL(10,2),
    OrderDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);

-- Insert Sample Data
INSERT INTO Orders VALUES
(501, 1, 101, 1200.00, '2026-07-15'),
(502, 2, 102, 450.00, '2026-07-16');

-- Display Data
SELECT * FROM Orders;