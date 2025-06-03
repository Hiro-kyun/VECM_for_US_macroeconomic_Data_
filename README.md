# Phan tich dong lien ket giua GDP va PCE bang mo hinh VECM

## Gioi thieu

Du an nay su dung mo hinh Vector Error Correction Model (VECM) de phan tich moi quan he dai han giua Tong san pham quoc noi thuc te (Real GDP - `GDPC1`) va Chi tieu tieu dung ca nhan (Personal Consumption Expenditures - `PCE`) cua My. Du lieu duoc lay tu tep CSV `merged_gdp_pce.csv`.

## Cac buoc thuc hien

1. **Doc va xu ly du lieu:**

   * Doc du lieu tu file CSV.
   * Chuyen doi cot `Date` thanh dinh dang thoi gian va dat lam chi muc.

2. **Chuan hoa du lieu:**

   * Chuan hoa GDP va PCE de ve bieu do tren cung mot truc y.

3. **Kiem tra tinh dung:**

   * Su dung kiem dinh Augmented Dickey-Fuller (ADF) de kiem tra tinh dung cua chuoi GDP va PCE (o muc goc va sai phan bac mot).

4. **Kiem tra dong lien ket:**

   * Su dung kiem dinh Johansen de xac dinh so luong quan he dong lien ket giua GDP va PCE.

5. **Uoc luong mo hinh VECM:**

   * Neu co dong lien ket, mo hinh VECM se duoc uoc luong.
   * Trich xuat vector dong lien ket (`beta`) va chuan hoa quan he dong lien ket.

6. **Truc quan hoa du lieu:**

   * Ve bieu do so sanh GDP, PCE va quan he dong lien ket (neu co) theo thoi gian.

## Yeu cau he thong

* Python 3.x
* Cac thu vien can thiet:

  ```bash
  pip install pandas numpy matplotlib statsmodels
  ```

## Cau truc tep CSV yeu cau

Tep `merged_gdp_pce.csv` phai chua it nhat 3 cot sau:

* `Date`: Chuoi ngay o dinh dang `YYYY-MM-DD`
* `GDPC1`: Tong san pham quoc noi thuc te
* `PCE`: Chi tieu tieu dung ca nhan

Vi du:

```csv
Date,GDPC1,PCE
1959-01-01,1234.56,789.01
1959-04-01,1245.67,790.12
...
```

## Ket qua dau ra

* In ra man hinh ket qua kiem dinh ADF cho tung chuoi.
* In ket qua kiem dinh Johansen de xac dinh so quan he dong lien ket.
* Neu co dong lien ket: in mo hinh VECM va vector dong lien ket.
* Bieu do hien thi GDP, PCE va quan he dong lien ket da chuan hoa.
