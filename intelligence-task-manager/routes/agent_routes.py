from fastapi import APIRouter, HTTPException
from database.agent_db import AgentDB
from database.db_connection import DB_connection

router = APIRouter(prefix="/agents")

db = DB_connection()

agent_repository = AgentDB(db)

@router.post("")
def create_agent(data: dict):
    return agent_repository.create_agent(data)


@router.get("")
def get_all_agents():
    return agent_repository.get_all_agents()


@router.get("/{id}")
def get_agent_by_id(id: int):
    return agent_repository.get_agent_by_id(id)


@router.put("{id}")
def update_agent(id: int, data: dict):
    return agent_repository.update_agent(id, data)


@router.put("/{id}/deactivate")
def deactivate_agent(id: int):
    return agent_repository.deactivate_agent(id)


@router.get("/{id}/performance")
def get_agent_performance(id: int):
    return agent_repository.get_agent_performance(id)