import socket
import math
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    filename='calc.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

HOST = "0.0.0.0"
PORT = 5000

clients = []


def calculate(op, nums):
    operations = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y,
        "mod": lambda x, y: x % y,
        "power": lambda x, y: x ** y,
        "max": lambda x, y: max(x, y),
        "min": lambda x, y: min(x, y),
        "gcd": lambda x, y: math.gcd(int(x), int(y)),  # GCD requires integers
        "lcm": lambda x, y: math.lcm(int(x), int(y)),  # LCM requires integers
        "square": lambda x: x ** 2,
        "cube": lambda x: x ** 3,
        "abs": lambda x: abs(x),
        "neg": lambda x: -x,
        "factorial": lambda x: math.factorial(int(x)),  # Factorial requires integers
        "sqrt": lambda x: math.sqrt(x),
        "log": lambda x: math.log10(x),
        "even": lambda x: x % 2 == 0,
        "odd": lambda x: x % 2 != 0
    }

    try:
        # Calculate first, log second, return third
        result = operations[op](*nums)
        logging.debug(f"Result for '{op}' with {nums} is {result}")
        return result
    except KeyError:
        logging.warning(f"Invalid operation attempted: {op}")
        return "Invalid operation"
    except ZeroDivisionError:
        logging.warning("Attempted division by zero")
        return "Cannot divide by zero"
    except TypeError:
        logging.warning(f"Wrong number of arguments passed to {op}")
        return "Invalid number of arguments for this operation"
    except ValueError as e:
        logging.warning(f"Math domain error: {e}")
        return "Math error (e.g., negative square root or factorial)"


def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    clients.append(conn)
    logging.info(f"Client connected: {addr}")

    conn.sendall(
        b"Welcome to Calculator Server\n"
        b"Usage: operation numbers (e.g., 'add 5 10' or 'sqrt 16')\n"
    )
    logging.info("Welcome message sent")

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break  # Client disconnected normally

            parts = data.split()
            if not parts:
                continue

            op = parts[0].lower()

            # Map inputs to floats so the calculator can handle decimals
            try:
                nums = list(map(float, parts[1:]))
            except ValueError:
                conn.sendall(b"Error: Please provide valid numbers.\n")
                continue  # Catch the typo, tell the user, but keep them connected

            result = calculate(op, nums)
            conn.sendall(f"Result: {result}\n".encode())

        except Exception as e:
            # Only break the loop and drop the client for critical socket errors
            conn.sendall(f"Critical Error: {e}\n".encode())
            logging.error(f"Critical Error with {addr}: {e}")
            break

    conn.close()
    if conn in clients:
        clients.remove(conn)
    print(f"Client disconnected: {addr}")
    logging.info(f"Client disconnected: {addr}")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allows immediate restart of the server without "Address already in use" errors
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print("Calculator Server started...")
    logging.info("Calculator Server started...")

    while True:
        conn, addr = server.accept()
        # Threading prevents the server from blocking on the handle_client loop
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()