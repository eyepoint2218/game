"""PyInstaller를 사용해 실행 파일을 생성합니다.

사용법:
    python build_exe.py

생성 결과:
    - Windows: dist/guess_number.exe
    - Linux/macOS: dist/guess_number
"""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    project_root = Path(__file__).resolve().parent
    target_script = project_root / "guess_number.py"

    if not target_script.exists():
        print("오류: guess_number.py 파일을 찾을 수 없습니다.")
        return 1

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--name",
        "guess_number",
        str(target_script),
    ]

    print("실행:", " ".join(cmd))
    completed = subprocess.run(cmd, cwd=project_root)

    if completed.returncode == 0:
        print("빌드 성공! dist 폴더에서 실행 파일을 확인하세요.")
    else:
        print("빌드 실패. 위 로그를 확인하세요.")

    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
