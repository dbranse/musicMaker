import time

#these will eventually be music files
bass = None
snare = None
hihat = None
clap = None

d = {0: bass, 1: snare, 2: hihat, 3: clap}

beatarr = [[0], [1, 2], [3], [1, 2]]
bpm = 100

#l is the number of beats
l = 100

#will loop until the number of beats is done
for i in range(l):
    # wil loop through the beat array at the correct index
    for sound in beatarr[i%len(beatarr)]:
        # we need to play asyncronously
        d[sound].play()
    # wait until the next beat
    time.sleep(bpm/60)