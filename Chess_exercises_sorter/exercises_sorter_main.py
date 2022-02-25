import os

dir_path = '/Users/daksh/Library/Mobile Documents/com~apple~CloudDocs/1MyFolder/tmp'
files = os.listdir(dir_path)

for f_path in files:
    file_full_path = os.path.join(dir_path, f_path)
    print(f"***** file full path: {file_full_path} ******")
    with open(file_full_path, 'r') as f:
        lines = f.readlines()
        is_qn_line = False
        is_last_qn_line = False
        qn_lines = []
        sol_lines = []
        for line in lines:
            if '[Event "?"]' in line:
                is_qn_line = True
                if sol_lines:
                    print("\n***** This is a Solution *****")
                    print("\n".join(sol_lines))
                    sol_lines = []

            if is_last_qn_line and line.startswith('[Event '):
                is_qn_line = False
                is_last_qn_line = False
                print("\n***** This is a question *****")
                print("\n".join(qn_lines))
                qn_lines = []

            if is_qn_line:
                qn_lines.append(line)
            else:
                sol_lines.append(line)

            if line.startswith('{[#]'):
                is_last_qn_line = True







