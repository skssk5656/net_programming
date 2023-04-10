import socket
import datetime
import time

HOST = 'localhost'
PORT1 = 9000
PORT2 = 9001

def request_data(device_num):
    try:
        if device_num == 1:
            device_host = HOST
            device_port = PORT1
            device_name = "Device1"
            message = "Request"
        elif device_num == 2:
            device_host = HOST
            device_port = 9001
            device_name = "Device2"
            message = "Request"
        else:
            return "Invalid device number."

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((device_host, device_port))
            client_socket.sendall(message.encode())

            data = client_socket.recv(1024).decode()
            current_time = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")
            with open("data.txt", "a") as f:
                f.write(f"{current_time}: {device_name}: {data}\n")
            
            return f"{device_name} data: {data}"
    
    except socket.error as e:
        return str(e)

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Select a device (1: Device1, 2: Device2) or enter 'quit' to exit: ")
            if user_input == 'quit':
                request_data(1)  # send quit message to Device1
                request_data(2)  # send quit message to Device2
                break
            elif user_input == '1':
                print(request_data(1))
            elif user_input == '2':
                print(request_data(2))
            else:
                print("Invalid input. Please try again.")
            time.sleep(1)
        except KeyboardInterrupt:
            request_data(1)  # send quit message to Device1
            request_data(2)  # send quit message to Device2
            break