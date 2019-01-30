# Square Fit Image
[![Powered By Electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)]()
[![Build With Love](https://forthebadge.com/images/badges/built-with-love.svg)]()


This script allows user to add white color (can be changed via code) to a directory containing images and resize them to square shape, without stretching or diminishing them! (Recursive, not checked)

For example, if I have an image thats 1920x1080 (ie. in landscape), this script will add white borders automatically to top and bottom to make it 1920x1920 (ie. the bigger of the two dimensions). Pretty Neat.

---

### Prerequisites
You must have PIL or Pillow installed. To install it using pip, use the code below:

```
pip install pillow
```

---

### Usage
Run the script and enter the absoulute path of directory that contains the image. If the script finds an image it will be converted and stored in a folder 'converted' relative to input path.

---

### Screenshots
Left image is original and right one is converted!
<p align="center"><img src="https://raw.githubusercontent.com/vaibhavkandwal/square-fit-image/master/screen1.png"></p>
<p align="center"><img src="https://raw.githubusercontent.com/vaibhavkandwal/square-fit-image/master/screen2.png"></p>
