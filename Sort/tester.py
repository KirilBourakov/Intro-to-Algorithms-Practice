import helpers
import time

class Tester:
    def __init__(self, num):
        self.to_sort = helpers.active_generator(num)
        return
    
    def time(self, sorting_func):
        start_time = time.time()
        final = sorting_func(self.to_sort)
        print(f"{sorting_func} --- Ran in %s seconds ---" % (time.time() - start_time))
        assert  final == sorted(self.to_sort)