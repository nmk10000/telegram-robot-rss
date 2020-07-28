import os
import json


def main():
    """
    Creates a config file using docker environment variables
    """

    # Create Config
    telegram_bot_token = os.environ["1002212360:AAEkhO8Ju7inwVlK7xK34Bq514q2wtZXfZY"]
    update_interval = os.environ["300"]

    config = {}
    config["telegram_token"] = telegram_bot_token
    config["update_interval"] = update_interval

    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filepath = os.path.join(base_path, "resources/credentials.json")

    with open(filepath, 'w+') as outfile:
        json.dump(config, outfile)


if __name__ == '__main__':
    main()
