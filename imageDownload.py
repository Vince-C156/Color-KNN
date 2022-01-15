from bs4 import BeautifulSoup
from googleimagedownloader.googleimagedownloader import GoogleImageDownloader
import requests
from bing_image_downloader import downloader
    

if __name__ == "__main__":

  "this script just uses random bing image downloader to download images from multiple search querys"

  #list of colors to search. Edit/add to list to modify search
  colorlist = ['orange']

  #words before color in color list to specify search
  queryStr = 'solid dark '

  d = downloader

  for color in colorlist:

    searchStr = queryStr + color + ' background'
    print(searchStr)
    d.download(searchStr, limit=35, output_dir='downloads', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

