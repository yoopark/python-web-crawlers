import sys
import requests
from bs4 import BeautifulSoup
import subprocess

if len(sys.argv) != 3:
    print("Error: Insufficient arguments")
    print("Usage: python crawler.py [Problem Number] [Your Python Filename]")
    sys.exit()
    

problem_num = int(sys.argv[1])
url = "https://acmicpc.net/problem/" + str(problem_num)
response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

filename = sys.argv[2]
filename = filename.strip()
if filename[-3:] != ".py":
    filename += ".py"

def diff(lines1, lines2):
    for i, (l1, l2) in enumerate(zip(lines1, lines2)):
        l1, l2 = l1.rstrip(), l2.rstrip()
        if l1 != l2:
            return i+1
    return 0

def print_with_line_num(lines):
    for i, line in enumerate(lines):
        print(str(i+1).rjust(3, " ") + "|" + line)

title = html.select_one("#problem_title").text
print(f"{problem_num}번: {title}")
print("--------------")
        
for i in range(1, 10): # 예제 입력 1 ~ 9
    sample_input_elem = html.select_one("#sample-input-" + str(i))
    if not sample_input_elem:
        break
    sample_output_elem = html.select_one("#sample-output-" + str(i))
    
    sample_input = sample_input_elem.text
    sample_output = sample_output_elem.text

    ps = subprocess.run(
        args=["python", filename], 
        input=sample_input.encode("UTF-8"),
        capture_output=True
    )
    
    user_output = ps.stdout.decode("UTF-8")
    
    sample_output = sample_output.rstrip("\r\n ")
    user_output = user_output.rstrip("\n ")
    
    sample_output_lines = sample_output.split("\n")
    user_output_lines = user_output.split("\n")
    
    result = diff(sample_output_lines, user_output_lines)
    if result == 0:
    	print("TEST", i, "✔️")
    else:
        print("TEST", i, "❌")
        print("[Input]")
        print(sample_input)
        print("[Expected]")
        print_with_line_num(sample_output_lines)
        print(f"[Output] (check line {result})")
        print_with_line_num(user_output_lines)
    print("--------------")
