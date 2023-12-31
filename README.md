# ASCII Art Generator

Welcome to my ASCII Art Generator project! This repository contains code that allows you to transform images into captivating ASCII art. This project is based on the tutorial by Robert Heaton, which you can find [here](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/).

## Project Overview

This project involves the following steps:

1. **Load Images:** I use an image processing library to load images and access their pixel data.

2. **Convert to Brightness:** I transform the RGB tuples of pixels into single brightness values.

3. **ASCII Transformation:** I map the brightness values to ASCII characters, creating an ASCII representation of the image.

## Getting Started

To run this project, follow these steps:

1. Clone this repository:

   ```
   git clone https://github.com/joethesaint/ascii-art-generator.git
   ```

2. Install the required library. For Python, you can use Pillow:

   ```
   pip install Pillow
   ```

3. Place your image in the repository directory and update the image path in the code.

4. Run the Python script:

   ```
   python ascii_art_generator.py
   ```

## Code Structure

- `ascii_art_generator.py`: The main script that performs image loading, brightness conversion, and ASCII transformation.

## ASCII Character Mapping

In this project, I've used the following ASCII character set for mapping brightness to characters:

```plaintext
`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
```

## Results

Upon running the script, you'll see the ASCII representation of your image printed in the terminal. Experiment with different images and character sets to create unique ASCII art!

## Acknowledgements

This project is based on Robert Heaton's tutorial on [Programming Projects for Advanced Beginners: ASCII Art](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/).

## License

This project is licensed under the [MIT License](LICENSE).
