from services.user_services import create_user
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from services.user_services import CreateUserSchema
from models.user import User
from storage import db
from random import randint

SESSIONS = {}

async def request_token(session: AsyncSession, user: CreateUserSchema):
    random_number = randint(0, 6000)
    user.reset_token = random_number
    await session.commit()
    await session.refresh(user)
    return user.reset_token

async def user_reset_token(session: AsyncSession, user: CreateUserSchema):
    user.reset_token = False

  
async def register_user(session: AsyncSession,  user_data):
    existing_user = await db.get_by_email(session, User, user_data.email)
    if existing_user:
        return("User already exists!!")
    user = await create_user(session, user_data)
    print(user)
    token = await request_token(session, user)
    return{f"Token for verification {token}, please verify via link: http://localhost:8000/verify/{token}"}


async def verify_user(session: AsyncSession, token):
    user_token = await db.verify(session, User, token)
    if not user_token:
        return{"status": "failed",
               "message": "Incorrect token"}
    return("status: success",
           "message: User successfully registered!!")


async def login_user(session: AsyncSession, email: EmailStr, password: str):
    user = await db.get_by_email(session, User, email)
    if not user or user.password != password:
        return("Invalid credentials")
    
    token = await request_token(session, user)
    SESSIONS[token] = user.id
    await user_reset_token(session, user)
    return {
        "status": "success",
        "user": user.username
    }









# # Register New User --> Post Request
# # Verfiy Email
# # Login User with User/Email and Password
# # Request Token
# # Reset Password ---> 
# """
# Request Token -->

# 1. Request user's email
# 2. Check if it is in the database
# 3. Generate a token
# 4. Update User's reset token with the generated (Token)
# 5. Send a message (Reset Token)
# """

# """
# Request Password -->

# 1. Get a token from the user
# 2. Get User by Token
# 3. Update the user object with the new password
# 4. Set token back to empty string
# """