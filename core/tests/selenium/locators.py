class GenericLocators:
    CREATE_LINK = '//a[contains(text(), "Create")]'
    EDIT_LINK = '//a[contains(text(), "Edit")]'
    DISCUSS_LINK = '//a[contains(text(), "Discuss")]'
    REVIEW_LINK = '//a[contains(text(), "Review")]'
    LOGIN_LINK = '//a[contains(text(), "Login")]'
    HAMBURGER = '//button[@id="hamburger"]'

    # edit/create page inputs
    EDIT_BUTTON = '//button[@id="edit"]'
    ADD_BUTTON = '//button[@id="add"]'
    SHARE_BUTTON = '//button[@id="share"]'
    LIST_ITEM = '//div[@class="list-item"]'
    FORM_LIST_ITEM = '//div[@class="list-item edit"]'
    TITLE_INPUT = '//input[@id="id_title"]'
    DESCRIPTION_INPUT = '//input[@id="id_description"] '
    SAVE_CHANGES_BUTTON = '//button[contains(text(), "Save Changes")]'
    CANCEL_CHANGES_BUTTON = '//button[@id="Cancel"]'
    DISCUSSION_TOPIC_TITLE = f"{LIST_ITEM}//h3"
    DISCUSSION_TOPIC_DESC = f"{LIST_ITEM}//p"


class LoginPageLocators:
    USERNAME_INPUT = '//input[@id="id_username"]'
    PASSWORD_INPUT = '//input[@id="id_password"]'
    SUBMIT_BUTTON = '//input[@value="login"]'
    LOST_PASSWORD = '//a[contains(text(), "Lost password")]'
