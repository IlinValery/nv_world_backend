# nv world backend
written with django-rest framework
## initial setup
**server with backend url:** TODO
 
 deployment path: /var/www/nv_world_backend
 use sftp to connect in pycharm
## database configuration

```bash
create user nv_user_db with password 'passwordQAZSWXDE';
alter role nv_user_db set client_encoding to 'utf8';
alter role nv_user_db set default_transaction_isolation to 'read committed';
alter role nv_user_db set timezone to 'UTC';
create database nv_world_db owner nv_user_db;
```


### Team
- Polina Ponomareva (polina.ponomareva@skoltech.ru)
- Liza Kiseleva (elizaveta.kiseleva@skoltech.ru)
- Mohamed Abbas (mohamed.abbas@skoltech.ru)
- Valery Ilin (valery.ilin@skoltech.ru)
- Elvira Zainulina (elvira.zainulina@skoltech.ru)

<p align="center">
<img src="https://old.sk.ru/resized-image.ashx/__size/550x0/__key/telligent-evolution-components-attachments/13-50-00-00-00-02-16-56/skoltech-rastr-ENG.png" height="40">
<img src="https://www.overclockers.ua/news/logo/118740-nvidia-logo-1.jpg" height="40">
</p>
