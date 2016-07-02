"""Dynamic Picture Creator

    Example:
        errormessage("text")
        eventmessage("text")
        standardmessage("text")
        reset()

"""


class DPC:
    def __init__(self):
        from ConfigParser import ConfigParser
        config = ConfigParser()
        inifile = "config.ini"  # INI-Datei definieren
        config = ConfigParser()  # Objekt config von ConfigParser erstellen
        config.read(inifile)  # INI-Datei einlesen
        self.backgroundred = config.get('DPC BACKGROUND', 'red')  # Standardwert fuer Hintergrundfarbe rot
        self.backgroundblue = config.get('DPC BACKGROUND', 'blue')  # Standardwert fuer Hintergrundfarbe blau
        self.backgroundgreen = config.get('DPC BACKGROUND', 'blue')  # Standardwert fuer Hintergrundfarbe gruen
        self.fontred = config.get('DPC TEXT', 'red')  # Standardwert fuer Schriftfarbe rot
        self.fontblue = config.get('DPC TEXT', 'blue')  # Standardwert fuer Schriftfarbe blau
        self.fontgreen = config.get('DPC TEXT', 'green')  # Standardwert fuer Schriftfarbe gruen
        self.yaxis = config.get('DPC TEXT', 'yaxis')  # Standardwert fuer Position Y-Achse (Text)
        self.xaxis = config.get('DPC TEXT', 'xaxis')  # Standardwert fuer Position X-Achse (Text)
        self.step = config.get('DPC TEXT', 'steps')  # Standardwert fuer Schrittgroesse
        self.picpath = config.get('DPC PICTURE', 'picpath')  # Standardwert fuer Bildverzeichnis
        self.height = config.get('DPC PICTURE', 'height')  # Standardwert fuer Bildhoehe in Pixel
        self.width = config.get('DPC PICTURE', 'width')  # Standardwert fuer Bildbreite in Pixel

        self.bmp = self.picpath + "pic.bmp"  # BMP Standard Pfad
        self.png = self.picpath + "pic.png"  # PNG Standard Pfad

    def breakthetext(self, text):
        itera = text
        step = int(self.step)
        stext=""
        if len(itera) > step:
            while len(itera) > step:  # solange itera groesser als step
                """Durchiterieren"""
                stext += itera[:step] + "\n"  # speichere die Zeichen bis zum schnitt in text


                itera = itera[step:]  # anschliessend setzte itera zum rest
                if len(itera) < step:
                    stext += itera
            return str(stext)
        else:
            return str(itera)

    def drawimage(self, text, bred, bgreen, bblue, tred, tgreen, tblue):
        """

        :param text:
        :param bred:
        :param bgreen:
        :param bblue:
        :param tred:
        :param tgreen:
        :param tblue:
        :return:
        """
        from PIL import ImageFont
        from PIL import Image
        from PIL import ImageDraw

        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
        img = Image.new("RGBA", (int(self.width), int(self.height)), (int(bred), int(bgreen), int(bblue)))
        draw = ImageDraw.Draw(img)
        draw.text((40, 40), text, (int(tred), int(tgreen), int(tblue)), font=font)
        draw = ImageDraw.Draw(img)
        # draw = ImageDraw.Draw(img)
        img.save(self.png)
        im = Image.open(self.png)
        im.save(self.bmp)

    def errormessage(self, text):
        """ Rotes Bild mit Event-Ueberschrift

        :param text:
        :return:
        """
        self.reset()
        bred = 255
        bblue = 0
        bgreen = 0
        tred = 255
        tblue = 255
        tgreen = 255
        text = "    !! WARNING !! \n" + self.breakthetext(text)
        self.drawimage(text, bred, bgreen, bblue, tred, tgreen, tblue)

    def eventmessage(self, text):
        """ Gelbes Bild mit Event-Ueberschrift

        :param text:
        :return:
        """
        self.reset()
        bred = 255
        bblue = 51
        bgreen = 255
        tred = 0
        tblue = 0
        tgreen = 0
        text = "       Event:  \n" + self.breakthetext(text)
        self.drawimage(text, bred, bgreen, bblue, tred, tgreen, tblue)

    def standardmessage(self, text):
        """ Standardbild Zeichnen

        Nimmt die Einstellungen aus der config.ini
        und Zeichnet daraus ein Bild.
        """
        self.reset()
        self.drawimage(text, self.backgroundred, self.backgroundgreen, self.backgroundblue, self.fontred,
                       self.fontgreen, self.fontblue)

    def reset(self):
        """ Bildschirminhalt auf RGB 255,255,255 setzen """
        bred = 255
        bblue = 255
        bgreen = 255
        tred = 255
        tblue = 255
        tgreen = 255
        text = ""
        self.drawimage(text, bred, bgreen, bblue, tred, tgreen, tblue)


""" TEST PASSAGE """

# test = DPC()
# test.errormessage("TTTTTTTTTTTTTTTest")
# text = test.breakthetext("Test1234567")
# print(text)