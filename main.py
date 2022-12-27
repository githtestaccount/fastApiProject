from fastapi import FastAPI
from enum import Enum

class Pet_moods(Enum):
    ANGRY = "angry"
    LONELY = "lonely"
    HUNGRY = "hungry"
    BORED = "bored"


class Pet_care_actions(Enum):
    CALM = "calm"
    PET = "pet"
    FEED = "feed"
    PLAY = "play"


care_log = []
mood = Pet_moods.ANGRY


app = FastAPI()

@app.get("/pet_id")
async def get_pet_id():
    return {"name": "waldi", "version": 0.1}


@app.get("/care_log")
async def get_care_log():
    return care_log


@app.get("/mood")
async def get_mood():
    return mood.value


@app.post("/manage_mood")
async def manage_mood(action: Pet_care_actions):
    care_log.append(action)
    global mood
    if (mood == Pet_moods.ANGRY) and (action == Pet_care_actions.CALM):
        mood = Pet_moods.LONELY
        return 0
    elif (mood == Pet_moods.LONELY) and (action == Pet_care_actions.PET):
        mood = Pet_moods.HUNGRY
        return 0
    elif (mood == Pet_moods.HUNGRY) and (action == Pet_care_actions.FEED):
        mood = Pet_moods.BORED
        return 0
    elif (mood == Pet_moods.BORED) and (action == Pet_care_actions.PLAY):
        mood = Pet_moods.ANGRY
        return 0
    else:
        mood = Pet_moods.ANGRY
        return 1


