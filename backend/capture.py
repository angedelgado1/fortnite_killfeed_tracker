import cv2
import numpy as np
import pyautogui

# Define the region where the kill feed appears (adjust based on your resolution)
KILL_FEED_REGION = (100, 200, 400, 150)  # (x, y, width, height)

# Frame skipping settings
frame_skip = 10  # Only process every 10th frame
frame_count = 0  # Counter to track frame numbers

# Toggle between live game capture or video testing
USE_VIDEO = False  # Set to True to test with video instead of live feed
VIDEO_PATH = "test_videos/killfeed_test.mp4"

# Load video if testing with recorded footage
if USE_VIDEO:
    cap = cv2.VideoCapture(VIDEO_PATH)

def capture_screen():
    """Captures the Fortnite kill feed region from the screen or video."""
    global frame_count

    frame_count += 1
    if frame_count % frame_skip != 0:  # Skip frames
        return None

    if USE_VIDEO:
        # Capture from video
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video if it ends
            return None
    else:
        # Capture from live screen
        screenshot = pyautogui.screenshot(region=KILL_FEED_REGION)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    return frame

if __name__ == "__main__":
    while True:
        frame = capture_screen()
        if frame is not None:
            cv2.imshow("Kill Feed Capture", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
