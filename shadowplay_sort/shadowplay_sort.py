import os
from datetime import datetime
from pathlib import Path


def get_date(file):
    """
    Get the date from the file name
    """

    split = file.split('.')
    date_string = split[0] + '.' + split[1] + '.' + split[2] + '.' + split[3] + '.' + split[4]

    if ".DVR.mp4" in file:
        date_string = date_string.split(' ', 1)[1]

    if ".png" in file:
        date_string = date_string.split(' ', 2)[2]

    return datetime.strptime(date_string, '%Y.%m.%d - %H.%M.%S')


def get_type(file):
    """
    Check if file is a screenshot or a video
    """

    if ".DVR.mp4" in file:
        type = "videos"
    if ".png" in file:
        type = "screenshots"

    return type


def main(path):
    """
    sort files in a directory by date
    """

    # Get all files in the path
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]

    for file in files:

        if ".DVR.mp4" or ".png" in file:

            # Get the date from the file name
            date = get_date(file)

            # Get the type from the file name
            type = get_type(file)

            # Define target path
            target_path = Path(path + '/' + date.strftime('%Y') + '/' +
                               date.strftime('%m') + '/' + date.strftime('%d') + '/' + type)

            # Check if folder exists and create it if not
            if not os.path.exists(target_path):
                print("Creating folder: " + str(target_path))
                target_path.mkdir(parents=True, exist_ok=True)

            # Move the file to the correct folder
            os.rename(path + '/' + file, str(target_path) + '/' + file)

            # print the file moved
            print(file + "   --->>>   " + str(target_path) + '/' + file)


if __name__ == '__main__':
    """
    Entry point
    """

    # Get the current working directory
    main(os.getcwd())
