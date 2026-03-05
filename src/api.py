from fastapi import FastAPI, Request, HTTPException
import uvicorn
from pydantic import BaseModel

# Exportable variable

application = FastAPI()

# API (status of bot)

@application.get("/")
def status(request: Request):
    bot = request.app.state.bot
    return {
        "Nome": bot.user.name,
        "ID": bot.user.id,
        "Servidores": f"{len(bot.guilds)}",
        "Usuários": f"{len(set(bot.get_all_members()))}",
        "Latência": f"{round(bot.latency * 1000)}ms"
    }