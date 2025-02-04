import cv2
import numpy as np
import pyautogui

# Define the region where the kill feed appears (adjust based on your resolution)
KILL_FEED_REGION = (100, 200, 400, 150)  # (x, y, width, height)

def capture_screen():
    """Captures the Fortnite kill feed region and returns an image."""
    screenshot = pyautogui.screenshot(region=KILL_FEED_REGION)
    frame = np.array(screenshot)
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

if __name__ == "__main__":
    while True:
        frame = capture_screen()
        cv2.imshow("Kill Feed Capture", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
