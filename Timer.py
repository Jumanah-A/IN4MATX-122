import time
import threading

class Timer(object):
    def __init__(self, duration=10):
        self.duration = duration
        self.timeLeft = duration
        self.timerThread = threading.Thread(target=self._thread_function)
        self._stop_event = threading.Event()

    def startTimer(self):
        try:
            self.timerThread.start()
        except RuntimeError:
            print("ERROR: Timer has already started")

    def _thread_function(self):
        print("Timer started")
        for x in range(self.timeLeft):
            if self._stop_event.is_set():
                break
            print(self.timeLeft)
            time.sleep(1)
            self.timeLeft -= 1
        print(self.timeLeft)
        self.stopGame()

    def stopGame(self):
        print("Stop the Game Here")

    def resetTimer(self):
        if self.timerThread.is_alive():
            self._stop_event.set()
            time.sleep(1)
            self.timerThread.join()
            self.timerThread = threading.Thread(target=self._thread_function)
        self.timeLeft = self.duration
        self._stop_event.clear()


if __name__ == "__main__":
    #print("TESTING TIMER")
    timer = Timer()
    timer.startTimer()
    time.sleep(3)
    timer.resetTimer()
    time.sleep(2)
    timer.startTimer()
    print("TIMER Should not have finished yet")