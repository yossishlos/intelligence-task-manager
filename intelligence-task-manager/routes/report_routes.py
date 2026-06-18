from fastapi import APIRouter, HTTPException
from database.agent_db import AgentDB
from database.mission_db import MissionDB
from database.db_connection import DB_connection

router = APIRouter(prefix="/reports")

db = DB_connection()

missions_repository = MissionDB(db)

# @router.get("/summary")
# def 


@router.get("/missions-by-status")
def missions_by_status():
    result = {}
    result["open"] = missions_repository.count_by_status("ASSIGNED")
    result["in_progress"] = missions_repository.count_by_status("IN_PROGRESS")
    result["completed"] = missions_repository.count_by_status("COMPLETED")
    result["failed"] = missions_repository.count_by_status("FAILED")
    result["CANCELLED"] = missions_repository.count_by_status("CANCELLED")
    return result


@router.get("/top-agent")
def get_top_agent():
    return missions_repository.get_top_agent()