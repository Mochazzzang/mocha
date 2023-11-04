import openpyxl
from openpyxl.styles import Font, Side, Border, Alignment

save_path = '03. 엑셀 자동화/total.xlsx'

# 기존의 엑셀 파일 불러오기
wb = openpyxl.load_workbook(save_path)

# 시트 선택
ws = wb['data']

# 열 너비 변경
ws.column_dimensions['B'].width = 20

# 행 높이 변경
ws.row_dimensions[1].height = 30

# 저장
wb.save(save_path)