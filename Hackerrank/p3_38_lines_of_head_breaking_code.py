# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    arr = []
    N = int(input("How many commands? "))

    for i in range(N):
        cmd = input("Enter command ")  # append 5 / print
        cmd = cmd.lower()
        if cmd == "print":
            print(arr)

        elif cmd.startswith("append"):
            cmd = cmd.split(" ")
            if len(cmd) == 2:
                cmd[1] = int(cmd[1])
                arr.append(cmd[1])
            else:
                print("Incorrect command, Get out of here")

        elif cmd.startswith("insert"):
            cmd = cmd.split(" ")
            if len(cmd) == 3:
                cmd[1] = int(cmd[1])
                cmd[2] = int(cmd[2])
                arr.insert(cmd[1], cmd[2])
            else:
                print("Incorrect command, Get out of here")

        elif cmd.startswith("remove"):
            cmd = cmd.split(" ")
            cmd[1] = int(cmd[1])
            if cmd[1] in arr:
                arr.remove(cmd[1])
            else:
                print("Unidentified value")

        elif cmd.startswith("sort"):
            arr.sort()

        elif cmd.startswith("reverse"):
            arr.reverse()

        elif cmd.startswith("pop"):
            arr.pop()
    print(arr)