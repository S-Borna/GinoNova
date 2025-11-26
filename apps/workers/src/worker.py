from .event_consumer import EventConsumer

def main():
    consumer = EventConsumer()
    consumer.run()

if __name__ == "__main__":
    main()
