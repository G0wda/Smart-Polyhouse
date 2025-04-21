import network
import socket
import json
import machine
import dht
import time

# WiFi Credentials
SSID = "NetVoid"
PASSWORD = ""

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    pass

print("Connected to WiFi:", wifi.ifconfig())

# Sensor Pin Configurations
soil_moisture = machine.ADC(0)  # Soil moisture sensor on A0
dht_sensor = dht.DHT11(machine.Pin(14))  # DHT sensor on GPIO2 (D4)

# NPK Analog Inputs
n_pin = machine.Pin(5, machine.Pin.IN)  # Nitrogen on GPIO5 (D1)
p_pin = machine.Pin(4, machine.Pin.IN)  # Phosphorus on GPIO4 (D2)
k_pin = machine.Pin(0, machine.Pin.IN)  # Potassium on GPIO0 (D3)

# Start HTTP Server
server_socket = socket.socket()
server_socket.bind(('', 80))
server_socket.listen(2)

def get_sensor_data():
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
    except Exception as e:
        print("Failed to read DHT sensor:", e)
        temp, humidity = None, None

    # Read Soil Moisture (convert to %)
    moisture_value = soil_moisture.read()
    soil_moisture_percent = int((1023 - moisture_value) / 1023 * 100)

    # Read NPK Sensor (simulated values for now)
    nitrogen = n_pin.value() * 100  # Simulated scale
    phosphorus = p_pin.value() * 100
    potassium = k_pin.value() * 100

    return {
        "temperature": temp,
        "humidity": humidity,
        "soil_moisture": soil_moisture_percent,
        "npk": {"nitrogen": nitrogen, "phosphorus": phosphorus, "potassium": potassium}
    }

while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024)

    if b"GET /data" in request:
        sensor_data = get_sensor_data()
        response = json.dumps(sensor_data)
        
        # HTTP Response with CORS enabled
        http_response = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: application/json\n"
            "Access-Control-Allow-Origin: *\n\n"
            + response
        )
        
        conn.send(http_response)

    conn.close()
 
