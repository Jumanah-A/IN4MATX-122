import time
import threading

class Timer(object):
    def __init__(self, gui, duration=30):
        self.gui = gui
        self.duration = duration
        self.timeLeft = duration
        self.timerThread = threading.Thread(target=self._thread_function)
        self._stop_event = threading.Event()

    def startTimer(self):
        try:
            self.timeLeft = self.duration
            self.timerThread.start()
        except RuntimeError:
            print("ERROR: Timer has already started")

    def _thread_function(self):
        #print("Timer started")
        for x in range(self.timeLeft):
            if self._stop_event.is_set():
                break
            #print(self.timeLeft)
            time.sleep(1)
            self.timeLeft -= 1
            # Here; draw timer using the GUI
            self.gui.displayTimer(self)
        #print(self.timeLeft)
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
        #print("RESET")

    def setDuration(self, duration):
        self.duration = duration

    def getRemainingTime(self):
        return self.timeLeft


if __name__ == "__main__":
    # Test Case 1: Timer runs same time as main and finishes (PASSED)
    # timer = Timer()
    # timer.startTimer()
    # time.sleep(3)
    # print("3 SECONDS HAVE PASSED")
    # time.sleep(4)
    # print(f'REMAINING TIME: {timer.getRemainingTime()}')

    # Test Case 2: Timer runs, finishes running, resets, and runs again fine (PASSED)
    # timer = Timer()
    # timer.startTimer()
    # time.sleep(3)
    # print(f'REMAINING TIME: {timer.getRemainingTime()}')
    # time.sleep(8)
    # print("STARTING AGAIN")
    # timer.resetTimer()
    # timer.startTimer()
    # time.sleep(6)
    # print(f'REMAINING TIME: {timer.getRemainingTime()}')

    # Test Case 3: Timer is reset during run to stop it (PASSED)
    # timer = Timer()
    # timer.startTimer()
    # time.sleep(3)
    # print("Time to Restart Timer")
    # timer.resetTimer()
    # time.sleep(2)
    # print("hello")

    # Test Case 4: Timer is reset during run, and then ran again
    timer = Timer()
    timer.startTimer()
    time.sleep(3)
    timer.resetTimer()
    time.sleep(2)
    timer.startTimer()
    print("TIMER Should not have finished yet")
    time.sleep(4)
    print("TIMER STILL GRINDING")