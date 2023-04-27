import cv2
import os

# Define the video file path
# video_path = 'Users\Maruf\Downloads\nn.mp4'
home_dir = os.path.expanduser('~')

# Set the video file name and path
video_name = 'nn.mp4'
video_path = os.path.join(home_dir, 'Downloads', video_name)

# Create a directory to store the screenshots
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print('Error: Could not open video file')
    exit()

# Initialize a variable to keep track of the current second
current_second = 0

# Loop through the video frames
while True:
    # Read the next frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Get the current frame number
    frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)

    # Get the current time in seconds
    current_time = frame_num / cap.get(cv2.CAP_PROP_FPS)

    # Check if we have reached a new second
    if current_time >= current_second + 1:
        # Set the current second to the new second
        current_second = int(current_time)

        # Save the current frame as a screenshot
        screenshot_path = os.path.join('screenshots', f'screenshot_{current_second}.jpg')
        cv2.imwrite(screenshot_path, frame)

# Release the video file
cap.release()


## for time frame
# # Create a directory to store the screenshots
# if not os.path.exists('screenshots'):
#     os.makedirs('screenshots')

# # Open the video file
# cap = cv2.VideoCapture(video_path)

# # Check if the video file was opened successfully
# if not cap.isOpened():
#     print(f'Error: Could not open video file "{video_path}"')
#     exit()

# # Initialize a variable to keep track of the current minute
# current_minute = 0

# # Loop through the video frames
# while True:
#     # Read the next frame
#     ret, frame = cap.read()

#     # Check if the frame was read successfully
#     if not ret:
#         break

#     # Get the current frame number
#     frame_num = cap.get(cv2.CAP_PROP_POS_FRAMES)

#     # Get the current time in seconds
#     current_time = frame_num / cap.get(cv2.CAP_PROP_FPS)

#     # Check if we have reached a new minute
#     if current_time >= current_minute + 60:
#         # Set the current minute to the new minute
#         current_minute = int(current_time / 60)

#     # Check if the current time is a multiple of 20 seconds
#     if int(current_time) % 20 == 0:
#         # Save the current frame as a screenshot
#         screenshot_path = os.path.join('screenshots', f'screenshot_{current_minute}_{int(current_time)}.jpg')
#         cv2.imwrite(screenshot_path, frame)

# # Release the video file
# cap.release()
# print("SS DOne")