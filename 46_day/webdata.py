import pandas as pd

web = pd.read_html("https://en.wikipedia.org/wiki/"
"Python_(programming_language)")

table = web [1]
print(table.head())


