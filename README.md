
Тестовое задание для hands.ru

---

Для получения номеров в нужном формате достаточно вызвать метод ``` resolve_and_format(adress, path)```, где

<br> ```adress``` - ссылка на сайт компании
<br>``` path ```- список, содержащий все пути до страниц с контактами на сайте компании

---

Пример использования:
```
resolve_and_format('https://hands.ru/', ['company/about', 'contact-us/'])
```
В случае, если index страница содержит контакты:
```
resolve_and_format('https://repetitors.info/', [''])
```

---
Для установки зависимостей:
```
pip3 install -r requirements.txt
```
