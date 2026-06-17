from db_connection import DB_connection

class AgentDB:
    def __init__(self, db: DB_connection):
        self.db = db
        self.db.get_connection()


    def create_agent(self, data: dict):
        try:
            self.db.cursor.execute("""
INSERT INTO agents (name, specialty, is_active, agent_rank) VALUES (%s, %s, %s, %s)
""", (data["name"], data["specialty"], data["is_active"], data["agent_rank"]))
            self.db.connection.commit()
            self.db.cursor.execute("""
select * from agents where name = %s
""", (data["name"],))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def get_all_agents(self):
        try:
            self.db.cursor.execute("""
select * from agents
""")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    
    def get_agent_by_id(self, id: int):
        try:
            self.db.cursor.execute("""
select * from agents where id = %s
""", (id,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    

    def update_agent(self, id: int, data: dict):
        try:
            self.db.cursor.execute("""
update agents set name = %s, specialty = %s, is_active = %s, agent_rank = %s where id = %s
""", (data["name"], data["specialty"], data["is_active"], data["agent_rank"], id))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)
    

    def deactivate_agent(self, id):
        try:
            self.db.cursor.execute("""
update agents set is_active = False where id = %s
""",(id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)

    
    def increment_completed(self, id):
        try:
            self.db.cursor.execute("""
update agents set completed_missions = completed_missions + 1 where id = %s
""", (id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)
        
    
    def increment_failed(self, id):
        try:
            self.db.cursor.execute("""
update agents set failed_missions = failed_missions + 1 where id = %s
""", (id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)

    
    def get_agent_performance(self, id):
        try:
            self.db.cursor.execute("""
select completed_missions, failed_missions, from agents where id = %s
""", (id,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def count_active_agents(self):
        try:
            self.db.cursor.execute("""
select
""")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)













db = DB_connection()

adb = AgentDB(db)

data = {"name" : "yossi", "specialty" : "a", "is_active" : False, "agent_rank" : "Commander"}
update_data = {"name" : "shoshi", "specialty" : "b", "is_active" : True, "agent_rank" : "Senior"}
print(adb.create_agent(data=data))
print(adb.get_all_agents())
print(adb.get_agent_by_id(14))
print(adb.update_agent(id=13, data=update_data))