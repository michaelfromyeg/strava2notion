"""
Feel free to experiment with the Notion API here.
"""

from notion_client import Client
from strava2notion.config import TOKEN_V3, DATABASE_ID

notion = Client(auth=TOKEN_V3)

parent = {"type": "database_id", "database_id": DATABASE_ID}

properties = {
    "Name": {
        "type": "title",
        "title": [{"type": "text", "text": {"content": "testmac"}}],
    },
    "Type": {"type": "select", "select": {"name": "Run"}},
    "Length": {"type": "number", "number": 1.49},
    "Time": {"type": "number", "number": 1.49},
    "Date": {"type": "date", "date": {"start": "2021-05-11"}},
    "Strava Link": {
        "type": "url",
        "url": "https://www.strava.com/activities/7776467252",
    },
}

notion.pages.create(parent=parent, properties=properties)
