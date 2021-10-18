from mpi4py import MPI
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

def plot(image, title):
    plot.i += 1
    plt.subplot(2, 2, plot.i)
    plt.imshow(image)
    plt.gray()
    plt.title(title)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Parallel Grayscaling image
'''
if rank == 0:
    img = misc.face()
    height = img.shape[0]
    width = img.shape[1]
    chunks = np.array_split(img, size - 1, 0)
    for slave_node_index in range(0, size - 1):
        comm.send(chunks[slave_node_index], dest = slave_node_index + 1)
    result = []
    for k in range(1, size):
        result += comm.recv(source=k)
    misc.imsave("newface.png", result)
else:
    image_chunk = comm.recv(source=0)
    grey_image = []
    chunk_height = image_chunk.shape[0]
    chunk_width = image_chunk.shape[1]
    for i in range(chunk_height):
        inner_arr = []
        for j in range(chunk_width):
            value = image_chunk[i, j, 0]
            inner_arr.append([value, value, value])
        grey_image.append(inner_arr)
    comm.send(grey_image, dest=0)
'''
plot.i = 0
# Load data... , Must be Gray image
im = misc.imread('lena.png')
data = np.array(im, dtype=float)
plot(data, 'Original')
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])
high_pass_3x3 = ndimage.convolve(data, kernel)
plot(high_pass_3x3, 'Simple 3x3 High pass')
#kernel = np.array([[-1, -1, -1, -1, -1],
#                   [-1,  1,  2,  1, -1],
#                   [-1,  2,  4,  2, -1],
#                   [-1,  1,  2,  1, -1],
#                   [-1, -1, -1, -1, -1]])
#highpass_5x5 = ndimage.convolve(data, kernel)
#plot(highpass_5x5, 'Simple 5x5 High pass')
plt.show()
