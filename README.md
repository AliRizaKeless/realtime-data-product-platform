\# Real-Time Data Product Platform



!\[Data Pipeline CI](https://github.com/AliRizaKeless/realtime-data-product-platform/actions/workflows/data-pipeline-ci.yml/badge.svg)



\## Overview

This project demonstrates a modern data engineering platform that combines batch and real-time data processing to deliver reliable, analytics-ready data products.



The platform simulates a real-world scenario where data engineers are responsible not only for building pipelines, but also for delivering high-quality, well-modeled data that can be used for analytics and decision-making.



\## Goals

\- Build a production-style data platform

\- Combine batch and streaming data pipelines

\- Implement data modeling using dbt

\- Ensure data quality and reliability

\- Deliver business-ready data products



\## Architecture



Architecture documentation is available in:



\- docs/architecture.md



Architecture diagram:



!\[Architecture](docs/images/architecture.png)



\### High-Level Components



\- Data Sources (simulated order events)

\- Bronze Layer (raw parquet data)

\- Silver Layer (cleaned and validated data)

\- Gold Layer (business-ready metrics)

\- dbt Transformation Layer

\- Data Contract Validation

\- Data Quality Testing

\- GitHub Actions CI/CD



\## Tech Stack (Planned)

\- Python

\- dbt

\- Airflow (or similar)

\- Kafka (for streaming)

\- Docker

\- SQL



\## CI/CD



This project includes a GitHub Actions workflow that automatically validates the data pipeline on every push and pull request.



The CI pipeline:

\- installs project dependencies

\- runs the full data pipeline

\- validates the data contract



A successful workflow run confirms that the pipeline is reproducible and reliable.



\## Project Status

&#x20;  In progress

