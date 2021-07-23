import cv2
import argparse

# Parse command prompt args
parser = argparse.ArgumentParser(description='Get Size and Resize images')
parser.add_argument('--input', type=str, required=True,
                    help='[REQUIRED] Source image path')
parser.add_argument('--output', type=str, required=True,
                    help='[REQUIRED] Destination image path like: output.jpg')
parser.add_argument('--display_height', type=str, required=False, default= '0',
                    help='[OPTIONAL] Display window height size')
parser.add_argument('--display_width', type=str, required=False, default= '0',
                    help='[OPTIONAL] Display window width size')
parser.add_argument('--output_height', type=str, required=False, default= '0',
                    help='[OPTIONAL] Output image height')
parser.add_argument('--output_width', type=str, required=False, default= '0',
                    help='[OPTIONAL] Output image width')

args = parser.parse_args()

def main(args):
    # Display window name
    window_name = 'Image'
    # Read image
    image = cv2.imread(args.input)
    
    # Dispay source image width, height, and channel
    print(' Source image width: ', image.shape[1])
    print(' Source image height: ', image.shape[0])
    print(' Source image channel [1: Gray scale, 3: RGB]: ', image.shape[2])
    print('\n<------------------------------------------------>\n')
    
    if int(args.display_height) > 0 and int(args.display_width) > 0:
        # Create a normal window size
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        
        # Display image in customized window size
        cv2.resizeWindow(window_name, int(args.display_width), int(args.display_height))
    
    # Display image
    cv2.imshow(window_name, image)
    
    # Hold image until user press any key
    cv2.waitKey(0)
    
    # Close all windows
    cv2.destroyAllWindows()
    
    
    if int(args.output_height) > 0 and int(args.output_width) > 0:
        # Resize image
        image = cv2.resize(image, (int(args.output_width), int(args.output_height)))
    
    # Write image
    cv2.imwrite(args.output, image)
    
    # Dispay output image width, height, and channel
    print(' Output image width: ', image.shape[1])
    print(' Output image height: ', image.shape[0])
    print(' Output image channel [1: Gray scale, 3: RGB]: ', image.shape[2])

main(args)