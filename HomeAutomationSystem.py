class HomeAutomation:
    def __init__(self):
        self.devices = {
            "lights": {"state": "off"},
            "thermostat": {"temperature": 70},
            "security_system": {"armed": False}
        }
    def toggle_lights(self):
        if self.devices['lights']['state'] == "off":
            self.devices['lights']['state'] = "on"
            print("Lights turned on")
        else:
            self.devices['lights']['state'] = "off"
            print("Lights turned off")
    def adjust_temperature(self, temperature):
        self.devices['thermostat']['temperature'] = temperature
        print(f"Temperature set to {temperature}")
    def toggle_security_system(self):
        if self.devices['security_system']['armed']:
            self.devices['security_system']['armed'] = False
            print("Security system disarmed")
        else:
            self.devices['security_system']['armed'] = True
            print("Security system armed")
    def show_status(self):
        print("Current status: ")
        for device, status in self.devices.items():
            print(f"{device}: {status}")
def main():
    home = HomeAutomation()
    print("Welcome to home Automation App")
    while True:
        print("\nWhat would like to do ?")
        print("1. Toggle lights")
        print("2. Adjust thermostat temperature")
        print("3. Toggle security system")
        print("4. Show current status")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            home.toggle_lights()
        elif choice == "2":
            temperature = int(input("Enter the desire temperature: "))
            home.adjust_temperature(temperature)
        elif choice == "3":
            home.toggle_security_system()
        elif choice == "4":
            home,show_status()
        elif choice == "5":
            print("Exiting the Home automation app.Goodbye")
            break
        else:
            print("Invalid choice. Please enter a number b/w 1 and 5.")
if __name__ == "__main__":
    main()
