# Simple get size, and resize images using OpenCV

A simple code snippet to get size, and resize images using the Python OpenCV library.
**Python >= 3.6**

## Windows

### Step 1 - Clone repository

    git clone https://github.com/BehzadRp98/SizeResizeImages_Python_Component.git

### Step 2 - Optional step
It is recommended that a virtual environment be enabled to install and test the code snippet.

##### 1 - Install python virtual enviroment

    python -m pip install virtualenv

##### 2 - Create a virtual enviroment

    python -m venv srImages

##### 3 - Activate virtual enviroment

    srImagesEnv\Scripts\activate

### Step 3 - Install requirements

    python -m pip install -r requirements.txt

### Step 4 - Quick start
To test the repository quickly there is a flower photo in "images" folder:

    python srImages.py --input images\flower.jpg --output out.png --display_height 500 --display_width 500 --output_height 500 --output_width 500

All options:

    python srImages.py --help
    usage: srImages.py [-h] --input INPUT --output OUTPUT [--display_height DISPLAY_HEIGHT]
                           [--display_width DISPLAY_WIDTH] [--output_height OUTPUT_HEIGHT] [--output_width OUTPUT_WIDTH]
        
        Get Size and Resize images
        
        optional arguments:
          -h, --help            show this help message and exit
          --input INPUT         [REQUIRED] Source image path
          --output OUTPUT       [REQUIRED] Destination image path like: output.jpg
          --display_height DISPLAY_HEIGHT
                                [OPTIONAL] Display window height size
          --display_width DISPLAY_WIDTH
                                [OPTIONAL] Display window width size
          --output_height OUTPUT_HEIGHT
                                [OPTIONAL] Output image height
          --output_width OUTPUT_WIDTH
                                [OPTIONAL] Output image width

## Unbutu
### Step 1 - Clone repository

    git clone https://github.com/BehzadRp98/SizeResizeImages_Python_Component.git

### Step 2 - Optional step
It is recommended that a virtual environment be enabled to install and test the code snippet

##### 1- Install python virtual enviroment

    python3 -m pip install virtualenv

##### 2 - Create a virtual enviroment

    python3 -m venv srImages

##### 3 - Activate virtual enviroment

    source ./srImages/bin/activate

##### NOTE: If virtual enviroment activated use "python" instead of "python3"

### Step 3 - Install requirements

    python3 -m pip install -r requirements.txt

### Step 4 - Quick start
To test the repository quickly there is a flower photo in "images" folder:

    python3 srImages.py --input ./images/flower.jpg --output ./out.png --display_height 500 --display_width 500 --output_height 500 --output_width 500

All options:

    python3 srImages.py --help
    usage: srImages.py [-h] --input INPUT --output OUTPUT [--display_height DISPLAY_HEIGHT]
                       [--display_width DISPLAY_WIDTH] [--output_height OUTPUT_HEIGHT] [--output_width OUTPUT_WIDTH]
    
    Get Size and Resize images
    
    optional arguments:
      -h, --help            show this help message and exit
      --input INPUT         [REQUIRED] Source image path
      --output OUTPUT       [REQUIRED] Destination image path like: output.jpg
      --display_height DISPLAY_HEIGHT
                            [OPTIONAL] Display window height size
      --display_width DISPLAY_WIDTH
                            [OPTIONAL] Display window width size
      --output_height OUTPUT_HEIGHT
                            [OPTIONAL] Output image height
      --output_width OUTPUT_WIDTH
                            [OPTIONAL] Output image width

## Raspberry Pi 4

### Step 1 - Clone repository

    git clone https://github.com/BehzadRp98/SizeResizeImages_Python_Component.git

### Step 2 - Optional step
It is recommended that a virtual environment be enabled to install and test the code snippet

##### 1 - Install python virtual enviroment

    python3 -m pip install virtualenv

##### 2 - Create a virtual enviroment

    python3 -m venv srImages

##### 3 - Activate virtual enviroment

    source ./srImages/bin/activate

##### NOTE: If virtual enviroment activated use "python" instead of "python3"

### Step 3 - Install requirements
OpenCV is the only requirement of this repository. To install it on Raspberry Pi 4, follow steps in https://qengineering.eu/install-opencv-4.3-on-raspberry-pi-4.html

### Step 4 - Quick start
To test the repository quickly there is a flower photo in "images" folder:

    python3 srImages.py --input ./images/flower.jpg --output ./out.png --display_height 500 --display_width 500 --output_height 500 --output_width 500

All options:

    python3 srImages.py --help
    usage: srImages.py [-h] --input INPUT --output OUTPUT [--display_height DISPLAY_HEIGHT]
                       [--display_width DISPLAY_WIDTH] [--output_height OUTPUT_HEIGHT] [--output_width OUTPUT_WIDTH]
    
    Get Size and Resize images
    
    optional arguments:
      -h, --help            show this help message and exit
      --input INPUT         [REQUIRED] Source image path
      --output OUTPUT       [REQUIRED] Destination image path like: output.jpg
      --display_height DISPLAY_HEIGHT
                            [OPTIONAL] Display window height size
      --display_width DISPLAY_WIDTH
                            [OPTIONAL] Display window width size
      --output_height OUTPUT_HEIGHT
                            [OPTIONAL] Output image height
      --output_width OUTPUT_WIDTH
                            [OPTIONAL] Output image width
