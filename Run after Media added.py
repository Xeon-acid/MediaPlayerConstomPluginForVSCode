import os
import re

# 定义 HTML 文件路径
html_file_path = "workbench.html"
media_dir = "./media"  # 媒体目录路径（正斜杠）

# 检查 media 目录是否存在
if not os.path.exists(media_dir):
    print(f"错误：{media_dir} 目录不存在。")
    exit()

# 获取媒体文件并强制使用正斜杠
media_files = [
    os.path.join(media_dir, f).replace("\\", "/")  # 关键修改：替换反斜杠
    for f in os.listdir(media_dir)
    if f.lower().endswith(('.mp4', '.mp3', '.wav'))
]

if not media_files:
    print(f"{media_dir} 目录下没有支持的媒体文件。")
    exit()

# 显示文件名（不带路径）
print(f"{media_dir} 目录下的媒体文件：")
for i, file in enumerate(media_files, start=1):
    print(f"[{i}] {os.path.basename(file)}")

# 用户选择
user_input = input("请输入需要的文件编号和顺序（空格分隔，直接回车使用默认顺序，输入0载入空列表）：").strip()

if user_input:  # 如果用户输入了内容
    if user_input == "0":  # 如果用户输入0
        selected_files = []  # 载入空列表
        print("已选择载入空列表。")
    else:
        selected_indices = list(map(int, user_input.split()))
        selected_files = [media_files[i-1] for i in selected_indices]  # 已包含正斜杠路径
else:  # 如果用户直接回车
    selected_files = media_files  # 使用默认顺序
    print("使用默认顺序：")
    for i, file in enumerate(selected_files, start=1):
        print(f"[{i}] {os.path.basename(file)}")

# 更新HTML文件
with open(html_file_path, 'r+', encoding='utf-8') as f:
    updated = re.sub(
        r'const videos\s*=\s*\[.*?\];',
        f'const videos = {selected_files};',
        f.read(),
        flags=re.DOTALL
    )
    f.seek(0)
    f.write(updated)
    f.truncate()

print(f"播放列表已更新：\n{selected_files}\n请重启VS Code生效。")