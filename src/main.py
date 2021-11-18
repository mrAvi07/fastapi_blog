from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List, Optional
import datetime

app = FastAPI()

blogs = []


class BlogList(BaseModel):
    id : int
    title : str
    content : str
    created_at : str = datetime.datetime.now()
    status : Optional[bool] = False


@app.get('/', status_code = status.HTTP_200_OK)
async def root():
    return {"home": "Home Page"}


@app.get('/get_blogs', status_code = status.HTTP_200_OK)
async def get_blogs():
    return {'payload': blogs}


@app.post('/new_blog', status_code = status.HTTP_201_CREATED)
async def add_blog(blog: BlogList):
    blogs.append(blog)
    return {'message': "Blog was added.", 'payload': blog}


@app.get('/update_blog/{blog_id}/', status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int):
    try:
        blog = blogs[blog_id-1]
        return blog
    except:
        return {'error': "Invalid Blog ID"}


@app.put('update_blog/{blog_id}/', status_code = status.HTTP_201_CREATED)
async def update_blog(blog_id: int, blog: BlogList):
    try:
        prev_blog = blogs[blog_id-1]
        blogs[prev_blog] = blog
        return {"message": "Blog ID was updated!", "payload": blog}

    except:
        return {'error': "Invalid Blog ID"}