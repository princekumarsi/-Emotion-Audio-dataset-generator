"""
Central configuration file for the Audio Emotion Dataset Pipeline.
Contains dataset metadata, emotion mappings, and processing settings.
"""
import os

# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')
OUTPUT_DIR = os.path.join(BASE_DIR, 'Final_Audio_Dataset')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# Target directory structure
TARGET_DIRS = {
    'happy': os.path.join(OUTPUT_DIR, 'happy'),
    'sad': os.path.join(OUTPUT_DIR, 'sad'),
    'angry': os.path.join(OUTPUT_DIR, 'angry'),
    'calm': os.path.join(OUTPUT_DIR, 'calm'),  # Neutral emotions mapped here
    'fear': os.path.join(OUTPUT_DIR, 'fear')
}

# Emotions to exclude from final dataset
EXCLUDE_EMOTIONS = ['disgust', 'surprised', 'surprise', 'disgusted']

# Audio processing settings
AUDIO_FORMAT = 'wav'
SAMPLE_RATE = 16000
CHANNELS = 1  # Mono

# Dataset configurations
DATASETS = {
    'ravdess': {
        'name': 'RAVDESS',
        'local_path': os.path.join(RAW_DATA_DIR, 'ravdess'),
        'urls': [
            'https://zenodo.org/record/1188976/files/Audio_Speech_Actors_01-24.zip',
            'https://zenodo.org/record/1188976/files/Audio_Song_Actors_01-24.zip'
        ],
        'emotion_map': {
            '01': 'neutral',  # neutral -> calm
            '02': 'calm',
            '03': 'happy',
            '04': 'sad',
            '05': 'angry',
            '06': 'fearful',  # fearful -> fear
            '07': 'disgust',  # excluded
            '08': 'surprised'  # excluded
        },
        'filename_pattern': r'(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})\.wav',
        'emotion_index': 2,  # Third field in filename
        'expected_count': 1500
    },
    'crema_d': {
        'name': 'CREMA-D',
        'local_path': os.path.join(RAW_DATA_DIR, 'crema_d'),
        'urls': [
            'https://github.com/CheyneyComputerScience/CREMA-D/archive/refs/heads/master.zip'
        ],
        'emotion_map': {
            'NEU': 'neutral',  # neutral -> calm
            'HAP': 'happy',
            'SAD': 'sad',
            'ANG': 'angry',
            'FEA': 'fearful',  # fearful -> fear
            'DIS': 'disgust'  # excluded
        },
        'filename_pattern': r'(\d+)_([A-Z]+)_([A-Z]+)_([A-Z]+)\.wav',
        'emotion_index': 2,  # Third field in filename
        'expected_count': 7500
    },
    'tess': {
        'name': 'TESS',
        'local_path': os.path.join(RAW_DATA_DIR, 'tess'),
        'huggingface_repo': 'Ren/tess-emotion-speech',  # Hugging Face repository ID
        'emotion_map': {
            'neutral': 'neutral',  # neutral -> calm
            'happy': 'happy',
            'sad': 'sad',
            'angry': 'angry',
            'fear': 'fearful',  # fearful -> fear
            'disgust': 'disgust',  # excluded
            'ps': 'surprised'  # excluded
        },
        'filename_pattern': r'OAF_[a-z]+_([a-z]+)\.wav|YAF_[a-z]+_([a-z]+)\.wav',
        'emotion_index': 1,  # Emotion is in the filename
        'expected_count': 2800
    },
    'savee': {
        'name': 'SAVEE',
        'local_path': os.path.join(RAW_DATA_DIR, 'savee'),
        'huggingface_repo': 'Ejfrai/SAVEE',  # Hugging Face repository ID (fallback: limjiayi/SAVEE)
        'emotion_map': {
            'n': 'neutral',  # neutral -> calm
            'h': 'happy',
            'sa': 'sad',
            'a': 'angry',
            'f': 'fearful',  # fearful -> fear
            'd': 'disgust',  # excluded
            'su': 'surprised'  # excluded
        },
        'filename_pattern': r'([a-z]+)\d+\.wav',
        'emotion_index': 1,  # First field in filename
        'expected_count': 480
    },
    'esd': {
        'name': 'ESD',
        'local_path': os.path.join(RAW_DATA_DIR, 'esd'),
        'urls': [
            'https://github.com/HLTSingapore/Emotional-Speech-Data/archive/refs/heads/main.zip'
        ],
        'emotion_map': {
            'Neutral': 'neutral',  # neutral -> calm
            'Happy': 'happy',
            'Sad': 'sad',
            'Angry': 'angry',
            'Fear': 'fearful',  # fearful -> fear
            'Disgust': 'disgust',  # excluded
            'Surprise': 'surprised'  # excluded
        },
        'filename_pattern': r'.*',
        'emotion_index': None,  # Will be extracted from directory structure
        'expected_count': 15000,
        'language_filter': 'English'  # Filter for English-only files
    }
}

# Final emotion mapping (dataset emotions -> target emotions)
# This maps the intermediate emotions to final target categories
FINAL_EMOTION_MAP = {
    'neutral': 'calm',
    'calm': 'calm',
    'happy': 'happy',
    'sad': 'sad',
    'angry': 'angry',
    'fearful': 'fear',
    'fear': 'fear',
    'disgust': None,  # excluded
    'surprised': None,  # excluded
    'surprise': None,  # excluded
    'disgusted': None  # excluded
}
