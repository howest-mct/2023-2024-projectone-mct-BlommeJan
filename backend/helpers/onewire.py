import time
# import matplotlib.pyplot as plt


class OneWire:
    """One Wire bus class
    The one wire bus needs to be enabled on the raspberry pi via raspi-config
    When it starts reading data on this bus this will be stored in a file in the following directory:
    /sys/bus/w1/devices/w1_bus_master1/28-00af570000af/w1_slave
    28-00af570000af is different every time and needs to be parsed into this class
    """

    def __init__(self, device_id):
        self.file_path = f"/sys/bus/w1/devices/w1_bus_master1/{device_id}/w1_slave"

    def read_temperature(self):
        with open(self.file_path, "r") as file:
            content = file.readlines()
            for line in content:
                if "t=" in line:
                    temp_string = line.split("t=")[-1].strip()
                    return float(temp_string) / 1000.0
# Example usage
if __name__ == "__main__":
    try:
        ow = OneWire("28-8590fd1d64ff")
        temp = []
        while True:
            t = ow.read_temperature()
            temp.append(t)
            print(f"Temperature: {t:.1f} °C")
            time.sleep(1)

            # plt.plot(temp)
            # plt.title("Temperature")
            # plt.xlabel("Time")
            # plt.ylabel("Temperature (°C)")
            # plt.savefig("temperature.png")

    except KeyboardInterrupt as e:
        "\nQuitting..."
