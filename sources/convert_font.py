from fontTools import ttLib
f = ttLib.TTFont()
f.importXML("nyan.xml")
f.save("NyanTemplate.ttf")