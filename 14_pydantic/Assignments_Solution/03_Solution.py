from pydantic import BaseModel, Field, computed_field


class Booking_model(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., le=1, description="Number of nights")
    rate_per_night: float

    @computed_field
    @property
    def total(self) -> float:
        return self.nights * self.rate_per_night
