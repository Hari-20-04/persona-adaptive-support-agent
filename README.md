# Persona Adaptive Support Agent

## Overview

Persona Adaptive Support Agent is an AI-powered customer support system that combines Persona Classification, Retrieval-Augmented Generation (RAG), Adaptive Responses, and Escalation Management.

The system retrieves relevant information from a knowledge base, identifies the user's persona, and generates tailored responses using Google Gemini.

## Features

* Persona Classification

  * Technical Expert
  * Frustrated User
  * Business Executive

* Retrieval-Augmented Generation (RAG)

  * ChromaDB
  * HuggingFace Embeddings
  * LangChain

* Adaptive Response Generation

* Escalation Workflow

  * Refund requests
  * Unauthorized charges
  * Fraud-related issues

* Streamlit User Interface

## Knowledge Base

The system uses support documents including:

* password_reset.txt
* billing_policy.txt
* refund_policy.txt
* api_authentication.txt
* account_locked.txt
* subscription_upgrade.txt
* subscription_cancel.txt
* payment_failed.txt
* email_verification.txt
* login_troubleshooting.txt

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Google Gemini API

## Project Structure

persona-support-agent/
├── app.py
├── data/
├── src/
├── requirements.txt
├── README.md
└── .gitignore

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

python -m streamlit run app.py

## Sample Queries

* My API authentication token is not working
* I am frustrated because I cannot log in
* How does subscription upgrade affect billing?
* I need a refund for an unauthorized charge
