# Sharer

# Запуск сервисов в docker
```
sudo docker-compose up -d 
```


# Для локальной разработки 
```
(поднимается только БД и Кэш):
sudo docker-compose up -d db cache

Бэкенд можно стартовать локально:
python src/app.py --host 0.0.0.0 --port 8080
```

# Env Variables
```
Копирование файла с примерами переменных окружения
cp .env.example .env

```


# Creating database structure
```
docker-compose exec backend python src/models/models.py
```



# Swagger Docs available on
```
http://0.0.0.0:8080/docs
```


