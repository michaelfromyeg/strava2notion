from stravaio import strava_oauth2
from stravaio import StravaIO

from strava2notion.config import CLIENT_ID, CLIENT_SECRET, ALL_DATA
from strava2notion.notion_api import most_recent_activity_date

def get_activities():
    """
    Fetch the user's Strava activities.
    """
    token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    client = StravaIO(access_token=token["access_token"])

    print("Logged into Strava!")

    if ALL_DATA:
        after_date = 0
    else:
        after_date = most_recent_activity_date()

    activities = client.get_logged_in_athlete_activities(after=after_date)
    print("Activities fetched")
    return activities
