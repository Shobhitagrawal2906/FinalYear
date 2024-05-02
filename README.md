# Vehicle Speed Detection using YOLOv8

![Demo](demo.gif)

## Overview

This repository contains the implementation of a real-time vehicle speed detection system using YOLOv8, a state-of-the-art object detection model. The system is capable of accurately identifying vehicles in video footage, tracking their movements, and estimating their speeds based on their displacements between consecutive frames.

## Key Features

- **Real-time Speed Estimation**: The system provides real-time estimation of vehicle speeds from video input.
- **Object Detection**: Utilizes YOLOv8 for robust vehicle detection in varying environmental conditions.
- **Object Tracking**: Implements algorithms for tracking vehicles across frames to estimate their trajectories.
- **Speed Calculation**: Computes vehicle speeds based on their displacements between frames.
- **Database storage and Output**: Stores the results in MongoDB with path to the image file in your system. Stores the images of cars crossing speed limit with a circle over it.
## Getting Started

### Prerequisites

- Python 3.x
- YOLOv8 (Prefer official Docs)
- OpenCV
- NumPy
- Matplotlib
- MongoDB

### Installation

1. Clone this repository:
   **```git clone https://github.com/Shobhitagrawal2906/FinalYear.git```**
2. Install dependencies:
   ```pip install -r requirements.txt```
### Usage

1. Download the YOLOv8 weights from the official repository or use pre-trained weights.
2. Prepare your video footage for speed detection.
3. Provide the path to video file in the constants.py
4. Download any pretrained YOLOv8 Model.
5. Create a folder "images" in the same directory as **app.py**
6. You can upload a frame of your video to **ROBOFLOW** and create ROI (Region of interest) and then download JSON file (like **highway.json**) Check: https://blog.roboflow.com/getting-started-with-roboflow/
7. Run the main script: ```python app.py```
8. Check MongoDB (recommended to install prior to running).
9. Check "images" folder.

## Sample Output

![18757614](https://github.com/Shobhitagrawal2906/FinalYear/assets/75949429/4ee07a02-85ee-4845-98e0-2ba999d0097f)


