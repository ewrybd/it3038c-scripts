# Lab 7

======

### Using Pillow in Python

======

These python scripts are designed to perform the following actions to any .jpeg file, but can easily be adapted to any image: Blur the image, Convert the image to a .png file, Create a Thumbnail out of the image, and Find the edges of the image to highlight them. In this folder is the example of the original test image and then all of the variations of what it will look like when running the scripts. 

To install all of the required modules, open powershell and run the following commands:

```powershell
pip install virtualenv
virtualenv ~/venv/webscraping/
.\~/venv/webscraping/Scripts/activate.ps1
pip install Pillow
```

Now open python and import the module using this command:

```powershell
$ python

>>>import PIL
```

Once all of the required modules are installed, download the scripts that are in this folder and test them out for yourself! For these scripts to work with any image, simply replace every instance of "testimage.jpeg" with the image file that you want to use.

#### IMPORTANT: For these scripts to work, the downloaded image needs to be in the same directory that you are operating in. For example, if you download all of these scripts to the same location, you will need to change to that directory to run the scripts.

======
