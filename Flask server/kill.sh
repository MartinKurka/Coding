#!/bin/bash
pkill -f run.py
pkill -f save_bitcoin_to_db.py
pkill -f read_room_temp_and_humidity.py
echo "Killed all processes"
