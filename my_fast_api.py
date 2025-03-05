import uvicorn
from bot_instance import api  # FastAPI





if __name__ == "__main__":
    uvicorn.run("bot_instance:api", host="0.0.0.0", port=8000)