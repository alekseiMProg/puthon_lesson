from time import sleep


class TrafficLight:
    __color = "red"

    def running(self):
        print(f"{self.__color}")
        sleep(7)
        self.__color = "yellow"
        print(f"{self.__color}")
        sleep(2)
        self.__color = "Green"
        print(f"{self.__color}")


start = TrafficLight()
start.running()
