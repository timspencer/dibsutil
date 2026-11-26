#!/bin/sh
# 18U HOUSE/C TOURNAMENT
# DECEMBER 11-13th, 2026

rm events.csv
./dibs.py --type home_tournament_game       --start "12/11/2026 08:00 AM" --category 18U
./dibs.py --type home_tournament_game       --start "12/11/2026 09:15 AM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/11/2026 10:30 AM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/11/2026 11:45 AM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/11/2026 01:00 PM" --category 18U
./dibs.py --type home_tournament_game       --start "12/11/2026 04:15 PM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/11/2026 05:30 PM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/11/2026 06:45 PM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/11/2026 08:00 PM" --category 18U

./dibs.py --type home_tournament_game       --start "12/12/2026 06:00 AM" --category 18U
./dibs.py --type home_tournament_game       --start "12/12/2026 07:15 AM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/12/2026 08:30 AM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/12/2026 09:45 AM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/12/2026 03:15 PM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/12/2026 04:30 PM" --category 18U
./dibs.py --type home_tournament_game       --start "12/12/2026 05:45 PM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/12/2026 07:00 PM" --category 18U
./dibs.py --type home_tournament_otherteams --start "12/12/2026 08:15 PM" --category 18U

./dibs.py --type home_tournament_game --start "12/13/2026 06:00 AM" --category 18U
./dibs.py --type home_tournament_game --start "12/13/2026 07:15 AM" --category 18U
./dibs.py --type home_tournament_game --start "12/13/2026 08:30 AM" --category 18U
./dibs.py --type home_tournament_game --start "12/13/2026 09:45 AM" --category 18U
./dibs.py --type home_tournament_game --start "12/13/2026 11:00 AM" --category 18U
./dibs.py --type home_tournament_game --start "12/13/2026 12:15 PM" --category 18U

