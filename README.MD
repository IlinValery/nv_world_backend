# NV WORLD backend project
Backend project of NVIDIA hack (02-04 oct 2020) 

Written with django-rest framework


## Initial setup
**Server with backend url:** *deleted*
 
Deployment path: /var/www/nv_world_backend

In *PyCharm* use sftp to connect and sync with server

Database dump and nginx configs in ```./data``` folder
### Database configuration
For project ```postgresql``` was used as database framework. To create user and database use following commands:
#### bash
```shell script
sudo -u postgres psql postgres
```
#### postgres
```postgresql
create user nv_user_db with password 'passwordQAZSWXDE';
alter role nv_user_db set client_encoding to 'utf8';
alter role nv_user_db set default_transaction_isolation to 'read committed';
alter role nv_user_db set timezone to 'UTC';
create database nv_world_db owner nv_user_db;
```
### Environment configuration

#### Initial 
```shell script
apt-get install git nginx python3 python3-pip python3-dev postgresql postgresql-contrib libpq-dev
sudo -u postgres psql postgres # use commands from database conf -> postgres

cd /var/www/
git clone https://github.com/IlinValery/nv_world_front
git clone https://github.com/IlinValery/nv_world_backend

# backend:
cd nv_world_backend/
pip3 install -r requirements.txt 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver

# frontend
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
apt-get install -y nodejs
npm install -g create-react-app
cd ../cd nv_world_front/
npm i
npm run build

# nginx
nano /etc/nginx/sites-available/default # insert from ./data/nginx-default.conf
nginx -t
service nginx restart
``` 

## Team
- Polina Ponomareva (polina.ponomareva@skoltech.ru)
- Liza Kiseleva (elizaveta.kiseleva@skoltech.ru)
- Mohamed Abbas (mohamed.abbas@skoltech.ru)
- Valery Ilin (valery.ilin@skoltech.ru)
- Elvira Zainulina (elvira.zainulina@skoltech.ru)

<p align="center">
<img src="https://old.sk.ru/resized-image.ashx/__size/550x0/__key/telligent-evolution-components-attachments/13-50-00-00-00-02-16-56/skoltech-rastr-ENG.png" height="40">
<img src="https://www.overclockers.ua/news/logo/118740-nvidia-logo-1.jpg" height="40">
</p>
