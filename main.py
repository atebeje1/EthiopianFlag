from PIL import Image
import numpy as np

def Ethiopian_flag(fileName):
  data = np.ones((600, 1200, 3), dtype = np.uint8)
  data[0:200, 0:1200] = [0, 154, 68]
  data[200:400, 0:1200] = [254, 221, 0]
  data[400:600, 0:1200] = [239, 51, 64]
  print(data)
  img = Image.fromarray(data, 'RGB')
  img.save(fileName)
  img.show()

Ethiopian_flag('flag.png')