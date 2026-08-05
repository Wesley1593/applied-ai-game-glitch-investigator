import json
import os


def log_game(data):

    os.makedirs("logs", exist_ok=True)

    file = "logs/game_log.json"

    logs = []

    if os.path.exists(file):

        with open(file,"r") as f:
            logs=json.load(f)


    logs.append(data)


    with open(file,"w") as f:
        json.dump(logs,f,indent=4)