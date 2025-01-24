import pyautogui
import openpyxl
import pyperclip  # 클립보드 복사를 위한 라이브러리
import time

# 엑셀 파일 읽기
def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active  # 첫 번째 시트 사용
    return sheet, workbook

# 엑셀 파일에 처리 완료 여부 기록
def mark_done(sheet, row_num):
    sheet[f'B{row_num}'] = 'o'  # B열에 'o' 기록
    print(f"Row {row_num}: 처리 완료")

# 자동화 작업
def automate_process(sheet, start_row=1, end_row=260, file_path='auto.xlsx'):
    for i in range(start_row, end_row):  # A열의 start_row부터 end_row까지 작업
        acctn_value = sheet[f'A{i}'].value  # A열에서 acctn 읽기

        if acctn_value:  # 값이 있을 경우에만 실행
            # 숫자 타입이면 문자열로 변환
            acctn_value = str(acctn_value)

            # 값을 클립보드에 복사
            pyperclip.copy(acctn_value)
            print(f"Row {i}: 클립보드에 복사된 값 - {acctn_value}")

            # 1. 사내 프로그램에 acctn# 입력
            pyautogui.moveTo(625, 329)  # acct no 위치
            pyautogui.click()

            time.sleep(1)  # 클릭 후 잠시 대기

            pyautogui.click()

            time.sleep(1)  # 클릭 후 잠시 대기
            pyautogui.press('right')
            pyautogui.press('backspace')  # 기존 값 삭제
            pyautogui.press('backspace')  # 기존 값 삭제

            pyautogui.press('backspace')  
            pyautogui.press('backspace')  
            
            pyautogui.press('backspace')  
            pyautogui.press('backspace')
            pyautogui.press('backspace')  
            pyautogui.press('backspace')          
            pyautogui.press('delete')
            pyautogui.press('delete')
            pyautogui.press('delete')
            pyautogui.press('delete')


            time.sleep(1)  # 클릭 후 잠시 대기

            # 클립보드에 값 붙여넣기 시도
            pyautogui.hotkey('ctrl', 'v')  # Ctrl + V로 붙여넣기
            time.sleep(2)

            pyautogui.press('enter')

            time.sleep(2)  # 프로그램에서 반응을 기다림

            # 2. Transaction 탭 클릭
            pyautogui.moveTo(702, 190)  # transaction 위치
            pyautogui.click()

            time.sleep(1)

            # 3. Transaction type 클릭
            pyautogui.moveTo(990, 429)  # Transaction type 위치
            pyautogui.click()

            time.sleep(1)

            # 4. Credit 선택
            pyautogui.moveTo(924, 481)  # credit 위치
            pyautogui.click()

            time.sleep(1)

            # 5. Amount에 -6 입력
            pyautogui.moveTo(979, 464)  # amount 위치
            pyautogui.click()
            pyautogui.write('-15')  # 새로운 값 입력
            pyautogui.press('delete')  # 기존 값 삭제

            time.sleep(1)

            pyautogui.moveTo(922, 668)
            pyautogui.click()
            pyperclip.copy("구독금액변경 크레딧")
            time.sleep(1)
            pyperclip.copy("구독금액변경 크레딧")
            pyautogui.hotkey('ctrl', 'v')  # Ctrl + V로 붙여넣기
            time.sleep(3)

            pyautogui.moveTo(959, 748)
            pyautogui.click()


            time.sleep(1)  # 잠시 대기

# 메인 실행 부분
if __name__ == "__main__":
    file_path = r"C:\Users\admin\OneDrive\바탕 화면\a118.xlsx"  # 엑셀 파일 경로
    sheet, workbook = read_excel(file_path)
    automate_process(sheet, start_row=1, end_row=117, file_path=file_path)
