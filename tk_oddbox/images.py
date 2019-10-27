"""Provides Images class.

Synopsis:

# The tkinter object images will be used with MUST be created first.

root = tkinter.Tk()





"""

from typing import Union
from tkinter import PhotoImage

from pathlib import Path


class Images:
    """Container that loads the gif images."""

    _images = {}  # {<name>: <PhotoImage>,...}

    @classmethod
    def load_dir(cls, directory: Union[Path, str], glob: str):
        """Load files within directory with specified suffix.

        Files are named after

        Args:
            directory: directory to find files directly under.
            glob: file extension including . for example: ".gif"
        """
        # If directory arg is a string, make it a Path
        if isinstance(directory, str):
            directory = Path(directory)
        # find images and load them.
        for path in directory.glob(glob):
            name = path.stem
            if name.startswith("_"):
                raise ValueError(f'Image name may not start with "_" {path}')
            image = PhotoImage(file=path)
            self._images[name] = image
            setattr(cls, name, image)




    @classmethod
    def init_class(cls, directory: Path, extension: str=".gif"):
        """Load must happen after tkinter.Tk() instance is created.

        Args:
            directory: directory,

        """
        if not cls._initialized:
            cls._already_loaded = True
            for path in directory.iterdir():
                if path.suffix == ".gif" and path.stem:
                    image = PhotoImage(file=path)
                    setattr(cls, path.stem, image)


