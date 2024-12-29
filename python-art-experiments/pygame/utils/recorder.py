# Directly lifted from https://gist.github.com/RicardoRibeiroRodrigues/9c40f36909112950860a410a565de667
#
# A simple utility class to save pygame frames into an animated gif

import pygame
from PIL import Image
import numpy as np


class PygameRecord:
    def __init__(self, filename: str, fps: int):
        self.fps = fps
        self.filename = filename
        self.frames = []

    def add_frame(self):
        curr_surface = pygame.display.get_surface()
        x3 = pygame.surfarray.array3d(curr_surface)
        x3 = np.moveaxis(x3, 0, 1)
        array = Image.fromarray(np.uint8(x3))
        self.frames.append(array)

    def save(self):
        self.frames[0].save(
            self.filename,
            save_all=True,
            optimize=False,
            append_images=self.frames[1:],
            loop=0,
            duration=int(1000 / self.fps),
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred: {exc_value}")
        self.save()
        # Return False if you want exceptions to propagate, True to suppress them
        return False
