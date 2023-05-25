from config import settings


class TasksGenerator:
    # def __init__(self) -> None:
    #     self.build: dict = settings.build_data
    #     with open(TASKS_FILE_PATH) as tasks_file:
    #         self.tasks: dict = settings.tasks_data

    def _add_tasks(self, result: list, dependencies: list | None) -> None:
        if dependencies is None:
            raise
        for task in dependencies:
            if new_deps := settings.tasks_data[task]:
                self._add_tasks(result, new_deps)
            else:
                result.append(task)

    def get_tasks(self, build_name: str) -> list:
        result: list = []
        self._add_tasks(result, settings.build_data.get(build_name))
        return result
