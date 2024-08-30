## Шаблоны CURL запросов

### Токены пользователей
```python
users_token = {
    'user1': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsImV4cCI6MTcyNTAxMTk4Nn0.33efkxUEFcN2dnfoZbgjHf4RnFCWizzsYgXi9kz2P94',
    'user2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMiIsImV4cCI6MTcyNTAxMjE3OH0.dS6zshb7P45SiYLLXa8WKjZnSRFqkSBto7vmoddkZBU',
    'user3': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMyIsImV4cCI6MTcyNTAxMjIwOH0.xhrahXaGXkB6C6aESv0YuSi-GmjK4-r2LPTmRbSHqYM',
    'user4': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyNCIsImV4cCI6MTcyNTAxMjIyNn0.OKB99vyxHD9UQJrTfx2-Ah_G5M9KzzlJdwi3yc808jc',
}
```

### Получить все заметки пользователя:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/note' -H 'accept: application/json' \
-H 'Authorization: Bearer {{ users.token }}'
```

#### Пример:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/note' -H 'accept: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsImV4cCI6MTcyNTAxMTk4Nn0.33efkxUEFcN2dnfoZbgjHf4RnFCWizzsYgXi9kz2P94'
```

### Создать заметку для пользователя:
```bash
curl -X 'POST' 'http://0.0.0.0:8000/note?title={{ title_note }}&description={{ description_note }}' -H 'accept: application/json' -d '' \
-H 'Authorization: Bearer {{ users.token }}'
 ```

#### Пример:
```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/note?title=Title&description=Description' -H 'accept: application/json' -d '' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyNCIsImV4cCI6MTcyNTAxMjIyNn0.OKB99vyxHD9UQJrTfx2-Ah_G5M9KzzlJdwi3yc808jc'
```