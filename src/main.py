from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List, Optional
import datetime


app = FastAPI(title="Blog API")


blogs = []


#pydantic Base Model
class BlogList(BaseModel):
    id          : int
    title       : str
    content     : str
    created_at  : str = datetime.datetime.now()
    status      : Optional[bool] = False


#root endpoint
@app.get('/', status_code = status.HTTP_200_OK)
async def root():
    return {"home": "Home Page"}


'''
    Get All Blog posts from blogs List
'''
@app.get('/get_blogs', status_code = status.HTTP_200_OK)
async def get_blogs():
    return {'payload': blogs}


'''
    Create a new blog post
'''
@app.post('/new_blog', status_code = status.HTTP_201_CREATED)
async def add_blog(blog: BlogList):
    blogs.append(blog)
    return {'message': "Blog was added.", 'payload': blog}


'''
    Get a specific blog post using blog_id
'''
@app.get('/blog/{blog_id}/', status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int):
    try:
        blog = blogs[blog_id-1]
        return blog
    except:
        return {'error': "Invalid Blog ID"}


'''
    Update Blog Post
'''
@app.put('/update_blog/{blog_id}/', status_code = status.HTTP_201_CREATED)
async def update_blog(blog_id: int, blog: BlogList):
    try:
        blogs[blog_id] = blog
        return {"message": "Blog ID was updated!", "payload": blog}

    except:
        return {'error': "Invalid Blog ID"}


'''
    Delete Blog Post
'''
@app.delete('/delete/{blog_id}/', status_code = status.HTTP_200_OK)
async def delete_blog(blog_id: int):
    try:
        blogs.pop(blog_id - 1)
        return {"message": "blog was deleted."}

    except:
        return {"error": "Invalid BlogID."}
