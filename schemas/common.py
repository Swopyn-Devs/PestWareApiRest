from pydantic import BaseModel


class MapS3UrlField(BaseModel):
    url: str
    name: str
