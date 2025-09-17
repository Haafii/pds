import webbrowser
import os

#file_path = os.path.abspath("echart2.html")
file_path = os.path.abspath("echart.html")
print(file_path)
webbrowser.open(f"file://{file_path}")