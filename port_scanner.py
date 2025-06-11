import socket
import threading
from queue import Queue
import time

# Defines the scan_port function, which takes the target ip, a port to scan, and a list open_ports to store results.
def scan_port(ip, port, open_ports):
    # Starts a try-except block to handle potential errors during socket operations.
    try:
    # Creates a new TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP).
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Sets a 1-second timeout for the socket to avoid hanging on unresponsive ports.
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
    # Attempts to connect to the target ip and port. Returns 0 if the connection succeeds (port is open) or an error code otherwise.    
        if result == 0:
      # Checks if the connection was successful (port is open), if it is appends the port number to the open_ports list
            open_ports.append(port)
        # Closes the socket to free resources.
        sock.close()
    # Catches any errors during the connection attempt (e.g., network issues) and uses "pass" to ignore errors silently and continue scanning other ports.
    except Exception:
        pass
# Defines the worker function for threads, taking the target ip, a port_queue for ports to scan, and the open_ports list.
def worker(ip, port_queue, open_ports):
  #  Loops until the queue of ports to scan is empty 
    while not port_queue.empty():
    # Retrieves the next port from the queue to scan and calls scan_port to check if the port is open on the target IP.
        port = port_queue.get()
        scan_port(ip, port, open_ports)
    # Signals that the port has been processed, helping the queue track progress.
        port_queue.task_done()

# Defines the scan_ports function, which manages the scanning process. Then takes the target ip, start_port, end_port, and optional num_threads (default 100) and prints a message indicating the target IP and port range being scanned.
def scan_ports(ip, start_port, end_port, num_threads=100):
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    # Records the start time of the scan for calculating duration.
    start_time = time.time()
    
    # Creates a new Queue object to hold ports to be scanned while open_ports initializes an empty list to store open ports found during the scan.
    port_queue = Queue()
    open_ports = []
    
    # Loops through the port range (inclusive of end_port) and adds each port to the queue for processing by worker threads.
    for port in range(start_port, end_port + 1):
        port_queue.put(port)
    
    # Initializes an empty list to store thread objects.
    threads = []

    # Loops to create the specified number of threads (default 100), then creates a thread that runs the worker function with the ip, port_queue, and open_ports as arguments.
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(ip, port_queue, open_ports))

        # Starts the thread to begin scanning ports then adds the thread to the threads list for tracking.
        thread.start()
        threads.append(thread)
    
    # Loops through all created threads and waits for each thread to finish processing, ensuring all ports are scanned before proceeding.
    for thread in threads:
        thread.join()
    
    # Records the end time of the scan then prints the total scan duration, formatted to two decimal places.
    end_time = time.time()
    print(f"Scan completed in {end_time - start_time:.2f} seconds")
    
    # Checks if any open ports were found and prints a header if open ports exist, looping through the open_ports list in sorted order for cleaner output. If no open ports are found a message is printed informing the user no ports were open in that range.
    if open_ports:
        print("Open ports found:")
        for port in sorted(open_ports):
            print(f"Port {port} is open")
    else:
        print("No open ports found")

# Defines the main function to handle user input and initiate the scan.
def main():
    # We begin a try-catch block to catch exceptions
    try:
      # Prompts for a target IP or hostname, defaulting to 127.0.0.1 if the user presses Enter
        target = input("Enter target IP or hostname (e.g., 127.0.0.1): ") or "127.0.0.1"

      # Prompts for the start port, converting it to an integer, defaulting to 1 if its empty.
        start_port = int(input("Enter start port (e.g., 1): ") or 1)

      # Prompts for the end port, converting it to an integer, defaulting to 1000 if its empty.
        end_port = int(input("Enter end port (e.g., 1000): ") or 1000)
        
      # Resolves the target hostname to an IP address (or uses the IP directly if provided).   
        ip = socket.gethostbyname(target)

      # Calls scan_ports with the resolved IP and port range to start the scan.  
        scan_ports(ip, start_port, end_port)

      # Catches errors from resolving the hostname (e.g., invalid or unreachable hostname) then prints an error message for hostname resolution failure.
    except socket.gaierror:
        print("Error: Could not resolve hostname")

      # Catches errors from invalid port inputs (e.g., non-numeric input) then prints an error message for invalid port inputs.
    except ValueError:
        print("Error: Invalid port number")

      # Catches EOF errors (e.g., user interrupts input with Ctrl+D or Ctrl+Z) then prints an error message for interrupted input.
    except EOFError:
        print("Error: Input interrupted")

# Checks if the script is being run directly (not imported as a module) then calls the main function to start the program.
if __name__ == "__main__":
    main()