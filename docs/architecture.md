\# Architecture



\## Overview



This project follows a medallion architecture pattern:



\- Bronze: raw generated order data

\- Silver: cleaned and standardized order data

\- Gold: business-ready product sales metrics



\## Data Flow



1\. `generate\_orders.py` creates raw order data.

2\. `transform\_orders.py` cleans and standardizes the data.

3\. `create\_gold\_layer.py` creates aggregated business metrics.

4\. `validate\_orders\_contract.py` validates the silver dataset against the data contract.

5\. GitHub Actions runs the pipeline automatically on every push and pull request.



\## Key Engineering Concepts



\- Medallion architecture

\- Data contracts

\- Data quality testing with dbt

\- CI/CD validation

\- Reproducible pipelines

