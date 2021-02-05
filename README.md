# OpenCV

<i>OpenCV is a library of programming functions mainly aimed at real-time computer vision. (Originally developed by Intel)</i>

<h2>Image Processing Vs Computer Vision</h2>

  In <b>image processing</b>, an image is "processed", that is, transformations are applied to an input image and an output image is returned. The transformations can e.g. be "smoothing", "sharpening", "contrasting" and "stretching". The transformation used depends on the context and issue to be solved.

  In <b>computer vision</b>, an image or a video is taken as input, and the goal is to understand (including being able to infer something about it) the image and its contents. Computer vision uses image processing algorithms to solve some of its tasks.

  The main difference between these two approaches are the goals (not the methods used). For example, if the goal is to enhance an image for later use, then this may be called image processing. If the goal is to emulate human vision, like object recognition, defect detection or automatic driving, then it may be called computer vision.
  
<h2>Storing an Image</h2>

<b>The Mat class</b> of OpenCV library is used to store the values of an image. It represents an n-dimensional array and is used to store image data of grayscale or color images, voxel volumes, vector fields, point clouds, tensors, histograms, etc.

This class comprises of two data parts: the header and a pointer

<b>Header</b> − Contains information like size, method used for storing, and the address of the matrix (constant in size).

<b>Pointer</b> − Stores the pixel values of the image (Keeps on varying).
