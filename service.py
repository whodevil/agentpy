from fastapi import FastAPI
from pydantic import BaseModel

from agent.agent_setup import agent

api = FastAPI()


class Query(BaseModel):
    query: str


@api.post("/")
def research_agent(query: Query):
    return agent({"input": query.query})['output']
