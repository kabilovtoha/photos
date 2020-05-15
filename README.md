##  Как развернуть проект
```sh
pipenv shell
pipenv install

npm install 

# for development
npm run dev

python3 manage.py collectstatic
python3 manage.py runserver

```
#### Стартовые данные:
##### Пользователи:
В приложенном проекте в sqlite-базе уже есть
 три пользователя с логинами/паролями admin:admin, user1:user1, user2:user2
##### Прочие данные:
Так же в проекте уже есть приложение geo с моделью City () базе этот справочник заполнен  тысячей городов) и 
моделью Photo с несколькими записями

------------------------
### Примеры вызовов API
### API examples
######  /api/v1/ 
- Корневой зарос к API, возвращает список дочерних запросов

###### /api/v1/photos/
read only
- список фото
- list of photos
