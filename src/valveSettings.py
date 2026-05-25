import json
import os
import logging

class valveSettings:
    def __init__(self, valveSettings_path='valveSettings.json', scheduleSettings_path='scheduleSettings.json'):
        self.controllerMac = []
        self.valveUnits = {}
        self.schedule = {}
        self.loadConf(valveSettings_path, scheduleSettings_path)

    def loadConf(self, valveSettings_path='valveSettings.json', scheduleSettings_path='scheduleSettings.json'):
        if os.path.exists(valveSettings_path):
            with (open(valveSettings_path, 'r') as f):
                vs = json.load(f)
                for data in vs.get('data'):
                    self.controllerMac.append(data.get('controllerMac'))
                    self.valveUnits[data.get('controllerMac')] = data.get('valveUnits')
                print(self.valveUnits)
        if os.path.exists(scheduleSettings_path):
            with ((open(scheduleSettings_path, 'r')) as f):
                ss = json.load(f)
                for data in ss.get('data'):
                    vUnit = data.get('valveUnit')
                    scheduleDay = {}
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

                ss["data"].append({
                    "valveUnit": vUnit,
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
    print(valveSettings.schedule["DE2B"][0][3][2]["start"])