# Audio Emotion Dataset Pipeline - Project Plan

## Project Structure

```
dataset-generator-cursor/
├── src/
│   ├── downloaders/
│   │   ├── __init__.py
│   │   ├── base_downloader.py          # Abstract base class
│   │   ├── ravdess_downloader.py
│   │   ├── crema_d_downloader.py
│   │   ├── tess_downloader.py
│   │   ├── savee_downloader.py
│   │   └── esd_downloader.py
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── audio_processor.py          # Audio normalization (librosa/soundfile)
│   │   └── label_mapper.py             # Emotion mapping logic
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py               # File operations, collision handling
│   │   └── logger.py                   # Logging configuration
│   └── main.py                         # Entry point
├── config.py                           # Central configuration
├── requirements.txt
├── plan.md                             # This file
├── README.md                           # Usage instructions
└── Final_Audio_Dataset/                # Output directory (created at runtime)
    ├── happy/
    ├── sad/
    ├── angry/
    ├── calm/                           # Neutral emotions mapped here
    └── fear/
```

## Key Components

### 1. Configuration (`config.py`)
- Dataset metadata (URLs, local paths, expected file counts)
- Emotion mappings (dataset-specific labels → target emotions)
- Audio processing settings (16kHz, Mono, WAV)
- Target directory structure
- Exclusion list (disgust, surprise)

### 2. Downloaders (`src/downloaders/`)
- Base downloader with common functionality
- Dataset-specific downloaders inheriting from base
- Support for multiple download methods (direct URLs, Hugging Face)
- Progress tracking and error handling
- Resume capability

### 3. Audio Processor (`src/processors/audio_processor.py`)
- Format conversion (any → WAV)
- Resampling (any → 16kHz)
- Channel conversion (any → Mono)
- Quality preservation

### 4. Label Mapper (`src/processors/label_mapper.py`)
- Extract emotions from filenames/paths
- Map to target emotion categories
- Filter excluded emotions
- Handle edge cases

### 5. File Utils (`src/utils/file_utils.py`)
- Collision handling (unique filenames)
- Directory creation
- File validation
- Audio file discovery

### 6. Main Pipeline (`src/main.py`)
- Orchestrates entire workflow
- Downloads datasets
- Processes audio files
- Organizes into target structure
- Generates summary statistics

## Implementation Details

### Download Methods
- **RAVDESS**: Direct download from Zenodo
- **CREMA-D**: GitHub repository download
- **TESS**: Manual download from Kaggle (instructions provided)
- **SAVEE**: Manual download from Kaggle (instructions provided)
- **ESD**: GitHub repository download with English filtering

### Audio Processing
- Load with librosa (preserve original format)
- Convert to mono if needed
- Resample to 16kHz
- Save as WAV with soundfile

### File Naming
- Format: `{DATASET}_{original_filename}.wav`
- Prevents collisions across datasets
- Counter added if duplicate exists

### Error Handling
- Network errors: Retry with exponential backoff
- Corrupted files: Skip and log
- Missing labels: Skip and log
- Processing errors: Continue with next file

## Dependencies

- `datasets`: Hugging Face datasets library
- `librosa`: Audio processing
- `soundfile`: Audio I/O
- `pandas`: Data manipulation
- `tqdm`: Progress bars
- `requests`: HTTP downloads
- `numpy`: Numerical operations

## Execution Flow

1. Initialize directories
2. Download datasets (with resume capability)
3. For each dataset:
   - Extract emotion labels
   - Map to target emotions
   - Filter excluded emotions
   - Process audio (normalize format, sample rate, channels)
   - Rename files
   - Copy to target directory
4. Generate summary statistics

## Expected Output

- `Final_Audio_Dataset/` with ~25k files
- All files: WAV, 16kHz, Mono
- Unique filenames with dataset prefixes
- Log file with processing details

