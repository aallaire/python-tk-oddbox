# python_tk_oddbox
A few odd tkinter utilities.

### Brief Description
* Images class for loading gif images as tkinter image objects from specified directory.
* ImageMenu tkinter Frame for selecting images associated with a StringVar value.

### CAVEATS
1) The package is likely too specific in focus to be useful to many.
1) Backwards compatibility is not expected to be maintained.
2) This code is probably never going to be production grade and very little maintenance is anticipated.

#### Example Usage of Images class

This example assumes the following directory structure
```
/directory/path
    flower.jpg
    bear.gif
    some.txt
```
The following code will load flower and bear as PhotoImages
that are accessible as Images.bear and Images.flower. The
some.txt file is ignored because we don't load the directory
with ".txt"
```python
from tkinter import Tk, Label
from tk_oddbox import Images

tk = Tk()

Images.load("/directory/path", "*.jpg")
Images.load("/directory/path", "*.gif")

flower_label = Label(image=Images.flower)
bear_label = Label(image=Images.bear)
```
The expressions like "*.gif" are glob expressions and are
passed to the Path.glob() method in the pathlib module.

##### Caveats:
 * tkinter.Tk() must be called before any images are loaded
(due to how tk handles caching).
 * Files are keyed by their stem name, so care should be
 used to avoid name collisions. To help, a ValueError
 is raised when this occurs.
 * The stem names of the image files loaded should be
 conventional python attribute.
 * File names starting with underscores are not allowed
 and will trigger a ValueError if loaded.

