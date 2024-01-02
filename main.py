import os

csv_file = 'selected_stocks.csv'

if os.path.exists(csv_file):
    os.startfile(csv_file)
else:
    print(f"{csv_file} 파일을 찾을 수 없습니다.")

