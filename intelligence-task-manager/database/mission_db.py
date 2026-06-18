from database.db_connection import DB_connection

class MissionDB:
    def __init__(self, db: DB_connection):
        self.db = db
        self.db.get_connection()


    def create_mission(self, data: dict):
        try:
            self.db.cursor.execute("""
insert into missions (title, description, location, difficulty, importance) values (%s, %s, %s, %s, %s)
""", (data["title"], data["description"], data["location"], data["difficulty"], data["importance"]))
            self.db.connection.commit()
            self.db.cursor.execute("""
select * from missions where title = %s
""", (data["title"],))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    
    def get_all_missions(self):
        try:
            self.db.cursor.execute("""
select * from missions
""")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def get_mission_by_id(self, id: int):
        try:
            self.db.cursor.execute("""
select * from missions where id = %s
""", (id,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    

    def assign_mission(self, m_id: int, a_id: int):
        try:
            self.db.cursor.execute("""
update missions set assigned_agent_id = %s where id = %s
""", (a_id, m_id))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)

    
    def update_mission_status(self, id: int, status):
        try:
            self.db.cursor.execute("""
update missions set status = %s where id = %s
""", (status, id))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)

    
    def get_open_missions_by_agent(self, id: int):
        try:
            self.db.cursor.execute("""
select * from missions where status = ASSIGNED or status = IN_PROGRESS and id = %s
""", (id,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    
    def count_all_missions(self):
        try:
            self.db.cursor.execute("""
select count(*) from missions
""")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    

    def count_by_status(self, status):
        try:
            self.db.cursor.execute("""
select count(*) from missions where status = %s
""", (status,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    

    def count_open_missions(self):
        try:
            self.db.cursor.execute("""
select count(*) from missions group by status
""")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    
    def count_critical_missions(self):
        try:
            self.db.cursor.execute("""
select count(*) from missions where status = CRITICAL
""")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    

    def get_top_agent(self):
        try:
            self.db.cursor.execute("""
select max(completed_missions) from agents
""")
            the_max = self.db.cursor.fetchall()
            
            self.db.cursor.execute("""
select * from missions where completed_missions = %s
""",(the_max,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)