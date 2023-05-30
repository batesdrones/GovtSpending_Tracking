import ast
import traceback

def check_syntax(code):
    try:
        ast.parse(code)
    except SyntaxError as e:
        error_msg = str(e)
        traceback.print_exc()
        if "leading zeros in decimal integer literals" in error_msg:
            corrected_code = code.replace("0", "0o", 1)
            try:
                ast.parse(corrected_code)
            except SyntaxError:
                print("SyntaxError: Leading zeros in decimal integer literals are not permitted. Use an 0o prefix for octal integers instead.")
            else:
                print(f"Suggestion: Update the code to '{corrected_code}'")
                print(corrected_code)
        else:
            raise e
    else:
        print("No syntax errors found.")

# Test the script with example code
code_with_error = "x = 0123"
check_syntax(code_with_error)

code_without_error = "x = 123"
check_syntax(code_without_error)

# Test SQL code separately
sql_code = "9700_9700_N6829222F3001_P00001_N6264920D0020_0, CONT_AWD_N6829222F3001_9700_N6264920D0020_9700, N6829222F3001, P00001, 0.0, 9700, "DEPT OF DEFENSE", N6264920D0020, 0, -16053.41, 20347.6, 0, -16053.41, 20347.6, -16053.41, 20347.6, 0, 0, 0, 0, 0, '2021-12-14 00:00:00', 2022, '2021-10-05 00:00:00', '2021-10-31 00:00:00', '10/31/2021 0:00', 0, 0, 97, 'Department of Defense', 1700, 'Department of the Navy', N68292, 'NAVAL HOSPITAL YOKOSUKA', 97, 'Department of Defense', 1700, 'Department of the Navy', N68292, 'NAVAL HOSPITAL YOKOSUKA', 0, 0, 0, 0, 'X', 'NA', 0

check_syntax(sql_code)