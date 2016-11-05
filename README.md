# OpenBracket - Open Source Targeting Solution

A working version of this project can be found at http://census.delawareagenda.com/

The first **"Population"** map requests population data from online the US Census data, enhances it with geo-json features and sends it to the front end site for display.

Generalization of this code could display many more of the data sets available from the US Census.

The second **"Worker Flow"** map uses our own processed data from the census and calculates worker flows from home residence to place of work.

![Population Density Heatmap](https://raw.githubusercontent.com/OpenBracketDelaware/Open-Source-Target-Marketing-Solution-Group3/master/readme_images/population_heatmap.png "Population Density Heatmap")

![Worker Flow Heatmap](https://raw.githubusercontent.com/OpenBracketDelaware/Open-Source-Target-Marketing-Solution-Group3/master/readme_images/worker_flow__heatmap.png "Worker Flow Heatmap")

# Dev Notes

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
