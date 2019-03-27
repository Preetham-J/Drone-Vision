#!/bin/bash
# This script will download the SSDlite MobileNetV2 and YOLOv3 models from their official sources

echo "Downloading SSD MobileNetv2 and YOLOV3 models..."

mkdir -p models/ssd_mobilenetv2 && cd models
wget https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/ssd_mobilenet_v2_coco_2018_03_29.pbtxt -P ssd_mobilenetv2
wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
tar -C ssd_mobilenetv2 -xzf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz ssdlite_mobilenet_v2_coco_2018_05_09/frozen_inference_graph.pb --strip-components=1
rm ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz

mkdir yolov3
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg -P yolov3/
wget https://pjreddie.com/media/files/yolov3.weights -P yolov3/

echo "Completed downloading models!"
