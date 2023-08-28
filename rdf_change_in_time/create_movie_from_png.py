import cv2
import os
import re


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
    #print(pattern)
    print('I\'m using pattern for PNG files: ', pattern)
    allfiles = os.listdir()
    png_files = list(filter(lambda fn: (pattern in fn) and fn.endswith('.png'),
                            allfiles))
    #print(rdf_files)
    #print(png_files)
    return png_files
    

    
def create_video(png_pattern, vid_name):
    '''
    Creates a video from png files
    '''

    images = list_of_png(png_pattern)
    print(images)
    vid_name = images[0][:-3] + '_film.avi'

    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(vid_name, 0, 1, (width, height))

    for img in images:
        video.write(cv2.imread(img))

    cv2.destroyAllWindows()
    video.release()

def run_function():
    """ Take input from a user and run the module """

    print("Give me a pattern for PNG images. Beginning of the name is sufficient, png extension isn't required:")
    png_name = input()

    print("Give me the name of a video you want to be created .AVI will be added at the end:")
    #vid_name = input()

    create_video(png_name, vid_name)



if __name__ == '__main__':
    run_function()


#thank you stackoverflow :)
"""
image_folder = 'images'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
"""