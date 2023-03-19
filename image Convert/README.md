# image Convert.lbaction

提供一个选框，包含 jpeg 和 png 两个选项，选择后可将图片批量转换为您选取的格式；如果输入的文件是 PDF，则提取其第一页并转换。

Legacy 版本使用原生命令行工具，但是在 macOS 13 Ventura 下已经部分失效，您可以使用另一版本，不过需要提前在电脑上安装 [imagemagick](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiO_Iew66r7AhWdQfUHHVKlA3MQFnoECA8QAQ&url=https%3A%2F%2Fwww.imagemagick.org%2F&usg=AOvVaw2K9e9LxUTmQUcy5gUizL2h)，如果您使用 M1 芯片的电脑，并且使用 HomeBrew 安装的 imagemagick，请将 PATH 地址修改为 `/opt/homebrew/bin/magick`。