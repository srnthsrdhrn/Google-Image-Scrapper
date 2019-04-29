# Google Image Scrapper 

This project is a simple implementation of Google Image Scrapper using the google_images_download library

Fill in your keywords in keywords.csv file   
**Example:** 
    
    brad pitt   
    George Clooney  
    Paul L. Nolan  
    Bernie Mac  
    Mark Gantt  
    Tim Perez  
    Elliott Gould
    
These keywords will be searched through google images.

The python file will accept three arguments:  
`--image_count`: Number of Images per keyword to download  
`--directory`: The directory to store the downloaded images. It will be created if it doesnt exist  
`--keywords_file`: This is the location of the csv file which contains the keywords in Space Delimited format


###Basic usage:

`python scrapper.py`