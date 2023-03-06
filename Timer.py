import time
import threading

class Timer(object):
    def __init__(self, duration=10):
        self.duration = duration
        self.timeLeft = duration

    def startTimer(self):
        print("STARTING TIMER")
        x = threading.Thread(target = self.thread_function)
        x.start()

    def thread_function(self):
        time.sleep(self.duration)
        self.stopGame()

    def stopGame(self):
        print("Stop the Game Here")

    def resetTimer(self):
        self.timeLeft = self.duration


if __name__ == "__main__":
    print("TESTING TIMER")
    timer = Timer()
    timer.startTimer()
    print("TIMER Should not have finished yet")