#1
import threading
from math import isqrt
from queue import Queue

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result_queue):
    """Check primes in the range [start, end) and put results in the queue."""
    for number in range(start, end):
        if is_prime(number):
            result_queue.put(number)

def main():
    # Input range
    lower_bound = 10
    upper_bound = 50

    # Number of threads
    num_threads = 4

    # Calculate sub-range size
    range_size = upper_bound - lower_bound
    step = range_size // num_threads

    threads = []
    result_queue = Queue()

    for i in range(num_threads):
        start = lower_bound + i * step
        end = lower_bound + (i + 1) * step if i < num_threads - 1 else upper_bound
        thread = threading.Thread(target=check_primes_in_range, args=(start, end, result_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Collect results from the queue
    primes = []
    while not result_queue.empty():
        primes.append(result_queue.get())

    primes.sort()
    print(f"Primes in the range [{lower_bound}, {upper_bound}): {primes}")

if __name__ == "__main__":
    main()

#2
        import threading

        def read_file_thread(file_path, start_byte, end_byte):
            with open(file_path, 'r') as file:
                file.seek(start_byte)
                content = file.read(end_byte - start_byte)
                # Process content here
                print(f"Thread {threading.current_thread().name}: Read {len(content)} bytes")


        def concurrent_read_threads(file_path, num_threads):
            file_size = os.path.getsize(file_path)
            chunk_size = file_size // num_threads
            threads = []
            for i in range(num_threads):
                start_byte = i * chunk_size
                end_byte = (i + 1) * chunk_size if i < num_threads - 1 else file_size
                thread = threading.Thread(target=read_file_thread, args=(file_path, start_byte, end_byte))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()


        if __name__ == "__main__":
            file_path = "your_file.txt"
            num_threads = 4
            concurrent_read_threads(file_path, num_threads)
