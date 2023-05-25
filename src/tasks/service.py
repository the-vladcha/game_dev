from config import settings
from tasks.exceptions import NonExistentTask


class TasksGenerator:
    def __init__(self) -> None:
        self.stash: set = set()

    def _add_tasks(self, result: list, dependencies: list | None) -> None:
        if dependencies is None:
            raise NonExistentTask
        for task in dependencies:
            if new_deps := settings.tasks_data[task]:
                self._add_tasks(result, new_deps)
            else:
                if task not in self.stash:
                    result.append(task)
                    self.stash.add(task)

    def get_tasks(self, build_name: str) -> list:
        result: list = list()
        self._add_tasks(result, settings.build_data.get(build_name))
        return result
