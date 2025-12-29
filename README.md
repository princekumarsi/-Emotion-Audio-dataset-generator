# Audio Emotion Dataset Pipeline

A robust Python-based data pipeline to aggregate, normalize, and organize audio emotion datasets from multiple open-source sources into a standardized directory structure.

## Overview

This pipeline downloads and processes audio emotion datasets (RAVDESS, CREMA-D, TESS, SAVEE, ESD) and organizes them into a unified structure with standardized audio format (WAV, 16kHz, Mono) and emotion mappings.

## Target Output Structure

```
Final_Audio_Dataset/
├── happy/
├── sad/
├── angry/
├── calm/      # Neutral emotions mapped here
└── fear/
```

## Features

- **Fully Automated**: Single entry point (`python src/main.py`) - no manual downloads required
- **Automatic Downloads**: Downloads datasets from various sources (Zenodo, GitHub, Hugging Face)
- **Hugging Face Integration**: TESS and SAVEE automatically downloaded from Hugging Face datasets
- **Audio Normalization**: Converts all audio to WAV, 16kHz, Mono
- **Emotion Mapping**: Standardizes emotion labels across datasets
- **Collision Handling**: Unique filenames with dataset prefixes
- **Progress Tracking**: Progress bars for downloads and processing
- **Resume Capability**: Skips already downloaded/processed files
- **Comprehensive Logging**: Detailed logs for debugging and monitoring

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the pipeline:
```bash
python src/main.py
```

The pipeline will:
1. Create necessary directories
2. Download all datasets automatically (if not already present)
3. Process and normalize audio files
4. Organize files into target directory structure
5. Generate summary statistics

**No manual downloads required!** All datasets are downloaded automatically from their respective sources.

## Dataset Information

| Dataset | Files | Source | Download Method |
|---------|-------|--------|----------------|
| RAVDESS | ~1,500 | Zenodo | Automatic (Direct Download) |
| CREMA-D | ~7,500 | GitHub | Automatic (Direct Download) |
| TESS | ~2,800 | Hugging Face | Automatic (Hugging Face Datasets) |
| SAVEE | ~480 | Hugging Face | Automatic (Hugging Face Datasets) |
| ESD | ~15,000 | GitHub | Automatic (English subset) |

**Note**: TESS and SAVEE are automatically downloaded from Hugging Face using the `datasets` library. The pipeline will attempt multiple repository sources if the primary one is unavailable.

## Configuration

Edit `config.py` to:
- Modify emotion mappings
- Change audio processing settings (sample rate, format)
- Add or remove datasets
- Adjust target directory structure
- Change Hugging Face repository IDs for TESS and SAVEE (if needed)

**Hugging Face Repositories**:
- TESS: `Ren/tess-emotion-speech` (with fallback to `hughlan1214/SER`)
- SAVEE: `Ejfrai/SAVEE` (with fallbacks to `limjiayi/SAVEE` and `hughlan1214/SER`)

## Emotion Mappings

The pipeline maps dataset-specific emotion labels to target categories:

- **RAVDESS**: `01` (neutral) → `calm`, `03` → `happy`, `04` → `sad`, `05` → `angry`, `06` → `fear`
- **CREMA-D**: `NEU` → `calm`, `HAP` → `happy`, `SAD` → `sad`, `ANG` → `angry`, `FEA` → `fear`
- **TESS**: `neutral` → `calm`, `happy` → `happy`, `sad` → `sad`, `angry` → `angry`, `fear` → `fear`
- **SAVEE**: `n` → `calm`, `h` → `happy`, `sa` → `sad`, `a` → `angry`, `f` → `fear`
- **ESD**: `Neutral` → `calm`, `Happy` → `happy`, `Sad` → `sad`, `Angry` → `angry`, `Fear` → `fear`

**Excluded emotions**: disgust, surprise (filtered out)

## Project Structure

```
dataset-generator-cursor/
├── src/
│   ├── downloaders/          # Dataset downloaders
│   ├── processors/           # Audio processing and label mapping
│   ├── utils/                # Utility functions
│   └── main.py               # Entry point
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── README.md                 # This file
└── Final_Audio_Dataset/      # Output directory (created at runtime)
```

## Output

After processing, you'll find:
- `Final_Audio_Dataset/`: Organized audio files by emotion
- `data/raw/`: Raw downloaded datasets
- `logs/`: Processing logs

All audio files are:
- Format: WAV
- Sample Rate: 16kHz
- Channels: Mono
- Naming: `{DATASET}_{original_filename}.wav`

## Troubleshooting

### Download Failures
- Check internet connection
- For Hugging Face datasets (TESS, SAVEE), the pipeline will automatically try fallback repositories
- Check logs in `logs/` directory for detailed error messages
- Ensure you have sufficient disk space (datasets can be large)

### Processing Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that audio files are not corrupted
- Review logs for specific file errors
- Verify that `librosa` and `soundfile` are properly installed

### Missing Files
- Verify dataset downloads completed successfully
- Check logs for any download errors or warnings
- Review summary statistics in logs to see which datasets were processed
- For Hugging Face datasets, check if the repository is accessible (may require internet connection)

## License

This pipeline is provided as-is for research and educational purposes. Please respect the licenses of the individual datasets:
- RAVDESS: CC BY-NC-SA 4.0
- CREMA-D: Check original repository
- TESS: Check original repository
- SAVEE: Check original repository
- ESD: Check original repository

## Contributing

Feel free to extend this pipeline with additional datasets or features. Key extension points:
- Add new downloaders in `src/downloaders/`
- Extend emotion mappings in `config.py`
- Add processing steps in `src/processors/`

