from fastapi import APIRouter, HTTPException
from database.mission_db import MissionDB
from database.db_connection import DB_connection

router = APIRouter(prefix="/missions")

db = DB_connection()

missions_repository = MissionDB(db)

@router.post("")
def create_mission(data: dict):
    return missions_repository.create_mission(data)


@router.get("")
def get_all_missions():
    return missions_repository.get_all_missions()


@router.get("/{id}")
def get_mission_by_id(id: int):
    return missions_repository.get_mission_by_id(id)


@router.put("/{id}/assign/{agent_id}")
def assign_mission(m_id: int, a_id: int):
    return missions_repository.assign_mission(m_id, a_id)


@router.put("/{id}/start")
def update_mission_status(id: int, status):
    return missions_repository.update_mission_status(id, status)


@router.put("/{id}/complete")
def update_mission_complete(id: int):
    return missions_repository.update_mission_status(id, "COMPLETED")


@router.put("/{id}/fail")
def update_mission_fail(id: int):
    return missions_repository.update_mission_status(id, "FAILED")


@router.put("/{id}/cancel")
def update_mission_cancel(id: int):
    return missions_repository.update_mission_status(id, "CANCELLED")