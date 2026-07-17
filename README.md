# Multi Model AI Translator


AI-powered subtitle translation system using multiple translation engines.


<img width="1913" height="857" alt="image" src="https://github.com/user-attachments/assets/cac94e4a-a338-443c-b2f7-b6e16c062475" />



## Features

- Upload SRT subtitle files
- Stream translation results
- Multiple translation models
- LLM based translation
- Transformer based translation


## Architecture


Client
 |
Flask API
 |
Translation Service
 |
-----------------
|               |
LLM          mBART
Model        Model


## Tech Stack

Python
Flask
Transformers
Docker
REST API
SSE Streaming


## Run locally

pip install -r requirements.txt

python run.py


## Run with Docker

docker compose up --build

