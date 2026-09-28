# Stock Portfolio Tracker

A simple console program that calculates the total value of a stock portfolio using manually defined stock prices.

**Author:** Pratyush Singh

---

## Features

- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN)
- User enters stock names and quantities (type `done` to finish)
- Shows the value of each holding and the total investment
- Handles invalid stock names and invalid quantities without crashing
- Entering the same stock again adds to its quantity
- Optionally saves the summary to `portfolio.txt`

## Concepts Used

Dictionary, input/output, basic arithmetic, loops, file handling

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run

1. Keep `stock_tracker.py` in a folder.
2. Open a terminal in that folder.
3. Run:

```
python stock_tracker.py
```

If `python` is not recognized, use `py stock_tracker.py`.

## Sample Run

```
=== STOCK PORTFOLIO TRACKER ===
Available stocks and prices:
  AAPL: $180
  TSLA: $250
  GOOGL: $140
  MSFT: $330
  AMZN: $130

Enter stock name and quantity. Type 'done' to finish.

Stock name: aapl
Quantity of AAPL: 10
Added 10 x AAPL

Stock name: tsla
Quantity of TSLA: 5
Added 5 x TSLA

Stock name: done

--- Portfolio Summary ---
AAPL: 10 x $180 = $1800
TSLA: 5 x $250 = $1250
-------------------------
Total Investment: $3050

Save result to a file? (y/n): y
Saved to portfolio.txt
```

## Changing Stock Prices

Edit the `STOCK_PRICES` dictionary at the top of `stock_tracker.py`:

```python
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
}
```

## Files

```
task2_stock_tracker/
├── README.md
└── stock_tracker.py
```

`portfolio.txt` is created automatically when you choose to save.
