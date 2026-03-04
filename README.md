# 숫자 맞추기 게임

1부터 100 사이 숫자를 컴퓨터가 정하고, 사용자가 입력해 맞추는 콘솔 게임입니다.

## 실행 방법

```bash
python guess_number.py
```

## EXE 파일 만들기 (Windows 포함)

PyInstaller를 사용하면 실행 파일을 만들 수 있습니다.

1) PyInstaller 설치

```bash
pip install pyinstaller
```

2) 실행 파일 빌드

```bash
python build_exe.py
```

3) 결과 확인

- Windows: `dist/guess_number.exe`
- Linux/macOS: `dist/guess_number`

> 참고: EXE는 Windows 환경에서 빌드하는 것을 권장합니다.
