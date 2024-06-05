import argparse
import gdown
import os

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Download a file based on dataset')

# Add an argument for the dataset
parser.add_argument('dataset', choices=['lip', 'atr', 'pascal'], help='Dataset name')

# Parse the command-line arguments
args = parser.parse_args()

# Set the URL based on the dataset
if args.dataset == 'lip':
    url = 'https://drive.google.com/uc?id=1k4dllHpu0bdx38J7H28rVVLpU-kOHmnH'
elif args.dataset == 'atr':
    url = 'https://drive.google.com/uc?id=1ruJg4lqR_jgQPj-9K0PP-L2vJERYOxLP'
elif args.dataset == 'pascal':
    url = 'https://drive.google.com/uc?id=1E5YwNKW2VOEayK9mWCS3Kpsxf-3z04ZE'

# Set the output file path
os.makedirs('checkpoints', exist_ok=True)
output = 'checkpoints/final.pth'

# Download the file
gdown.download(url, output, quiet=False)