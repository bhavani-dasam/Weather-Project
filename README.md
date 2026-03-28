# 🌦️ Weather-Based Delivery Delay System

## 📌 Overview
This project checks weather conditions for different cities and updates order delivery status based on weather using the OpenWeatherMap API.

---

## 🚀 Features
- Parallel API calls using asyncio
- Detects bad weather conditions
- Updates order status to "Delayed"
- Generates personalized messages
- Handles invalid cities without crashing
- Uses .env for API key security

---

## 🛠️ Tech Stack
- Python
- aiohttp
- asyncio
- OpenWeatherMap API

---

## 📂 Project Files
- main.py → main logic
- orders.json → input data
- updated_orders.json → output data
- .env → API key

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install aiohttp python-dotenv 

2.Add API key in .env:
API_KEY=your_api_key_here

3.Run:
python main.py

#Output Example
{
  "order_id": "1002",
  "customer": "Bob Jones",
  "city": "Mumbai",
  "status": "Delayed",
  "message": "Hi Bob Jones, your order to Mumbai is delayed due to clouds."
}