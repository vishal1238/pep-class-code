-- Create Users Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50),
    City VARCHAR(50),
    AccountType VARCHAR(20)   -- 'Regular' or 'Premium'
);

-- Insert Sample Data
INSERT INTO Users VALUES
(1, 'Aman Verma', 'Delhi', 'Premium'),
(2, 'Riya Sen', 'Mumbai', 'Regular');

-- Display Data
SELECT * FROM Users;