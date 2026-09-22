# End-to-End Chest Disease Classification

A deep learning-powered web application for classifying chest disease images from X-ray scans. The project combines a TensorFlow-based model pipeline with a Flask frontend so that users can upload an image and receive a prediction in a browser-based interface.

## Project Overview

Medical imaging plays a major role in timely diagnosis, but manual interpretation can be slow and inconsistent. This project tackles that challenge by creating an end-to-end machine learning workflow that automatically classifies chest images using a trained CNN model.

The application is designed to:
- collect and prepare chest X-ray image data
- train a deep learning model for classification
- evaluate the trained model
- expose the model through a Flask API
- allow users to upload images and get a prediction instantly

## Technologies Used

- Python
- TensorFlow / Keras
- Flask
- Flask-CORS
- NumPy
- Pandas
- Matplotlib
- Seaborn
- MLflow
- DVC
- Docker / Docker Compose
- HTML, CSS, and JavaScript for the web interface

## Key Features

- End-to-end chest disease classification workflow
- Browser-based image upload and prediction UI
- REST API for inference
- Modular training and evaluation pipeline
- Model artifacts stored in the `Artifacts/` directory
- Experiment tracking with MLflow and versioning with DVC
- Docker support for easier deployment and execution

## Project Structure

- `app.py` – main Flask application
- `main.py` – pipeline orchestration for the training workflow
- `Config/config.yaml` – project configuration values
- `Respire/` – core modules for model logic, pipeline, config, and utilities
- `templates/index.html` – frontend design for image upload and prediction
- `Artifacts/` – trained model and generated outputs
- `requirements.txt` – project dependencies
- `docker-compose.yml` – container configuration

## Prerequisites

- Python 3.9+
- pip
- Virtual environment (recommended)
- Docker (optional)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KalyanM45/End-to-End-Chest-Disease-Classification.git
   cd End-to-End-Chest-Disease-Classification
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Optional: install the package in editable mode:

   ```bash
   pip install -e .
   ```

## How to Run

### Start the web application

```bash
python app.py
```

Then open:

```text
http://localhost:8080
```

### Run the training pipeline

```bash
python main.py
```

This triggers the data ingestion, base model setup, training, and evaluation stages.

### Run with Docker

```bash
docker compose up --build
```

The app is configured to expose port `8080`.

## How to Use

1. Open the application in the browser.
2. Upload a chest X-ray image.
3. Click the prediction button.
4. The model will classify the image and display the result.

## Notes

- The model inference is loaded from the trained artifact under `Artifacts/Model_Training/`.
- DVC and MLflow are included to help with pipeline versioning and experiment tracking.
- The project is suitable for learning, experimentation, and further enhancement in medical imaging tasks.

## License

This project is intended for learning and research purposes. Please review the repository license before using it in a production or commercial setting.

## Acknowledgements

This project is inspired by the growing importance of AI-assisted medical diagnosis and the role of computer vision in healthcare.
