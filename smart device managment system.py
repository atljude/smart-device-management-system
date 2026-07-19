# OOP MINI PROJECT
# Smart Device Management System

# Parent Class
class SmartDevice:

    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__power_status = False

    # Getter
    def get_device_id(self):
        return self.__device_id

    # Setter
    def set_device_id(self, device_id):
        if device_id != "":
            self.__device_id = device_id
        else:
            print("Device ID cannot be empty.")

    def get_power_status(self):
        return self.__power_status

    def turn_on(self):
        self.__power_status = True
        print(self.name, "has been turned ON.")

    def turn_off(self):
        self.__power_status = False
        print(self.name, "has been turned OFF.")

    def display_info(self):
        print("\nDevice Name :", self.name)
        print("Device ID   :", self.__device_id)

        if self.__power_status:
            print("Power Status: ON")
        else:
            print("Power Status: OFF")


# Child Class
class TemperatureSensor(SmartDevice):

    def __init__(self, name, device_id, temperature):
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        print("Current Temperature:", self.temperature, "°C")

    def display_info(self):
        super().display_info()
        print("Temperature :", self.temperature, "°C")


# Child Class
class SmartLight(SmartDevice):

    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.__brightness = 50

    def increase_brightness(self):

        if self.__brightness < 100:
            self.__brightness = self.__brightness + 10

        print("Brightness:", self.__brightness)

    def decrease_brightness(self):

        if self.__brightness > 0:
            self.__brightness = self.__brightness - 10

        print("Brightness:", self.__brightness)

    def display_info(self):
        super().display_info()
        print("Brightness :", self.__brightness)


# Child Class
class SecurityCamera(SmartDevice):

    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.recording_status = False

    def start_recording(self):
        self.recording_status = True
        print("Camera is now recording.")

    def stop_recording(self):
        self.recording_status = False
        print("Recording stopped.")

    def display_info(self):
        super().display_info()
        print("Recording :", self.recording_status)


# Create Objects

sensor = TemperatureSensor("Temperature Sensor", "TS101", 27)

light = SmartLight("Smart Light", "SL201")

camera = SecurityCamera("Security Camera", "SC301")


# ===========================
# Menu
# ===========================

while True:

    print("\n========== SMART DEVICE MENU ==========")
    print("1. Display Device Information")
    print("2. Turn Devices ON")
    print("3. Turn Devices OFF")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Camera Recording")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        sensor.display_info()
        light.display_info()
        camera.display_info()

    elif choice == "2":

        sensor.turn_on()
        light.turn_on()
        camera.turn_on()

    elif choice == "3":

        sensor.turn_off()
        light.turn_off()
        camera.turn_off()

    elif choice == "4":

        sensor.read_temperature()

    elif choice == "5":

        print("\n1. Increase Brightness")
        print("2. Decrease Brightness")

        option = input("Choose an option: ")

        if option == "1":
            light.increase_brightness()

        elif option == "2":
            light.decrease_brightness()

        else:
            print("Invalid option.")

    elif choice == "6":

        print("\n1. Start Recording")
        print("2. Stop Recording")

        option = input("Choose an option: ")

        if option == "1":
            camera.start_recording()

        elif option == "2":
            camera.stop_recording()

        else:
            print("Invalid option.")

    elif choice == "7":

        print("Thank you for using the Smart Device Management System.")
        break

    else:
        print("Invalid choice. Please try again.")