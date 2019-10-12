# Investment-Charges-Comparison

While trying to compare investment options against their various attributes, I needed the capability to calculate and graph the data to help me evaluate my choices.

I was not able to find a program which could achieve this, so I created this Python script to calculate and plot the data. Hopefully, you can also find a use for the script in helping you evaluate your choices!

## Installation

```
sudo pacman -S python python-matplotlib
```

## Usage

The Python script reads in the values from a CSV file. This allows you to graph as many investments as you desire. You can define the input via the arguement `--input`.

e.g.

```
./investment-charges-comparison --input data.csv
```

## CSV Format

```
Format : Name, Colour, Monthly Contribution, Duration, Growth, Platform Fee, Platform Cap, Fund Fee

e.g.

HL, red, 200, 20, 5, 0, 0, 0.1
Vangaurd, green, 200, 20, 5, 0, 0, 0.15

```

