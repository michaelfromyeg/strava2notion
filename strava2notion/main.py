from strava2notion.config import DATABASE_ID
from strava2notion.notion_api import upload_to_notion
from strava2notion.strava_api import get_activities

if __name__ == "__main__":
    parent = {"type": "database_id", "database_id": DATABASE_ID}

    activities = get_activities()
    for activity in activities:
        upload_to_notion(parent=parent, data=activity)
        print("Uploaded activity")
