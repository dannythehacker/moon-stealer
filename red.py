import webbrowser
import pyautogui
import pyperclip
import time

# open the repository page in the default browser
url = 'https://github.com/Yuvi5001/moon-grabber'
webbrowser.open(url)

# wait for the page to load
time.sleep(5)

# copy the JavaScript code to the clipboard
js_code = """
(function() {
  // find the "Star" button and click it
  var starButton = document.querySelector('#repository-container-header > div.d-flex.flex-wrap.flex-justify-end.mb-3.px-3.px-md-4.px-lg-5 > ul > li:nth-child(4) > div > div.unstarred.BtnGroup.flex-1 > form > button');
  if (starButton) {
    starButton.click();
  }
})();
"""
pyperclip.copy(js_code)

# automate the keyboard shortcuts to open the console and paste the JavaScript code
pyautogui.hotkey('ctrl', 'shift', 'j')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
