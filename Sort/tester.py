import helpers
import time

class Tester:
    def __init__(self, num):
        self.num = num
        self.to_sort = []
        return
    
    def generate(self):
        self.to_sort = helpers.active_generator(self.num)

    def time(self, sorting_func):
        self.generate()
        start_time = time.time()
        final = sorting_func(self.to_sort)
        print(f"{sorting_func} --- Ran in %s seconds ---" % (time.time() - start_time))
        assert  final == sorted(self.to_sort)
    
    def timeClass(self, className, *args):
        self.generate()
        obj = className(self.to_sort)
        start_time = time.time()
        if len(args) > 0:
            obj.sort(*args)
        else:
            obj.sort()
        print(f"{obj} --- Ran in %s seconds ---" % (time.time() - start_time))
        assert  obj.getItems() == sorted(self.to_sort)