import imageio.v3 as iio

filenames = ['pic 1.png', 'pic 2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)