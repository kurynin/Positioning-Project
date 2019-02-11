# Positioning Project

### Требования
1. Python 3.5
2. Django 2.1.5

### Запуск
При первом запуске или после обновления нужно пересобрать статики и при
необходимости обновить структуру базы данных, а также пересобрать бинарь,
который отвечает за обработку файлов, если это нужно:
```bash
python src/dj_back/manage.py collectstatic
python src/dj_back/manage.py migrate
cd rc/dj_back/get_data_form/data_process/bin
g++ blackbox.cpp -o blackbox.exe
cd -
```

Также при первом запуске нужно создать суперпользователя, с
помощью него можно будет залогиниться:
```bash
python src/dj_back/manage.py createsuperuser
```
 
Теперь нужно запустить сам сервер:
```bash
python src/dj_back/manage.py runserver
```

После этого сервер должен быть доступен по
адресу <http://127.0.0.1:8000/>.

На данный момент проверялось только на линуксе.

### Админка
Админка находится по адресу <http://127.0.0.1:8000/admin> (нужен суперпользователь).
Из неё можно посмотреть на базу данных. На данный момент интересны таблицы:

Table name | Description
--- | ---
Users | Сюда складываются зарегестрированные пользователи
Submissions | Сюда складываются записи о посылках файлов
Results | Сюда складываются результаты обработки файлов

### Результаты
После отправки файла в `media/playground` должна появится новая папка, в которой
через 1-7 секунд после создания появятся результаты.
