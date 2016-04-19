import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')
        return

def main():
   for i in range(5):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    main()