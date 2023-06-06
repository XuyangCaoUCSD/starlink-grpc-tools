import subprocess
import socket
import time

SERVER_ADDR = "3.15.10.205"
SERVER_PORT = 20001
DUP_TIMES = 3

try:
    msg_from_client = str(1)
    bytes_to_send = str.encode(msg_from_client)
    server_addr = (SERVER_ADDR, SERVER_PORT)
    # create a UDP socket at client side
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    while True:
        time.sleep(0.1)
        status = subprocess.check_output(['python3', 'dish_grpc_text.py', 'ping_drop', "-v"])
        status_str = status.decode()
        
        # get the total ping drop (is this the efficient way?)
        total_ping_drop = 0
        status_str_lines = status_str.split("\n")
        for line in status_str_lines:
            # TODO: get the right value
            pass

        # an handover has occurred!
        if total_ping_drop > 0.0001:
            for i in range(DUP_TIMES):
                udp_client_socket.sendto(bytes_to_send, server_addr)
except KeyboardInterrupt:
    pass
finally:
    udp_client_socket.close()