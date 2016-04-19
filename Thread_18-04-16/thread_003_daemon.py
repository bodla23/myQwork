import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

def main():

    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    t = threading.Thread(name='non-daemon', target=non_daemon)
    d.start()
    t.start()

    d.join()
    t.join()


if __name__ == '__main__':		
	main()	