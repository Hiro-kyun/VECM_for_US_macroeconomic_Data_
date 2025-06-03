import pandas as pd

# Đọc hai file CSV
gdp = pd.read_csv('GDPC1.csv')
pce = pd.read_csv('PCE.csv')

# Đổi tên cột để dễ phân biệt
gdp = gdp.rename(columns={'Value': 'GDP'})
pce = pce.rename(columns={'Value': 'PCE'})

# Gộp dữ liệu dựa trên cột 'Date'
merged_data = pd.merge(gdp, pce, on='Date', how='inner')

# Lưu kết quả vào file CSV mới
merged_data.to_csv('merged_gdp_pce.csv', index=False)

# Hiển thị kết quả
print(merged_data)