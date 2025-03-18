from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.dependency import get_db
from models.user import User