#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pyvirtualdisplay import Display
from selenium import webdriver

from time import sleep
import sys

from contextlib import contextmanager


@contextmanager
def create_hidden_display(width, height):
    display = Display(visible=0, size=(width, height))
    display.start()
    yield display
    display.stop()

@contextmanager
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def capture_web(url):
    with create_hidden_display(1440, 900):
        with create_driver() as driver:
            driver.get(url)
            sleep(5)
            image_bin = driver.get_screenshot_as_png()

    return image_bin


if __name__ == '__main__':
    # Ex: python web_capturer.py https://taiga.io
    from io import BytesIO
    from palette_gen import generate_palette

    image_bin = capture_web(sys.argv[1])

    print(generate_palette(BytesIO(image_bin)))
