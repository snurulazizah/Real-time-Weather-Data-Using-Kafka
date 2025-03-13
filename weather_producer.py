from confluent_kafka import Producer
import json
import requests
import time

# Konfigurasi Kafka producer
KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092",
    "client.id": "weather-producer"
}

producer = Producer(KAFKA_CONFIG)
TOPIC = 'weather-topic'
INTERVAL = 60  # Mengirim data setiap 60 detik

# API Key WeatherAPI (gantilah dengan API key Anda)
API_KEY = "9dfe6ed2e18a484083c53754251303"
LOCATION = "Jakarta"  # Lokasi yang akan diambil datanya

# Fungsi untuk mengambil data cuaca dari WeatherAPI
def fetch_weather_data():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}"
    response = requests.get(url)
    data = response.json()
    
    return {
        "Datetime": time.strftime('%Y-%m-%d %H:%M:%S'),
        "Location": data["location"]["name"],
        "Temperature": data["current"]["temp_c"],
        "Condition": data["current"]["condition"]["text"],
        "Humidity": data["current"]["humidity"],
        "Wind Speed": data["current"]["wind_kph"]
    }

# Fungsi untuk mengirim data ke Kafka
def send_to_kafka(data):
    message = json.dumps(data).encode('utf-8')
    producer.produce(topic=TOPIC, value=message, callback=on_send_success)
    producer.flush()

# Callback untuk mencetak status pengiriman
def on_send_success(err, msg):
    if err:
        print(f"Error: {err}")
    else:
        print(f"Message sent: {msg.value().decode('utf-8')}")

# Main Loop untuk mengirim data ke Kafka
while True:
    weather_data = fetch_weather_data()
    send_to_kafka(weather_data)
    time.sleep(INTERVAL)
