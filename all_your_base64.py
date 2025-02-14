# This script is not intended for real-world security use and was created as part of the Lighthouse Labs Cybersecurity Bootcamp for educational purposes. Base64 is not encryption—if you use it to "secure" sensitive data, you’re doing it wrong.

import base64
import sys

def encode_text(text):
    """Encodes text into Base64."""
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode_text(encoded_text):
    """Decodes Base64 back into text."""
    try:
        decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        return f"Decoding failed! Are you sure that's Base64? Error: {e}"

def main():
    if len(sys.argv) < 3:
        print("Usage: python all_your_base64.py [encode|decode] \"your text here\"")
        sys.exit(1)

    action = sys.argv[1].lower()
    text = " ".join(sys.argv[2:])
    if action == "encode":
        print(f"Encoded Text: {encode_text(text)}")
    elif action == "decode":
        print(f"Decoded Text: {decode_text(text)}")
    else:
        print("Invalid action! Use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
