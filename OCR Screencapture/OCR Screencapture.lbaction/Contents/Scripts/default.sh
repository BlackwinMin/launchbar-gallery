# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/
screencapture -i ~/ocr.png
#tesseract ~/ocr.png stdout -l chi_sim+eng | pbcopy
tesseract ~/ocr.png stdout --oem 1 --psm 6 -l chi_sim+eng -c preserve_interword_spaces=1 | pbcopy
rm ~/ocr.png