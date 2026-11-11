# QA54_demoIlCarro

Test object: Registration form ([https://icarro-v1.netlify.app/register](https://icarro-v1.netlify.app/register))

Basic valid data (used in all tests except the field being checked):

First Name: "Test_first_name"

Last Name: "Test_last_name"

Email: "test_user_reg<unique_uuid>@gm.com" (generated separately for each test)

Password: valid password from .env (8+ characters, uppercase, lowercase, digit, special character)

Terms of use: checkbox checked (True)

List of implemented negative scenarios
1. test_invalid_registration_with_empty_name — Empty required field Name

Violated condition: firstName = "" (other fields are valid, checkbox (checked).

Expected result: The message "Name is required" appears under the Name field, the "Y'alla! " button is disabled.

Actual result: Matches expected (test passed).

2. test_invalid_registration_with_empty_last_name — Empty required field "Last name"

Violated condition: lastName = "" (other fields are valid, checkbox checked).

Expected result: The message "Last name is required" appears under the Last name field, the "Y'alla! " button is disabled.

Actual result: Matches expected (test passed).

3. test_invalid_registration_with_empty_email — Empty required field "Email"

Violated condition: email = "" (other fields are valid, checkbox checked).

Expected result: The message "Email is required" appears under the Email field, and the "Y'alla!" button is disabled.

Actual result: Matches expected (Test passed).

4. test_invalid_registration_with_invalid_email_format — Invalid email format (without the @ symbol)

Violated condition: email = "test1gg.com" (other fields are valid, checkbox checked).

Expected result: When focus is lost, the message "Wrong email format" appears under the Email field, and the "Y'alla!" button is disabled.

Actual result: Matches expected (Test passed).

5. test_invalid_registration_with_empty_password — Empty required Password field

Violated condition: password = "" (other fields are valid, checkbox checked).

Expected result: The message "Password is required" appears under the Password field, and the Y’alla! button is disabled.

Actual result: Matches expected (test passed).

6. test_invalid_registration_without_terms_checkbox — Terms of Use checkbox unchecked

Violated condition: The "I agree to the terms of use" checkbox is unchecked (all text fields are filled with valid data).

Expected result: The Y’alla! button remains disabled.

Actual result: Matches expected (test passed).

7. test_invalid_registration_existing_user — Registration using an existing email address

Violated condition: Entering an email address that has already been registered (other data is valid, checkbox checked).

Expected result: The Y’alla! button is enabled. After submitting the form, the server returns a 400 Bad Request status, and a modal window opens with the error text "User already exists."

Actual Result: Matches expected (Test Passed).

8. test_invalid_registration_with_space_in_name — Name field filled with a space (" ")

Violated condition: firstName = " " (other data is valid, checkbox is checked).

Expected Result: Name field validation error (the field cannot contain only spaces) or a readable error message from the server.

Actual Result (Discrepancy Fixed / Bug): Client-side validation considers the space character to be a valid character and enables the Y'alla! button. Upon submitting, the server returns a 400 Bad Request with the JSON object {"firstName": "must not be empty"} (in Russian in an English-language UI), and the frontend cannot parse the object and displays the string [object Object] in the modal window. (The test is marked with the @pytest.mark.xfail decorator in the code.)

9. test_invalid_registration_password_without_special_char — Password without a special character

Violated condition: password = "asdfghjklasdfaQ1" — 16 characters, contains an uppercase letter, a lowercase letter, and a number, but does not contain a special character (the rest of the data is valid).

Expected result: On the client, a password format hint appears and the "Y'alla!" button is blocked, or after submitting, a modal window displays the requirements text: "At least 8 characters; Must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number; Can contain special characters [@$#^&*!]".

Actual result (Discrepancy/Bug detected):

On the frontend, password complexity checking is completely absent — the "Y'alla!" button becomes active.

Despite the backend's "Can contain special characters" statement, the server rejects the password without the special character with a 400 Bad Request status.

Instead of the error text, the modal window displays [object Object]. (In the code, the test is marked with the @pytest.mark.xfail decorator.)

===================================================================================

Объект тестирования: Форма регистрации ([https://icarro-v1.netlify.app/register](https://icarro-v1.netlify.app/register))

Базовые валидные данные (используются во всех тестах, кроме проверяемого поля):

First Name: "Test_first_name"

Last Name: "Test_last_name"

Email: "test_user_reg<уникальный_uuid>@gm.com" (генерируется отдельно для каждого теста)

Password: валидный пароль из .env (8+ символов, заглавная, строчная, цифра, спецсимвол)

Terms of use: чекбокс отмечен (True)

Список реализованных негативных сценариев
1. test_invalid_registration_with_empty_name — Пустое обязательное поле Name

Нарушенное условие: firstName = "" (остальные поля валидны, чекбокс отмечен).

Ожидаемый результат: Под полем Name появляется сообщение "Name is required", кнопка Y’alla! неактивна (disabled).

Фактический результат: Совпадает с ожидаемым (Тест пройден).

2. test_invalid_registration_with_empty_last_name — Пустое обязательное поле Last name

Нарушенное условие: lastName = "" (остальные поля валидны, чекбокс отмечен).

Ожидаемый результат: Под полем Last name появляется сообщение "Last name is required", кнопка Y’alla! неактивна (disabled).

Фактический результат: Совпадает с ожидаемым (Тест пройден).

3. test_invalid_registration_with_empty_email — Пустое обязательное поле Email

Нарушенное условие: email = "" (остальные поля валидны, чекбокс отмечен).

Ожидаемый результат: Под полем Email появляется сообщение "Email is required", кнопка Y’alla! неактивна (disabled).

Фактический результат: Совпадает с ожидаемым (Тест пройден).

4. test_invalid_registration_with_invalid_email_format — Неверный формат Email (без символа @)

Нарушенное условие: email = "test1gg.com" (остальные поля валидны, чекбокс отмечен).

Ожидаемый результат: Под полем Email при потере фокуса появляется сообщение "Wrong email format", кнопка Y’alla! неактивна (disabled).

Фактический результат: Совпадает с ожидаемым (Тест пройден).

5. test_invalid_registration_with_empty_password — Пустое обязательное поле Password

Нарушенное условие: password = "" (остальные поля валидны, чекбокс отмечен).

Ожидаемый результат: Под полем Password появляется сообщение "Password is required", кнопка Y’alla! неактивна (disabled).

Фактический результат: Совпадает с ожидаемым (Тест пройден).

6. test_invalid_registration_without_terms_checkbox — Не отмечен чекбокс согласия с условиями (Terms of Use)

Нарушенное условие: Чекбокс I agree to the terms of use не отмечен (все текстовые поля заполнены валидными данными).

Ожидаемый результат: Кнопка Y’alla! остается неактивной (disabled).

Фактический результат: Совпадает с ожидаемым (Тест пройден).

7. test_invalid_registration_existing_user — Регистрация на уже существующий в базе Email

Нарушенное условие: Ввод email, который уже был зарегистрирован ранее (остальные данные валидны, чекбокс отмечен).

Ожидаемый результат: Кнопка Y’alla! активна. После отправки формы сервер возвращает статус 400 Bad Request, открывается модальное окно с текстом ошибки "User already exists".

Фактический результат: Совпадает с ожидаемым (Тест пройден).

8. test_invalid_registration_with_space_in_name — Поле Name, заполненное пробелом (" ")

Нарушенное условие: firstName = " " (остальные данные валидны, чекбокс отмечен).

Ожидаемый результат: Ошибка валидации поля Name (поле не может состоять только из пробелов) либо читаемое сообщение об ошибке от сервера.

Фактический результат (Зафиксировано расхождение / Баг): Клиентская валидация считает пробел допустимым символом и разблокирует кнопку Y’alla!. При отправке сервер возвращает 400 Bad Request с JSON-объектом {"firstName": "не должно быть пустым"} (на русском языке в англоязычном UI), а фронтенд не может распарсить объект и выводит в модальном окне строку [object Object]. (В коде тест помечен декоратором @pytest.mark.xfail).

9. test_invalid_registration_password_without_special_char — Пароль без спецсимвола

Нарушенное условие: password = "asdfghjklasdfaQ1" — 16 символов, содержит заглавную, строчную буквы и цифру, но не содержит спецсимвол (остальные данные валидны).

Ожидаемый результат: На клиенте появляется подсказка о формате пароля и блокируется кнопка Y’alla!, либо после отправки модальное окно выводит текст требований: "At least 8 characters; Must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number; Can contain special characters [@$#^&*!]".

Фактический результат (Зафиксировано расхождение / Баг):

На фронтенде полностью отсутствует проверка сложности пароля — кнопка Y’alla! становится активной.

Несмотря на формулировку бэкенда "Can contain special characters" («может содержать»), сервер отвергает пароль без спецсимвола со статусом 400 Bad Request.

Вместо текста ошибки в модальном окне пользователю выводится [object Object]. (В коде тест помечен декоратором @pytest.mark.xfail).