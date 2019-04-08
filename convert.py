import json

command_list = []
target_list = []
value_list = []

with open('file.json') as json_file:
    data = json.load(json_file)
    for p in data['Commands']:
        #print('Command: ' + p['Command'])
        command_list.append(p['Command'])
        #print('Target: ' + p['Target'])
        target_list.append(p['Target'])
        #print('Value: ' + p['Value'])
        value_list.append(p['Value'])
        #print('')

def convertCommand(command):
    value_length = ""
    #pause
    if command == "pause":
        #ms to s
        try:
            value_length = int(target_list[counter])
            value_length = float(value_length/1000)
        except:
            pass
        #if stop : stop
        if value_length == "":
            f.write("exit()")
        else:
            f.write("time.sleep(" + str(value_length) + ")")

    #store
    elif command == "store":
        pass
    elif command == "storeEval":
        pass
    elif command == "storeValue":
        pass

    #open
    elif command == "open":
        pass

    #csv
    elif command == "csvRead":
        pass
    elif command == "csvSave":
        pass

    #misc
    elif command == "deleteAllCookies":
        pass
    elif command == "type":
        pass
    elif command == "click":
        pass
    elif command == "if":
        pass




f = open("converted.py", "w+")

nextLine = 0
counter = 0

for command in command_list:
    #Formatting
    if command == "if":
        nextLine += 1
    if command == "endif":
        nextLine -= 1
    #Writing non-if statements
    if command != "endif" and command != "if" and command != "else":
        f.write(nextLine*"    ")
        if command == "pause":
            convertCommand(command)
        else:
            f.write(command)
        f.write("\n")
    #Writing if-like statements
    elif command == "if" or command == "else":
        f.write(command + ":")
        convertCommand(command)
        f.write("\n")

    #Indexing method
    counter += 1


f.close()