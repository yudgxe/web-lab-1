# web-lab-1
1) Примеры создания папок
 * http://127.0.0.1:8000/create/?dirname=home/
 * http://127.0.0.1:8000/home/create/?dirname=project/
 * http://127.0.0.1:8000/home/project/create/?dirname=init/

2) Примеры перхода между папок
 * http://127.0.0.1:8000/home/
 * http://127.0.0.1:8000/home/project/
 * http://127.0.0.1:8000/home/project/init/

3) Загрузка фалов на сервер
 * http://127.0.0.1:8000/home/upload/
 * http://127.0.0.1:8000/home/project/upload/
 * http://127.0.0.1:8000/home/project/init/upload/

4) Скачивание файлов с сервера
 * http://127.0.0.1:8000/home/download/?filename=file/
 * http://127.0.0.1:8000/home/project/download/?filename=file/
 * http://127.0.0.1:8000/home/project/init/download/?filename=file/

5 ) Удаление папок
 * http://127.0.0.1:8000/home/project/delete/?dirname=init/
 * http://127.0.0.1:8000/home/delete/?dirname=project/
 * http://127.0.0.1:8000/delete/?dirname=home/


