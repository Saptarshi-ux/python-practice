#The tax calculation structure for the New Tax Regime:


gross_income=int(input("Enter ur Gross Annual Income:"))
is_salaried=input("Are u a salaried employee? (Yes/No):").strip().lower()
std_deduction=75000 if is_salaried=="yes" else 0
taxable_income=max(0,gross_income-std_deduction)
final_taxable_income=taxable_income

tax=0
if taxable_income>2400000:
  tax+=(taxable_income-2400000)*0.30
  taxable_income=2400000
if taxable_income>2000000:
  tax+=(taxable_income-2000000)*0.25
  taxable_income=2000000
if taxable_income>1600000:
  tax+=(taxable_income-1600000)*0.20
  taxable_income=1600000
if taxable_income>1200000:
  tax+=(taxable_income-1200000)*0.15
  taxable_income=1200000
if taxable_income>800000:
  tax+=(taxable_income-800000)*0.10
  taxable_income=800000
if taxable_income>400000:
  tax+=(taxable_income-400000)*0.05
  taxable_income=400000

#Apply Section 87A Rebate (No tax if taxable income <= 12L)
if final_taxable_income<=1200000:
  tax=0
#Surcharge
surcharge=0
if final_taxable_income>20000000:
  surcharge=tax*0.25
elif final_taxable_income>5000000:
  surcharge=tax*0.1

total_tax=tax+surcharge
print(f"\nYour Taxable Income is: INR {final_taxable_income:,.2f}")
print(f"The total tax payable for FY 2025-26 is: INR {total_tax:,.2f}")





