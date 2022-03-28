from fastapi.routing import APIRoute
from fastapi import Request
from utils import jwt


class VerifyToken(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token(request: Request):
            token = request.headers['Authorization'].split(' ')[1]
            validation_response = jwt.validate_token(token)
            if validation_response is None:
                return await original_route(request)
            else:
                return validation_response



