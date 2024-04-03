# Soil Type Classifier

This is a Streamlit web application for classifying soil types using a TensorFlow model.

## Usage

1. Upload an image of soil.
2. Click the "Predict" button to classify the soil type.
3. The predicted soil type and confidence level will be displayed.

## Requirements

- Python 3.x
- TensorFlow
- Streamlit
- PIL (Python Imaging Library)



1. Clone the repository:

git clone [https://github.com/Idk507/Soil-type-detection.git](https://github.com/Idk507/Soil_type_detection/)


The application will open in your web browser. You can then upload an image of soil and click the "Predict" button to classify the soil type.

## Project Structure

The project structure is organized as follows:

- `app.py`: Python script containing the Streamlit application code.
- `my_model.h5`: Pre-trained TensorFlow model for soil type classification.
- `requirements.txt`: Text file listing the required Python packages and their versions.

## Model Architecture

The TensorFlow model used for soil type classification follows a convolutional neural network (CNN) architecture. It consists of several convolutional and max pooling layers followed by fully connected layers. The model is trained on images of various soil types to learn the patterns and features necessary for classification.

## Dataset

The dataset used for training the model consists of images of different soil types, including Black Soil, Cinder Soil, Laterite Soil, Peat Soil, and Yellow Soil. These images are preprocessed and divided into training and validation sets for model training.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code for any purpose, with proper attribution to the original authors.

## Author

[Dhanushkumar] - [Your GitHub Profile](https://github.com/Idk507)

