import os
import random
import shutil

# Paths
data_dir = './images'  # Current directory with .jpg files
labels_dir = './labels'  # Directory containing corresponding .txt files

valid_images_dir = '../valid/images'
valid_labels_dir = '../valid/labels'

test_images_dir = '../test/images'
test_labels_dir = '../test/labels'

# Create output directories if they don't exist
os.makedirs(valid_images_dir, exist_ok=True)
os.makedirs(valid_labels_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)

# Get all .jpg files in the current directory
jpg_files = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]

# Shuffle and select 10% for validation and 10% for testing
random.shuffle(jpg_files)
num_valid = len(jpg_files) // 10
num_test = len(jpg_files) // 10

valid_files = jpg_files[:num_valid]
test_files = jpg_files[num_valid:num_valid + num_test]

def move_files(files, src_images_dir, src_labels_dir, dest_images_dir, dest_labels_dir):
    for file in files:
        base_name = os.path.splitext(file)[0]
        image_src = os.path.join(src_images_dir, file)
        label_src = os.path.join(src_labels_dir, base_name + '.txt')

        # Destination paths
        image_dest = os.path.join(dest_images_dir, file)
        label_dest = os.path.join(dest_labels_dir, base_name + '.txt')

        # Move image file
        if os.path.exists(image_src):
            shutil.move(image_src, image_dest)

        # Move corresponding label file
        if os.path.exists(label_src):
            shutil.move(label_src, label_dest)

# Move validation files
move_files(valid_files, data_dir, labels_dir, valid_images_dir, valid_labels_dir)

# Move test files
move_files(test_files, data_dir, labels_dir, test_images_dir, test_labels_dir)

print("Files have been successfully moved.")
