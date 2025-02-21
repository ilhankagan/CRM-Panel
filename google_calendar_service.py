from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
SERVICE_ACCOUNT_FILE = "admin-api-451215-13db0160e668.json"


def get_events(start_date, end_date):
    """Belirtilen tarih aralığındaki etkinlikleri çeker"""
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=creds)

    calendar_id = "agpakilhan@gmail.com"

    # Tarihleri RFC3339 formatına dönüştürelim (Google Calendar API formatı)
    start_time = datetime.strptime(start_date, "%Y-%m-%d").isoformat() + "Z"
    end_time = datetime.strptime(end_date, "%Y-%m-%d").isoformat() + "Z"

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=start_time,
        timeMax=end_time,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    event_list = []
    for event in events:
        event_list.append({
            "summary": event.get("summary", "Bilinmeyen Etkinlik"),
            "start": event["start"].get("dateTime", "Zaman Bilinmiyor"),
            "organizer": event.get("organizer", {}).get("email", "Bilinmiyor"),
            "attendees": [att.get("email", "") for att in event.get("attendees", []) if "email" in att]
        })

    return event_list
