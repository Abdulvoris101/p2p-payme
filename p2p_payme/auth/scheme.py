from pydantic import BaseModel, Field


class Device(BaseModel):
    id: str = Field(..., alias="_id")
    key: str

    @classmethod
    def from_response(cls, response: dict) -> 'Device':
        return cls.parse_obj(response.get('result'))

