# nv world backend
written with django-rest framework
## initial setup
**server with backend url:** TODO
 
## database configuration

```bash
create user nv_user_db with password 'passwordQAZSWXDE';
alter role nv_user_db set client_encoding to 'utf8';
alter role nv_user_db set default_transaction_isolation to 'read committed';
alter role nv_user_db set timezone to 'UTC';
create database nv_world_db owner nv_user_db;
```


## TODO Elvira team info
here