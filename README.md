# Parallel-High-Pass-Filter

## Description:

It is used to make the image appear sharper. Note, if there is no change in intensity, nothing happens. But if one pixel is brighter than its neighbors, it gets boosted. High
pass filters amplifies noise. It allows high frequency components of the image to pass through and block low frequencies. The image will The idea is the same as the Low
Pass Filter above but with using another kernel which is:
<br>

     [ 0 -1  0 ]
     [ -1 4 -1 ]
     [ 0 -1  0 ]


## Input and Output:

<img src="https://user-images.githubusercontent.com/45972231/137756488-0023bde2-29e2-499c-9497-892a056edd4c.png" height="427" width="434"> ![Capture](https://user-images.githubusercontent.com/45972231/137756064-727956bc-5d0d-401c-8f42-2af75d36a7b7.PNG)


