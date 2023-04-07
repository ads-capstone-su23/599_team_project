# Folder Notes

## Websites
* https://pywavelets.readthedocs.io/en/latest/
* https://joss.theoj.org/papers/10.21105/joss.01237
* https://nicolasfauchereau.github.io/posts/wavelet-analysis-with-python/

## Books
* https://github.com/CRCTransformers/deepdive-book
* https://a.co/d/5lULGTB
* https://a.co/d/5anpNFa
* https://a.co/d/aFApfv6

## Videos
* "Understanding Wavelets, Part 1: What Are Wavelets": https://youtu.be/QX1-xGVFqmw
* "The Wavelet Transform for Beginners": https://youtu.be/kuuUaqAjeoA

## chatGPT notes
Wavelet transform is a powerful tool for analyzing signals and data in various domains, including images and videos. One way to use wavelet transform for predicting image or video data is by using it as a feature extraction method and then using a machine learning algorithm to predict future data points.

Here are the general steps for using wavelet transform for prediction:
1. Preprocess the image or video data to prepare it for analysis. This may involve resizing the data, converting it to grayscale, or normalizing the pixel values.
2. Apply wavelet transform to the image or video data to extract relevant features. The wavelet transform breaks down the signal into different frequency bands, allowing you to analyze the data at different scales.
3. Select the wavelet coefficients that contain the most useful information for prediction. This can be done through feature selection techniques or by examining the coefficients visually.
4. Train a machine learning algorithm on the selected wavelet coefficients to learn the patterns in the data and make predictions. The algorithm can be a regression model, classification model, or any other type of predictive model that is suitable for your data.
5. Test the trained model on new data to evaluate its accuracy and adjust the parameters if necessary.

It is worth noting that wavelet transform can also be used directly for prediction without the need for feature extraction. This approach involves applying wavelet transform to the data at each time step and then using the resulting coefficients to make predictions for the next time step. This is known as wavelet time series analysis and can be useful for predicting time-varying data such as video frames. However, this approach can be computationally expensive and may require a significant amount of memory, depending on the size of the data.
