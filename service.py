from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from agent.agent_setup import agent
from agent import agent_key

api = FastAPI()


class Query(BaseModel):
    key: str
    query: str


@api.post("/")
def research_agent(query: Query):
    if query.key != agent_key:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"message": "unauthorized"})
    return agent({"input": query.query})['output']
