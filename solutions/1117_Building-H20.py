import threading

class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3)
        self.oxygen_sem = threading.Semaphore(1)
        self.hydrogen_sem = threading.Semaphore(2)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_sem.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()

        self.hydrogen_sem.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_sem.acquire()
        self.barrier.wait()

        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()

        self.oxygen_sem.release()


