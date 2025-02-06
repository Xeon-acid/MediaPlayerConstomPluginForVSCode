# 媒体播放魔改插件使用说明

本魔改依靠 DeepSeek 完成, 作者并未系统学过相关的 Python, JavScript, HTML, CSS 代码, 其中错误之处, 还请有闲之士斧正. 文件中的 audio.jpg 仅用作示例, 如有侵权, 请联系本作者立即删除.

## 修改透明度

在 `<VS Code 根目录>\resources\app\out\vs\workbench\workbench.desktop.main.css` 的最后添加一句

```CSS
.monaco-workbench{opacity: 0.8 !important;}
```

可能会有警告, 无需理会. 可以将 0.8 自行调整为喜欢的不透明度, 建议不低于 0.7. 设为 1 时完全不透明, 也就是不可见背景.

同级目录下提供 `opacity.py` 脚本文件以设置透明度.

使用方式:

```python
python .\opacity.py <Number in 0 to 1>
```

举例, 执行 `python .\opacity.py 0.8` 可将透明度设置为 0.8.

修改之后必须重启 VS Code 才能应用.

## 替换 HTML 文件

将提供的  `workbench.html` 和 `Run after Media added.py` 文件置于目录 `<VS Code>\resources\app\out\vs\code\electron-sandbox\workbench` 下, 替换掉原本的 `workbench.html` 文件.

可以自行修改 html 中的内容.

## 刷新媒体文件列表

同级目录下提供 `Run after Media added.py` 脚本文件以设置媒体文件列表.

支持的媒体文件包括 `.mp4`, `.mp3`, `.wav`, 支持字幕文件 `.lrc` 及 `.wav`.

在 `workbench.html` 所在目录下新建一个子目录 `media`, 再将喜欢的媒体文件和字幕文件扔进去. 注意字幕文件前缀名要严格等同于对应媒体文件前缀名.

在此处打开命令行, 然后运行 Python 脚本 `Run after Media added.py`. 脚本会读取 media 目录中所有支持的媒体文件, 然后给出列表, 输入希望选择的指定顺序, 即可向 `.html` 文件自动重载媒体文件列表.

如果不输入直接回车, 脚本会以默认顺序全部载入; 如果输入 0 回车, 脚本会载入空列表.

更改 `.html` 文件后, 包括运行 Python 脚本后, 重启 VS Code 或在 VS Code 顶栏依次点击 `帮助 -> 切换开发人员工具`, 将页面作为 HTML 本地网页刷新.

## 状态栏功能说明

提供若干选项, 用处依次是 向前切换媒体, 暂停/播放, 向后切换媒体, 切换静音 (提供对数坐标形式的音量滑块), 切换单集循环/列表循环, 直接选择切换媒体.

## 其他文件

* **audio.jpg:** 播放音频时的背景图片. 可自行更改, 但要将 `.html` 内的名称同时更改, 否则不会加载背景图片;
* **ChironSungHK-B_0.ttf:** 存在歌词文件时, 歌词文本采用的字体. 可自行更改, 注意同上一条.

## 视频媒体声音问题

VS Code 用的 `ffmpeg.dll` 是魔改过的, 只需换成 Electron 相应版本的即可.

方式:

1. VS Code 顶栏依次点击 `帮助 -> 关于`, 查看 Electron 版本.
2. 去[这里](https://registry.npmmirror.com/binary.html?path=electron/)下载对应版本的 Electron 压缩包, 从里面取出 ffmpeg.dll, 替换掉 VS Code 根目录的同名文件.
3. 重启应用.

## 注意

1. 建议自行备份原本的 `workbench.html` 等文件, 以免修改错误导致 VS Code 无法使用, 从而只能使用 NotePad 或其他不趁手的文本编辑器修复问题.
2. **不要更新** VS Code. 软件更新时会重置其根目录下所有目录和文件. 更新的 VS Code, 安全的魔改, 二择其一而无得兼. 禁用自动更新的方式是 `Ctrl + Shift + P` 输入 `首选项: 打开用户设置(JSON)`, 在已存在的大括号中新添一行
   ```json
   "update.mode": "none",
   ```

   然后 `Ctrl + S` 保存更改. 此处的更改会永远立即生效, 所以无需重启 VS Code.

## 未能解决的几个问题

如前所说, 本人并不熟练于这份代码使用的语言, 目前存在以下问题亟待解决:

1. 魔改会将搜索功能的几个图标改坏, 但并不影响使用;
2. 直接选择切换媒体按钮会弹出一个二级菜单以供选择, 这个菜单的样式有些不太好.
