# marketing_site/utils/jwt_token.py
import jwt
import datetime
from django.conf import settings

def generate_matching_key_token(user_id):
    payload = {
        "sub": str(user_id),
        "iat": int(datetime.datetime.utcnow().timestamp()),
    }
    return jwt.encode(payload, settings.MATCHING_KEY_SECRET, algorithm="HS256")
