import openpyxl

save_path = '03. 엑셀 자동화/스마트스토어.xlsx'

# 기존 엑셀 파일 불러오기
wb = openpyxl.load_workbook(save_path)

# data 시트 선택
ws = wb['data']

# 01. 모든 셀 데이터 가져오기
# -> 행과 열 개수를 아는 경우
for x in range(1, 9+1):
  for y in range(1, 5+1):
      print(ws.cell(row=x,column=y).value, end=" ")
  print()
