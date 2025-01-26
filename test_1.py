import os
import subprocess
import time
from datetime import datetime, timedelta

# Git 저장소 경로와 대상 폴더 경로
REPO_PATH = "C:/Users/admin/OneDrive/바탕 화면/AutoCommit"  # 경로 수정 (백슬래시 문제 해결)
FOLDER_PATH = "C:/Users/admin/OneDrive/바탕 화면/AutoCommit" 


COMMIT_INTERVAL = 86400  # 하루에 한 번 (24시간 간격)

def commit_and_push(file_path):
    try:
        # Git 명령 실행
        subprocess.run(["git", "add", file_path], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", f"Test commit: {os.path.basename(file_path)}"], cwd=REPO_PATH, check=True)
        # 원격 저장소와 연결 후 푸시
        subprocess.run(["git", "push", "--set-upstream", "origin", "main"], cwd=REPO_PATH, check=True)  # 'main' 브랜치로 수정
        print(f"Committed and pushed: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during commit/push: {e}")

def main():
    # 커밋 기록용 파일
    log_file = os.path.join(REPO_PATH, "commit_log.txt")
    committed_files = set()

    # 이전에 커밋된 파일 로드
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            committed_files = set(f.read().splitlines())

    # 대상 폴더에서 Python 파일 찾기
    files = sorted([f for f in os.listdir(FOLDER_PATH) if f.endswith(".py")])

    # 아직 커밋되지 않은 파일 찾기
    for file_name in files:
        file_path = os.path.join(FOLDER_PATH, file_name)
        if file_path not in committed_files:
            commit_and_push(file_path)
            
            # 커밋 로그에 기록
            with open(log_file, "a") as f:
                f.write(file_path + "\n")
            
            # 다음 파일까지 대기 (하루에 한 번 커밋되도록 설정)
            print("Waiting for the next commit...")
            time.sleep(COMMIT_INTERVAL)  # 하루에 한 번 커밋

if __name__ == "__main__":
    main()
