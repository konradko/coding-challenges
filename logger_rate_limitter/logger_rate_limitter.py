class LoggerRateLimitter(object):
    def __init__(self):
        self.timestamp_per_message = {}

    def should_print_message(self, timestamp: int, message: str):
        should_print_message = False

        previous_timestamp = self.timestamp_per_message.get(message)

        if previous_timestamp is None:
            self.timestamp_per_message[message] = timestamp
            should_print_message = True

        elif timestamp - previous_timestamp >= 10:
            self.timestamp_per_message[message] = timestamp
            should_print_message = True

        return should_print_message
