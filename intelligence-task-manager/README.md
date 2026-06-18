# Intelligence Task Manager

---

## 1. תיאור המערכת

המערכת מאפשרת למשתמש לנהל משימות וסוכנים על ידי פעולות כמו הוספת והסרת משימות והוספת והסרת סוכנים, שיוך משימה לסוכן הגדרות הצלחה למשימה, קבלת נתוני סוכן ונתוני משימה.

## 2. מבנה התקיות

```
intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 3. מבנה הטבלאות

### טבלת agent
```
שדה                        סוג                     הערות

מזהה ייחודי     INT, AUTO_INCREMENT, PK               id

שם הסוכן                    VARCHAR                  name

תחום התמחות                 VARCHAR             specialty

TRUE :מחדל ברירת            BOOLEAN             is_active

0 :מחדל ברירת                  INT      completed_missions

0 :מחדל ברירת                  INT         failed_missions

בלבד Junior / Senior / Commander ENUM / VARCHAR agent_rank
```

### טבלת missions
```
שדה                                                         סוג                         הערות

מזהה ייחודי                    INT, AUTO_INCREMENT,PK                                          id

כותרת המשימה                                  varchar                                        title

תיאור מפורט                                      TEXT                                  description

מיקום                                          VARCHAR                                     location

בלבד 10–1                                         INT                                    difficulty

בלבד 10–1                                         INT                                    importance

NEW :מחדל ברירת                               VARCHAR                                        status

מחושב אוטומטית — לא מגיע מהמשתמש             VARCHAR                                    level_risk

שיוך עד NULL                                      INT                              assigned_agent_id
```
## 4. הסבר על מחלקות ה-DB

### AgentDB

---

agent_create: 
יוצרת סוכן חדש ומחזירה את האובייקט של הסוכן

agents_all_get: 
מחזירה רשימת כל הסוכנים

get_agent_by_id: 
None או ,ID לפי אחד סוכן מחזירה

update_agent: 
)id לשנות אפשרות אין )השורה לכל UPDATE

agent_deactivate: 
מגדירה מצב סוכן ללא פעיל

completed_increment: 
מעדכן את כמות המשימות שהושלמו

failed_increment: 
מעדכן את כמות המשימות שנכשלו

get_agent_performance: 
completed, failed, total, האלו המפתחות עם מילון מחזירה
success_rate
)שימו לב לחשב את הערך הזה rate_success - כמה באחוזים משימות
הסתיימו בהצלחה מתוך הסך הכולל(

agents_active_count: 
מחזירה את מספר הסוכנים הפעילים

### MissionDB

---

mission_create: 
יצירת משימה חדשה ומחזירה את כל האובייקט

missions_all_get: 
מחזירה את כל המשימות

get_mission_by_id: 
None או ,ID לפי אחת משימה מחזיר

assign_mission: 
סוכן משימה משייכת

update_mission_status: 
סטטוס שינוי לכל משמשת

get_open_missions_by_agent: 
סוכן של ASSIGNED/IN_PROGRESS משימות מחזירה

missions_all_count: 
סה"כ משימות

status_by_count: 
סופרת לפי סטטוס מסוים

missions_open_count: 
סופרת משימות פתוחות

count_critical_missions: 
CRITICAL משימות סופרת

get_top_agent: 
ביותר הגבוה completed_missions עם הסוכן

### connection_db

---

connection_get(): 
מחזירה חיבור פעיל ל-MySQ

database_create(): 
יוצרת את db_Intelligence אם לא קיים

tables_create(): 
יוצרת את שתי הטבלאות אם לא קיימות

## 5. חוקי המערכת
```
1. rank חייב להיות Commander / Senior / Junior — כל ערך אחר זורק שגיאה.

2. difficulty ו-importance חייבים להיות בין 1 ל10- — אחרת שגיאה.

3. level_risk מחושב אוטומטית בעת יצירת משימה — המשתמש לא שולח אותו.

4. סוכן עם False=active_is לא יכול לקבל משימות.

5. סוכן לא יכול להחזיק יותר מ3- משימות פתוחות )PROGRESS_IN / ASSIGNED )במקביל.

6. אם CRITICAL=level_risk — רק סוכן בדרגת Commander יכול לקבל את המשימה.

7. ניתן לשייך רק משימה בסטטוס NEW. לאחר שיוך: ASSIGNED=status.

8. ניתן להתחיל רק משימה בסטטוס ASSIGNED. לאחר: PROGRESS_IN=status.

9. ניתן לסיים רק משימה. PROGRESS_IN ולשנות לסטטוס completed or failed

10. ניתן לבטל רק משימה בסטטוס NEW או ASSIGNED — אחרת שגיאה
```
## 6. הוראות הרצה

מריצים את הפקודה הזאת:
```
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0
```

# עדכון README — חלק יום ב׳

## 7. רשימת Endpoints

### agents
```
post /agents
get /agents
get /agents/{id}
put /agents/{id}
put /agents/{id}/deactivate
get /agents/{id}/performance
```
### missions
```
post /missions
get /missions
get /missions/{id}
put /missions/{id}/assign/{agent_id}
put /missions/{id}/start
put /missions/{id}/complete
put /missions/{id}/fail
put /missions/{id}/cancel
```
### reports
```
get /reports/summary
get /reports/missions-by-status
get /reports/top-agent
```
## 8. זרימת המערכת
```
admin
    agents
        agent_create
        agents_all_get
        get_agent_by_id
        update_agent
        agent_deactivate
        completed_increment
        failed_increment
        get_agent_performance
        agents_active_count
    missions
        mission_create
        missions_all_get
        get_mission_by_id
        assign_mission
        update_mission_status
        get_open_missions_by_agent
        missions_all_count
        status_by_count
        missions_open_count
        count_critical_missions
    reports
        get_general_system_report
        get_missions_by_status
        get_top_agent
```
## 9. הוראות הרצה מעודכן

### 1.
לעשות clone: 
```
https://github.com/yossishlos/intelligence-task-manager.git
```
### 2.
להריץ פקודת docker run:
```
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0
```
### 3.
להתקין את מה שיש בrequirements
### 4.
כדי להפעיל את השרת צריך לכתוב את פקודת:
```
uvicorn main:app --reload
```