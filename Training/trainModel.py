import os
import random
import shutil

 # Randomly splitting images in the train and test folder

def split_dataset(dataset_path, test_ratio=0.2):
    # List all files in the dataset directory
    data_list = [f for f in os.listdir(dataset_path) if os.path.isfile(os.path.join(dataset_path, f))]
    dataset_total_files = len(data_list)

    # Calculate the number of test files
    test_file_num = int(dataset_total_files * test_ratio)
    
    # Randomly sample test files without replacement
    test_files = random.sample(data_list, test_file_num)
    
    # Move test files to the 'test' directory
    for file in test_files:
        shutil.move(os.path.join(dataset_path, file), os.path.join(test_dir, file))
        print(f"Moved File {file} to test successfully!")

    # Move the remaining files to the 'train' directory
    train_files = set(data_list) - set(test_files)
    for file in train_files:
        shutil.move(os.path.join(dataset_path, file), os.path.join(train_dir, file))
        print(f"Moved File {file} to train successfully!")

    print(f"Dataset successfully split into {len(train_files)} train files and {len(test_files)} test files.")
    

dataset_path = "/home/sharjeel/dev/myenv1/projects/customStylegan2adapytorch/Dataset/img_align_celeba"
data_list = os.listdir(dataset_path)
datasetTotalFiles = len(data_list)

# Find the 80 and 20 percent of the dataset, respectively
print("Total Files:", datasetTotalFiles)
train_file_num = int(datasetTotalFiles * 0.8)
test_file_num = int(datasetTotalFiles * 0.2)
print("Train Files:", train_file_num)
print("Test Files:", test_file_num)

# Creating a test folder in the same dir as the dataset

train_dir = os.path.join(dataset_path, 'train')
test_dir = os.path.join(dataset_path, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)


split_dataset(dataset_path)