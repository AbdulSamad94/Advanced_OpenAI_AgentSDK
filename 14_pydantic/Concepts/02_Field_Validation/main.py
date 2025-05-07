# from pydantic import BaseModel, Field  # type: ignore
# from typing import List, Dict, Optional


# class Cart(BaseModel):
#     user_id: int = Field(..., gt=0, description="User ID")
#     items: List[str]
#     quantities: Dict[str, int]


# class BlogPost(BaseModel):
#     title: str
#     content: str = Field(..., min_length=50, max_length=1000)
#     image_url: Optional[str] = None


# my_input = {
#     "title": "Agentic AI",
#     "content": "hello sjajhsgjsgjs jagjasgjsajgsjgasjhghjsjhsdgjsgjsgjsjgsjgjsjshjgsjgjsgjsgj",
#     "image_url": "http",
# }

# output = BlogPost(**my_input)
# print(output)

for i in range(10):
    print(i)
