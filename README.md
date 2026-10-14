# Computer Vision Experiments

A collection of Python examples for basic image processing, motion detection,
YOLO object detection, segmentation, tracking, and object counting. It includes
sample images and videos, along with the YOLO model weights used by the examples.

## Contents

| Folder/file | Description |
| --- | --- |
| `lec1/` | OpenCV image processing, drawing, image display, and camera motion detection |
| `Lec2/` | YOLO object detection from an image or live camera |
| `object_tracking_counting/` | YOLO image/video detection, tracking, segmentation, and counting |
| `R-CNN lec1/` | Image and notes for an R-CNN lesson; no runnable Python script currently included |
| `README.md` | Project overview, setup, and run instructions |
| `yolov8n.pt` | YOLOv8 nano detection model used by detection/tracking examples |
| `yolov8n-seg.pt` | YOLOv8 nano segmentation model used by the segmentation example |
| `requirements.txt` | Python package dependencies |
| `.gitignore` | Excludes local virtual environments and generated Python cache files |

## Requirements

- Python 3.8 or newer
- A desktop environment capable of opening OpenCV windows for scripts using
  `cv2.imshow`
- A webcam for the live-camera examples

The included videos, images, and model weights are tracked with the project;
the local `hand_on_cv` virtual environment is not. Create a fresh environment
after cloning rather than copying that directory.

## Setup

Run these commands from the project root.

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The first run of a script may take longer while it loads the model. The
repository includes the model weight files, so run the scripts from
the project root to let their relative model, image, and video paths resolve.

## Run the examples

Each command below is run from the project root, with the virtual environment
activated.

### `lec1/`: OpenCV basics

| Command | What it does | Input/output |
| --- | --- | --- |
| `python lec1/annoataion.py` | Draws a line on an in-memory blank canvas | The current script does not display or save the canvas |
| `python lec1/cam_capture.py` | Detects motion from a webcam and displays frames with motion | Uses camera index `0`; writes `motion_detected.jpg` when motion is detected |
| `python lec1/image_process.py` | Displays resized, grayscale, blurred, and edge-detected versions of an image | Reads `dataset-card.png`; press a key to close the windows |
| `python lec1/read_image.py` | Displays two images | Reads `download.jpeg` and `dataset-card.png`; writes/overwrites `output_image.jpg` |

### `Lec2/`: YOLO detection

| Command | What it does | Input/output |
| --- | --- | --- |
| `python "Lec2/live_cam.py"` | Runs YOLO object detection on live camera frames | Uses camera index `2`; press `q` to quit |
| `python Lec2/simple_object_detect.py` | Runs YOLO object detection on one image | Reads `output_image.jpg`; press a key to close the window |

### `object_tracking_counting/`: detection, tracking, and segmentation

| Command | What it does | Input/output |
| --- | --- | --- |
| `python object_tracking_counting/live_cam.py` | Runs live YOLO object detection | Uses camera index `2` (Brio 100 on the original Linux setup); press `q` to quit |
| `python object_tracking_counting/object_detection.py` | Detects objects in one image | Reads `download.jpeg`; press a key to close the window |
| `python object_tracking_counting/multiple_object.py` | Detects people in a video | Reads `tracking.mp4`; press `q` to quit |
| `python object_tracking_counting/object_counting.py` | Tracks people and displays the number of unique track IDs | Reads `walking.mp4`; press `q` to quit |
| `python object_tracking_counting/segmenation.py` | Tracks people and overlays segmentation masks | Reads `walking.mp4`; press `q` to quit |
| `python object_tracking_counting/walking_tracking.py` | Tracks vehicles and draws IDs and trails | Reads `car_tracking.mp4`; writes/overwrites `annotated_round_racking.mp4`; press `q` to quit |

### Camera selection

Camera indices depend on the computer and operating system. Change the index
in the relevant script if the camera does not open:

- `object_tracking_counting/live_cam.py`: set `USB_CAMERA_INDEX`
- `lec1/cam_capture.py`: change `cv2.VideoCapture(0)`
- `Lec2/live_cam.py`: change `cv2.VideoCapture(2)`

On the original Linux computer, the Brio 100 is `/dev/video2` (OpenCV index
`2`), and the built-in webcam is `/dev/video0` (index `0`). Another computer
may assign different indices. On Linux, `v4l2-ctl --list-devices` can help
identify available camera devices if the `v4l-utils` package is installed.

## Sample assets

The following media files are included. Some are inputs to the scripts above;
the rest are example or previously generated media.

| File | Use |
| --- | --- |
| `download.jpeg` | Input image for `lec1/read_image.py` and `object_tracking_counting/object_detection.py` |
| `dataset-card.png` | Input image for `lec1/image_process.py` and `lec1/read_image.py` |
| `output_image.jpg` | Image generated by `lec1/read_image.py`; input to `Lec2/simple_object_detect.py` |
| `walking.mp4` | Input to person counting/tracking and segmentation examples |
| `tracking.mp4` | Input to `object_tracking_counting/multiple_object.py` |
| `car_tracking.mp4` | Input to `object_tracking_counting/walking_tracking.py` |
| `cars.mp4`, `round_car.mp4`, `street.mp4`, `vechile_tracking.mp4`, `walk_pepole.mp4`, `pople_walking.mp4`, `bottle-detection.mp4` | Additional sample video files |
| `annotated_car_tracking.mp4`, `annotated_round_racking.mp4`, `annotated_tracking.mp4`, `annotated_vehicle_tracking.mp4` | Example annotated/output videos; `walking_tracking.py` overwrites `annotated_round_racking.mp4` when run |
| `Object_detected_live_cam.png`, `Object Detection_screenshot_14.10.2026.png` | Example screenshots |
| `R-CNN lec1/image.png`, `R-CNN lec1/Note` | R-CNN lesson reference image and notes |

## Notes

- These are individual learning scripts, not one integrated application. Run
  the script for the example you want to try.
- Scripts that show a window require a graphical desktop session; a
  headless/server environment will not display OpenCV windows by default.
- `output_image.jpg`, `motion_detected.jpg`, and
  `annotated_round_racking.mp4` are written in the current working directory.
- The repository ignores the local `hand_on_cv` virtual environment and Python
  cache files. Install dependencies using `requirements.txt` instead.
