import librosa
import os
import pyloudnorm as pyln
import soundfile as sf

test_path = ''     # example audio file


def loudnessnorm(pathaudio, peakwant=-1.0, loudnesswant=-13.0):
    print(f'Normalize audio to {loudnesswant}LKFS.')

    # Load audio data
    read, sr = librosa.load(pathaudio, sr=None, mono=False)
    data = read.T.copy()

    # Get sampling rate and duration
    samplerate = librosa.core.get_samplerate(pathaudio)
    duration = librosa.get_duration(filename=pathaudio)

    # Measure the loudness before normalization
    meter = pyln.Meter(samplerate)   # create BS.1770-4 meter
    loudness_before = meter.integrated_loudness(data)

    # Peak normalization
    peak_normalized_audio = pyln.normalize.peak(data, peakwant)

    # loudness normalize audio to loudnessNorm value
    loudness_normalized_audio = pyln.normalize.loudness(peak_normalized_audio, loudness_before, loudnesswant)

    # Measure the loudness after normalization
    loudness_after = meter.integrated_loudness(loudness_normalized_audio)

    # Export audio normalized.
    basename, ext = os.path.splitext(pathaudio)
    sf.write(f'{basename}_new.wav', loudness_normalized_audio, samplerate)

    print(f'Raw sampling rate is {samplerate}Hz.')
    print(f'Duration of File is {duration}s.')
    print(f'Loudness before normalization is {loudness_before}LKFS.')
    print(f'Loudness after normalization is {loudness_after}LKFS.')
    print('Loudness normalization is done!')


if __name__ == '__main__':
    loudnessnorm(test_path)
