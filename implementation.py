from selene import browser



def test_page():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Ilzira')
    browser.element('#lastName').type('Nurmukhametova')
    browser.element('#userEmail').type('test@mail.ru')
    browser.element('[value="Female"]').click()
    browser.element('#userNumber').type('9876543210')
    browser.element('#dateOfBirthInput').click()
    browser.element("[class='react-datepicker__year-select']").click()
    browser.element("[value='1998']").click()
    browser.element("[value='3']").click()
    browser.element("[aria-label='Choose Tuesday, April 22nd, 1997']").click()

