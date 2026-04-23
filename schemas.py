from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class AppUserAnalytics(BaseModel):
    id: int
    session_id: str
    action: str
    version: Optional[str]=None
    timestamp: Any
    user_agent: Optional[str]=None
    locale: Optional[str]=None
    location: Optional[str]=None
    referrer: Optional[str]=None
    pathname: Optional[str]=None
    href: Optional[str]=None
    created_at: Any


class ReadAppUserAnalytics(BaseModel):
    id: int
    session_id: str
    action: str
    version: Optional[str]=None
    timestamp: Any
    user_agent: Optional[str]=None
    locale: Optional[str]=None
    location: Optional[str]=None
    referrer: Optional[str]=None
    pathname: Optional[str]=None
    href: Optional[str]=None
    created_at: Any
    class Config:
        from_attributes = True


class Foods(BaseModel):
    id: int
    name: str
    calories_per_100g: float
    protein_per_100g: float
    carbs_per_100g: float
    fat_per_100g: float
    is_custom: int
    created_by_user_id: Optional[Union[int, float]]=None
    created_at: Optional[str]=None


class ReadFoods(BaseModel):
    id: int
    name: str
    calories_per_100g: float
    protein_per_100g: float
    carbs_per_100g: float
    fat_per_100g: float
    is_custom: int
    created_by_user_id: Optional[Union[int, float]]=None
    created_at: Optional[str]=None
    class Config:
        from_attributes = True


class MealLogs(BaseModel):
    id: int
    user_id: int
    food_id: int
    meal_type: str
    serving_grams: float
    calories_consumed: float
    protein_consumed: float
    carbs_consumed: float
    fat_consumed: float
    logged_date: str
    created_at: Optional[str]=None


class ReadMealLogs(BaseModel):
    id: int
    user_id: int
    food_id: int
    meal_type: str
    serving_grams: float
    calories_consumed: float
    protein_consumed: float
    carbs_consumed: float
    fat_consumed: float
    logged_date: str
    created_at: Optional[str]=None
    class Config:
        from_attributes = True


class Profiles(BaseModel):
    id: int
    user_id: int
    name: str
    age: Optional[Union[int, float]]=None
    weight_kg: Optional[float]=None
    height_cm: Optional[float]=None
    activity_level: str
    goal_type: str
    daily_calorie_goal: int
    onboarding_completed: int


class ReadProfiles(BaseModel):
    id: int
    user_id: int
    name: str
    age: Optional[Union[int, float]]=None
    weight_kg: Optional[float]=None
    height_cm: Optional[float]=None
    activity_level: str
    goal_type: str
    daily_calorie_goal: int
    onboarding_completed: int
    class Config:
        from_attributes = True


class Users(BaseModel):
    id: int
    email: str
    password: str
    created_at: Optional[str]=None


class ReadUsers(BaseModel):
    id: int
    email: str
    password: str
    created_at: Optional[str]=None
    class Config:
        from_attributes = True




class PostFoods(BaseModel):
    id: Union[int, float] = Field(...)
    name: str = Field(..., max_length=150)
    calories_per_100g: Any = Field(...)
    protein_per_100g: Any = Field(...)
    carbs_per_100g: Any = Field(...)
    fat_per_100g: Any = Field(...)
    is_custom: Union[int, float] = Field(...)
    created_by_user_id: Optional[Union[int, float]]=None
    created_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutFoodsId(BaseModel):
    id: Union[int, float] = Field(...)
    name: str = Field(..., max_length=150)
    calories_per_100g: Any = Field(...)
    protein_per_100g: Any = Field(...)
    carbs_per_100g: Any = Field(...)
    fat_per_100g: Any = Field(...)
    is_custom: Union[int, float] = Field(...)
    created_by_user_id: Optional[Union[int, float]]=None
    created_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostProfiles(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Union[int, float] = Field(...)
    name: str = Field(..., max_length=100)
    age: Optional[Union[int, float]]=None
    weight_kg: Optional[Any]=None
    height_cm: Optional[Any]=None
    activity_level: str = Field(..., max_length=20)
    goal_type: str = Field(..., max_length=20)
    daily_calorie_goal: Union[int, float] = Field(...)
    onboarding_completed: Union[int, float] = Field(...)

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostAppUserAnalytics(BaseModel):
    id: Union[int, float] = Field(...)
    session_id: str = Field(..., max_length=100)
    action: str = Field(..., max_length=100)
    version: Optional[str]=None
    timestamp: str = Field(..., max_length=100)
    user_agent: Optional[str]=None
    locale: Optional[str]=None
    location: Optional[str]=None
    referrer: Optional[str]=None
    pathname: Optional[str]=None
    href: Optional[str]=None
    created_at: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PutAppUserAnalyticsId(BaseModel):
    id: Union[int, float] = Field(...)
    session_id: str = Field(..., max_length=100)
    action: str = Field(..., max_length=100)
    version: Optional[str]=None
    timestamp: str = Field(..., max_length=100)
    user_agent: Optional[str]=None
    locale: Optional[str]=None
    location: Optional[str]=None
    referrer: Optional[str]=None
    pathname: Optional[str]=None
    href: Optional[str]=None
    created_at: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PutProfilesId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Union[int, float] = Field(...)
    name: str = Field(..., max_length=100)
    age: Optional[Union[int, float]]=None
    weight_kg: Optional[Any]=None
    height_cm: Optional[Any]=None
    activity_level: str = Field(..., max_length=20)
    goal_type: str = Field(..., max_length=20)
    daily_calorie_goal: Union[int, float] = Field(...)
    onboarding_completed: Union[int, float] = Field(...)

    class Config:
        from_attributes = True



class PostMealLogs(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Union[int, float] = Field(...)
    food_id: Union[int, float] = Field(...)
    meal_type: str = Field(..., max_length=20)
    serving_grams: Any = Field(...)
    calories_consumed: Any = Field(...)
    protein_consumed: Any = Field(...)
    carbs_consumed: Any = Field(...)
    fat_consumed: Any = Field(...)
    logged_date: str = Field(..., max_length=100)
    created_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutMealLogsId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Union[int, float] = Field(...)
    food_id: Union[int, float] = Field(...)
    meal_type: str = Field(..., max_length=20)
    serving_grams: Any = Field(...)
    calories_consumed: Any = Field(...)
    protein_consumed: Any = Field(...)
    carbs_consumed: Any = Field(...)
    fat_consumed: Any = Field(...)
    logged_date: str = Field(..., max_length=100)
    created_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: Union[int, float] = Field(...)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Union[int, float] = Field(...)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetFoodsIdQueryParams(BaseModel):
    """Query parameter validation for get_foods_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetProfilesIdQueryParams(BaseModel):
    """Query parameter validation for get_profiles_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteFoodsIdQueryParams(BaseModel):
    """Query parameter validation for delete_foods_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetAppUserAnalyticsIdQueryParams(BaseModel):
    """Query parameter validation for get_app_user_analytics_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteProfilesIdQueryParams(BaseModel):
    """Query parameter validation for delete_profiles_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteAppUserAnalyticsIdQueryParams(BaseModel):
    """Query parameter validation for delete_app_user_analytics_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetMealLogsIdQueryParams(BaseModel):
    """Query parameter validation for get_meal_logs_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteMealLogsIdQueryParams(BaseModel):
    """Query parameter validation for delete_meal_logs_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
