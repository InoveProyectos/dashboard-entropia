# dashboard_iot

{"Velocidad": 10, "Altura": 30, "Paracaidas": true}

mosquitto_pub -h 69.46.4.131 -u brego -P mqttiot -t sensores/esp32 -m '{"Velocidad": 10, "Altura": 30, "Paracaidas": true}'
