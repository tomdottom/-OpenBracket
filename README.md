# OpenBracket

## Running dev server

*Install requirements*

```
pip install -r ./server/requirements.txt
pip install -r ./server/dev_requirements.txt  # Note that this installs supporting packages in editable mode
```

*Run the development server*

```
./server/run_dev_server.sh
```

## Loading mysql db

*create user*
```
mysql -u -p
> CREATE USER 'ob_census_user'@'%' IDENTIFIED BY 'ob_census_pass';
> GRANT ALL PRIVILEGES ON ob_census.* TO 'ob_census_user'@'%' IDENTIFIED BY 'ob_census_pass';
> create database ob_census;
> use ob_census;
> source ob_census.sql

```
