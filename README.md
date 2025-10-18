# 🚀 Real-Time Stock Market Data Pipeline  

### 🧰 Tech Stack  
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

---

## 📘 Project Overview  

This project demonstrates a **real-time data pipeline** using the **Modern Data Stack** to stream and analyze live stock market data.  
It captures real-time prices from an external API, processes and streams them using Kafka, orchestrates ETL workflows with Airflow, performs transformations in Snowflake via DBT, and finally visualizes insights in Power BI.  

The result is a fully automated, end-to-end system for **streaming analytics** — scalable, modular, and cloud-ready.  

---

## 🏗️ Architecture  

*(Insert architecture diagram here)*  

A modern, containerized architecture designed to process streaming data in real time and deliver analytics-ready datasets to business intelligence tools.  

---

## ⚡ Tools & Technologies  

- **Snowflake** → Cloud data warehouse for secure and scalable analytics  
- **DBT** → SQL-based transformation and modeling framework  
- **Apache Airflow** → Orchestrates data workflows and schedules tasks  
- **Apache Kafka** → Handles real-time streaming and data transport  
- **Python** → Fetches and processes live market data from APIs  
- **Docker** → Containerizes all services for easy deployment  
- **Power BI** → Builds real-time visual dashboards for analytics  

---

## 🌟 Key Features  

- Pulls **live stock market data** directly from an external API  
- Implements a **real-time Kafka streaming pipeline**  
- Automates ingestion, transformation, and loading via **Airflow DAGs**  
- Uses **DBT** for modular SQL transformations in Snowflake  
- **Dockerized setup** for consistent, reproducible environments  
- **Power BI** dashboards displaying KPIs and candlestick metrics  

---

## 📁 Recommended Repository Structure  

