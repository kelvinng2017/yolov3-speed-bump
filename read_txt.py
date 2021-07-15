import os
import csv
from sys import path
def mkdir(path):
    folder =os.path.exists(path)
    if not folder:
         os.makedirs(path)
         print("new folder")
    else:
        print("There is this folder")


need_save_csv =['ap','f1','prec','rec','tpfp']
print(need_save_csv[-1])


for file_index in range(5,8):
    file = "./result_csv_iou0"+str(file_index)
    mkdir(file)
    txt_path ='./model_data/npustspeedbump.txt'
    f_txt= open(txt_path,'r')
    lines  =  f_txt.readlines()
    for line in lines:
        line_split = line.split("\n")
        print(line_split[0])
        for need_save_csv_index in need_save_csv:
            print(need_save_csv_index)
            if need_save_csv_index == "tpfp":
                header_of_csv = ["epochname","tp","fp"]
                with open('./result_csv_iou0'+str(file_index)+'/'+line_split[0]+'_tpfp.csv','w',encoding='UTF8',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header_of_csv)
            else:
                header_name2 = need_save_csv_index
                header_of_csv = ["epochname",header_name2]
                with open('./result_csv_iou0'+str(file_index)+'/'+line_split[0]+'_'+header_name2+'.csv','w',encoding='UTF8',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header_of_csv)


header_fps =["epoch","result"]
with open ('./result_csv_iou05/fps_result.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header_fps )
"""
test1 ="a"
test2="b"
header = ["test1",test2]
print(type(header))
with open('./test/countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
"""

"""
txt_path ='./model_data/voc_classes.txt'
f = open(txt_path,'r')
lines  = f.readlines()
#txt_dict={}

for line in lines:
    line_split = line.split("\n")
    print(line_split[0])
"""

