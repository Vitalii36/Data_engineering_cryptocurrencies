# Poloniex.com Data Engineering Project

## Motivation
The primary objective of this project was to gain a deeper understanding of 
data engineering concepts and tools. This was achieved through building an 
ETL data pipeline (API + apache airflow + PostgreSQL)

## Pipeline

Steps in the Data Pipeline:     
1.Python scripts retrieve data from poloniex.com via their API and save 
it to csv file.     
2.Python scripts then transform the data and then loads the data into a relational Postgres databas


<div align="center">
    <img align="center" src="https://github.com/Vitalii36//Data_engineering_cryptocurrencies/blob/master/img/Schema.png?raw=true">
</div> 

## How it work

data obtained from poloniex.com API (https://docs.poloniex.com/#returnticker) 
are stored in CSV format using the library pandas, then using sqlalchemy data 
is formed into various tables based on cryptocurrency and stored in the database
 PostgreSQL for use and analysis, in the example selected some of the most famous 
 cryptocurrencies, but this process can be expanded to a larger number. 
 Also in the work used to simulate accelerated work, but airflow can do this
  work at different intervals

<div align="center">
    <img align="center" src="https://github.com/Vitalii36//Data_engineering_cryptocurrencies/blob/master/img/img_3.png?raw=true">
    <>
    <img align="center" src="https://github.com/Vitalii36//Data_engineering_cryptocurrencies/blob/master/img/img_4.png?raw=true">
</div> 

The green boxes indicate a scheduled run of the pipeline and if the steps ran 
successfully. The black tooltip shows an example of Airflow running these steps 
for a specific date. I was able to succesfully backfill the data all for 45 cycles

## Resume
It’s convenience way to setting schedule and control everything with airflow.
 We can create any job that we want and schedule them. it powerful tools that 
 you should try once and it can applier with any task that you need to make sure
  it running so you can sleep all night long.
  
## Example visualization

<div align="center">
    <img align="center" src="https://github.com/Vitalii36//Data_engineering_cryptocurrencies/blob/master/img/Example1.png?raw=true">
</div> 
    
##License
Format is MIT
