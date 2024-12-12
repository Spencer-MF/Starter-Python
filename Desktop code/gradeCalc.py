import utility

class grade_calculator:

    def __init__(self):
        self.grade_weights = {}
        self.grades = []


    def final_grade_master(self):
        pass

    def current_grade_master(self):
        pass

class request_manager:

    def __init__(self, gc):
        self.gc = gc
        self.type = None
        self.invalid_input = True

    def calc_type(self):
        print('What type grade calculation would you like to do?')
        print('1) Final grade\n2) Current grade')
        while(self.invalid_input):
            self.type = input()
            if self.type == ['1', 'final grade', 'Final grade']:
                self.final_grade_controler()
                self.invalid_input = False
            elif self.type == ['2', 'Current grade', 'current grade']:
                self.current_grade_controler()
                self.invalid_input = False
            else:
                print('Invalid input. Try again')
    
    def final_grade_controler(self):
        gc.final_grade_master()

    def current_grade_controler(self):
        gc.current_grade_master()


gc = grade_calculator()
rm = request_manager(gc)