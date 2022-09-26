## Basic Student rating api using fastApi and postgress

>As you can see, the plan is to use fast API to create a student rating API and store the data in a Postgres database, but installing Postgres in Linux is a pain, so I'll have to use something lighter, like Sqlite or SQL Alchemy and I forgot one thing the postgres driver "psycopg" I don't even know how to pronounce it also its unstable this project will be down for some time.

### postgres installation
```
sudo apt update
```
```
sudo apt install postgresql postgresql-contrib
```
```
sudo systemctl start postgresql.service
```
```
sudo -i -u postgres
```
```
psql
```
```
postgres=# /q
```
