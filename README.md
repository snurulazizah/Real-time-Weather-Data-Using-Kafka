# Real-time-Weather-Data-Using-Kafka
Weather Realtime - Kafka Streaming 🌤️
Deskripsi
Weather Realtime adalah sistem streaming data cuaca real-time menggunakan Apache Kafka. Data cuaca diambil dari WeatherAPI dan dikirim ke Kafka melalui Kafka Producer, lalu dikonsumsi oleh Kafka Consumer yang menampilkan dan memvisualisasikan data secara langsung.

Fitur
✅ Kafka Producer mengumpulkan data cuaca dari WeatherAPI setiap 60 detik.
✅ Kafka Consumer membaca data cuaca dari topik weather-topic.
✅ Visualisasi real-time suhu menggunakan Matplotlib.
✅ Menangani error otomatis, seperti kegagalan koneksi atau data tidak valid.

Alur Kerja
Kafka Producer mengambil data cuaca dari WeatherAPI.
Data dikirim ke Kafka Broker dalam format JSON.
Kafka Consumer membaca data dari weather-topic.
Data ditampilkan dalam log dan divisualisasikan secara real-time.
Cara Menjalankan
1. Menjalankan Kafka
Pastikan Kafka sudah berjalan di localhost:

sh
Salin
Edit
kafka-server-start.sh config/server.properties
Buat topik weather-topic jika belum ada:

sh
Salin
Edit
kafka-topics.sh --create --topic weather-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
2. Menjalankan Kafka Producer
Pastikan Anda sudah memiliki API Key dari WeatherAPI.
Kemudian jalankan:

sh
Salin
Edit
python weather_producer.py
3. Menjalankan Kafka Consumer
Buka Jupyter Notebook dan jalankan Weather Kafka Consumer untuk melihat data real-time:

sh
Salin
Edit
jupyter notebook
