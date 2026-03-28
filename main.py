import asyncio 
import aiohttp 
import json 
import os 
from dotenv import load_dotenv 

load_dotenv()
API_KEY = os.getenv("API_KEY")

DELAY_CONDITION=["Rain","Snow","Extreme"]


def generate_message(customer, city, condition):
    if condition == "Rain":
        return f"Hi {customer}, your order to {city} is delayed due to heavy rain. Thanks for your patience!"
    elif condition == "Snow":
        return f"Hi {customer}, snowfall in {city} is causing delays. We’re working to deliver soon!"
    elif condition == "Extreme":
        return f"Hi {customer}, severe weather in {city} has impacted delivery timelines. We appreciate your understanding."
    else:
        return f"Hi {customer}, your order to {city} is slightly delayed. Thank you for your patience!"
async def fetch_weather(session, order):
    city= order["city"] 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"       

    try:
        async with session.get(url) as response:
            data = await response.json()
            
            if response.status != 200:
                print(f"Error for city :{city}")
                return order 

            weather_condition = data["weather"][0]["main"]
            if weather_condition != "Clear":
                order["status"] = "Delayed"  
                order["message"] = generate_message(order["customer"], city, weather_condition)
            return order 

    except Exception as e:
        print(f"Error fetching weather for {city}: {e}")
        return order 

async def main():
    with open("orders.json","r") as f:
        orders = json.load(f) 
    async with aiohttp.ClientSession() as session: 
        tasks = [fetch_weather(session, order) for order in orders]
        updated_orders = await asyncio.gather(*tasks)  

    with open("updated_orders.json","w") as f: 
        json.dump(updated_orders,f,indent=2)  

    print("Updated orders saved to updated_orders.json")                       

if __name__ == "__main__":
    asyncio.run(main())
