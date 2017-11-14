import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_run():

    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts.plot()
    plt.show()

if __name__ == "__main__":
    test_run()