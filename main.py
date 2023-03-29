import random
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
import scrapper
from extract import *
import os

SECRET = os.getenv("SECRET")

#
app = FastAPI()


class Msg(BaseModel):
    msg: str
    secret: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver = createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage


@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}


@app.get("/events/")
async def read_site(url: str):
    results = []
    if scrapper.check_all_textf(url):
        links = scrapper.get_all_links(url)
        results.append("yes its indian :" + url)
        for x in range(5):
            try:
                link = random.choice(links)
                print(link)
                if scrapper.check_all_textf(link):
                    results.append("yes its indian :" + link)
            except ValueError:
                try:
                    newLink = url + '/' + link
                except:
                    results.append("no its not indian :" + link)
    else:
        results.append("no its not indian :" + url)
    if scrapper.check_all_image(url):
        results.append("yes its good image")
    else:
        results.append("Not good image")
    return results
    # except ValueError:
    #     return "Some the values are wrong"


@app.get("/links/")
async def read_site(url: str):
    return scrapper.get_all_links(url)
