Prompt
I need a neural network architecture using Python, tensorflow, and keras that takes videos stored on a local Windows machine, and outputs a prediction of whether the video falls into one of three exclusive classes.
The training videos are separated by class in three separate folders ("C:\Users\acarr\Documents\ads_data_local\capstone\celeb-df-v2\Celeb-real", "C:\Users\acarr\Documents\ads_data_local\capstone\celeb-df-v2\Celeb-synthesis", "C:\Users\acarr\Documents\ads_data_local\capstone\celeb-df-v2\YouTube-real"), so upon ingestion, the architecture should create target labels based on the name of the folder they are in.
To avoid out of memory issues, include a way to ingest the videos as part of each batch and not as a single numpy, but the intial size is effectively (None, 250, 200, 200, 3), where (number of videos, frames/video, image height, image width, number of channels).
I need at least two convolutional and associated pooling layers to process the images, at least one dense layer, and an output layer. Since it is multiclass, I want 'y' to be in sparse categorical form in order to use the sparse_categorical_crossentropy loss function. Since this is a video, TimeDistributed() should be used. Activation for all of the layers except the output should be ReLU and the output should be softmax.
In addition I need the following transformations, which should somehow be part of a pipeline to avoid data leakage across training and testing data:
1. Any videos shorter than a maximum number of frames must be padded.
2. Any videos longer than the maximum number of frames must be cutoff.
3. All images must be resized.
4. All images must be convereted to grayscale.
5. Feature extraction should occur using wavelet transform, such as pywt.dwt2()
6. All wavelet outputs should be normalized.

Output the number of frames for the shortest and longest videos, as well as the median number of frames for all videos.
Output the height and width for of largest and smallest images, as well as the median height and width for all videos.

At the compile stage, I want both accuracy and precision to be output as the metrics.
I also need the code to test the predictions on a test set of videos.