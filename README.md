
Тестовое задание для hands.ru

---

Для получения номеров в нужном формате достаточно вызвать метод ``` resolve_and_format(adress, path)```, где

<br> ```adress``` - ссылка на сайт компании
<br>``` path ```- список, содержащий все пути до страниц с контактами на сайте компании

---

Пример испоьзования:
```
resolve_and_format('https://hands.ru/', ['company/about', 'contact-us/'])
```

---
Для установки зависимостей:
```
pip3 install -r requirements.txt
```