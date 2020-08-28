import time
def get_first_track_time(path_origen):
    with open(path_origen, "r") as f:
        for i, line in enumerate(f):
            song = line.split(sep=":")
            return int(song[0]), int(song[1])


class Track:
    def __init__(self):
        self.nombre = ""
        self.hora = 0
        self.hora_abs = 0
        self.minuto = 0
        self.minuto_abs = 0
        self.hr_first_track = get_first_track_time(path)[0]
        self.min_first_track = get_first_track_time(path)[1]

    def get_time(self):
        self.minuto = self.minuto_abs - self.min_first_track
        self.hora = self.hora_abs - self.hr_first_track
        if self.minuto < 0 or (self.minuto == 0 and self.hora != 0):
            self.minuto = self.hora * 60 + self.minuto


def convert(path_origen):
    with open(path_origen, "rt") as f:
        track_list = []
        for i, line in enumerate(f, start=1):
            song = line.split(sep=":")
            track = Track()
            track.hora_abs = int(song[0])
            track.minuto_abs = int(song[1])
            track.nombre = song[2]
            track.get_time()
            track_list.append(track)

    with open(path_origen, "wt") as f:
        for track in track_list:
            f.write(f"{str(track.minuto).zfill(2)}:00 : {track.nombre}")
    print("Convertido! -> tracklist_convertida.txt")
    time.sleep(2)


while True:
    try:
        path = input("Path del tracklist a convertir: ")
        convert(path)
        break
    except FileNotFoundError:
        print("Path erroneo")