import easyocr
import cv2
from capture import capture_screen

# Initialize the OCR reader (English)
reader = easyocr.Reader(["en"])

def extract_kill_feed_text():
    """Captures the kill feed and extracts text using OCR."""
    frame = capture_screen()  # Capture the kill feed region
    results = reader.readtext(frame, detail=0)  # Extract only text, no bounding boxes
    return results

if __name__ == "__main__":
    # Test OCR functionality
    extracted_text = extract_kill_feed_text()
    
    print("\nKill Feed OCR Output:")
    for line in extracted_text:
        print(f"- {line}")
