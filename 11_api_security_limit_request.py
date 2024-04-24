# demo limit request (throttling)

import time

class Throttle:
    def __init__(self, limit, interval):
        self.limit = limit
        self.interval = interval
        self.requests = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            client_ip = args[0]  # Assuming client IP is the first argument
            current_time = time.time()

            # Remove old requests
            self.requests[client_ip] = [req_time for req_time in self.requests.get(client_ip, []) if req_time > current_time - self.interval]

            # Check if number of requests exceeds limit
            if len(self.requests.get(client_ip, [])) < self.limit:
                self.requests.setdefault(client_ip, []).append(current_time)
                return func(*args, **kwargs)
            else:
                return "Too many requests", 429  # HTTP status code for Too Many Requests

        return wrapper

# Usage example
throttle = Throttle(limit=3, interval=60)  # Limiting to 3 requests per minute

@throttle
def protected_resource(client_ip):
    return "This is the protected resource!"

# Simulate requests
for _ in range(5):
    print(protected_resource("127.0.0.1"))
    # kalo dipasang sleep 20 bisa karena accepted 3 request per minute
    time.sleep(5)  # Introduce a delay between requests
