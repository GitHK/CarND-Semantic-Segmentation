import imageio

DATA_DIR = './1545576582.0125058/'

from os import listdir
from os.path import isfile, join

image_files = [DATA_DIR + f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f)) if f.endswith('.png')]

images = []
for filename in image_files:
    images.append(imageio.imread(filename))
imageio.mimsave(DATA_DIR.replace('./', '').replace('/', '') + '.gif', images)

if __name__ == '__main__':
    pass
