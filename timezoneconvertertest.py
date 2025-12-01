import time

file_path = r'timezone-convertor/request-file/timezone_request.txt'

def write_to_file(text):
    f = open(file_path, 'w')
    f.write(text)
    f.close

def read_file():
    f = open(file_path, 'r')
    data = f.read().strip()
    f.close()
    return data

def main():

    print("Type 'current' to see the current time in a different timezone ")
    print("Type 'convert' to see a time changed from one timezone to another")
    command = input("Enter the command: ")

    if command.lower().strip() == 'current':
        timezone = input("Enter in the timezone you want to see")
        final_string = 'current' + ' ' + timezone
        time.sleep(5)
        write_to_file(final_string)
        print(read_file())
        

        

    elif command.lower().strip() == 'convert':
        timezone1 = input("Enter in the first timezone: ")
        timezone2 = input("Enter in the second timezone: ")
        time_entered = input("Enter in the time: ")
        final_string = 'convert' + ' ' + timezone1 + ' ' + timezone2 + " " + time_entered
        write_to_file(final_string)
        time.sleep(5)
        print(read_file())

main()
