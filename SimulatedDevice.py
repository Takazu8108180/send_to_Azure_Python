# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

import csv
import numpy as np

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=SIDA-Input.azure-devices.net;DeviceId=SIDA-RFIDdevice;SharedAccessKey=Wz4tIgJAGpddB76TmN6TMkQ/eRV9UTENu8johqDkA+A="

# Define the JSON message to send to IoT Hub.
#TEMPERATURE = 20.0
#HUMIDITY = 60
#MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

pressure_or_not = 0
difference_of_pressuredata = 0
std_fronttag = 0
std_outtag = 0
std_intag = 0
MSG_TXT = '{{"pressure_or_not": {pressure_or_not},"difference_of_pressuredata": {difference_of_pressuredata},"std_fronttag": {std_fronttag},"std_outtag": {std_outtag},"std_intag": {std_intag}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        with open('C:\\Users\\koich\\OneDrive\\デスクトップ\\ASNsampledata.csv', 'r',encoding="utf-8") as f: 
          reader = csv.reader(f)
          for row in reader:
              # Build the message with simulated telemetry values.
              #temperature = TEMPERATURE + (random.random() * 15)
              #humidity = HUMIDITY + (random.random() * 20)
              #msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
              #message = Message(msg_txt_formatted)
              pressure_or_not = row[0]
              difference_of_pressuredata = row[1]
              std_fronttag = row[2]
              std_outtag = row[3]
              std_intag = row[4]
              msg_txt_formatted = MSG_TXT.format(pressure_or_not=pressure_or_not, difference_of_pressuredata=difference_of_pressuredata, std_fronttag=std_fronttag, std_outtag=std_outtag, std_intag=std_intag)
              message = Message(msg_txt_formatted)

              # Add a custom application property to the message.
              # An IoT hub can filter on these properties without access to the message body.
              #if temperature > 30:
              #  message.custom_properties["temperatureAlert"] = "true"
              #else:
              #  message.custom_properties["temperatureAlert"] = "false"

              # Send the message.
              print( "Sending message: {}".format(message) )
              client.send_message(message)
              print ( "Message successfully sent" )
              print ( "-" * 50 )
              time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()