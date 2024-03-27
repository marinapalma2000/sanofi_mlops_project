# ML Ops Project

## Overview
This project demonstrates a basic machine learning operationalization using PyTorch, focused on CIFAR-10 dataset classification.

## Structure
- `src/`: Contains the source code.
- `models/`: Contains saved model files.
- `data/`: Contains data used by the model.
- `tests/`: Contains test scripts for the project components.

## Setup
To run this project, first clone the repository and navigate to the project directory.

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Running the Application
To train the model, run:

```bash
python src/train.py
```

To evaluate the model, run:

```bash
python src/evaluate.py
```

## Docker
This project can be containerized using Docker. To build and run the Docker container, use:

```bash
docker build -t mlops_project .
docker run -p 4000:80 mlops_project
```

## Testing
To run tests, execute the following command in the project directory:

```bash
python -m unittest discover -s tests
```
