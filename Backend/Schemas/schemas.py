# schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


# ---------- StateEmployee Schemas ----------
class StateEmployeeBase(BaseModel):
    title: str

class StateEmployeeCreate(StateEmployeeBase):
    pass

class StateEmployeeResponse(StateEmployeeBase):
    id_state: int
    
    class Config:
        from_attributes = True


# ---------- LicenseApp Schemas ----------
class LicenseAppBase(BaseModel):
    title: str
    description: Optional[str] = None

class LicenseAppCreate(LicenseAppBase):
    pass

class LicenseAppResponse(LicenseAppBase):
    id_license: int
    
    class Config:
        from_attributes = True


# ---------- Employee Schemas ----------
class EmployeeBase(BaseModel):
    id_card: str
    position: str
    name: str
    secondname: Optional[str] = ""
    lastname: str
    secontlastname: Optional[str] = ""
    phone: str
    email: EmailStr
    id_state: int = 1

class EmployeeCreate(EmployeeBase):
    password: str

class EmployeeUpdate(BaseModel):
    id_card: Optional[str] = None
    position: Optional[str] = None
    name: Optional[str] = None
    secondname: Optional[str] = None
    lastname: Optional[str] = None
    secontlastname: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    id_state: Optional[int] = None

class EmployeeLogin(BaseModel):
    email: EmailStr
    password: str

class EmployeeResponse(EmployeeBase):
    id_employee: int
    state: Optional[StateEmployeeResponse] = None
    licenses: Optional[List['EmployeeLicenseResponse']] = None
    
    class Config:
        from_attributes = True


# ---------- EmployeeLicense Schemas ----------
class EmployeeLicenseBase(BaseModel):
    id_employee: int
    id_license: int
    granted_by: int

class EmployeeLicenseCreate(EmployeeLicenseBase):
    pass

class EmployeeLicenseResponse(EmployeeLicenseBase):
    id_employee_license: int
    granted_at: datetime
    license: Optional[LicenseAppResponse] = None
    
    class Config:
        from_attributes = True


# ---------- RefreshToken Schemas ----------
class RefreshTokenBase(BaseModel):
    refresh_token: str
    expires_at: datetime

class RefreshTokenCreate(RefreshTokenBase):
    id_refresh_token: int

class RefreshTokenResponse(RefreshTokenBase):
    id_refresh_token: int
    revoked: bool
    
    class Config:
        from_attributes = True


# ---------- Auth Schemas ----------
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenRefresh(BaseModel):
    refresh_token: str


# Update forward references
EmployeeResponse.model_rebuild()