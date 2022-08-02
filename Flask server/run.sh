#!/bin/bash
nohup python3.8 run.py > _server_console.log &
echo "Run.py"
nohup python3.5 -u save_bitcoin_to_db.py > _bitcoin_db.log &
echo "save_bitcoin_to_db.py"
nohup python3.8 -u read_room_temp_and_humidity.py > _read_room_temp.log &
echo "read_room_temp_and_humidity.py"

echo "Run....."
pwd
