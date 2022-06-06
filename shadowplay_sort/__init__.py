import os
from .shadowplay_sort import main

def main():
    """ Entrypoint, parsing current path """

    # Get the current working directory
    shadowplay_sort.main(os.getcwd())
