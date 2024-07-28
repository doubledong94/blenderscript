import sys
import librosa

audio_file = librosa.load(sys.argv[1])
y, sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)
print(len(beat_times))
