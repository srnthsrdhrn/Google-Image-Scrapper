from google_images_download import google_images_download
import csv
import argparse

parser = argparse.ArgumentParser(description='Input Parameters for Scrapper')
parser.add_argument('--image_count', required=False, type=int, default=10,
                    help='Number of Images to scrap per keyword')
parser.add_argument('--directory', required=False, default='downloads',
                    help='Directory to store the downloaded images')
parser.add_argument('--keywords_file', required=False, default='keywords.csv',
                    help='Location of the keywords.csv file')

args = parser.parse_args()
IMAGE_COUNT = args.image_count
DIRECTORY = args.directory
KEYWORDS_FILE = args.keywords_file
print(IMAGE_COUNT, DIRECTORY, KEYWORDS_FILE)
response = google_images_download.googleimagesdownload()

reader = csv.reader(open(KEYWORDS_FILE), delimiter=' ')
count = 0
for row in reader:
    absolute_image_paths = response.download({
        'limit': IMAGE_COUNT,
        'keywords': " ".join(row),
        'prefix': " ".join(row),
        'no_directory': True,
        'output_directory': DIRECTORY,
        # 'exact_size': '800,480',
        # Both size and exact size shouldn't be specified
        'size': '>400*300',
        'type': 'photo'
    })
    count += 1
    print("count: {}".format(count))
