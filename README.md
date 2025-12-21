# AISAP Chatbot (Laravel–Python Integrated Web Application)

This project is a web application that integrates a **Laravel backend/frontend** with a **Python-based API**. Laravel handles the web interface and request flow, while Python runs the trained model and serves predictions through a dedicated API.

---

## Project Overview

* **Laravel** is used for the web interface, routing, controllers, and communication with the Python API.
* **Python** is used for loading the trained model and providing real-time prediction results via `api.py`.

The trained model files are already included in this repository, so **no model training is required** to run the application.

---

## About `code1.ipynb`

* `code1.ipynb` contains the **model training and generation process**.
* Running this notebook will generate the `model/` directory.
* Since the `model/` directory is **already included**, you do **not** need to run `code1.ipynb`.
* You can directly run the application using `api.py`.

---

## Prerequisites

Ensure the following are installed on your system:

* **Python 3.x**
* **PHP 8.x** (recommended)
* **Composer**

### Installation

Install the necessary Laravel dependencies by running:

```bash
composer install

```

---

## How to Run the Project

> [!IMPORTANT]
> Both servers must be running simultaneously for the application to function correctly.

### Step 1: Run the Python API

Open a terminal in the project root directory and run:

```bash
python api.py

```

This starts the Python API and loads the pre-generated model. **Keep this terminal running.**

### Step 2: Run the Laravel Server

Open a **new** terminal and run:

```bash
php artisan serve

```

The Laravel application will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Important Notes

* **Continuous Connection:** Do not close the Python API terminal while using the application.
* **Integration:** Laravel communicates with the Python API for all processing and prediction tasks.
* **Ready-to-Use:** No additional model setup or training is required.
