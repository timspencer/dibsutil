#!/usr/local/bin/python3

import argparse
import csv
import os
from datetime import datetime, timedelta

HEADERS = [
    "name", "description", "location", "location_url", "start_date_time",
    "end_date_time", "credit_value", "cancel_window", "all_day_event",
    "category", "fulfiller_phone_required", "fulfiller_email_required",
    "status", "athlete_name", "athlete_email", "fulfiller_name",
    "fulfiller_phone", "fulfiller_email", "cancel_requested",
    "complete_requested", "extra_credit"
]

# Examples:
# 18UAway Game Locker Room Monitor    SafeSport and background check required to fulfill this position. 45 min before and 30 min after.   Frontier Ice Arena      02/06/2027 09:45 AM 02/06/2027 12:15 PM 1.25    1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE
# 18UAway Game Locker Room Monitor    SafeSport and background check required to fulfill this position. 45 min before and 30 min after.   Frontier Ice Arena      02/06/2027 09:45 AM 02/06/2027 12:15 PM 1.25    1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE
# 18UAway Game Penalty Box    SafeSport and background check required to fulfill this position.   Frontier Ice Arena      02/06/2027 03:00 PM 02/06/2027 04:00 PM 1.0 1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE
# 18U Home Game Locker Room Monitor   SafeSport and background check required to fulfill this position.  45 min before and 30 min after.  Palouse Ice Rink        01/22/2027 05:40 PM 01/22/2027 08:05 PM 1.25    1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE
# 18U Home Game Penalty Box   SafeSport and background check required to fulfill this position.   Palouse Ice Rink        01/22/2027 06:25 PM 01/22/2027 07:35 PM 1.0 1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE
# 18U Home Game Scorekeeper   Must be able to write legibly.  Palouse Ice Rink        01/22/2027 06:25 PM 01/22/2027 07:35 PM 1.0 1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE
# 18U Home Game Clock/Scoreboard      Palouse Ice Rink        01/22/2027 06:25 PM 01/22/2027 07:35 PM 1.0 1   FALSE   18U FALSE   FALSE   unclaimed                       FALSE   FALSE   FALSE

EVENTS = {
    "practice": [
        {
            "count": 2,
            "name": "Practice Locker Room Monitor",
            "description": "SafeSport and background check required to fulfill this position. 45 min before and 30 min after.",
            "location": "Palouse Ice Rink",
            "location_url": "",
            "start_date_time": -45,
            "end_date_time": 90,
            "credit_value": 1.25,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        }
    ],
    "home_game": [
        {
            "count": 2,
            "name": "Home Game Locker Room Monitor",
            "description": "SafeSport and background check required to fulfill this position. 45 min before and 30 min after.",
            "location": "Palouse Ice Rink",
            "location_url": "",
            "start_date_time": -45,
            "end_date_time": 90,
            "credit_value": 1.25,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        },
        {
            "count": 1,
            "name": "Home Game Penalty Box",
            "description": "SafeSport and background check required to fulfill this position.",
            "location": "Palouse Ice Rink",
            "location_url": "",
            "start_date_time": 0,
            "end_date_time": 60,
            "credit_value": 1,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        },
        {
            "count": 1,
            "name": "Home Game Scorekeeper",
            "description": "Must be able to write legibly.",
            "location": "Palouse Ice Rink",
            "location_url": "",
            "start_date_time": 0,
            "end_date_time": 60,
            "credit_value": 1,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        },
        {
            "count": 1,
            "name": "Home Game Clock/Scoreboard",
            "description": "",
            "location": "Palouse Ice Rink",
            "location_url": "",
            "start_date_time": 0,
            "end_date_time": 60,
            "credit_value": 1,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        }
    ],
    "away_game": [
        {
            "count": 2,
            "name": "Away Game Locker Room Monitor",
            "description": "SafeSport and background check required to fulfill this position. 45 min before and 30 min after.",
            "location": "",
            "location_url": "",
            "start_date_time": -45,
            "end_date_time": 90,
            "credit_value": 1.25,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        },
        {
            "count": 1,
            "name": "Away Game Penalty Box",
            "description": "SafeSport and background check required to fulfill this position.",
            "location": "",
            "location_url": "",
            "start_date_time": 0,
            "end_date_time": 60,
            "credit_value": 1,
            "cancel_window": 1,
            "all_day_event": "FALSE",
            "category": "",
            "fulfiller_phone_required": "TRUE",
            "fulfiller_email_required": "TRUE",
            "status": "",
            "athlete_name": "",
            "athlete_email": "",
            "fulfiller_name": "",
            "fulfiller_phone": "",
            "fulfiller_email": "",
            "cancel_requested": "",
            "complete_requested": "",
            "extra_credit": ""
        }
    ]
}

types = list(EVENTS.keys())

def calculate_time(start_date, minute_offset):
    # 01/22/2027 06:25 PM
    parsed_time = datetime.strptime(start_date, "%m/%d/%Y %I:%M %p")
    newtime = parsed_time + timedelta(minutes=minute_offset)
    return newtime.strftime("%D %I:%M:%S %p")

def main():
    parser = argparse.ArgumentParser(description="Add an event row to an events CSV file.")
    
    # File option
    parser.add_argument("-o", "--output", default="events.csv", help="Output CSV filename (default: events.csv)")
    
    # Core event details (Required)
    parser.add_argument("--type", required=True, help="Type of the event:  " + ", ".join(types))
    parser.add_argument("--start", required=True, dest="start_date_time", help="Start date/time (e.g., 2026-12-01T09:00:00)")
    parser.add_argument("--category", required=True, help="Event category/type")
    
    # Optional event details with sensible defaults
    parser.add_argument("--prefix", default="", help="Prefix for every entry")
    parser.add_argument("--location", default="", help="Location name or address")
    parser.add_argument("--locationurl", default="", help="URL for location/map")
    parser.add_argument("--allday", dest="all_day_event", default="FALSE", choices=["TRUE", "FALSE"], help="Is all-day event (TRUE/FALSE)")
    
    args = parser.parse_args()
    
    # Check if file exists and is non-empty so we only write headers once
    file_exists = os.path.isfile(args.output) and os.path.getsize(args.output) > 0
    
    with open(args.output, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        if not file_exists:
            writer.writeheader()
        rows = []
        for i in EVENTS[args.type]:
            i["name"] = args.category + " " + i["name"]
            if args.prefix != "":
                i["name"] = args.prefix + " " + i["name"]
            i["start_date_time"] = calculate_time(args.start_date_time, i["start_date_time"])
            i["end_date_time"] = calculate_time(args.start_date_time, i["end_date_time"])
            i["category"] = args.category
            if args.location != "":
                i["location"] = args.location
            if args.locationurl != "":
                i["location_url"] = args.locationurl
            if args.all_day_event != "FALSE":
                i["all_day_event"] = args.all_day_event
            count = i.pop("count", None)
            for z in range(count):
                rows.append(i)
        writer.writerows(rows)
        
    # print(f"Added '{args.name}' ({args.category}) to {args.output}")

if __name__ == "__main__":
    main()

