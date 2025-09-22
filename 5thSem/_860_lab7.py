import math
import threading
import time

pi = math.pi
def calculate_sin(x):
    print(f"Starting sin calculation at {threading.current_thread().name}")
    result = math.sin(math.radians(x))
    print(f"sin({x:.2f} degrees) = {result:.4f}")

def calculate_cos(y):
    print(f"Starting cos calculation at {threading.current_thread().name}")
    result = math.cos(math.radians(y))
    print(f"cos({y:.2f} degrees) = {result:.4f}")

def calculate_tan(z):
    print(f"Starting tan calculation at {threading.current_thread().name}")
    result = math.tan(math.radians(z))
    print(f"tan({z:.2f} degrees) = {result:.4f}")


if __name__ == "__main__":
    x = 30  # Example value for x
    y = 45  # Example value for y
    z = 60 # Example value for z

    print("time taken:",time.time())
    thread_sin = threading.Thread(target=calculate_sin, args=(x,))
    print("time taken:",time.time())
    thread_cos = threading.Thread(target=calculate_cos, args=(y,))
    print("time taken:",time.time())
    thread_tan = threading.Thread(target=calculate_tan, args=(z,))

    # Start the threads
    thread_sin.start()
    thread_cos.start()
    thread_tan.start()

    # Calculate the final result
    c = math.sin(math.radians(x)) + math.cos(math.radians(y)) + math.tan(math.radians(z))
    print(f"c = sin(x) + cos(y) + tan(z) = {c:.4f}")