import getopt, math, os, struct, sys, wave


sound= wave.open('tone.wav','r')
#spf2 = wave.open('opera_new.wav','r')
params = sound.getparams()
num_channels = sound.getnchannels()
sample_width = sound.getsampwidth()
num_frames = sound.getnframes()
num_samples = num_frames * num_channels

if (sample_width == 1):  # samples are unsigned 8-bit integers
    fmt = "{}B".format(num_samples)
    #min_sample = -(1 << 8)
elif (sample_width == 2):  # samples are signed 16-bit integers
    fmt = "{}h".format(num_samples)
else:
    # Python's wave module doesn't support higher sample widths
    raise ValueError("File has an unsupported bit-depth")

raw_data = list(struct.unpack(fmt, sound.readframes(num_frames)))

# for i in raw_data:
#     print(i)
