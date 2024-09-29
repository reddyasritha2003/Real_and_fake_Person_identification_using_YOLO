from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data='Dataset/splitData/dataoffline.yaml', epochs=5)



