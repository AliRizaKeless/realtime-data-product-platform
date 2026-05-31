\# Real-Time Data Product Platform



\## Overview

This project demonstrates a modern data engineering platform that combines batch and real-time data processing to deliver reliable, analytics-ready data products.



The platform simulates a real-world scenario where data engineers are responsible not only for building pipelines, but also for delivering high-quality, well-modeled data that can be used for analytics and decision-making.



\## Goals

\- Build a production-style data platform

\- Combine batch and streaming data pipelines

\- Implement data modeling using dbt

\- Ensure data quality and reliability

\- Deliver business-ready data products



\## Architecture (High-Level)

\- Data Sources (API, simulated events)

\- Ingestion Layer (Batch + Streaming)

\- Data Lake (Bronze / Silver / Gold)

\- Transformation Layer (dbt)

\- Data Quality \& Testing

\- Data Product (Analytics / Dashboard)



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

