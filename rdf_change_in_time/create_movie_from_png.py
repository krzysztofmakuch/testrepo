import cv2
import os

def list_of_png(pattern):
    '''(str) -> list
    Takes a png pattern and returns list of all
    PNG files matching it. You don't have to
    add .png or numbering at the endo of pattern.

    Possible improvement:
    It's somehow redundant to list of xvg in
    create_image_from_xvg
    '''
    pattern = re.sub('_?[0-9]*(\.png)?$','',pattern)
    print('I\'m using pattern for PNG files: ', pattern)
    allfiles = os.listdir()
    png_files = list(filter(lambda fn: (pattern in fn) and fn.endswith('.pg'),
                            allfiles))
    #print(rdf_files)

    return png_files
    

    
def create_video(png, video_name):
    '''
    Creates a video from png files
    '''
    
