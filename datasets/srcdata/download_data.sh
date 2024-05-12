pip install kaggle
kaggle datasets download -d valerytamrazov/msrvttqa
unzip msrvttqa
mkdir msrvtt
cd msrvtt && mkdir videos && cd ..
mv archive/TrainValVideo/*.mp4 msrvtt/videos/
rm -rf archive/