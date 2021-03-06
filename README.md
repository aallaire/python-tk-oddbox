# python_tk_oddbox
A few odd tkinter utilities.

### Basic Description
* Images class--supports PhotoImages organized by file stem names they were loaded from.
* ImageMenuButton--uses images so loaded to make an image based menubutton/menu
with an associated StringVar control variable. The user can select an image and
its name will be set in the StringVar and displayed on the button. If the StringVar
is set, the image displayed on button will change automatically--but it should always
be a name of an image in Images.

### CAVEATS
1) The package is likely too specific in focus to be useful to many.
1) Backwards compatibility is not expected to be maintained.
2) This code is probably never going to be production grade and very little maintenance is anticipated.

#### Example Usage of Images class

This example assumes the following directory structure
```
/directory/path
    lion.jpg
    tiger.jpg
    bear.gif
    some.txt
```
The following code will load lion, tiger, and bear as PhotoImages
that are accessible as Images.bear and Images.flower. The
some.txt file is ignored because we don't load the directory
with ".txt". Then it will create a menubutton that will select
between lion, tiger, and bear based on images. The value of
the text variale animal will be bound to this menubutton such
that changing it will change the image on the button and
selecting an image will change the text variable.
```python
from tkinter import Tk, Label, StringVar
from tk_oddbox import Images, ImageLoader, ImageLabel, ImageMenuButton

tk = Tk()

loader = ImageLoader(tk)

loader.load_dir("/directory/path", "*.jpg")
loader.load_dir("/directory/path", "*.gif")

lion_image_1 = Images.lion
lion_image_2 = Images["lion"]
assert lion_image_1 is lion_image_2
assert "lion" in Images


animal_var = StringVar()
animal_var.set("lion")
animal_choices = ["lion", "tiger", "bear"]

animal_label = ImageLabel(tk, animal_var)
animal_menu = ImageMenuButton(tk, animal_var, animal_choices) 

animal_menu.grid(row=0, column=0)

tk.mainloop()
```
The expressions like "*.gif" are glob expressions and are
passed to the Path.glob() method in the pathlib module.

##### Caveats:
 * Files are keyed by their stem name, so care should be
 used to avoid name collisions.
 * File stem names starting with underscores or which are not
 valid python identifiers should be avoided.
 * StringVar control variable associated with an ImageMenuButton
 should never be set to something other than a name in Images.
 This means an Entry widget with this StringVar is probably a
 bad idea.

