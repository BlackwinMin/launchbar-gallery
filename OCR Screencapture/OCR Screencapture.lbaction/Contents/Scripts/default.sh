# LaunchBar Action Script
#

PATH=$PATH:/usr/local/bin/
screencapture -i ~/ocr.png
tesseract ~/ocr.png stdout -l chi_sim+eng | pbcopy
rm ~/ocr.png
