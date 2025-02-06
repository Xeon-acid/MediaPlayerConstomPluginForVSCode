import sys
import re

def update_opacity(file_path, opacity_value):
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式替换 opacity 值
        updated_content = re.sub(
            r'\.monaco-workbench\{opacity: \d+(\.\d+)? !important;\}',
            f'.monaco-workbench{{opacity: {opacity_value} !important;}}',
            content
        )

        # 将更新后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"成功将 opacity 更新为 {opacity_value}！")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 检查参数是否正确
    if len(sys.argv) != 2:
        print("使用方法: python opacity.py <number>")
        sys.exit(1)

    # 获取 opacity 值
    opacity_value = sys.argv[1]

    # 文件路径
    file_path = r"..\..\..\workbench\workbench.desktop.main.css"

    # 调用函数更新 opacity
    update_opacity(file_path, opacity_value)