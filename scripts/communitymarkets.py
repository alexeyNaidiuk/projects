import requests

import module

url = 'https://www.communitymarkets.com/wp-admin/admin-ajax.php'

'''
https://www.communitymarkets.com/about/contact-us
https://www.communitymarkets.com/about/community-grant-program
'''
headers = {
    'authority': 'www.communitymarkets.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.communitymarkets.com',
    'referer': 'https://www.communitymarkets.com/about/contact-us',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-newrelic-id': 'VwIGU1FbCxABUVFaDwYHUVAI',
    'x-requested-with': 'XMLHttpRequest',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MTI3ODMiLCJhcCI6IjE1ODg2MzkwOTIiLCJpZCI6IjMyMjY0OThmMzE2MWY4NzkiLCJ0ciI6IjNlYzUxMjVjNTI3NWQ4YTU3N2IxZGVlODY2ZWI5NjkwIiwidGkiOjE2NzE1Mjc0MTgyNTl9fQ==',
    'traceparent': '00-3ec5125c5275d8a577b1dee866eb9690-3226498f3161f879-01',
    'tracestate': '3412783@nr=0-1-3412783-1588639092-3226498f3161f879----1671527418259',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = 'action=nf_ajax_submit&security=9d9acfb9d3&formData=%7B%22id%22%3A%224%22%2C%22fields%22%3A%7B%2219%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A19%7D%2C%2220%22%3A%7B%22value%22%3A%22softumwork%40gmail.com%22%2C%22id%22%3A20%7D%2C%2222%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A22%7D%2C%2223%22%3A%7B%22value%22%3A%2213%22%2C%22id%22%3A23%7D%2C%2224%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A24%7D%2C%2225%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A25%7D%2C%2226%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A26%7D%7D%2C%22settings%22%3A%7B%22objectType%22%3A%22Form+Setting%22%2C%22editActive%22%3A%221%22%2C%22title%22%3A%22Contact+Us%22%2C%22created_at%22%3A%222021-05-26+15%3A33%3A43%22%2C%22form_title%22%3A%22Contact+Us%22%2C%22default_label_pos%22%3A%22above%22%2C%22show_title%22%3A%220%22%2C%22clear_complete%22%3A%221%22%2C%22hide_complete%22%3A%221%22%2C%22logged_in%22%3A%220%22%2C%22key%22%3A%22%22%2C%22conditions%22%3A%5B%5D%2C%22wrapper_class%22%3A%22%22%2C%22element_class%22%3A%22%22%2C%22add_submit%22%3A%221%22%2C%22not_logged_in_msg%22%3A%22%22%2C%22sub_limit_number%22%3A%22%22%2C%22sub_limit_msg%22%3A%22%22%2C%22calculations%22%3A%5B%5D%2C%22container_styles_background-color%22%3A%22%22%2C%22container_styles_border%22%3A%22%22%2C%22container_styles_border-style%22%3A%22%22%2C%22container_styles_border-color%22%3A%22%22%2C%22container_styles_color%22%3A%22%22%2C%22container_styles_height%22%3A%22%22%2C%22container_styles_width%22%3A%22%22%2C%22container_styles_font-size%22%3A%22%22%2C%22container_styles_margin%22%3A%22%22%2C%22container_styles_padding%22%3A%22%22%2C%22container_styles_display%22%3A%22%22%2C%22container_styles_float%22%3A%22%22%2C%22container_styles_show_advanced_css%22%3A%220%22%2C%22container_styles_advanced%22%3A%22%22%2C%22title_styles_background-color%22%3A%22%22%2C%22title_styles_border%22%3A%22%22%2C%22title_styles_border-style%22%3A%22%22%2C%22title_styles_border-color%22%3A%22%22%2C%22title_styles_color%22%3A%22%22%2C%22title_styles_height%22%3A%22%22%2C%22title_styles_width%22%3A%22%22%2C%22title_styles_font-size%22%3A%22%22%2C%22title_styles_margin%22%3A%22%22%2C%22title_styles_padding%22%3A%22%22%2C%22title_styles_display%22%3A%22%22%2C%22title_styles_float%22%3A%22%22%2C%22title_styles_show_advanced_css%22%3A%220%22%2C%22title_styles_advanced%22%3A%22%22%2C%22row_styles_background-color%22%3A%22%22%2C%22row_styles_border%22%3A%22%22%2C%22row_styles_border-style%22%3A%22%22%2C%22row_styles_border-color%22%3A%22%22%2C%22row_styles_color%22%3A%22%22%2C%22row_styles_height%22%3A%22%22%2C%22row_styles_width%22%3A%22%22%2C%22row_styles_font-size%22%3A%22%22%2C%22row_styles_margin%22%3A%22%22%2C%22row_styles_padding%22%3A%22%22%2C%22row_styles_display%22%3A%22%22%2C%22row_styles_show_advanced_css%22%3A%220%22%2C%22row_styles_advanced%22%3A%22%22%2C%22row-odd_styles_background-color%22%3A%22%22%2C%22row-odd_styles_border%22%3A%22%22%2C%22row-odd_styles_border-style%22%3A%22%22%2C%22row-odd_styles_border-color%22%3A%22%22%2C%22row-odd_styles_color%22%3A%22%22%2C%22row-odd_styles_height%22%3A%22%22%2C%22row-odd_styles_width%22%3A%22%22%2C%22row-odd_styles_font-size%22%3A%22%22%2C%22row-odd_styles_margin%22%3A%22%22%2C%22row-odd_styles_padding%22%3A%22%22%2C%22row-odd_styles_display%22%3A%22%22%2C%22row-odd_styles_show_advanced_css%22%3A%220%22%2C%22row-odd_styles_advanced%22%3A%22%22%2C%22success-msg_styles_background-color%22%3A%22%22%2C%22success-msg_styles_border%22%3A%22%22%2C%22success-msg_styles_border-style%22%3A%22%22%2C%22success-msg_styles_border-color%22%3A%22%22%2C%22success-msg_styles_color%22%3A%22%22%2C%22success-msg_styles_height%22%3A%22%22%2C%22success-msg_styles_width%22%3A%22%22%2C%22success-msg_styles_font-size%22%3A%22%22%2C%22success-msg_styles_margin%22%3A%22%22%2C%22success-msg_styles_padding%22%3A%22%22%2C%22success-msg_styles_display%22%3A%22%22%2C%22success-msg_styles_show_advanced_css%22%3A%220%22%2C%22success-msg_styles_advanced%22%3A%22%22%2C%22error_msg_styles_background-color%22%3A%22%22%2C%22error_msg_styles_border%22%3A%22%22%2C%22error_msg_styles_border-style%22%3A%22%22%2C%22error_msg_styles_border-color%22%3A%22%22%2C%22error_msg_styles_color%22%3A%22%22%2C%22error_msg_styles_height%22%3A%22%22%2C%22error_msg_styles_width%22%3A%22%22%2C%22error_msg_styles_font-size%22%3A%22%22%2C%22error_msg_styles_margin%22%3A%22%22%2C%22error_msg_styles_padding%22%3A%22%22%2C%22error_msg_styles_display%22%3A%22%22%2C%22error_msg_styles_show_advanced_css%22%3A%220%22%2C%22error_msg_styles_advanced%22%3A%22%22%2C%22changeEmailErrorMsg%22%3A%22Please+enter+a+valid+email+address!%22%2C%22changeDateErrorMsg%22%3A%22Please+enter+a+valid+date!%22%2C%22confirmFieldErrorMsg%22%3A%22These+fields+must+match!%22%2C%22fieldNumberNumMinError%22%3A%22Number+Min+Error%22%2C%22fieldNumberNumMaxError%22%3A%22Number+Max+Error%22%2C%22fieldNumberIncrementBy%22%3A%22Please+increment+by+%22%2C%22formErrorsCorrectErrors%22%3A%22Please+correct+errors+before+submitting+this+form.%22%2C%22validateRequiredField%22%3A%22This+is+a+required+field.%22%2C%22honeypotHoneypotError%22%3A%22Honeypot+Error%22%2C%22fieldsMarkedRequired%22%3A%22Fields+marked+with+an+%3Cspan+class%3D%5C%22ninja-forms-req-symbol%5C%22%3E*%3C%2Fspan%3E+are+required%22%2C%22currency%22%3A%22%22%2C%22repeatable_fieldsets%22%3A%22%22%2C%22unique_field_error%22%3A%22A+form+with+this+value+has+already+been+submitted.%22%2C%22drawerDisabled%22%3A%22%22%2C%22allow_public_link%22%3A0%2C%22embed_form%22%3A%22%22%2C%22ninjaForms%22%3A%22Ninja+Forms%22%2C%22fieldTextareaRTEInsertLink%22%3A%22Insert+Link%22%2C%22fieldTextareaRTEInsertMedia%22%3A%22Insert+Media%22%2C%22fieldTextareaRTESelectAFile%22%3A%22Select+a+file%22%2C%22formHoneypot%22%3A%22If+you+are+a+human+seeing+this+field%2C+please+leave+it+empty.%22%2C%22fileUploadOldCodeFileUploadInProgress%22%3A%22File+Upload+in+Progress.%22%2C%22fileUploadOldCodeFileUpload%22%3A%22FILE+UPLOAD%22%2C%22currencySymbol%22%3Afalse%2C%22thousands_sep%22%3A%22%2C%22%2C%22decimal_point%22%3A%22.%22%2C%22siteLocale%22%3A%22en_US%22%2C%22dateFormat%22%3A%22m%2Fd%2FY%22%2C%22startOfWeek%22%3A%221%22%2C%22of%22%3A%22of%22%2C%22previousMonth%22%3A%22Previous+Month%22%2C%22nextMonth%22%3A%22Next+Month%22%2C%22months%22%3A%5B%22January%22%2C%22February%22%2C%22March%22%2C%22April%22%2C%22May%22%2C%22June%22%2C%22July%22%2C%22August%22%2C%22September%22%2C%22October%22%2C%22November%22%2C%22December%22%5D%2C%22monthsShort%22%3A%5B%22Jan%22%2C%22Feb%22%2C%22Mar%22%2C%22Apr%22%2C%22May%22%2C%22Jun%22%2C%22Jul%22%2C%22Aug%22%2C%22Sep%22%2C%22Oct%22%2C%22Nov%22%2C%22Dec%22%5D%2C%22weekdays%22%3A%5B%22Sunday%22%2C%22Monday%22%2C%22Tuesday%22%2C%22Wednesday%22%2C%22Thursday%22%2C%22Friday%22%2C%22Saturday%22%5D%2C%22weekdaysShort%22%3A%5B%22Sun%22%2C%22Mon%22%2C%22Tue%22%2C%22Wed%22%2C%22Thu%22%2C%22Fri%22%2C%22Sat%22%5D%2C%22weekdaysMin%22%3A%5B%22Su%22%2C%22Mo%22%2C%22Tu%22%2C%22We%22%2C%22Th%22%2C%22Fr%22%2C%22Sa%22%5D%2C%22recaptchaConsentMissing%22%3A%22reCapctha+validation+couldn%26%23039%3Bt+load.%22%2C%22recaptchaMissingCookie%22%3A%22reCaptcha+v3+validation+couldn%26%23039%3Bt+load+the+cookie+needed+to+submit+the+form.%22%2C%22recaptchaConsentEvent%22%3A%22Accept+reCaptcha+cookies+before+sending+the+form.%22%2C%22currency_symbol%22%3A%22%22%2C%22beforeForm%22%3A%22%22%2C%22beforeFields%22%3A%22%22%2C%22afterFields%22%3A%22%22%2C%22afterForm%22%3A%22%22%7D%2C%22extra%22%3A%7B%7D%7D'

        data = data.replace('softumwork%40gmail.com', target)
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        response = requests.post(url, headers=headers, data=data,
                                 proxies=self.get_proxies(),
                                 timeout=20
                                 )
        return response


if __name__ == '__main__':
    project_name = 'communitymarkets'
    success_message = 'Form submitted successfully.'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3G57aOY'
    spam = ConcreteSpam(
        project_name, success_message,
        referal_project_name=project,
        promo_link=promo_link,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(100)
