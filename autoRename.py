# rename caption files and video files to match each other
# make sure caption files and video files are in the same folder, and the number of caption files is the same as the number of video files

import os
import argparse

def autoRename(animationDirName,videoSuffix='mkv', captionSuffix='ass',videoAssetPath='C:/Users/29402/Videos/animation/'):
    # get all files in the current folder
    path=videoAssetPath+ animationDirName
    files = os.listdir(path)
    # get caption files
    captionSuffix='.'+captionSuffix
    captionFiles = [file for file in files if file.endswith(captionSuffix)]
    
    # get all video files
    videoSuffix='.'+videoSuffix
    videoFiles = [file for file in files if file.endswith(videoSuffix)]

    # check if the number of caption files is the same as the number of video files
    if len(captionFiles) != len(videoFiles):
        print('The number of caption files is not the same as the number of video files.')
        return

    # rename caption files and video files to match each other
    for i in range(len(captionFiles)):
        # get the new name
        videoNewName = f"{i+1:03}"+videoSuffix
        captionNewName=f"{i+1:03}"+captionSuffix
        # rename caption files
        os.rename(path+'/'+videoFiles[i], path+'/'+videoNewName)
        os.rename(path+'/'+captionFiles[i], path+'/'+captionNewName)
        print(f'{videoFiles[i]} -> {videoNewName}')
        print(f'{captionFiles[i]} -> {captionNewName}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename caption files and video files to match each other.')
    parser.add_argument('-v','--videoSuffix', type=str, default='mkv', help='the suffix of video files')
    parser.add_argument('-c','--captionSuffix', type=str, default='ass',help='the suffix of caption file')
    parser.add_argument('-p','--videoAssetPath',type=str,default='C:/Users/29402/Videos/animation/',help="the path of your video assets")
    parser.add_argument("dirName", type=str,help="the animation dirory's name")

    arg=parser.parse_args()
    autoRename(animationDirName=arg.dirName,videoSuffix=arg.videoSuffix,captionSuffix=arg.captionSuffix,videoAssetPath=arg.videoAssetPath)
