
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image

# Dataset path
DATASET_DIR = (
    Path.home()
    / "Downloads"
    / "Rice Leaf Disease Image Samples"
    / "Rice Leaf Disease Images"
)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# Find image files for each class
class_dirs = sorted(
    folder for folder in DATASET_DIR.iterdir()
    if folder.is_dir()
)

class_images = {}

for folder in class_dirs:
    class_images[folder.name] = sorted(
        image for image in folder.iterdir()
        if image.is_file()
        and image.suffix.lower() in IMAGE_EXTENSIONS
    )

# Print class counts
print("RICE LEAF DISEASE DATASET")
print("-" * 35)

for class_name, images in class_images.items():
    print(f"{class_name}: {len(images)} images")

print("Total images:", sum(len(images) for images in class_images.values()))

# Plot class distribution
plt.figure(figsize=(9, 5))
plt.bar(
    class_images.keys(),
    [len(images) for images in class_images.values()]
)
plt.title("Rice Leaf Disease Dataset: Class Distribution")
plt.xlabel("Disease Class")
plt.ylabel("Number of Images")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("class_distribution.png", dpi=200)
plt.show()

# Display three sample images per class
fig, axes = plt.subplots(
    len(class_dirs), 3,
    figsize=(10, 12)
)

for row, folder in enumerate(class_dirs):
    images = class_images[folder.name]

    for col in range(3):
        with Image.open(images[col]) as image:
            axes[row, col].imshow(image.convert("RGB"))

        axes[row, col].set_title(folder.name)
        axes[row, col].axis("off")

fig.suptitle("Sample Images from Each Rice Leaf Disease Class")
plt.tight_layout()
plt.savefig("sample_images.png", dpi=200)
plt.show()

print("\nSaved class_distribution.png")
print("Saved sample_images.png")
