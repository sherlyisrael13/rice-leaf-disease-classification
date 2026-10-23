# Rice Leaf Disease Classification Using CNN

## Project Overview
This project develops a Convolutional Neural Network (CNN) to classify rice leaf images into four disease categories: Bacterial Blight, Blast, Brown Spot, and Tungro.

## Dataset
The project uses the **Rice Leaf Disease Image Samples** dataset provided for the CBL problem statement. It contains 5,932 images across four classes.

## Methodology
- Explore the dataset and examine class distribution.
- Resize images to 128 × 128 pixels and normalize pixel values.
- Split the data into training, validation, and test sets.
- Build and train a CNN using TensorFlow/Keras.
- Evaluate performance using accuracy, precision, recall, F1-score, and a confusion matrix.
- Inspect misclassified test images to understand model errors.

## Results
- **Test accuracy:** 96.29%
- **Macro F1-score:** 0.9637
- **Test images:** 890
- **Misclassified test images:** 33
- **Best validation accuracy:** 97.19%

The confusion matrix shows that 14 Brown Spot images were classified as Blast. This is an important error case for further analysis.

## Repository Contents
- `Rice_Leaf_Disease_Classification.ipynb` — project notebook
- `01_dataset_exploration.py` — dataset exploration script
- `best_rice_disease_cnn.keras` — trained CNN model
- `class_distribution.png` — dataset class distribution
- `training_validation_curves.png` — training and validation curves
- `confusion_matrix.png` — confusion matrix
- `misclassified_test_images.png` — examples of incorrect predictions
- `classification_report.csv` — per-class evaluation metrics
- `evaluation_summary.csv` — summary of test results
- `Rice_Disease_Submission.zip` — packaged project outputs

## Limitations
Performance on new images may differ from the reported test results. Images captured under different lighting, backgrounds, camera conditions, and disease stages should be tested before practical deployment.

## Tools and Technologies
Python, TensorFlow/Keras, NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn.

## Reproducibility
Refer to the notebook for the data-processing steps, model architecture, training procedure, and evaluation code. The dataset must be obtained separately if it is not redistributed with this repository.
