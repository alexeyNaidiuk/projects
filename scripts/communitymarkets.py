import requests

from module.spam_abstraction import Spam

cookies = {
    '_gid': 'GA1.2.1141966077.1668083303',
    '_gat': '1',
    'fp-session': '%7B%22token%22%3A%2267c34351ed55bea2d4a2731ee04dd042%22%7D',
    'fp-pref': '%7B%7D',
    '_gat_gtag_UA_76428239_29': '1',
    '_gat_gtag_UA_96526929_1': '1',
    'PHPSESSID': '3gdafb0tanudc4o0r57vt7vgrv',
    'fp-history': '%7B%220%22%3A%7B%22name%22%3A%22%2F%22%7D%2C%221%22%3A%7B%22name%22%3A%22account-create%22%7D%2C%222%22%3A%7B%22name%22%3A%22%2Fabout%2Fcontact-us%22%7D%7D',
    '_ga': 'GA1.2.2083815158.1668083303',
    '_ga_BBJ3DH13JF': 'GS1.1.1668083302.1.1.1668083331.0.0.0',
}

headers = {
    'authority': 'www.communitymarkets.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MTI3ODMiLCJhcCI6IjE1ODg2MzkwOTIiLCJpZCI6ImI2OTY1Y2VmODYyMDMxOWQiLCJ0ciI6ImY1Y2VmYTU1MGJmOWE0MTc1MDQwYzQxNmQ4ZmFjNTliIiwidGkiOjE2NjgwODMzNTU4ODd9fQ==',
    'origin': 'https://www.communitymarkets.com',
    'referer': 'https://www.communitymarkets.com/about/contact-us',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-f5cefa550bf9a4175040c416d8fac59b-b6965cef8620319d-01',
    'tracestate': '3412783@nr=0-1-3412783-1588639092-b6965cef8620319d----1668083355887',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-newrelic-id': 'VwIGU1FbCxABUVFaDwYHUVAI',
    'x-requested-with': 'XMLHttpRequest',
}
url = 'https://www.communitymarkets.com/wp-admin/admin-ajax.php'


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        data = 'action=nf_ajax_submit&security=feff42cc01&formData=%7B%22id%22%3A%224%22%2C%22fields%22%3A%7B%2219%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A19%7D%2C%2220%22%3A%7B%22value%22%3A%22softumwork%40gmail.com%22%2C%22id%22%3A20%7D%2C%2222%22%3A%7B%22value%22%3A%22test+https%3A%2F%2Fwww.communitymarkets.com%2Fabout%2Fcontact-us%22%2C%22id%22%3A22%7D%2C%2223%22%3A%7B%22value%22%3A%223%22%2C%22id%22%3A23%7D%2C%2224%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A24%7D%2C%2225%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A25%7D%2C%2226%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A26%7D%7D%2C%22settings%22%3A%7B%22objectType%22%3A%22Form+Setting%22%2C%22editActive%22%3A%221%22%2C%22title%22%3A%22Contact+Us%22%2C%22created_at%22%3A%222021-05-26+15%3A33%3A43%22%2C%22form_title%22%3A%22Contact+Us%22%2C%22default_label_pos%22%3A%22above%22%2C%22show_title%22%3A%220%22%2C%22clear_complete%22%3A%221%22%2C%22hide_complete%22%3A%221%22%2C%22logged_in%22%3A%220%22%2C%22key%22%3A%22%22%2C%22conditions%22%3A%5B%5D%2C%22wrapper_class%22%3A%22%22%2C%22element_class%22%3A%22%22%2C%22add_submit%22%3A%221%22%2C%22not_logged_in_msg%22%3A%22%22%2C%22sub_limit_number%22%3A%22%22%2C%22sub_limit_msg%22%3A%22%22%2C%22calculations%22%3A%5B%5D%2C%22container_styles_background-color%22%3A%22%22%2C%22container_styles_border%22%3A%22%22%2C%22container_styles_border-style%22%3A%22%22%2C%22container_styles_border-color%22%3A%22%22%2C%22container_styles_color%22%3A%22%22%2C%22container_styles_height%22%3A%22%22%2C%22container_styles_width%22%3A%22%22%2C%22container_styles_font-size%22%3A%22%22%2C%22container_styles_margin%22%3A%22%22%2C%22container_styles_padding%22%3A%22%22%2C%22container_styles_display%22%3A%22%22%2C%22container_styles_float%22%3A%22%22%2C%22container_styles_show_advanced_css%22%3A%220%22%2C%22container_styles_advanced%22%3A%22%22%2C%22title_styles_background-color%22%3A%22%22%2C%22title_styles_border%22%3A%22%22%2C%22title_styles_border-style%22%3A%22%22%2C%22title_styles_border-color%22%3A%22%22%2C%22title_styles_color%22%3A%22%22%2C%22title_styles_height%22%3A%22%22%2C%22title_styles_width%22%3A%22%22%2C%22title_styles_font-size%22%3A%22%22%2C%22title_styles_margin%22%3A%22%22%2C%22title_styles_padding%22%3A%22%22%2C%22title_styles_display%22%3A%22%22%2C%22title_styles_float%22%3A%22%22%2C%22title_styles_show_advanced_css%22%3A%220%22%2C%22title_styles_advanced%22%3A%22%22%2C%22row_styles_background-color%22%3A%22%22%2C%22row_styles_border%22%3A%22%22%2C%22row_styles_border-style%22%3A%22%22%2C%22row_styles_border-color%22%3A%22%22%2C%22row_styles_color%22%3A%22%22%2C%22row_styles_height%22%3A%22%22%2C%22row_styles_width%22%3A%22%22%2C%22row_styles_font-size%22%3A%22%22%2C%22row_styles_margin%22%3A%22%22%2C%22row_styles_padding%22%3A%22%22%2C%22row_styles_display%22%3A%22%22%2C%22row_styles_show_advanced_css%22%3A%220%22%2C%22row_styles_advanced%22%3A%22%22%2C%22row-odd_styles_background-color%22%3A%22%22%2C%22row-odd_styles_border%22%3A%22%22%2C%22row-odd_styles_border-style%22%3A%22%22%2C%22row-odd_styles_border-color%22%3A%22%22%2C%22row-odd_styles_color%22%3A%22%22%2C%22row-odd_styles_height%22%3A%22%22%2C%22row-odd_styles_width%22%3A%22%22%2C%22row-odd_styles_font-size%22%3A%22%22%2C%22row-odd_styles_margin%22%3A%22%22%2C%22row-odd_styles_padding%22%3A%22%22%2C%22row-odd_styles_display%22%3A%22%22%2C%22row-odd_styles_show_advanced_css%22%3A%220%22%2C%22row-odd_styles_advanced%22%3A%22%22%2C%22success-msg_styles_background-color%22%3A%22%22%2C%22success-msg_styles_border%22%3A%22%22%2C%22success-msg_styles_border-style%22%3A%22%22%2C%22success-msg_styles_border-color%22%3A%22%22%2C%22success-msg_styles_color%22%3A%22%22%2C%22success-msg_styles_height%22%3A%22%22%2C%22success-msg_styles_width%22%3A%22%22%2C%22success-msg_styles_font-size%22%3A%22%22%2C%22success-msg_styles_margin%22%3A%22%22%2C%22success-msg_styles_padding%22%3A%22%22%2C%22success-msg_styles_display%22%3A%22%22%2C%22success-msg_styles_show_advanced_css%22%3A%220%22%2C%22success-msg_styles_advanced%22%3A%22%22%2C%22error_msg_styles_background-color%22%3A%22%22%2C%22error_msg_styles_border%22%3A%22%22%2C%22error_msg_styles_border-style%22%3A%22%22%2C%22error_msg_styles_border-color%22%3A%22%22%2C%22error_msg_styles_color%22%3A%22%22%2C%22error_msg_styles_height%22%3A%22%22%2C%22error_msg_styles_width%22%3A%22%22%2C%22error_msg_styles_font-size%22%3A%22%22%2C%22error_msg_styles_margin%22%3A%22%22%2C%22error_msg_styles_padding%22%3A%22%22%2C%22error_msg_styles_display%22%3A%22%22%2C%22error_msg_styles_show_advanced_css%22%3A%220%22%2C%22error_msg_styles_advanced%22%3A%22%22%2C%22changeEmailErrorMsg%22%3A%22Please+enter+a+valid+email+address!%22%2C%22changeDateErrorMsg%22%3A%22Please+enter+a+valid+date!%22%2C%22confirmFieldErrorMsg%22%3A%22These+fields+must+match!%22%2C%22fieldNumberNumMinError%22%3A%22Number+Min+Error%22%2C%22fieldNumberNumMaxError%22%3A%22Number+Max+Error%22%2C%22fieldNumberIncrementBy%22%3A%22Please+increment+by+%22%2C%22formErrorsCorrectErrors%22%3A%22Please+correct+errors+before+submitting+this+form.%22%2C%22validateRequiredField%22%3A%22This+is+a+required+field.%22%2C%22honeypotHoneypotError%22%3A%22Honeypot+Error%22%2C%22fieldsMarkedRequired%22%3A%22Fields+marked+with+an+%3Cspan+class%3D%5C%22ninja-forms-req-symbol%5C%22%3E*%3C%2Fspan%3E+are+required%22%2C%22currency%22%3A%22%22%2C%22repeatable_fieldsets%22%3A%22%22%2C%22unique_field_error%22%3A%22A+form+with+this+value+has+already+been+submitted.%22%2C%22drawerDisabled%22%3A%22%22%2C%22allow_public_link%22%3A0%2C%22embed_form%22%3A%22%22%2C%22ninjaForms%22%3A%22Ninja+Forms%22%2C%22fieldTextareaRTEInsertLink%22%3A%22Insert+Link%22%2C%22fieldTextareaRTEInsertMedia%22%3A%22Insert+Media%22%2C%22fieldTextareaRTESelectAFile%22%3A%22Select+a+file%22%2C%22formHoneypot%22%3A%22If+you+are+a+human+seeing+this+field%2C+please+leave+it+empty.%22%2C%22fileUploadOldCodeFileUploadInProgress%22%3A%22File+Upload+in+Progress.%22%2C%22fileUploadOldCodeFileUpload%22%3A%22FILE+UPLOAD%22%2C%22currencySymbol%22%3Afalse%2C%22thousands_sep%22%3A%22%2C%22%2C%22decimal_point%22%3A%22.%22%2C%22siteLocale%22%3A%22en_US%22%2C%22dateFormat%22%3A%22m%2Fd%2FY%22%2C%22startOfWeek%22%3A%221%22%2C%22of%22%3A%22of%22%2C%22previousMonth%22%3A%22Previous+Month%22%2C%22nextMonth%22%3A%22Next+Month%22%2C%22months%22%3A%5B%22January%22%2C%22February%22%2C%22March%22%2C%22April%22%2C%22May%22%2C%22June%22%2C%22July%22%2C%22August%22%2C%22September%22%2C%22October%22%2C%22November%22%2C%22December%22%5D%2C%22monthsShort%22%3A%5B%22Jan%22%2C%22Feb%22%2C%22Mar%22%2C%22Apr%22%2C%22May%22%2C%22Jun%22%2C%22Jul%22%2C%22Aug%22%2C%22Sep%22%2C%22Oct%22%2C%22Nov%22%2C%22Dec%22%5D%2C%22weekdays%22%3A%5B%22Sunday%22%2C%22Monday%22%2C%22Tuesday%22%2C%22Wednesday%22%2C%22Thursday%22%2C%22Friday%22%2C%22Saturday%22%5D%2C%22weekdaysShort%22%3A%5B%22Sun%22%2C%22Mon%22%2C%22Tue%22%2C%22Wed%22%2C%22Thu%22%2C%22Fri%22%2C%22Sat%22%5D%2C%22weekdaysMin%22%3A%5B%22Su%22%2C%22Mo%22%2C%22Tu%22%2C%22We%22%2C%22Th%22%2C%22Fr%22%2C%22Sa%22%5D%2C%22recaptchaConsentMissing%22%3A%22reCapctha+validation+couldn%26%23039%3Bt+load.%22%2C%22recaptchaMissingCookie%22%3A%22reCaptcha+v3+validation+couldn%26%23039%3Bt+load+the+cookie+needed+to+submit+the+form.%22%2C%22recaptchaConsentEvent%22%3A%22Accept+reCaptcha+cookies+before+sending+the+form.%22%2C%22currency_symbol%22%3A%22%22%2C%22beforeForm%22%3A%22%22%2C%22beforeFields%22%3A%22%22%2C%22afterFields%22%3A%22%22%2C%22afterForm%22%3A%22%22%7D%2C%22extra%22%3A%7B%7D%7D'
        data = data.replace('softumwork%40gmail.com', target)
        data = data.replace('test', text.encode().decode('latin-1'))
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Form submitted successfully.'
    project_name = 'communitymarkets'
    promo_link = 'bit.ly/3A6oLma'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
