# LeMondeDeSora_node-red
Le Monde de Sora Minecraft Roleplay Server - Node-Red automations


# Installation:
## Install nodejs and node-red 
* `sudo apt update`
* `sudo apt install nodejs`
* `sudo apt install npm`
* `sudo npm install -g --unsafe-perm node-red`

## Install local mosquitto broker 
### About mosquitto
Eclipse Mosquitto is an open source message broker that implements the MQTT protocol.  

The MQTT protocol provides a lightweight method of carrying out messaging using a publish/subscribe model. This makes it suitable for Internet of Things messaging such as with low power sensors or mobile devices such as phones, embedded computers or microcontrollers.

This will implement a local mqtt-broker for the node-red flows. After installtion, you should see the following log information at node-red startup: 
` [info] [mqtt-broker:localhost] Connected to broker: mqtt://localhost:1883`

### Installation steps on ubuntu 20.04

* `sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa`
* `sudo apt-get update`
* `sudo apt-get install mosquitto`
* `sudo apt-get install mosquitto-clients`
* `sudo apt clean`
