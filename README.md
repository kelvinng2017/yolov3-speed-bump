# yolov3-speed-bump-使用pytorch深度學習框架

## ubuntu18.04 教學
### cuda 11.0
+ 在google雲端下載訓練所需影像集
  - https://drive.google.com/drive/folders/1fmXyado3aHQ0QXLe5CCx_vwfddIm9ZsG?usp=sharing
  -  ![unsplash 圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%9C%A8google%E9%9B%B2%E7%AB%AF%E4%B8%8B%E8%BC%89%E5%BD%B1%E5%83%8F%E9%9B%86.png?raw=true)
  - 將下載好的影像資料存放到  yolov3-speed-bump 根目錄的 VOCdevkit文件夾
  - ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%B0%87%E5%BD%B1%E5%83%8F%E9%9B%86%E5%84%B2%E5%AD%98%E5%9C%A8vocdevkit.png?raw=true)


+ 下載yolov3預設模型
  - https://drive.google.com/file/d/1CFbBv0yhj8KYvB3grOaQ5s1Nw2euruwC/view?usp=sharing
   - ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%9C%A8google%20drive%E4%B8%8B%E8%BC%89yolov3%E9%A0%90%E8%A8%AD%E6%A8%A1%E5%9E%8B.png?raw=true)
  - 將下載好的yolov3模型存放在 yolov3-speed-bump根目錄的的model_data裡面
  - ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%B0%87yolov3%E9%A0%90%E8%A8%AD%E6%A8%A1%E5%9E%8B%E5%AD%98%E5%9C%A8model%20_data.png?raw=true)

+ 建立目標物體txt標籤名稱
    - 在yolov3-speed-bump根目錄的model_data建立npustspeedbunp.txt
     - ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%9C%A8model_data%E5%BB%BA%E7%AB%8B%E7%9B%AE%E6%A8%99%E7%89%A9%E9%AB%94txt%E5%90%8D%E7%A8%B1.png?raw=true)
     - txt的內有有
        - npustspeedbreak
        - npustspeedbump
        -  usaspeedbumprubber
        -  usaspeedbumpsign
  
+ 建立含有圖像路徑和對應物體座標文件
  -  打開ubuntu18.04 的終端幾 先啓動含有pytorch1.7深度學習框架的虛擬環境
   - ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/ubuntu18.04%E7%B5%82%E7%AB%AF%E5%B9%BE%E5%95%93%E5%8B%95%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83.png?raw=true)
   -  使用終端機尋找專案目標路徑
   -   ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/cd%20%E5%88%B0project%E7%9A%84%E8%B7%AF%E5%BE%91.png?raw=true)
   -   在終端機輸入 pytho voc_annotation
   -   ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%9F%B7%E8%A1%8C%20voc_annotation.png?raw=true)
   -   可以yolov3-speed-bump根目錄看到多了訓練集、測試集、驗證集
   -    ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%A4%9A%E4%BA%86%E4%B8%89%E5%80%8B%E6%96%87%E4%BB%B6.png?raw=true)
   -    如果txt呈現以下畫面代表讀取影像個座標文件成功
   -    ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E8%AE%80%E5%8F%96txt%E6%88%90%E5%8A%9F.png?raw=true)
  
+ 訓練yolov3 模型前置作業
  - 打開train.py  在138行將model_path輸入"model_data/yolo_weights.pth"
  -  打開train.py  在164行將annotation_path輸入"2007_train.txt"
  -  打開train.py  在108行可以修改每個epoch訓練好後儲存的文件夾，預設是存在logs
  -  打開yolo.py 按照圖下進行修改
  -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E4%BF%AE%E6%94%B9yolo%E9%A0%90%E8%A8%AD%E5%80%BC.png?raw=true)
  -  打開utils的config.py 第12行 classes的值，依據被訓練的目標物體數量進行修改
  
+ 開始訓練模型
  - 在終端機輸入 python train.py
  -  如果出現下面的畫面代表成功開始訓練
  -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E6%88%90%E5%8A%9F%E9%96%8B%E5%A7%8B%E8%A8%93%E7%B7%B4.png?raw=true)
  -  訓練  100個 epoch 左右就差不多就能訓練完成
   -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E8%A8%93%E7%B7%B4%E5%AE%8C%E6%88%90%E5%BD%B1%E5%83%8F.png?raw=true)

+ 開始測試模型
    - 在終端機輸入python run.py 可以建立儲存相關測試指標的csv和對應文件夾
    -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/run%E5%BE%8C%E5%A4%9A%E7%9A%84%E6%96%87%E4%BB%B6.png?raw=true)
    -  在終端機輸入 python FPS_test.py 100 可以計算出訓練100次後的模型其fps的速度
    -  可以在終端幾看到所得到的fps值
    -   ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E7%B5%82%E7%AB%AF%E6%A9%9F%E9%A1%AF%E7%A4%BAfps%E7%9A%84%E5%80%BC.png?raw=true)
    -   fps會保存在csv,打開yolov3-speed-bump根目錄的result_csv_iou05 的fps_result.csv,如下圖所示
    -   ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/fps%E5%AD%98%E5%9C%A8csv.png?raw=true)
    -   在終端機輸入 python get_dr_txt.py 100 可以使用第100個epoch批量偵測圖像但是只產生txt文字結果值,如下圖所示
    -   ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E6%89%B9%E9%87%8F%E5%81%B5%E6%B8%AC%E5%9C%96%E5%83%8F%E4%BD%86%E6%98%AF%E5%80%BC%E7%94%A2%E5%87%BAtxt%E5%80%BC.png?raw=true)
    -   ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E6%89%B9%E9%87%8F%E7%94%A2%E5%87%BA%E5%81%B5%E6%B8%ACtxt%E7%B5%90%E6%9E%9C%E5%80%BC.png?raw=true)
    -   在終端機輸入python get_map 05.py 100 可以使用第100個訓練好的模型計算每個目標物體的ap值、f1-score、recall、precision值
    -   可以在終端機顯示相關評估指標的值，如下圖所示
    -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%9C%A8%E7%B5%82%E7%AB%AF%E6%A9%9F%E6%B1%82ap.png?raw=true)
    -  相關評估指標也會存在csv
    -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%B0%87ap%E5%80%BC%E5%AD%98%E5%9C%A8%E5%9C%A8csv.png?raw=true)
    -  在終端機輸入python predict.py 100 可以使用第100個訓練好的模型批量偵測圖像並產出含有預測框的圖像，如下圖所示
    -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E6%89%B9%E9%87%8F%E5%81%B5%E6%B8%AC%E5%9C%96%E5%83%8F%E7%94%A2%E5%87%BA%E5%90%AB%E6%9C%89%E9%A0%90%E6%B8%AC%E6%A1%86%E7%9A%84%E5%9C%96%E5%83%8F.png?raw=true)
    -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E5%90%AB%E6%9C%89%E9%A0%90%E6%B8%AC%E6%A1%86%E7%9A%84%E6%89%B9%E9%87%8F%E5%9C%96.png?raw=true)
+ 利用影片進行減速丘、減速標線、減速標誌的偵測
    -  打開根目錄的video.py在31行的video_path的影片名稱改成需要被偵測的影片名稱
    -  打開根目錄的video.py在31行的video_save_path輸入絕對路徑保存偵測後結果的影片
    -  在終端機輸入python video.py 就可以開始偵測影片，含有預測框的影片會保存在根目錄，如下圖所示
    -  -  ![unsplash圖片](https://github.com/kelvinng2017/yolov3-speed-bump/blob/main/%E5%9C%96%E5%83%8F%E8%AA%AA%E6%98%8E/%E6%B8%AC%E8%A9%A6%E5%BD%B1%E7%89%87.png?raw=true)
    -  將含有預測框的影片傳到youtube播放
    - [![IMAGE_ALT](https://img.youtube.com/vi/UmX4kyB2wfg/0.jpg)](https://youtu.be/GAroAnBUaKs)