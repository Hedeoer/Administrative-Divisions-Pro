import json
import pandas as pd
import sys, getopt
import os

def json_to_csv(file_name, out_file=None):
    print('[*] 开始处理：', file_name)
    try:
        with open(file_name, 'r', encoding='utf8') as f:
            jd = json.load(f)
    except:
        with open(file_name, 'r', encoding='gbk') as f:
            jd = json.load(f)
    
    lines = []
    citys = jd['city']
    for c in citys:
        countrys = c['country']
        for cc in countrys:
            towns = cc['town']
            for t in towns:
                villagetrs = t['villagetr']
                for v in villagetrs:
                    line = {
                        'province_name': jd['name'],
                        # 'province_code': jd['code'],
                        'city_name': c['name'],
                        'city_code': c['code'],
                        'town_name': cc['name'],
                        'town_code': cc['code'],
                        'villagetr_name': t['name'],
                        'villagetr_code': t['code'],
                        'street_name': v['name'],
                        'street_code': v['code'],
                        'street_type': v['type']
                    }
                    lines.append(line)
                    # print(line)

    df = pd.DataFrame(lines)
    if out_file:
        df.to_csv(out_file, index=False)
        print(f'[*] 文件转换成功！')
        print(f'[*] 输出文件：{os.path.abspath(out_file)}')
    return df

def convert_directory(input_dir, output_dir, merge=False, merge_filename=None):
    all_data = []
    file_count = 0
    for file in os.listdir(input_dir):
        if file.endswith('.json'):
            file_path = os.path.join(input_dir, file)
            df = json_to_csv(file_path)
            file_count += 1
            if merge:
                all_data.append(df)
            else:
                out_file = os.path.join(output_dir, file.replace('.json', '.csv'))
                df.to_csv(out_file, index=False)
                print(f'[*] 保存文件 {out_file}')
    
    if merge and all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        merge_file = os.path.join(output_dir, merge_filename)
        merged_df.to_csv(merge_file, index=False)
        print(f'[*] 成功合并 {file_count} 个JSON文件！')
        print(f'[*] 合并文件保存为：{os.path.abspath(merge_file)}')
    elif not merge:
        print(f'[*] 成功转换 {file_count} 个JSON文件！')
        print(f'[*] 输出目录：{os.path.abspath(output_dir)}')

def print_help():
    print('*' * 100)
    print('国家统计局行政区划爬虫 Json转CSV')
    print('http://h4ck.org.cn')
    print('obaby@mars')
    print('\n使用方法: python json2csv.py [选项]')
    print('\n选项:')
    print('  -h, --help            显示此帮助信息并退出')
    print('  -i, --input <路径>     指定输入文件或目录的路径')
    print('  -o, --output <路径>    指定输出文件或目录的路径')
    print('  -m, --merge           合并多个json文件为一个csv文件（仅在输入为目录时有效）')
    print('  -f, --filename <文件名> 指定合并后的文件名（仅在使用-m时有效）')
    print('\n示例:')
    print('  处理单个文件:')
    print('    python json2csv.py -i input.json -o output.csv')
    print('  处理目录中的所有json文件，生成多个csv文件:')
    print('    python json2csv.py -i input_directory -o output_directory')
    print('  处理目录中的所有json文件，合并为一个csv文件:')
    print('    python json2csv.py -i input_directory -o output_directory -m -f merged_output.csv')
    print('\n注意:')
    print('  1. 处理单个文件时，如果不指定输出文件名，将自动生成与输入文件同名的csv文件。')
    print('  2. 处理目录时，输出路径必须是一个有效的目录。')
    print('  3. 使用-m参数时必须同时使用-f参数指定合并后的文件名。')
    print('  4. 路径可以是相对路径或绝对路径。')
    print('  5. 如果文件名包含中文，请确保系统支持UTF-8编码。')
    print('\n转换成功提示:')
    print('  - 单个文件转换: 将显示输出文件的完整路径。')
    print('  - 目录转换（非合并）: 将显示成功转换的文件数量和输出目录路径。')
    print('  - 目录转换（合并）: 将显示成功合并的文件数量和合并文件的完整路径。')
    print('*' * 100)

def main(argv):
    input_path = None
    output_path = None
    merge = False
    merge_filename = None
    try:
        opts, args = getopt.getopt(argv, "hi:o:mf:", ["help", "input=", "output=", "merge", "filename="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help()
            sys.exit()
        elif opt in ("-i", "--input"):
            input_path = os.path.abspath(arg)
        elif opt in ("-o", "--output"):
            output_path = os.path.abspath(arg)
        elif opt in ("-m", "--merge"):
            merge = True
        elif opt in ("-f", "--filename"):
            merge_filename = arg

    if input_path:
        if os.path.exists(input_path):
            if os.path.isfile(input_path):
                # 处理单个文件
                if not output_path:
                    output_path = os.path.splitext(input_path)[0] + '.csv'
                elif os.path.isdir(output_path):
                    # 如果输出路径是目录，在目录中创建输出文件
                    output_filename = os.path.basename(os.path.splitext(input_path)[0] + '.csv')
                    output_path = os.path.join(output_path, output_filename)
                json_to_csv(input_path, output_path)
                print(f'[*] 文件转换成功！')
                print(f'[*] 输出文件：{output_path}')
            elif os.path.isdir(input_path):
                # 处理目录
                if not output_path or not os.path.isdir(output_path):
                    print("错误：处理目录时，输出路径必须是一个有效的目录")
                    sys.exit(2)
                if merge and not merge_filename:
                    print("错误：使用-m参数时必须指定-filename")
                    sys.exit(2)
                convert_directory(input_path, output_path, merge, merge_filename)
            else:
                print("错误：输入路径既不是文件也不是目录")
                sys.exit(2)
        else:
            print(f"错误：输入路径不存在 - {input_path}")
            sys.exit(2)
    else:
        print_help()

if __name__ == '__main__':
    main(sys.argv[1:])
