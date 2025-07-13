"# TictacToe-with-Ai" 
# I have used pygame for the ui of the game and also with the help of pygame functions what change will happen if i pressed the right click of mouse 
# done backend with python 
# Used BFS to help ai to make the best decision when player commit a change in the game board. Thank you 
🚀 Overall Process
1️⃣ Collected two datasets from Kaggle:

Dataset 1: Plastic Bottle Image Dataset (/content/data1)

Dataset 2: Images of Waste filtered for PET/HDPE only (/content/data2)

2️⃣ Cleaned and normalized dataset 2:

Filtered for PET/HDPE files

Renamed files to remove commas

Remapped their class to 0

3️⃣ Merged both datasets into a single YOLOv8-compatible folder structure:

kotlin
Copy
Edit
bottle_data/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
4️⃣ Created bottle.yaml with dataset configuration.

5️⃣ Trained a YOLOv8 nano (yolov8n.pt) model on the merged dataset.

6️⃣ Validated the model on the val set and checked key metrics.

7️⃣ Saved best.pt and other artifacts to persistent storage
