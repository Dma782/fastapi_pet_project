from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str | None = None
    model_config = ConfigDict(from_attributes=True)


class STaskUpdate(BaseModel):
    id: int
    name: str
    description: str | None = None
    model_config = ConfigDict(from_attributes=True)


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
