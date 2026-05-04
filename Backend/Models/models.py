# models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class StateEmployee(Base):
    __tablename__ = "StatesEmployees"
    
    id_state = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    
    # Relationships
    employees = relationship("Employee", back_populates="state")


class LicenseApp(Base):
    __tablename__ = "LicensesApps"
    
    id_license = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=True)
    
    # Relationships
    employee_licenses = relationship("EmployeeLicense", back_populates="license")


class Employee(Base):
    __tablename__ = "Employees"
    
    id_employee = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_card = Column(String(20), unique=True, nullable=False)
    position = Column(String(50), nullable=False)
    name = Column(String(25), nullable=False)
    secondname = Column(String(25), default="")
    lastname = Column(String(25), nullable=False)
    secontlastname = Column(String(25), default="")
    phone = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    id_state = Column(Integer, ForeignKey("StatesEmployees.id_state"), nullable=False, default=1)
    
    # Relationships
    state = relationship("StateEmployee", back_populates="employees")
    licenses = relationship("EmployeeLicense", back_populates="employee", foreign_keys="[EmployeeLicense.id_employee]")
    granted_licenses = relationship("EmployeeLicense", back_populates="granted_by_employee", foreign_keys="[EmployeeLicense.granted_by]")
    refresh_token = relationship("RefreshToken", back_populates="employee", uselist=False)


class EmployeeLicense(Base):
    __tablename__ = "EmployeeLicenses"
    
    id_employee_license = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_employee = Column(Integer, ForeignKey("Employees.id_employee"), nullable=False)
    id_license = Column(Integer, ForeignKey("LicensesApps.id_license"), nullable=False)
    granted_at = Column(DateTime, default=func.now())
    granted_by = Column(Integer, ForeignKey("Employees.id_employee"), nullable=False)
    
    # Relationships
    employee = relationship("Employee", back_populates="licenses", foreign_keys=[id_employee])
    license = relationship("LicenseApp", back_populates="employee_licenses")
    granted_by_employee = relationship("Employee", back_populates="granted_licenses", foreign_keys=[granted_by])
    
    __table_args__ = (
        UniqueConstraint('id_employee', 'id_license', name='unique_employee_license'),
    )


class RefreshToken(Base):
    __tablename__ = "RefreshTokens"
    
    id_refresh_token = Column(Integer, ForeignKey("Employees.id_employee"), primary_key=True)
    refresh_token = Column(String(500), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    revoked = Column(Boolean, default=False)
    
    # Relationships
    employee = relationship("Employee", back_populates="refresh_token")