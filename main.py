import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.vecm import VECM, select_coint_rank

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv("merged_gdp_pce.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
gdp = data['GDPC1']
pce = data['PCE']

# Chuẩn hóa dữ liệu để vẽ trên cùng trục
gdp_normalized = (gdp - gdp.mean()) / gdp.std()
pce_normalized = (pce - pce.mean()) / pce.std()

# Bước 1: Kiểm tra tính dừng (ADF Test)
def adf_test(series, name):
    result = adfuller(series, autolag='AIC')
    print(f'ADF Test for {name}:')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print(f'Critical Values: {result[4]}')
    print('Stationary' if result[1] < 0.05 else 'Non-stationary')
    print()

# Kiểm tra tính dừng trên mức và sai phân bậc một
adf_test(gdp, 'GDPC1 (Level)')
adf_test(gdp.diff().dropna(), 'GDPC1 (First Difference)')
adf_test(pce, 'PCE (Level)')
adf_test(pce.diff().dropna(), 'PCE (First Difference)')

# Bước 2: Kiểm tra đồng liên kết (Johansen Test)
data_vecm = data[['GDPC1', 'PCE']].dropna()
johansen_test = select_coint_rank(data_vecm, det_order=0, k_ar_diff=2)
print(johansen_test.summary())

# Bước 3: Ước lượng mô hình VECM
cointegrating_relation = None
if johansen_test.rank > 0:
    model = VECM(data_vecm, k_ar_diff=2, coint_rank=1)
    vecm_fit = model.fit()
    print(vecm_fit.summary())

    # Lấy quan hệ đồng liên kết (beta)
    beta = vecm_fit.beta
    print(f'Cointegrating vector (beta): {beta}')

    # Tính quan hệ đồng liên kết và chuẩn hóa
    cointegrating_relation = np.dot(data_vecm, beta)
    cointegrating_normalized = (cointegrating_relation - cointegrating_relation.mean()) / cointegrating_relation.std()
else:
    print("No cointegration found. Cannot estimate VECM.")

# Bước 4: Vẽ biểu đồ đơn giản bằng Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(data.index, gdp_normalized, label='GDPC1 (Normalized)', color='blue')
plt.plot(data.index, pce_normalized, label='PCE (Normalized)', color='orange')
if cointegrating_relation is not None:
    plt.plot(data.index, cointegrating_normalized, label='Cointegrating Relation (Normalized)', color='green')
plt.title('Normalized GDPC1, PCE, and Cointegrating Relation (1959-2025)')
plt.xlabel('Date')
plt.ylabel('Normalized Values')
plt.legend()
plt.grid(True)
plt.show()