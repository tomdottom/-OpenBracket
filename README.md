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
> grant all privileges on ob_census.* to ob_census_user* identified by 'ob_census_pass';
> create database ob_census;
> use ob_census;
> source ob_census.sql

```
