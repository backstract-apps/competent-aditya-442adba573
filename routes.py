from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal
from middleware.application_middleware import platform_auth_platform_auth_middleware_group_dependency, default_dependency


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/foods/')
async def get_foods(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_foods(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/foods/id/')
async def get_foods_id(request: Request, query: schemas.GetFoodsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_foods_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/foods/')
async def post_foods(request: Request, raw_data: schemas.PostFoods, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_foods(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/foods/id/')
async def put_foods_id(request: Request, raw_data: schemas.PutFoodsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_foods_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_users(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(request: Request, query: schemas.GetUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profiles/')
async def get_profiles(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_profiles(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profiles/id/')
async def get_profiles_id(request: Request, query: schemas.GetProfilesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_profiles_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profiles/')
async def post_profiles(request: Request, raw_data: schemas.PostProfiles, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_profiles(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/meal_logs/')
async def get_meal_logs(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_meal_logs(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/platform_auth_package/mayson/auth/user/login')
async def post_platform_auth_package_mayson_auth_user_login(request: Request, raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserLogin, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_platform_auth_package_mayson_auth_user_login(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/login/google')
async def get_platform_auth_package_mayson_sso_auth_login_google(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_login_google(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/foods/id/')
async def delete_foods_id(request: Request, query: schemas.DeleteFoodsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_foods_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/app_user_analytics/')
async def get_app_user_analytics(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_app_user_analytics(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/app_user_analytics/id/')
async def get_app_user_analytics_id(request: Request, query: schemas.GetAppUserAnalyticsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_app_user_analytics_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/app_user_analytics/')
async def post_app_user_analytics(request: Request, raw_data: schemas.PostAppUserAnalytics, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_app_user_analytics(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/app_user_analytics/id/')
async def put_app_user_analytics_id(request: Request, raw_data: schemas.PutAppUserAnalyticsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_app_user_analytics_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/profiles/id/')
async def put_profiles_id(request: Request, raw_data: schemas.PutProfilesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_profiles_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/profiles/id/')
async def delete_profiles_id(request: Request, query: schemas.DeleteProfilesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_profiles_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/app_user_analytics/id/')
async def delete_app_user_analytics_id(request: Request, query: schemas.DeleteAppUserAnalyticsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_app_user_analytics_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/meal_logs/id/')
async def get_meal_logs_id(request: Request, query: schemas.GetMealLogsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_meal_logs_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/meal_logs/')
async def post_meal_logs(request: Request, raw_data: schemas.PostMealLogs, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_meal_logs(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/meal_logs/id/')
async def put_meal_logs_id(request: Request, raw_data: schemas.PutMealLogsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_meal_logs_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/meal_logs/id/')
async def delete_meal_logs_id(request: Request, query: schemas.DeleteMealLogsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_meal_logs_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(request: Request, raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_users(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(request: Request, raw_data: schemas.PutUsersId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.put_users_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(request: Request, query: schemas.DeleteUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.delete_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/callback/')
async def get_platform_auth_package_mayson_sso_auth_callback(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_callback(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/platform_auth_package/mayson/auth/user/register')
async def post_platform_auth_package_mayson_auth_user_register(request: Request, raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserRegister, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.post_platform_auth_package_mayson_auth_user_register(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/me')
async def get_platform_auth_package_mayson_sso_auth_me(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency)):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_me(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

