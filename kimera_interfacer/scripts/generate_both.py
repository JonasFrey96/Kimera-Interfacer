import os
import time
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--exp",
    default="/home/jonfrey/ASL/cfg/exp/MA/scannet_self_supervision/create_labels_from_pretrained.yml",
    help="The main experiment yaml file.",
  )
  args = parser.parse_args()
  exp_cfg_path = args.exp

  cmd = f"""/bin/bash -c " source ~/conda.sh && conda deactivate && conda deactivate && which python3 && cd /home/jonfrey/catkin_ws/src/Kimera-Interfacer/kimera_interfacer/scripts && /usr/bin/python3 generate_maps.py --exp="{exp_cfg_path}" " """

  print(cmd)
  os.system(cmd)

  time.sleep(5)

  cmd = f"""/bin/bash -c " cd /home/jonfrey/catkin_ws/src/Kimera-Interfacer/kimera_interfacer/scripts && source ~/conda.sh && /home/jonfrey/miniconda3/envs/track4/bin/python generate_labels.py --exp="{exp_cfg_path}" " """
  print(cmd)
  os.system(cmd)
