-- Drop database if exists
DROP DATABASE IF EXISTS solution1;
CREATE DATABASE solution1;
USE solution1;

-- StatesEmployees table
CREATE TABLE StatesEmployees (
    id_state INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL
);

INSERT INTO StatesEmployees (title) VALUES 
('Contratado/Activo'),
('Suspendido'),
('Despedido'),
('Incapacidad'),
('Embarazo'),
('Vacaciones'),
('Permiso No Remunerado'),
('Permiso Remunerado');

-- LicensesApps table
CREATE TABLE LicensesApps (
    id_license INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    description VARCHAR(250) NULL
);

INSERT INTO LicensesApps (title, description) VALUES 
('Registrar empleados nuevos', 'Permite crear nuevos registros de empleados en el sistema'),
('Gestionar llamados de atencion', 'Permite crear y gestionar llamados de atención'),
('Gestionar licencias', 'Permite asignar o revocar licencias a empleados'),
('Ver todos los reportes', 'Acceso para visualizar todos los reportes del sistema'),
('Exportar datos', 'Permite exportar reportes a Excel/PDF'),
('Gestionar vehiculos', 'Permite registrar y administrar vehículos'),
('Gestionar clientes', 'Permite registrar y administrar clientes'),
('Administrar usuarios', 'Acceso completo de administración');

-- Employees table
CREATE TABLE Employees (
    id_employee INT AUTO_INCREMENT PRIMARY KEY,
    id_card VARCHAR(20) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL,
    name VARCHAR(25) NOT NULL,
    secondname VARCHAR(25) DEFAULT '',
    lastname VARCHAR(25) NOT NULL,
    secontlastname VARCHAR(25) DEFAULT '',
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    id_state INT NOT NULL DEFAULT 1,
    FOREIGN KEY (id_state) REFERENCES StatesEmployees(id_state)
);

-- EmployeeLicenses table (junction table)
CREATE TABLE EmployeeLicenses (
    id_employee_license INT AUTO_INCREMENT PRIMARY KEY,
    id_employee INT NOT NULL,
    id_license INT NOT NULL,
    granted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    granted_by INT NOT NULL,
    FOREIGN KEY (id_employee) REFERENCES Employees(id_employee),
    FOREIGN KEY (id_license) REFERENCES LicensesApps(id_license),
    FOREIGN KEY (granted_by) REFERENCES Employees(id_employee),
    UNIQUE KEY unique_employee_license (id_employee, id_license)
);

-- RefreshTokens table
CREATE TABLE RefreshTokens (
    id_refresh_token INT PRIMARY KEY,
    refresh_token VARCHAR(500) NOT NULL,
    expires_at DATETIME NOT NULL,
    revoked BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_refresh_token) REFERENCES Employees(id_employee)
);

-- Customer table
CREATE TABLE Customers (
    id_customer INT AUTO_INCREMENT PRIMARY KEY,
    tax_id VARCHAR(20),
    name VARCHAR(100)
);

-- Vehicle table
CREATE TABLE Vehicles (
    id_vehicle INT AUTO_INCREMENT PRIMARY KEY,
    license_plate VARCHAR(10) UNIQUE
);

-- Catalog table: Relationship
CREATE TABLE RelevantRelationships (
    id_relevant_relationship INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255)
);


-- Catalog table: LoadType
CREATE TABLE CargoTypes (
    id_cargo_type INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100)
);


-- Report table
CREATE TABLE Reports (
    id_report INT AUTO_INCREMENT PRIMARY KEY,
    report_date DATE,
    submission_date DATE,
    id_employee INT,
    id_customer INT,
    id_vehicle INT,
    id_relationship INT,
    id_load_type INT,
    FOREIGN KEY (id_employee) REFERENCES Employees(id_employee),
    FOREIGN KEY (id_customer) REFERENCES Customers(id_customer),
    FOREIGN KEY (id_vehicle) REFERENCES Vehicles(id_vehicle),
    FOREIGN KEY (id_relationship) REFERENCES RelevantRelationships(id_relevant_relationship),
    FOREIGN KEY (id_load_type) REFERENCES CargoTypes(id_cargo_type)
);

