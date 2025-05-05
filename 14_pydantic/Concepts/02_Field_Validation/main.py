from pydantic import BaseModel, Field  # type: ignore
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int = Field(..., gt=0, description="User ID")
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
