from utility import Utility

class grade_calculator:

    def __init__(self):
        self.finished_with_inputs = False
        self.grade_weights = {}
        self.grades = {}
        self.current_grade = 0
        self.vaild_total_weights = 0

        self.find_final_goal = None
        self.goal_grade = 0
        self.min_final_grade = 0

        self.find_theoretical_grades = None
        self.theoretical_granularity = 1
        self.theoretical_grades = {}

    def final_grade_master(self):
        self.find_final_goal = True
        self.final_grade_input_spesical()
        self.calculator()
        self.theoretical_calculator()
        self.display_grades()

    def current_grade_master(self):
        self.current_grade_input_spescial()
        self.calculator()
        self.display_grades()

    def grade_input(self):
        catagory_count = len(self.grade_weights) + 1 
        end = Utility.end_of_num(catagory_count)
        grade_catagory = input (f'Type the {catagory_count}{end} grade catagory\n')
        grade_weight = float(input (f'Input the weight of {grade_catagory} in percent\n'))
        grade = float(input(f'Input your current grade for {grade_catagory} in percent\n'))
        self.grade_weights[grade_catagory] = grade_weight
        self.grades[grade_catagory] = grade
        self.vaild_total_weights += grade_weight

    def final_grade_input_spesical(self):
        print('Input the grade catagories and weights then the grade you have in each of them')
        while not self.finished_with_inputs:
            self.grade_input()
            if self.find_final_goal and self.vaild_total_weights > 99:
                print('Are you sure that you input the correct grade weights?')
                Are_you_sure = input('whould you like to restart?\nY/N\n')
                if Are_you_sure in ['Y', 'y', 'yes', 'Yes']:
                    self.vaild_total_weights = 0
                    self.grade_weights.clear()
                    self.grades.clear()
                    self.final_grade_input_spesical()
            finished = input('Are you finished inputing your grades?\nY/N\n')
            if finished in ['Y', 'y', 'yes', 'Yes']:
                self.finished_with_inputs = True
            if self.find_final_goal:
                self.goal_grade = float(input('What percent would you like to get in this class?\n'))
            if self.vaild_total_weights == 100:
                self.find_final_goal = False
    
    def current_grade_input_spescial(self):
        while self.vaild_total_weights < 100:
            self.grade_input()
        if self.vaild_total_weights > 100:
            print('Invaild grade weights. Please try again')
            self.vaild_total_weights = 0
            self.grade_weights.clear()
            self.grades.clear()
            self.current_grade_input_spescial()

    def display_grades(self):
        print('catagories: weights grade')
        for catagories, weights in self.grade_weights.items():
            grade = self.grades[catagories]
            print(f'{catagories}: {weights}% {grade}%')
        current_grade = self.current_grade/(self.vaild_total_weights/100) * 100
        print(f'Current grade {current_grade:.2f}')
        if self.find_final_goal:
            print(f'To achieve a {self.goal_grade}% you need a {self.min_final_grade:.2f}% on the final')
        if self.find_theoretical_grades:
            print('grade on final -> grade in class')
            for scores, grades in self.theoretical_grades.items():
                print(f'{scores:.2f}% -----> {grades:.2f}%')

    def calculator(self):
        for catagories, weights in self.grade_weights.items():
            grade = self.grades[catagories]
            weight = weights / 100
            grade = grade / 100
            self.current_grade += (weight * grade)
        if self.find_final_goal:
            final_weight = 1 - self.vaild_total_weights/100
            self.min_final_grade = (((self.goal_grade/100) - (self.vaild_total_weights/100) * (self.current_grade/self.vaild_total_weights)*100)/(final_weight)) * 100

    def theoretical_calculator(self):
        final_weight = 1 - self.vaild_total_weights/100
        for i in range(self.theoretical_granularity):
            current_grade = self.current_grade
            final_grade = 1/self.theoretical_granularity*i
            current_grade += (final_weight * final_grade)
            self.theoretical_grades[final_grade * 100] = current_grade * 100
        if self.theoretical_granularity == 0:
            final_grade = 0
            current_grade = self.current_grade
            current_grade += (final_weight * final_grade)
            self.theoretical_grades[final_grade] = current_grade * 100
        final_grade = 1
        current_grade = self.current_grade
        current_grade += (final_weight * final_grade)
        self.theoretical_grades[final_grade * 100] = current_grade * 100
        

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
            if self.type in ['1', 'final grade', 'Final grade']:
                self.invalid_input = False
                self.final_grade_controler()
            elif self.type in ['2', 'Current grade', 'current grade']:
                self.invalid_input = False
                self.current_grade_controler()
            else:
                print('Invalid input. Try again')
    
    def final_grade_controler(self):
        print('For more advanced features press return a')
        advanced = input()
        if advanced == 'a':
            print('Would you like to see how theoretical final scores effect your grade?')
            theoretical = input('Y/N\n')
            if theoretical in ['Y', 'y', 'yes', 'Yes']:
                print('How many theroetical final grades would you like to see?')
                gc.theoretical_granularity = int(input())
                gc.find_theoretical_grades = True
        gc.final_grade_master()

    def current_grade_controler(self):
        gc.current_grade_master()


gc = grade_calculator()
rm = request_manager(gc)

def main():
    rm.calc_type()

main()