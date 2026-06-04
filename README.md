# Real-Time Data Product Platform

![Data Pipeline CI](https://github.com/AliRizaKeless/realtime-data-product-platform/actions/workflows/data-pipeline-ci.yml/badge.svg)

## Overview

This project demonstrates a modern data engineering platform that delivers reliable, analytics-ready data products using a medallion architecture, dbt models, data quality tests, data contracts, and CI/CD validation.

The platform simulates a real-world scenario where data engineers are responsible not only for building pipelines, but also for delivering high-quality, well-modeled data that can be used for analytics and decision-making.

## Goals

- Build a production-style data platform
- Implement medallion architecture with Bronze, Silver, and Gold layers
- Implement data modeling using dbt
- Ensure data quality and reliability
- Validate datasets using data contracts
- Deliver business-ready data products

## Architecture

Architecture documentation is available in:

- docs/architecture.md

Architecture diagram:

![Architecture](docs/images/architecture.png)

### High-Level Components

- Data Sources (simulated order events)
- Bronze Layer (raw parquet data)
- Silver Layer (cleaned and validated data)
- Gold Layer (business-ready metrics)
- dbt Transformation Layer
- Data Contract Validation
- Data Quality Testing
- Airflow Orchestration
- PostgreSQL Metadata Database
- GitHub Actions CI/CD
- Dashboard Consumption Layer

## Tech Stack

- Python
- Pandas
- Faker
- PyArrow
- SQL
- DuckDB
- dbt
- Airflow
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions

## CI/CD

This project includes a GitHub Actions workflow that automatically validates the data pipeline on every push and pull request.

The CI pipeline:

- installs project dependencies
- runs the full data pipeline
- validates the data contract

A successful workflow run confirms that the pipeline is reproducible and reliable.

## Data Quality & Documentation

The project uses dbt for:

- Data modeling
- Data quality testing
- Documentation generation

Current validation coverage:

- Unique order IDs
- Non-null business fields
- Product-level aggregation checks

dbt documentation can be generated locally using:

```bash
cd ecommerce_analytics
dbt docs generate
dbt docs serve


PowerShell:

```powershell
notepad README.md

## Pipeline Orchestration

The platform is orchestrated using Apache Airflow.

Current DAG flow:

1. Generate Orders (Bronze)
2. Transform Orders (Silver)
3. Create Gold Metrics
4. Validate Data Contract

The DAG is executed through:

- Airflow Scheduler
- Airflow Webserver
- PostgreSQL metadata database

All services are containerized using Docker Compose.

## Dashboard Layer

Gold layer datasets can be exported to dashboard-ready CSV files.

Export command:

```bash
python pipelines/export_gold_to_csv.py

Supported consumers:

Power BI
Excel
Looker Studio

## Project Status

Current capabilities:

- End-to-End Data Pipeline
- Medallion Architecture
- Airflow Orchestration
- dbt Modeling
- Data Contracts
- Data Quality Tests
- CI/CD Validation
- Dashboard Export Layer

Planned:

- Power BI Dashboard
- Kafka Streaming
- Great Expectations
- Azure Deployment
- Terraform Infrastructure



