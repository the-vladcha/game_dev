###Запуск сервиса с помощью docker-compose:
из корня проекта вызвать команду
```
docker-compose up
```

###Проверка сервиса:
c помощью Postman или другим способом вызвать POST ```http://127.0.0.1:8500/tasks/get_tasks/``` запрос с телом, например:
```
{'build': 'voice_central'}
```

пример запроса с помощью ```python``` и библиотеки ```requests```:
```
import requests

req = requests.post('http://127.0.0.1:8500/tasks/get_tasks/', json={'build': 'voice_central'})
print(req.json())
```