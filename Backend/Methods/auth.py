from dotenv import load_dotenv
load_dotenv()
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

from database import get_db
from Models.models import Employee
from Schemas.schemas import EmployeeCreate, EmployeeUpdate, EmployeeLogin, EmployeeResponse

SECRET_KEY = os.getenv("SECRET_KEY", "AppTalentHuman")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 15))


if SECRET_KEY is None or ALGORITHM is None:
    raise ValueError("SECRET_KEY y ALGORITHM deben definirse en el archivo .env")

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

router = APIRouter(prefix="/auth", tags=["autenticación"])

