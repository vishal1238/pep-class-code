-- Create Deliveries Table
CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY,
    OrderID INT,
    DeliveryStatus VARCHAR(20),   -- 'Delivered', 'Cancelled', 'In-Transit'
    DeliveryTimeMinutes INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert Sample Data
INSERT INTO Deliveries VALUES
(901, 501, 'Delivered', 25),
(902, 502, 'Delivered', 42);

-- Display Data
SELECT * FROM Deliveries;