# Detect number from image using OCR (Optical Character Recognition) with Python

import cv2
import requests
import io
import json

# Load an image from a file
img = cv2.imread("number.jpg")

# Url ocr API for send image
url_api = "https://api.ocr.space/parse/image"

# Encodes an image into a memory buffer using imencode with quality 100
_, compressedimage = cv2.imencode(".jpg", img, [100])

# Convert the image into bytes before sent to server
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              # File name and file bytes after compressed
              files = {"number.jpg": file_bytes},
              #KEY OCR API       
              data = {"apikey": "YOURAPIKEY"})

# Decode the bytes using codec registered for encoding
result = result.content.decode()
# Parse data for JSON string
result = json.loads(result)

# Get result OCR
parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
# Print result OCR
print("Result OCR")
print(text_detected)

# Get total of element
n = len(text_detected)
# Apply a function on all the elements of specified iterable and return map object
arr = list(map(int,text_detected.strip().split()))[:n]

# Sort number from smallest to biggest value
arr.sort()
print("Result Sort from smallest to biggest value", arr)

# Sort number form biggest to smallest value
arr.sort(reverse=True)
print("Result Sort from biggest to smallest value", arr)