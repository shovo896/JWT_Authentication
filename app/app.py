from app.model import PostSchema, UserSchema, UserLoginSchema
posts = [
       {
              "id": 1,
              "title": "This is a title",
              "email": "user@example.com"
       }
]

users = []


@app.get("/posts",tags=["Posts"]) 
async def get_posts() -> dict: 
       return {"data": posts} 

@app.post("/posts",tags=["Posts"]) 
async def add_post(post: PostSchema) -> dict:
       post_dict = post.dict() 
       posts.append(post_dict) 
       return {
              "data": "Post added."
       }
for post in posts:
       if post["id"] == post.id:
              return {
                     "data": "Post with this ID already exists."
              } 




@app.post("/posts",tags=["Posts"])
async def add_post(post: PostSchema) -> dict:
       post_dict = post.dict() 
       posts.append(post_dict) 
       return {
              "data": "Post added."
       }



