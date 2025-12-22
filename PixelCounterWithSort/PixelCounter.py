from PIL import Image
import os
import colorsys

class config:

    def __init__(self):

        self.path_base = os.getcwd()
        self.path = f'{os.getcwd()}/PixelCounterWithSort/'
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

    def __init__(self, c, i, s):
        self.c = c
        self.i = i
        self.s = s
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
        self.perVoids = self.voids * 100 / i.totalSize[j]
        self.perNon_voids = self.non_voids * 100 / i.totalSize[j]
        self.voidsZTotal = self.voids / self.ZTotal * 100
        self.non_voidsZTotal = self.non_voids / self.ZTotal * 100
    
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
        if (c.config_dict['Output sorted Image'] == 'True'):
            s.sort_all()
    
class sort_image: ##code orginally written by Evan Lu @ https://waffles-codes.github.io/##

    def __init__(self, c, i):
        self.c = c
        self.i = i
        self.outputpath_base = 'output_sorted_by_hue_'

    def sort_all(self):
        for j in range(c.num_of_images+1):
            self.image_to_sort(j)

    def image_to_sort(self, j):
        try:
            img = Image.open(i.image_name[j]).convert("RGB")
        except FileNotFoundError:
            print(f"Error: Image file not found at {i.image_name[j]}")

        pixels = list(img.getdata())

        processed_pixels = []
        for r, g, b in pixels:
            h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            processed_pixels.append((s, (r, g, b)))

        processed_pixels.sort(key=lambda x: x[0])

        sorted_rgb_pixels = [p[1] for p in processed_pixels]

        sorted_img = Image.new("RGB", img.size)
        sorted_img.putdata(sorted_rgb_pixels)
        sorted_img.save(f'{self.outputpath_base}{c.config_dict[c.config_key_list[3+j]]}')
        print(f"Sorted image saved to {self.outputpath_base}{c.config_dict[c.config_key_list[3+j]]}")

c = config()
i = image_import(c)
s = sort_image(c,i) ###code orginally written by Evan Lu @ https://waffles-codes.github.io/##
p = post_process(c,i,s)


def main():
    c.config_input()
    i.import_image()
    p.dispaly()


main()




    