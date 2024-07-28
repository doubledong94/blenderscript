import bpy
import sys
import librosa
import cv2
import wave

def get_duration_wave(file_path):
   with wave.open(file_path, 'r') as audio_file:
      frame_rate = audio_file.getframerate()
      n_frames = audio_file.getnframes()
      duration = n_frames / float(frame_rate)
      return duration

wav_path = "/home/ydd/Documents/shishan/resource/SnackTime.wav"
audio_file = librosa.load(wav_path)
y, sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(tempo)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)
print(len(beat_times))

frame_range = bpy.context.scene.frame_end
print(frame_range)

audio_duration = get_duration_wave(wav_path)

count = 0
for beat in beat_times:
    if (count % 8) == 7:
        beat_frame = (int) (frame_range * (beat/audio_duration))
        bpy.ops.sequencer.split(frame=beat_frame, channel=3, type='SOFT', side='LEFT')
#        bpy.ops.sequencer.retiming_key_add(timeline_frame=beat_frame)
    count+=1