class Streamer(object):

    def __init__(self, name):
     print("Streamy Award Show! ")
     self.name = name

    def __str__(self):
       rep = "Streamer of the Year is ...\n "
       rep += "name: " + self.name +  "\n"
       return rep
    
    def talk(self):
       print("Let me hear you say YEAH if you want to know who's the streamer of the year." "\n")

streamer1 = Streamer("Plaqueboymax")
streamer1.talk()

streamer2 = Streamer("Kai Cenat")
streamer2.talk()

print(streamer1)

print("Congratulations!")
