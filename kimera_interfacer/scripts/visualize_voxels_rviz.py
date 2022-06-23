if __name__ == "__main__":
  import os
  import sys

  sys.path.append(os.path.dirname(os.getcwd()) + "/scripts")
  sys.path.append(os.path.dirname(os.getcwd()) + "/scripts/pseudo_labels")
  print(os.path.dirname(os.getcwd()))

from label_generation import VoxelMap
from label_generation import RayCaster
from label_generation import Visualizer3D

if __name__ == "__main__":
  voxel_map = VoxelMap(map_serialized_path, size, r_sub)
