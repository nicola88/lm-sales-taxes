# Sales taxes

## Problem

Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. 
Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.

When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), 
finishing with the total cost of the items, and the total amounts of sales taxes paid. 

The rounding rules for sales tax are that for a tax rate of n%, 
a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.

Write an application that prints out the receipt details for these shopping baskets...

### INPUT

Input 1:
- 1 book at 12.49
- 1 music CD at 14.99
- 1 chocolate bar at 0.85

Input 2:
- 1 imported box of chocolates at 10.00
- 1 imported bottle of perfume at 47.50

Input 3:
- 1 imported bottle of perfume at 27.99
- 1 bottle of perfume at 18.99
- 1 packet of headache pills at 9.75
- 1 imported box of chocolates at 11.25

### OUTPUT

Output 1:
- 1 book : 12.49
- 1 music CD: 16.49
- 1 chocolate bar: 0.85

Sales Taxes: 1.50

Total: 29.83

Output 2:
- 1 imported box of chocolates: 10.50
- 1 imported bottle of perfume: 54.65

Sales Taxes: 7.65

Total: 65.15

Output 3:
- 1 imported bottle of perfume: 32.19
- 1 bottle of perfume: 20.89
- 1 packet of headache pills: 9.75
- 1 imported box of chocolates: 11.85

Sales Taxes: 6.70

Total: 74.68

## Requirements

- Python 3.6

## Usage

```bash
git clone https://github.com/nicola88/lm-sales-taxes.git
cd lm-sales-taxes
python print-receipt.py
```

The Python script computes sales taxes and total for each sample purchase file found in the _samples_ folder.

The purchase file must be a CSV file with headers and the following columns:

1. `name`: product name
2. `price`: product price
3. `category`: product category (admitted values: _book_, _food_, _medical_, _other_)
4. `imported`: if the product is imported (admitted values: _true_, _false_)
5. `quantity`: number of items purchased

The receipt is printed on the standard output as follows:

```
SIMULATION > <filename>

# One line for each product
<quantity> <product_name>: <product_subtotal_including_taxes>

Sales Taxes: <sales_taxes>

Total: <total>

```