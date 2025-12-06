from PIL import Image
import fileinput
import os

class config:

    def __init__(self):

        self.path_base = os.getcwd()
        self.path = f'{os.getcwd()}/SpencerPixelCounter/'
        self.file_name = f'{self.path}config.txt'

        self.config_dict = {}
        self.config_key_list = []
        self.num_of_images = None
         

        self.colors = {}
        self.built_in_colors = ["red", "green"]
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.congifColorLst = [self.red, self.green]
    
    def set_color(self):
        while(True):
            color_name = input("What is this color for (ex voids, circles, non-circles)\n")
            print("Input the colors you are counting in the rgb format")
            r = input("Red = ") 
            g = input("Green = ")
            b = input("Blue = ")
            color = [r, g, b]
            self.colors[color_name] = color
            cont = input("If you are done inputing colors press n\n")
            if(cont in ['n', 'N']):
                break

    def built_in_color_user(self):
        for i in range(len(self.built_in_colors)):
            color_name = input(f"What is {self.built_in_colors[i]} for (ex voids, circles, non-circles)\n")
            self.colors[color_name] = self.built_in_colors[i]
        
    def config_input(self):
        self.run_populate()
        self.built_in_color_congfig()
        self.number_of_images()

        
    def built_in_color_congfig(self):
        for i in range(len(self.built_in_colors)):
            color_name = self.config_dict[self.built_in_colors[i]]
            self.colors[color_name] = self.congifColorLst[i]

    def run_populate(self):  
        with open(f'{self.file_name}', 'r') as f:
            lines = f.readlines()
            self.populate_database(lines) 
    
    def populate_database(self, lines):
        for line in lines:
            line = line.strip()
            configName = line.split(':')[0].strip()
            configValue = line.split(':')[1].strip()
            if not line:
                continue
            if line.startswith(configName):
                 self.config_dict[configName] = configValue
                 self.config_key_list.append(configName)
            
    def number_of_images(self):
        num = self.config_dict[c.config_key_list[2]]
        self.num_of_images = self.str_to_int(num)
    
    def str_to_int(self, string):
        return int(string)

                 
class image_import:

    def __init__(self, c):
        self.c = c
        self.image_name = []

        self.totalSize = []
        self.red = []
        self.green = []


    def import_image(self):
        for i in range(c.num_of_images+1):
            self.name_image(i)
            self.populate_image(i)
        print(self.green, self.red, self.totalSize)

    def name_image(self, i):
        self.image_name.append(f'{c.path}{c.config_dict[c.config_key_list[3+i]]}')

    def populate_image(self, i):
        red = 0
        green = 0
        with Image.open(self.image_name[i]) as image:
            width, height = image.size
            self.totalSize.append(width*height)
            for pixel in image.getdata():
                if pixel == c.red:
                    red += 1
                elif pixel == c.green:
                    green += 1
        self.red.append(red)
        self.green.append(green)

class post_process:

    def __init__(self, c, i):
        self.c = c
        self.i = i
        self.voids = 0
        self.non_voids = 0
        self.perVoids = 0
        self.perNon_voids = 0
        self.ZTotal = 0
        self.voidsZTotal = 0
        self.non_voidsZTotal: 0

    def input_numbers(self,j):
        self.voids = i.red[j]
        self.non_voids = i.green[j]
        print(self.voids, self.non_voids)
        self.ZTotal = self.voids + self.non_voids

    def process(self, j):
        self.input_numbers(j)
        self.perVoids = self.voids / i.totalSize[j]
        self.perNon_voids = self.perNon_voids / i.totalSize[j]
        self.voidsZTotal = self.voids / self.ZTotal
        self.non_voidsZTotal = self.non_voids / self.ZTotal
    
    def output(self):
        with open("pixelcount.txt", "w") as file:
            for j in range(c.num_of_images+1):
                self.process(j)
                file.write(f'{c.config_dict[c.config_key_list[3+j]]}\n\n')
                file.write(f'circles: {self.voids}\n')
                file.write(f'non-circles: {self.non_voids}\n')
                file.write(f'whole image: {i.totalSize}\n')
                file.write(f'%circles: {self.perVoids}%\n')
                file.write(f'%non-circles: {self.perNon_voids}%\n')
                file.write(f'circles%holes: {self.voidsZTotal}%\n')
                file.write(f'non-circles%holes: {self.non_voidsZTotal}%\n\n')
    
    def dispaly(self):
        self.output()
    


c = config()
i = image_import(c)
p = post_process(c,i) 

def main():
    c.config_input()
    i.import_image()
    p.dispaly()


main()




    