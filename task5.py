def toggleSwitch(index, switches):
    if switches[index] == 1:
        switches[index] = 0
    else:
        switches[index] = 1
    print(switches)

# divide and conquer function
# to turn off all switches
def turnOff(start, end, switches):
    n = end - start + 1
    if n == 1:
        toggleSwitch(end, switches)
    elif n == 2:
        toggleSwitch(start, switches)
        toggleSwitch(end, switches)
    else:
        turnOff(start + 2, end, switches)
        toggleSwitch(start, switches)
        turnOn(start + 2, end, switches)
        turnOff(start +1 , end, switches)

def turnOn(start, end, switches):
    n = end - start + 1
    if n == 1:
        toggleSwitch(end, switches)
    elif n == 2:
        toggleSwitch(end, switches)
        toggleSwitch(start, switches)
    else:
        turnOn(start + 1, end, switches)
        turnOff(start + 2, end, switches)
        toggleSwitch(start, switches)
        turnOn(start +2, end, switches)

def main():
    size = int(input("Please enter the number of switches: "))
    switches = [1] * size
    print(switches)
    turnOff(0, size - 1, switches)

if __name__ == "__main__":
    main()