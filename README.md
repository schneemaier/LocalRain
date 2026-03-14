# LocalRain
LocalRain is a local implementation of Melnor RainCloud service which will be discontinued in April 2026

# The original idea
Jean-Philippe for the basic idea and to get started
- https://hackaday.io/project/160193-raincloud-de-cloudifier

Two original implementations:
- https://github.com/FreshX-GmbH/melnor_decloudify
- https://github.com/jpjodoin/sunshower

The above working versions are incomplete as they only support 1 controller with 1 valve unit. The original factory setup
support 1 controller with 2 valve units and 2 controllers per user account.  The goal is to provide a system which can
support:
- multiple controllers
- 2 valve unit per controller
- scheduling
- manual control
- humidity sensor

# Requirements
The project requires DNS spoofing to direct the two urls, ws.pusherapp.com and wifiaquatimer.com to the server running
the service.

In my setup I use a Raspberry PI 1 with DNSMasq for DNS and DHCP server. I also use an old 100MB router as the device is 
not supporting higher speeds and this helps to isolate the setup from the rest of the network.  

# Protocol
The device uses simple HTTP and WS communication. In general the device send HTTP requests and the server sends messages
via WS. Most of the protocol reverse engineering was done by the 2 predecessor projects, this project built on that
original work, but corrected and added some missing pieces, like multiple valve unit support and identified bits and
pieces for other functions, like the humidity sensor. The protocol still has holes, but it is good enough to build
working software.
- [Protocol (WIP)](Protocol/Data.md)
- [Handshake (WIP)](Protocol/Handshake.md)

# Current status (March 2026)

The initial python code is completed and partially tested with 3 controller units. 
- settings to add controller units and program schedule
- initialize controllers based on the program schedule
- display status information on the console

**The code is not tested enough to use it for any production environment. If you use it I take no responsibility for any
problems!**

# Missing (TODO):
- web page to show status and enable control
- REST API for programing, manual control stb
- code cleanup
- humidity sensor implementation
- possible mqtt modul
- if nothing else left to do create Openhab and Home Assistant connection
- download the firmware from the controller unit and try to decode and find any additional functions (ex is there a
- function for firmware upgrade) 

# Running the code
- clone, download the repository
- create a python virtual environment
- install packages
- run main.py in the virtual environment

My installed python packages:
- aiohappyeyeballs 2.6.1
- aiohttp          3.13.3
- aiosignal        1.4.0
- attrs            25.4.0
- bidict           0.23.1
- frozenlist       1.8.0
- h11              0.16.0
- idna             3.11
- multidict        6.7.1
- pip              25.1.1
- propcache        0.4.1
- python-engineio  4.13.1
- python-socketio  5.16.1
- simple-websocket 1.1.0
- wsproto          1.3.2
- yarl             1.22.0

