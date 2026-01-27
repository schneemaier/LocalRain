# LocalRain
LocalRain is a local implementation of Melnor RainCloud service with will be discontinued in 2026

# The original idea
Jean-Philippe for the basic idea and to get startet
- https://hackaday.io/project/160193-raincloud-de-cloudifier

Two implementations:
- https://github.com/FreshX-GmbH/melnor_decloudify
- https://github.com/jpjodoin/sunshower

The above working versions are incomplete as they only support 1 controller with 1 valce unit. The oringa setup support 1 controller with 2 valce units and multiple controllers per user account.  The goal is to provide a system which can support:
- multiple controllers
- 2 valve unit per controller
- scheduling
- humidity senor

# Requirements
The project requires DNS sppofing to direct the two urls, ws.pusherapp.com and wifiaquatimer.com to the server running the service
#TODO:
- write code :)
