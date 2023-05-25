class NonExistentTask(Exception):
    def __str__(self):
        return 'Несуществующая задача'
