import os
import shutil
import time 

delete_file_name_path=["predict","results_Epoch100_map0.5","results_Epoch100_map0.6","results_Epoch100_map0.7","result_csv_iou05","result_csv_iou06","result_csv_iou07"]
for delete_file_name_path_index in delete_file_name_path:
    if os.path.exists(delete_file_name_path_index):
        shutil.rmtree(delete_file_name_path_index)
    if os.path.exists(delete_file_name_path_index+"_frist_times_has_flip"):
        shutil.rmtree(delete_file_name_path_index+"_frist_times_has_flip")

delete_text_path = ["2007_test.txt","2007_train.txt","2007_val.txt"]
for  delete_text_path_index in delete_text_path :
    try:
        os.remove("./"+delete_text_path_index)
    except OSError as e:
        print(e)
    else:
        print("so delete")
os.system("python ./voc_annotation.py")

create_path =["./input","./predict"]
for create_path_index in create_path:
    if os.path.exists(create_path_index ):
        shutil.rmtree(create_path_index)
    time.sleep(.0000000000000001)
    os.makedirs(create_path_index)

#os.system("python ./train.py ")
os.system("python ./get_gt_txt.py ")
os.system("python ./read_txt.py ")

""""
for i in range(1,2):
    os.system("python ./FPS_test.py "+str(i))
    os.system("python ./get_dr_txt.py "+str(i))
    os.system("python ./get_map_05.py "+str(i))
    os.system("python ./get_map_06.py "+str(i))
    os.system("python ./get_map_07.py "+str(i))
    if(i==100):
        os.system("python ./predict.py "+str(i))
    #shutil.rmtree("./input/detection-results")
    #shutil.rmtree("./input/images-optional")
    

change_file_name_path=["predict","results_Epoch100_map0.5","results_Epoch100_map0.6","results_Epoch100_map0.7","result_csv_iou05","result_csv_iou06","result_csv_iou07"]
for  change_file_name_path_index  in change_file_name_path:
    print( change_file_name_path_index )
    os.rename(change_file_name_path_index,change_file_name_path_index+"_frist_times_has_flip")
"""

