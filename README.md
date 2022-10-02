
## Basic Student rating api using fastApi and postgress

>As you can see, the plan is to use fast API to create a student rating API and store the data in a Postgres database, but installing Postgres in Linux is a pain, so I'll have to use something lighter, like Sqlite or SQL Alchemy and I forgot one thing the postgres driver "psycopg" I don't even know how to pronounce it. also it's unstable this project will be down for some time.

## Step 1 — Installing PostgreSQL 
``` ```
## postgres installation


To install PostgreSQL, first refresh your server’s local package index:
```diff
+ sudo apt update
```
Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality:
```diff
+ sudo apt install postgresql postgresql-contrib
```
Ensure that the service is started:
```diff
+ sudo systemctl start postgresql.service
```
```diff
+ sudo -i -u postgres
```
```diff
+ psql
```
```diff
+ postgres=# /q
```
