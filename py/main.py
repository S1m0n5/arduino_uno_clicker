from pynput.keyboard import Key, Controller
import serial, time, os.path, sys

keyboard = Controller()

for i in range(0,20):
    portaSeriale= "COM"+str(i)
    try:
        arduino = serial.Serial(portaSeriale, 9600)
        break
    except Exception as e:
        if i == 19:
            print("[!] An error is occurred, please disconnect and connect your Arduino again")
            exit = input("Press ENTER key to exit...")
            sys.exit()


def main():
    history = []
    print("LEFT:"+left)
    print("RIGHT:"+right+"\n")
    arduino.write("main".encode())
    while True:
        output = arduino.readline().decode().replace("\r\n","")
        if output == left:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            history.append("LEFT")
            print("LEFT")
        if output == right:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            history.append("RIGHT")
            print("RIGHT")

time.sleep(2)
if os.path.isfile("../config.txt"):
    f = open("../config.txt","r")
    k = f.readline()[2:].replace("\n","")
    left = f.readline()[2:].replace("\n","")
    right = f.readline()[2:].replace("\n","")
    f.close()
    main()

else:
    #CONFIGURATION
    arduino.write("config".encode())
    command = []
    for i in range(0,4):
        if i == 0:
            print("Press LEFT button")
        elif i == 2:
            print("Press RIGHT button")
        output = arduino.readline()
        command.append(output)
        print(output.decode())

    left = command[0].decode().replace("\r\n","")
    right = command[2].decode().replace("\r\n","")
    k = list(set([x for x in command if command.count(x)>1]))[0].decode().replace("\r\n","")
    f = open("../config.txt","w")
    f.write("K:%s\nL:%s\nR:%s" % (k, left, right))
    f.close()
    print("Configuration terminated")
    #REBOOT
    main()

arduino.close()
