# class SmartDevice:
#
#       def turn_on(self):
#         self.is_on = True
#         print(f"{self.name} is on")
#
#       def turn_off(self):
#         self.is_on = False
#         print(f"{self.name} is off")
#
#       def show_status(self):
#         if self.is_on:
#           status = "on"
#         else:
#           status = "off"
#         print(f"Name: {self.name}")
#         print(f"Room: {self.room}")
#         print(f"Status: {status}")
#
# class SmartLight(SmartDevice):
#       def __init__(self, name, room, is_on, brightness):
#         self.name = name
#         self.room = room
#         self.is_on = False
#         self.brightness = brightness
#
#       def change_brightness(self, new_brightness):
#         self.brightness = new_brightness
#         print(f"Brightness of {self.name} is changed to {self.brightness}")
#
#       def show_light_information(self):
#           self.show_status()
#           print(f"Brightness: {self.brightness}")
#
# class SmartSpeaker(SmartDevice):
#
#   def __init__(self, name, room, is_on, volume):
#     self.name = name
#     self.room = room
#     self.is_on = is_on
#     self.volume = volume
#
#   def change_volume(self, new_volume):
#       self.volume = new_volume
#       print(f"Brightness of {self.name} is changed to {self.volume}")
#
#   def show_speaker_information(self):
#       self.show_status()
#       print(f"Volume: {self.volume}")
#
# class LightSensor(SmartDevice):
#   def __init__(self, name, room, light_level):
#     self.name = name
#     self.room = room
#     self.is_on = True
#     self.light_level = light_level
#
#   def read_value(self):
#     return self.light_level
#
# class NoiseSensor(SmartDevice):
#     def __init__(self, name, room, noise_level):
#         self.name = name
#         self.room = room
#         self.is_on = True
#         self.noise_level = noise_level
#     def read_value(self):
#         return self.noise_level
#
# class TemperatureSensor(SmartDevice):
#     def __init__(self, name, room, temperature_level):
#         self.name = name
#         self.room = room
#         self.is_on = True
#         self.temperature_level = temperature_level
#     def read_value(self):
#         return self.temperature_level
#
# class RemoteControl:
#   def __init__(self, owner, connected_device):
#     self.owner = owner
#     self.connected_device = None
#
#   def connect(self, device):
#     self.connected_device = device
#     print(f"{self.owner} is connected to {device.name}")
#
#   def disconnect(self):
#     pass
#
#   def turn_on_device(self):
#     pass
#
#   def turn_off_device(self):
#     pass
#
#   def show_connected_device(self):
#     pass
#
# class Dashboard:
#   def show_dashboard(self):
#     pass


import pandas as pd

df = pd.read_csv("C:/Ustudy3/u20/student_lifestyle_academic_performance.csv")

# Task 1
# Shavkatjonov Muhammadamin

correlations = {
    "Study Hours x Final Score": df["Study_Hours_Per_Day"].corr(df["Final_Score"]),
    "Attendance x Final Score": df["Attendance_Percent"].corr(df["Final_Score"]),
    "Sleep Hours x Final Score": df["Sleep_Hours_Per_Day"].corr(df["Final_Score"]),
    "Social Media Hours x Final Score": df["Social_Media_Hours"].corr(df["Study_Hours_Per_Day"]),
    "Total Screen Time Hours x Social Media Hours": df["Total_Screen_Time_Hours"].corr(df["Social_Media_Hours"])
}

for key, value in correlations.items():
    print(f"{key}: {value}")