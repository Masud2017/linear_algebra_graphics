import curses
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
class Display(object):
    def __init__(self):
        curses.initscr()
    def start_main_window(self):
        pass