# Overview:

```generate_maps```: Starts the mapping process of multiple scenes. These can be simply defined in the exp file with the correct identifier. Produces the resulting mesh + serialized voxel information


roslaunch kimera_interfacer predict_generic_scene.launch scene:=scene0000 aux_labels:=0.0 prob_main:=0 label_identifier:=create_labels_from_gt fps:= 0.5 prob_aux:= 0 voxel_size:= 0.05 label_identifier_out:=create_labels_from_gt_reprojected2 sub_reprojected:= 1


```generate_labels```: Reprojects the map back to the image plane for the full camera trajektory. Produces .png with class probabilities for each frame in the sequence and automatically creates the .png with the ```_reprojected``` identifier.

```dl_mock```: Allows publish information for Kimera-Semantics for ScanNet and pre-inferenced semantic labels.
