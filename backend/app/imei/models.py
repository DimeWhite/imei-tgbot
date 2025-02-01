from pydantic import BaseModel


class IMEICheckModel(BaseModel):
    token: str
    imei_number: str
