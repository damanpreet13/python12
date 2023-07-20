class Songs:
    def __init__(self , tracks="",artist=0,duration=4.43):
        self.tracks = tracks
        self.artist = artist
        self.duration = duration
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Tracks:",self.tracks)
        print("artist:",self.artist)
        print("duration:",self.duration)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
song1 = Songs("Chorni", "DIVINE, Sidhu Moose Wala", "03:01")       
song2 = Songs("Gustakhiyan", "Gurnam Bhullar", "03:39")
song3 = Songs("Kasol", "Mani Longia, Starboy X", "02:40")
song4 = Songs("Check It Out", "Parmish Verma, Paradox", "03:15")
song5 = Songs("Udd Jaa Kaale Kaava", "Udit Narayan, Mithoon,Uttam Singh,Alka Yagnik", "04:48")

song1.show()
song2.show()
song3.show()
song4.show()
song5.show()                  