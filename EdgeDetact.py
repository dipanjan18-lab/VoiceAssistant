from PIL import Image, ImageFilter
import datetime

Input_picture = "Gradient Now or Never Quote Wallpaper Dekstop (4)_page-0001.jpg"
# Opening the image (R prefixed to string
# in order to deal with '\' in paths)
image = Image.open(f"C:/Users/dipan/OneDrive/Pictures/Camera Roll/{Input_picture}")

# Converting the image to grayscale, as edge detection
# requires input image to be of mode = Grayscale (L)
image = image.convert("L")

# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)

# Time
current_time = datetime.datetime.now()

# Printing attributes of now().
New_filename = (f"{current_time.day}_{current_time.month}_{current_time.year}-{current_time.hour}_{current_time.minute}")
print(New_filename)

# Saving the Image Under the name Edge_Sample.png
image.save(f"C:/RIKI/images/{New_filename}.png")
