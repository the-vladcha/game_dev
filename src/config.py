import os

import yaml
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


def read_build_data():
    with open(os.environ['BUILDS_FILE_PATH']) as build_file:
        return dict([(item['name'], item['tasks']) for item in yaml.safe_load(build_file)['builds']])


def read_tasks_data():
    with open(os.environ['TASKS_FILE_PATH']) as tasks_file:
        return dict([(item['name'], item['dependencies']) for item in yaml.safe_load(tasks_file)['tasks']])


class Settings(BaseSettings):
    build_data: dict = read_build_data()
    tasks_data: dict = read_tasks_data()


settings = Settings()
