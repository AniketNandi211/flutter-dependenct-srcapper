from utils import printHtml, copy_to_clipboard
from flutter_dependecy_extractor import extract_flutter_package_versions

if __name__ == "__main__":
    extract_flutter_package_versions()
else:
    print("Please run the file from main.py")
