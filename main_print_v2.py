from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

# 기본 변수 설정
name = "Alice"
age = 25
score = 95.5

# Console 객체 생성 (고급 기능 사용 시 유용)
console = Console()

# 1. 기본 print 대신 rich의 print 사용
print("[bold green]Hello, Python![/bold green] :sparkles:")

# 2. Table을 사용해 정보 정리하기
# 표 객체를 생성합니다.
info_table = Table(title="[bold]학생 기본 정보[/bold]", show_header=True, header_style="bold magenta")
info_table.add_column("항목", style="cyan", width=12)
info_table.add_column("값", style="green")

# 표에 데이터를 추가합니다.
info_table.add_row("이름 (Name)", name)
info_table.add_row("나이 (Age)", str(age))
info_table.add_row("점수 (Score)", f"{score:.2f}")

console.print(info_table)

# 3. rich의 print는 데이터 구조를 자동으로 예쁘게 출력
data = {"name": name, "age": age, "score": score}
print("\n[bold]딕셔너리 데이터 자동 출력:[/bold]")
print(data)

# 4. f-string 내에서 스타일링 (Console Markup)
print("\n[bold]f-string 스타일링:[/bold]")
print(f"내년 나이: [bold yellow]{age + 1}[/bold yellow]세")
print(f"점수 (반올림): [bold cyan]{round(score)}[/bold cyan]점")
print(f"2025-09-23") # rich의 print는 sep, end 옵션도 대부분 호환됩니다.

# 5. Panel을 사용해 정보 블록 만들기 (요청하신 부분)
# 패널에 들어갈 내용을 f-string으로 만듭니다.
student_info_str = f"""
[bold]이름[/bold]: [cyan]{name}[/cyan]
[bold]나이[/bold]: [yellow]{age}[/yellow]
[bold]점수[/bold]: [magenta]{score:.2f}[/magenta]
"""

# Panel 객체를 생성하고 출력합니다.
console.print(Panel(
    student_info_str,
    title="[bold bright_blue]Student Info[/bold bright_blue]",
    subtitle="[italic]학생 정보 카드[/italic]",
    border_style="bright_green"
))