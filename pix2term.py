from PIL import Image
import sys

colorsteps = [0] + [i for i in range(95, 256, 40)]
colors = []

# Any efficient way to do this?
for i in colorsteps:
    for j in colorsteps:
        for k in colorsteps:
            colors.append((i, j, k, 255))

def avg_dist_idx(pixel: tuple):
    for idx, i in enumerate(colors):
        red_dist = abs(pixel[0] - i[0])
        green_dist = abs(pixel[1] - i[1])
        blue_dist = abs(pixel[2] - i[2])
        total_dist = red_dist + green_dist + blue_dist
        try:
            if lowest_dist > total_dist:
                lowest_dist = total_dist
                lowest_idx = idx
        except NameError:
            lowest_dist = total_dist
            lowest_idx = idx
    return lowest_idx

with open(sys.argv[1], 'rb') as orig:
    image = Image.open(orig)
    h = image.height
    w = image.width
    pix_list = list(image.getdata())

for idx, i in enumerate(pix_list):
    ansi_num = avg_dist_idx(i) + 16
    print(f'\033[48;5;{ansi_num}m  ', end='')
    if idx != 0 and idx % w == 0:
        print('\033[0m')
print('\033[0m')
