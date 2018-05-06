import pandas as pd
import math, quandl, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01 * len(df))) #Math ceil - zaokrąglenie do góry do następnej pełnej
# obliczamy 1% z próbki danych, wychodzi tutaj nam 35 dni

df['label'] = df[forecast_col].shift(-forecast_out) # tworzymy kolumne w której label to ile koszt akcji za te 35 dni wyliczone
# shift pozwala nam przesunac o te 35 dni ;)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X) # przy często powtarzajacych sie obliczeniach w czasie rzeczywistym krok często pomijany

X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print("Accuracy of Linear regression: ",accuracy)

forecast_set = clf.predict(X_lately)
#print(forecast_set)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400 #sekund w dniu
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    # Czyli dodajemy te 35 nowych dni, gdzie nie mamy danych do wszystkich kolumn - więc NAN, a na koncu dodajemy i -> forecast

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc='best')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

