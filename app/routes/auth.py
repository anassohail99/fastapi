"""Authenticated Routes."""

from fastapi import APIRouter, Depends
from app.schemas.auth import AuthResponse, UserToken
from app.auth.middleware import verify_firebase_token


router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.get('/me', response_model=AuthResponse)
async def get_current_user(user: UserToken = Depends(verify_firebase_token)):
    """Get current authenticated user information."""
    return AuthResponse(message="User authenticated successfully", user=user)
