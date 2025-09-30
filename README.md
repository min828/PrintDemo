# Python Print Formatting Examples 🐍

이 저장소는 파이썬의 표준 `print` 함수부터 강력한 `rich` 라이브러리를 활용한 고급 터미널 스타일링에 이르기까지, 다양한 출력 형식 지정 방법을 보여주는 예제 코드 모음입니다.

---

## 📂 프로젝트 파일 소개

* **`main_print_v1.py`**: 파이썬의 기본 `print()` 함수와 여러 표준 서식 지정 기법(f-string, `.format()` 등)을 보여주는 간단한 스크립트입니다.
* **`main_print_v1.ipynb`**: `main_print_v1.py`와 동일한 코드를 주피터 노트북 환경에서 대화형으로 실행할 수 있도록 만든 파일입니다.
* [cite_start]**`main_print_v2.py`**: `rich` 라이브러리를 사용하여 터미널에 색상, 표, 패널 등 다채롭고 구조적인 출력을 만드는 방법을 보여주는 고급 스크립트입니다. [cite: 1]
* [cite_start]**`requirements.txt`**: `main_print_v2.py`를 실행하는 데 필요한 파이썬 패키지 목록입니다. [cite: 1]

---

## ✨ 주요 기능 및 예제

### 기본 출력 예제 (`v1` 스크립트)

* **f-string**을 사용한 변수 출력
* `str.format()` 메서드를 사용한 서식 지정
* `%` 연산자를 사용한 C언어 스타일 서식 지정
* `end`와 `sep` 파라미터를 사용한 출력 제어
* 여러 줄 문자열(`"""..."""`) 출력

### `rich` 라이브러리 활용 예제 (`v2` 스크립트)

* **색상 및 스타일**이 적용된 텍스트 출력 (`[bold green]...[/]`)
* 데이터를 깔끔하게 정리하는 **표(Table)** 생성
* 텍스트 블록을 시각적으로 강조하는 **패널(Panel)** 사용
* 딕셔너리, 리스트 등 데이터 구조 **자동 예쁘게 출력(Pretty Printing)**

---

## 🚀 설치 및 실행 방법

### 1. 환경 설정

먼저 이 저장소를 복제(clone)하고, 가상 환경을 설정한 뒤 필요한 패키지를 설치합니다.

```bash
# 1. 프로젝트 폴더로 이동
# cd your-project-folder

# 2. 가상 환경 생성
python -m venv venv

# 3. 가상 환경 활성화
# Windows
# venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

# 4. requirements.txt 파일로 패키지 설치
pip install -r requirements.txt
```

### 2. 스크립트 실행

터미널에서 아래 명령어를 입력하여 각 스크립트를 실행할 수 있습니다.

```bash
# 기본 print 예제 실행
python main_print_v1.py

# Rich 라이브러리 예제 실행
python main_print_v2.py
```

`main_print_v1.ipynb` 파일은 VS Code, Jupyter Lab, Jupyter Notebook과 같은 환경에서 열어 셀 단위로 실행해 보세요.

---

## 🖼️ 실행 결과 비교

### `main_print_v1.py`의 일반 출력

```text
Hello,Python!
Name ALice Age: 25 Score 95.5
My name is ALice, I am [25 years old, score 95.5
My name is ALice, I am 25 years old, score: 95.5
...
Student Info:
 -Name : ALice
 -Age : 25
 -Score : 95.50
```

### `main_print_v2.py`의 Rich 라이브러리 출력

(실제 터미널에서는 아래 출력이 모두 색상과 스타일이 적용되어 보입니다.)
```text
 Hello, Python! ✨

                              학생 기본 정보
┏━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ 항목         ┃ 값       ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ 이름 (Name)  │ Alice    │
│ 나이 (Age)   │ 25       │
│ 점수 (Score) │ 95.50    │
└──────────────┴──────────┘

 딕셔너리 데이터 자동 출력:
{
    'name': 'Alice',
    'age': 25,
    'score': 95.5
}

 f-string 스타일링:
내년 나이: 26세
점수 (반올림): 96점
2025-09-23

╭──────────────── Student Info ─────────────────╮
│                                               │
│ 이름: Alice                                   │
│ 나이: 25                                      │
│ 점수: 95.50                                   │
│                                               │
╰──────────────── 학생 정보 카드 ────────────────╯
```