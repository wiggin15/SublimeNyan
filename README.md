This is a plugin for Sublime that adds "Nyan Mode" like in emacs.

This plugin requires installing a font on the computer.

This plugin only works on Sublime Text 3 on Mac computers (the font used is not supported on other platforms)

Installation
============
* Install the plugin: `wget https://github.com/wiggin15/SublimeNyan/raw/master/nyan.py -O ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/nyan.py`
* Install the font: `wget https://github.com/wiggin15/SublimeNyan/raw/master/Nyan.ttf -O ~/Library/Fonts/Nyan.ttf`

Screenshot
==========
![Alt text](/screenshot.png?raw=true)

Generating the Font
===================
The font was generated using Python with FontTools and Jens Kutilek 'sbix' code.
* Install FontTools: `easy_install FontTools`
* Follow the instructions in http://typophile.com/node/103268 on how to install
the sbix code

To generate the nyan font, under "font_sources", run:
* Run `python convert_font.py` (this will generate a NyanTemplate.ttf)
* Run `python addSbixImages.py` (this will add the pngs and to the template and create Nyan.ttf)