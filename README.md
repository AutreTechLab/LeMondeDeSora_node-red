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

# Configure the python environment
## Approach
For our projects, we would like to be able to execute python scripts from node-red. After testing several options, we decided to go for  
`node-red-contrib-pythonshell`. It allows us to maintain and test the code outside of node-red, which gives the flexibility to keep the code within the node-red project or maintain it in separate git repositories. 
Input to the node will become the argument for the python script, output of the script will be sent to output of the node. 
## Creating a virtual environment 
The `node-red-contrib-pythonshell` requires the use of a virtual environment, which is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. Here is an example of how to create a virtual environment under the node-red project.
* `apt-get install python3-venv` (you need to install python3-venv when doing it for the first time)
* `cd ~/.node-red/projects/<your project>`
* `mkdir py-src` 
* `python3 -m venv .`
* `source ./bin/activate`
Now you can install all the modules needed for your project. 
