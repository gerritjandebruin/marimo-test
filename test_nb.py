# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.14.16"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    pd.Series([0, 1, 2])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
