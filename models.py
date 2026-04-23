from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text as text_sql, Interval
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class AppUserAnalytics(Base):
    __tablename__ = "app_user_analytics"

    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    action = Column(String)
    version = Column(String, nullable=True)
    timestamp = Column(DateTime, server_default=text_sql("now()"))
    user_agent = Column(String, nullable=True)
    locale = Column(String, nullable=True)
    location = Column(String, nullable=True)
    referrer = Column(String, nullable=True)
    pathname = Column(String, nullable=True)
    href = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=text_sql("now()"))


class Foods(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories_per_100g = Column(Float)
    protein_per_100g = Column(Float)
    carbs_per_100g = Column(Float)
    fat_per_100g = Column(Float)
    is_custom = Column(Integer)
    created_by_user_id = Column(Integer, nullable=True)
    created_at = Column(String, nullable=True)


class MealLogs(Base):
    __tablename__ = "meal_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    food_id = Column(Integer)
    meal_type = Column(String)
    serving_grams = Column(Float)
    calories_consumed = Column(Float)
    protein_consumed = Column(Float)
    carbs_consumed = Column(Float)
    fat_consumed = Column(Float)
    logged_date = Column(String)
    created_at = Column(String, nullable=True)


class Profiles(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    age = Column(Integer, nullable=True)
    weight_kg = Column(Float, nullable=True)
    height_cm = Column(Float, nullable=True)
    activity_level = Column(String)
    goal_type = Column(String)
    daily_calorie_goal = Column(Integer)
    onboarding_completed = Column(Integer)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    created_at = Column(String, nullable=True)


