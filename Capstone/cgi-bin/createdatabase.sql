-- Create Database
CREATE DATABASE PythonTest;
GO
USE PythonTest;
GO

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Company NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL,
    Phone NVARCHAR(50),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Password NVARCHAR(50) NOT NULL
);
GO

-- Table: Employees
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Title NVARCHAR(100),
    Email NVARCHAR(100) NOT NULL,
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Password NVARCHAR(50) NOT NULL
);
GO

-- Table: Incidents
CREATE TABLE Incidents (
    IncidentID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    Date DATETIME DEFAULT GETDATE(),
    Protocol NVARCHAR(50),
    SourceIP NVARCHAR(50),
    DestinationIP NVARCHAR(50),
    SourceMAC NVARCHAR(50),
    DestinationMAC NVARCHAR(50),
    DestinationPort NVARCHAR(10),
    Info NVARCHAR(255),
    AttackType NVARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
GO

-- Insert sample customers (3)
INSERT INTO Customers (Name, Company, Email, Phone, Username, Password)
VALUES 
('Shad Feral', 'Akamai', 'shad@akamai.com', '555-1001', 'shadf', 'password'),
('Selina Kyle', 'Gotham Design', 'selina@gothamdesign.com', '555-1002', 'selina', 'cat123'),
('Bruce Wayne', 'Wayne Enterprises', 'bruce@wayne.com', '555-1003', 'brucew', 'batpass');
GO

-- Insert sample employees (2)
INSERT INTO Employees (Name, Title, Email, Username, Password)
VALUES
('Alfred Pennyworth', 'Network Administrator', 'alfred@batcavenetwork.com', 'alfred', 'butler1'),
('Lucius Fox', 'Chief Engineer', 'lucius@batcavenetwork.com', 'lucius', 'battech');
GO

-- Sample data for testing
INSERT INTO Incidents (CustomerID, Protocol, SourceIP, DestinationIP, Info, AttackType)
VALUES
(1, 'TCP', '192.168.1.10', '192.168.1.10', '[SYN]', 'SYN Flood'),
(2, 'ARP', '08-00-27-11-22-33', '192.168.1.20', 'Duplicate ARP Entry', 'ARP Poisoning');
GO
