from pydantic import BaseModel

class WbsDataBase(BaseModel):
    value: str
    item: int

class wbsData(WbsDataBase):
    class Config():
        from_attributes = True