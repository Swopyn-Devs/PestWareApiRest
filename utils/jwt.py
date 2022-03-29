from datetime import timedelta

from decouple import config

expires = timedelta(hours=int(config('ACCESS_TOKEN_EXPIRE_HOURS')))
