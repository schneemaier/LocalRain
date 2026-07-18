import json
import os
import logging
from datetime import datetime

class valveSettings:
    def __init__(self, valveSettings_path='valveSettings.json', scheduleSettings_path='scheduleSettings.json'):
        self.controllerMac = []
        self.valveUnits = {}
        self.schedule = {}
        self.sensor = {}
        self.raindelay = {}
        self.loadConf(valveSettings_path, scheduleSettings_path)

    def loadConf(self, valveSettings_path='valveSettings.json', scheduleSettings_path='scheduleSettings.json'):
        if os.path.exists(valveSettings_path):
            with (open(valveSettings_path, 'r') as f):
                vs = json.load(f)
                for data in vs.get('data'):
                    self.controllerMac.append(data.get('controllerMac'))
                    self.valveUnits[data.get('controllerMac')] = data.get('valveUnits')
        if os.path.exists(scheduleSettings_path):
            with ((open(scheduleSettings_path, 'r')) as f):
                ss = json.load(f)
                for data in ss.get('data'):
                    vUnit = data.get('valveUnit')
                    scheduleDay = {}
                    valve1sensor = data.get('valve1sensor',0)
                    valve2sensor = data.get('valve2sensor',0)
                    valve3sensor = data.get('valve3sensor',0)
                    valve4sensor = data.get('valve4sensor',0)
                    self.sensor[vUnit] = [valve1sensor, valve2sensor, valve3sensor, valve4sensor]
                    valve1raindelay = datetime.fromisoformat(data.get('valve1raindelay','1970-01-01'))
                    valve2raindelay = datetime.fromisoformat(data.get('valve2raindelay', '1970-01-01'))
                    valve3raindelay = datetime.fromisoformat(data.get('valve3raindelay', '1970-01-01'))
                    valve4raindelay = datetime.fromisoformat(data.get('valve4raindelay', '1970-01-01'))
                    self.raindelay[vUnit] = [valve1raindelay, valve2raindelay, valve3raindelay, valve4raindelay]
                    for day in data.get('schedule'):
                        d = day["day"]
                        valve1 = day["valve1"]
                        valve2 = day["valve2"]
                        valve3 = day["valve3"]
                        valve4 = day["valve4"]
                        scheduleDay[d] = [valve1, valve2, valve3, valve4]
                        #for c in range(0,6):
                        #    print(data.get('valveUnit'),day["day"],"valve1",valve1[c]["period"])
                        #    print(data.get('valveUnit'),day["day"],"valve2",valve2[c]["period"])
                    self.schedule[vUnit] = scheduleDay

    def saveConf(self, valveSettings_path='valveSettings.json', scheduleSettings_path='scheduleSettings.json'):
        if os.path.exists(valveSettings_path):
            vs = {
                "data": [
                    {"controllerMac": mac, "valveUnits": self.valveUnits[mac]}
                    for mac in self.controllerMac
                ]
            }
            with open(valveSettings_path, 'w') as f:
                json.dump(vs, f, indent=4)
        if os.path.exists(scheduleSettings_path):
            ss = {"data": []}
            for vUnit, scheduleDay in self.schedule.items():
                schedule_list = []
                for d, valves in scheduleDay.items():
                    schedule_list.append({
                        "day": d,
                        "valve1": valves[0],
                        "valve2": valves[1],
                        "valve3": valves[2],
                        "valve4": valves[3]
                    })
                sensor = self.sensor.get(vUnit, [0, 0, 0, 0])
                raindelay = self.raindelay.get(vUnit, [datetime.fromisoformat('1970-01-01')] * 4)
                ss["data"].append({
                    "valveUnit": vUnit,
                    "valve1sensor": sensor[0],
                    "valve2sensor": sensor[1],
                    "valve3sensor": sensor[2],
                    "valve4sensor": sensor[3],
                    "valve1raindelay": raindelay[0].isoformat(),
                    "valve2raindelay": raindelay[1].isoformat(),
                    "valve3raindelay": raindelay[2].isoformat(),
                    "valve4raindelay": raindelay[3].isoformat(),
                    "schedule": schedule_list
                })

            # Save the reconstructed data to the JSON file
            with open(scheduleSettings_path, 'w') as f:
                json.dump(ss, f, indent=4)

valveSettings = valveSettings()

if __name__ == "__main__":
    #valveSettings = valveSettings()
    print(valveSettings.controllerMac)
    print(valveSettings.valveUnits)
    print(valveSettings.schedule)
    # print(valveSettings.schedule["DE2B"][0][3][2]["start"])