import pyautogui
import time
import random
import string
import webbrowser
import ctypes
import re


def getClip6digit():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            return str(re.findall(r'(\d{6})', (str(value))))
    finally:
        user32.CloseClipboard()


def getMail():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            if "@dropmail.me" in str(value) or "@emltmp.com" in str(value) or "@spymail.one" in str(
                    value) or "@10mail.org" in str(value):
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
                return str(match.group(0))
            return False
    finally:
        user32.CloseClipboard()


def randomize(
        _option_,
        _length_
):
    if _length_ > 0:

        # Options:6Ww$oRvfSVk95tyM  6Ww$oRvfSVk95tyM    
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_ = '1234567890'
        elif _option_ == '-m':
            string._characters_ = 'JFMASOND'

        if _option_ == '-d':
            _generated_info_ = random.randint(1, 28)
        elif _option_ == '-y':
            _generated_info_ = random.randint(1950, 2000)
        else:
            _generated_info_ = ''
            for _counter_ in range(0, _length_):
                _generated_info_ = _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        return 'error'


def verification():
    try:
        while pyautogui.locateCenterOnScreen("imgs\\learn_more.png", confidence=0.89):
            pyautogui.hotkey("ctrlleft", "\t")
            newMail = True
            while True:
                pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
                time.sleep(12)
                # pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
                copy_button_x, copy_button_y = pyautogui.locateCenterOnScreen("imgs\\copy_button_img.png", confidence=0.89)
                pyautogui.moveTo(copy_button_x, copy_button_y)
                pyautogui.click()
                newMail = getMail()
                if newMail:
                    break
            pyautogui.hotkey("ctrlleft", "shiftleft", '\t')
            time.sleep(1)
            pyautogui.hotkey("ctrlleft", "a")
            pyautogui.press('backspace')
            pyautogui.hotkey("ctrlleft", "v")
            pyautogui.typewrite('\n')
            time.sleep(12)
    except Exception as e:
        print('verification', e)
        return True


def main():
    #webbrowser.open('https://account.proton.me/signup?plan=free')
    time.sleep(5)

    # Username
    _username_ = randomize('-s', 5) + randomize('-s', 5) + randomize('-s', 5)
    pyautogui.typewrite(_username_ + '\t\t\t')
    time.sleep(0.5)

    # Password
    print("Username:" + _username_)
    _password_ = randomize('-p', 16)
    pyautogui.typewrite(_password_ + '\t' + _password_ + '\t')
    time.sleep(0.5)
    print("Password:" + _password_)

    pyautogui.typewrite('\n')
    time.sleep(5)

    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')

    time.sleep(10)
    pyautogui.typewrite('https://dropmail.me/\n')

    time.sleep(16)

    newMail = True
    while True:
        if not newMail:
            pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
            time.sleep(5)
        copy_button_x, copy_button_y = pyautogui.locateCenterOnScreen("imgs\\copy_button_img.PNG", confidence=0.85)
        pyautogui.moveTo(copy_button_x, copy_button_y)
        pyautogui.click()
        newMail = getMail()
        if newMail:
            print("10 min mail: " + newMail)
            break
    pyautogui.hotkey("ctrlleft", "shiftleft", '\t')
    time.sleep(1)

    pyautogui.hotkey("ctrlleft", "v")

    pyautogui.typewrite('\n')
    time.sleep(10)

    if verification():
        try:
            if pyautogui.locateCenterOnScreen("imgs\\verification_code.png", confidence=0.89):
                print('verification passed')
                pyautogui.hotkey("ctrlleft", "\t")
                time.sleep(15)

                code_x, code_y = pyautogui.locateCenterOnScreen("imgs\\verification_code_img.png", confidence=0.9)
                pyautogui.doubleClick(code_x - 10, code_y + 15)
                pyautogui.hotkey('ctrlleft', 'c')
                pyautogui.hotkey('ctrlleft', 'shift', '\t')
                time.sleep(5)
                pyautogui.typewrite(str(getClip6digit()))
                time.sleep(10)
                pyautogui.typewrite('\n')
                time.sleep(30)
                pyautogui.typewrite('\n')
                time.sleep(10)
                pyautogui.typewrite('\t\t\t\n')
                time.sleep(10)
                pyautogui.typewrite('\t\n')
                time.sleep(3)
                pyautogui.typewrite('\t\n')
                time.sleep(3)
                pyautogui.typewrite('\t\n')

                print(_username_ + "@proton.me:" + _password_)

                with open("accLog.txt", "a") as logfile:
                    logfile.write(_username_ + "@proton.me:" + _password_ + "\n")
        except Exception:
            print('some error in the end')

if __name__ == "__main__":
    CF_TEXT = 1
    kernel32 = ctypes.windll.kernel32
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
    user32 = ctypes.windll.user32
    user32.GetClipboardData.restype = ctypes.c_void_p
    main()

# CHAPTCHA
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')

# pyautogui.typewrite('\n')
