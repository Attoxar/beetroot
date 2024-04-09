class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Worker must be an instance of Worker class.")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class.")


boss1 = Boss(1, "John", "Microsoft ")
boss2 = Boss(2, "Alice", "Apple ")
worker1 = Worker(101, "Bob", "microsoft ", boss1)
worker2 = Worker(102, "Eva", "Apple", boss2)
print("Boss 1's workers:", boss1.workers)
print("Boss 2's workers:", boss2.workers)
