from PIL import Image
import numpy as np

# Load the image
image_path = r'C:\Users\jadej\OneDrive\Pictures\Nitro\Nitro_Wallpaper_01_3840x2400.jpg'  # Replace with your image path
image = Image.open(r'C:\Users\jadej\OneDrive\Pictures\Nitro\Nitro_Wallpaper_01_3840x2400.jpg')

# Convert image to NumPy array
image_np = np.array(image)

# Dimension of the image (height, width)
height, width = image_np.shape[:2]
print(f"Dimension of the image: {height} x {width}")

# Shape of the image (height, width, channels)
print(f"Shape of the image: {image_np.shape}")

# Minimum pixel value in the Blue channel
# Pillow uses RGB order, so Blue channel is index 2
min_blue = image_np[:, :, 2].min()
print(f"Minimum pixel value in Blue channel: {min_blue}")