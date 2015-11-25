import os
import sys
import time

def remove(path):
    """
    Remove the file
    """
    try:
        if os.path.exists(path):
            os.remove(path)
    except OSError:
        print "Unable to remove file: %s" % path
 
def cleanup(path, latest_count):
    """
    Removes all files recursively in the path except for the
    latest count of files
    """
    for root, dirs, files in os.walk(path, topdown=False):
        print "Entering directory : " + root
        num_files = len(files)
        print num_files
        if num_files <= 1 :
            print "No files to delete in : " + root              
        else :
            sorted_files = sorted(os.listdir(root), key=os.path.getmtime)        
            for file_ in sorted_files:
                print "Deleting file : " + file_
                full_path = os.path.join(root, file_)
                stat = os.stat(full_path)
                
                num_files = len([f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))])
                if stat.st_mtime <= time_in_secs and num_files > latest_count:
                    remove(full_path)
 
if __name__ == "__main__":
    path, latest_count = sys.argv[1], int(sys.argv[2])
    cleanup(path, latest_count)
