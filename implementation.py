from selene import browser, have


def test_page():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ilzira')
    browser.element('#lastName').type('Nurmukhametova')
    browser.element('#userEmail').type('test@mail.ru')
    browser.element('[value="Female"]').double_click()
    browser.element('#userNumber').type('9876543210')
    browser.element('#dateOfBirthInput').click()
    browser.element("[class='react-datepicker__year-select']").click()
    browser.element("[value='1998']").click()
    browser.element("[value='3']").click()
    browser.element("[aria-label='Choose Wednesday, April 22nd, 1998']").click()
    browser.element('#subjectsInput').type('civics').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys('/home/user/Загрузки/fotografiya_visokogo_razresheniya (1).jpg')
    browser.element('#currentAddress').type('test street')
    browser.element('[id=react-select-3-input]').type('NCR').press_enter()
    browser.element('[id=react-select-4-input]').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.all('tbody tr').should(have.exact_texts('Student Name Ilzira Nurmukhametova',
                                                    'Student Email test@mail.ru',
                                                    'Gender Female',
                                                    'Mobile 9876543210',
                                                    'Date of Birth 22 April,1998',
                                                    'Subjects Civics',
                                                    'Hobbies Sports',
                                                    'Picture fotografiya_visokogo_razresheniya (1).jpg',
                                                    'Address test street',
                                                    'State and City NCR Delhi'))

