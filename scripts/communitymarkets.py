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
    # 'cookie': 'fp-session=%7B%22token%22%3A%22fb346f0236983ea1a7a6421ff90d1b26%22%7D; fp-pref=%7B%7D; _gid=GA1.2.1719224692.1670404136; PHPSESSID=kclvvaid60o6pqi8e7553792ff; _gat=1; _gat_gtag_UA_96526929_1=1; fp-history=%7B%220%22%3A%7B%22name%22%3A%22%2Fabout%2Fcontact-us%22%7D%2C%221%22%3A%7B%22name%22%3A%22%2Fabout%2Fcommunity-grant-program%22%7D%7D; _ga_BBJ3DH13JF=GS1.1.1670578099.6.1.1670578183.0.0.0; _ga=GA1.2.1960736323.1670316851; _ga_0MCW5VWV52=GS1.1.1670578182.6.1.1670578204.0.0.0',
    'origin': 'https://www.communitymarkets.com',
    'referer': 'https://www.communitymarkets.com/about/community-grant-program',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = 'action=nf_ajax_submit&security=54bfc53840&formData=%7B%22id%22%3A%226%22%2C%22fields%22%3A%7B%220%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A0%7D%2C%2259%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A59%7D%2C%2260%22%3A%7B%22value%22%3A%223%22%2C%22id%22%3A60%7D%2C%2261%22%3A%7B%22value%22%3A%22%22%2C%22id%22%3A61%7D%2C%2262%22%3A%7B%22value%22%3A%2212%2F17%2F2022%22%2C%22id%22%3A62%7D%2C%2263%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A63%7D%2C%2264%22%3A%7B%22value%22%3A%2212%2F24%2F2022%22%2C%22id%22%3A64%7D%2C%2265%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A65%7D%2C%2266%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A66%7D%2C%2267%22%3A%7B%22value%22%3A%22%3Cp%3E%3Cspan+style%3D%5C%22font-family%3A+myriad-pro%2C+helvetica%2C+arial%2C+sans-serif%3B+font-weight%3A+600%3B%5C%22%3EPlease+indicate+breakdown+of+overall+contribution+dollars+to+this+project%3A%3C%2Fspan%3E%3Cbr%3E%3C%2Fp%3E%22%2C%22id%22%3A67%7D%2C%2268%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A68%7D%2C%2269%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A69%7D%2C%2270%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A70%7D%2C%2271%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A71%7D%2C%2272%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A72%7D%2C%2273%22%3A%7B%22value%22%3A%22%3Cp%3E%3Cspan+style%3D%5C%22font-family%3A+myriad-pro%2C+helvetica%2C+arial%2C+sans-serif%3B%5C%22%3ESupporting+documentation+(optional)%3C%2Fspan%3E%3Cbr%3E%3C%2Fp%3E%22%2C%22id%22%3A73%7D%2C%2275%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A75%7D%2C%2276%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A76%7D%2C%2277%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A77%7D%2C%2278%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A78%7D%2C%2279%22%3A%7B%22value%22%3A%22AK%22%2C%22id%22%3A79%7D%2C%2280%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A80%7D%2C%2281%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A81%7D%2C%2282%22%3A%7B%22value%22%3A%22test%22%2C%22id%22%3A82%7D%2C%2283%22%3A%7B%22value%22%3A%22softumwork%40gmail.com%22%2C%22id%22%3A83%7D%7D%2C%22settings%22%3A%7B%22objectType%22%3A%22Form+Setting%22%2C%22editActive%22%3Atrue%2C%22title%22%3A%22Community+Grant+Program%22%2C%22created_at%22%3A%222022-06-22+05%3A59%3A54%22%2C%22default_label_pos%22%3A%22above%22%2C%22show_title%22%3A%220%22%2C%22clear_complete%22%3A%221%22%2C%22hide_complete%22%3A%221%22%2C%22logged_in%22%3A%220%22%2C%22key%22%3A%22%22%2C%22conditions%22%3A%5B%5D%2C%22wrapper_class%22%3A%22%22%2C%22element_class%22%3A%22%22%2C%22add_submit%22%3A%221%22%2C%22not_logged_in_msg%22%3A%22%22%2C%22sub_limit_number%22%3A%22%22%2C%22sub_limit_msg%22%3A%22%22%2C%22calculations%22%3A%5B%5D%2C%22container_styles_background-color%22%3A%22%22%2C%22container_styles_border%22%3A%22%22%2C%22container_styles_border-style%22%3A%22%22%2C%22container_styles_border-color%22%3A%22%22%2C%22container_styles_color%22%3A%22%22%2C%22container_styles_height%22%3A%22%22%2C%22container_styles_width%22%3A%22%22%2C%22container_styles_font-size%22%3A%22%22%2C%22container_styles_margin%22%3A%22%22%2C%22container_styles_padding%22%3A%22%22%2C%22container_styles_display%22%3A%22%22%2C%22container_styles_float%22%3A%22%22%2C%22container_styles_show_advanced_css%22%3A%220%22%2C%22container_styles_advanced%22%3A%22%22%2C%22title_styles_background-color%22%3A%22%22%2C%22title_styles_border%22%3A%22%22%2C%22title_styles_border-style%22%3A%22%22%2C%22title_styles_border-color%22%3A%22%22%2C%22title_styles_color%22%3A%22%22%2C%22title_styles_height%22%3A%22%22%2C%22title_styles_width%22%3A%22%22%2C%22title_styles_font-size%22%3A%22%22%2C%22title_styles_margin%22%3A%22%22%2C%22title_styles_padding%22%3A%22%22%2C%22title_styles_display%22%3A%22%22%2C%22title_styles_float%22%3A%22%22%2C%22title_styles_show_advanced_css%22%3A%220%22%2C%22title_styles_advanced%22%3A%22%22%2C%22row_styles_background-color%22%3A%22%22%2C%22row_styles_border%22%3A%22%22%2C%22row_styles_border-style%22%3A%22%22%2C%22row_styles_border-color%22%3A%22%22%2C%22row_styles_color%22%3A%22%22%2C%22row_styles_height%22%3A%22%22%2C%22row_styles_width%22%3A%22%22%2C%22row_styles_font-size%22%3A%22%22%2C%22row_styles_margin%22%3A%22%22%2C%22row_styles_padding%22%3A%22%22%2C%22row_styles_display%22%3A%22%22%2C%22row_styles_show_advanced_css%22%3A%220%22%2C%22row_styles_advanced%22%3A%22%22%2C%22row-odd_styles_background-color%22%3A%22%22%2C%22row-odd_styles_border%22%3A%22%22%2C%22row-odd_styles_border-style%22%3A%22%22%2C%22row-odd_styles_border-color%22%3A%22%22%2C%22row-odd_styles_color%22%3A%22%22%2C%22row-odd_styles_height%22%3A%22%22%2C%22row-odd_styles_width%22%3A%22%22%2C%22row-odd_styles_font-size%22%3A%22%22%2C%22row-odd_styles_margin%22%3A%22%22%2C%22row-odd_styles_padding%22%3A%22%22%2C%22row-odd_styles_display%22%3A%22%22%2C%22row-odd_styles_show_advanced_css%22%3A%220%22%2C%22row-odd_styles_advanced%22%3A%22%22%2C%22success-msg_styles_background-color%22%3A%22%22%2C%22success-msg_styles_border%22%3A%22%22%2C%22success-msg_styles_border-style%22%3A%22%22%2C%22success-msg_styles_border-color%22%3A%22%22%2C%22success-msg_styles_color%22%3A%22%22%2C%22success-msg_styles_height%22%3A%22%22%2C%22success-msg_styles_width%22%3A%22%22%2C%22success-msg_styles_font-size%22%3A%22%22%2C%22success-msg_styles_margin%22%3A%22%22%2C%22success-msg_styles_padding%22%3A%22%22%2C%22success-msg_styles_display%22%3A%22%22%2C%22success-msg_styles_show_advanced_css%22%3A%220%22%2C%22success-msg_styles_advanced%22%3A%22%22%2C%22error_msg_styles_background-color%22%3A%22%22%2C%22error_msg_styles_border%22%3A%22%22%2C%22error_msg_styles_border-style%22%3A%22%22%2C%22error_msg_styles_border-color%22%3A%22%22%2C%22error_msg_styles_color%22%3A%22%22%2C%22error_msg_styles_height%22%3A%22%22%2C%22error_msg_styles_width%22%3A%22%22%2C%22error_msg_styles_font-size%22%3A%22%22%2C%22error_msg_styles_margin%22%3A%22%22%2C%22error_msg_styles_padding%22%3A%22%22%2C%22error_msg_styles_display%22%3A%22%22%2C%22error_msg_styles_show_advanced_css%22%3A%220%22%2C%22error_msg_styles_advanced%22%3A%22%22%2C%22changeEmailErrorMsg%22%3A%22Please+enter+a+valid+email+address!%22%2C%22changeDateErrorMsg%22%3A%22Please+enter+a+valid+date!%22%2C%22confirmFieldErrorMsg%22%3A%22These+fields+must+match!%22%2C%22fieldNumberNumMinError%22%3A%22Number+Min+Error%22%2C%22fieldNumberNumMaxError%22%3A%22Number+Max+Error%22%2C%22fieldNumberIncrementBy%22%3A%22Please+increment+by+%22%2C%22formErrorsCorrectErrors%22%3A%22Please+correct+errors+before+submitting+this+form.%22%2C%22validateRequiredField%22%3A%22This+is+a+required+field.%22%2C%22honeypotHoneypotError%22%3A%22Honeypot+Error%22%2C%22fieldsMarkedRequired%22%3A%22Fields+marked+with+an+%3Cspan+class%3D%5C%22ninja-forms-req-symbol%5C%22%3E*%3C%2Fspan%3E+are+required%22%2C%22currency%22%3A%22%22%2C%22repeatable_fieldsets%22%3A%22%22%2C%22unique_field_error%22%3A%22A+form+with+this+value+has+already+been+submitted.%22%2C%22drawerDisabled%22%3Afalse%2C%22allow_public_link%22%3A0%2C%22embed_form%22%3A%22%22%2C%22ninjaForms%22%3A%22Ninja+Forms%22%2C%22fieldTextareaRTEInsertLink%22%3A%22Insert+Link%22%2C%22fieldTextareaRTEInsertMedia%22%3A%22Insert+Media%22%2C%22fieldTextareaRTESelectAFile%22%3A%22Select+a+file%22%2C%22formHoneypot%22%3A%22If+you+are+a+human+seeing+this+field%2C+please+leave+it+empty.%22%2C%22fileUploadOldCodeFileUploadInProgress%22%3A%22File+Upload+in+Progress.%22%2C%22fileUploadOldCodeFileUpload%22%3A%22FILE+UPLOAD%22%2C%22currencySymbol%22%3Afalse%2C%22thousands_sep%22%3A%22%2C%22%2C%22decimal_point%22%3A%22.%22%2C%22siteLocale%22%3A%22en_US%22%2C%22dateFormat%22%3A%22m%2Fd%2FY%22%2C%22startOfWeek%22%3A%221%22%2C%22of%22%3A%22of%22%2C%22previousMonth%22%3A%22Previous+Month%22%2C%22nextMonth%22%3A%22Next+Month%22%2C%22months%22%3A%5B%22January%22%2C%22February%22%2C%22March%22%2C%22April%22%2C%22May%22%2C%22June%22%2C%22July%22%2C%22August%22%2C%22September%22%2C%22October%22%2C%22November%22%2C%22December%22%5D%2C%22monthsShort%22%3A%5B%22Jan%22%2C%22Feb%22%2C%22Mar%22%2C%22Apr%22%2C%22May%22%2C%22Jun%22%2C%22Jul%22%2C%22Aug%22%2C%22Sep%22%2C%22Oct%22%2C%22Nov%22%2C%22Dec%22%5D%2C%22weekdays%22%3A%5B%22Sunday%22%2C%22Monday%22%2C%22Tuesday%22%2C%22Wednesday%22%2C%22Thursday%22%2C%22Friday%22%2C%22Saturday%22%5D%2C%22weekdaysShort%22%3A%5B%22Sun%22%2C%22Mon%22%2C%22Tue%22%2C%22Wed%22%2C%22Thu%22%2C%22Fri%22%2C%22Sat%22%5D%2C%22weekdaysMin%22%3A%5B%22Su%22%2C%22Mo%22%2C%22Tu%22%2C%22We%22%2C%22Th%22%2C%22Fr%22%2C%22Sa%22%5D%2C%22recaptchaConsentMissing%22%3A%22reCapctha+validation+couldn%26%23039%3Bt+load.%22%2C%22recaptchaMissingCookie%22%3A%22reCaptcha+v3+validation+couldn%26%23039%3Bt+load+the+cookie+needed+to+submit+the+form.%22%2C%22recaptchaConsentEvent%22%3A%22Accept+reCaptcha+cookies+before+sending+the+form.%22%2C%22currency_symbol%22%3A%22%22%2C%22beforeForm%22%3A%22%22%2C%22beforeFields%22%3A%22%22%2C%22afterFields%22%3A%22%22%2C%22afterForm%22%3A%22%22%7D%2C%22extra%22%3A%7B%7D%7D'

        data = data.replace('softumwork%40gmail.com', target)
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        response = requests.post(url, headers=headers, data=data,
                                 # proxies=self.get_proxies(),
                                 # timeout=10
                                 )
        return response


if __name__ == '__main__':
    project_name = 'communitymarkets'
    success_message = 'Form submitted successfully.'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3OOhJsc'
    spam = ConcreteSpam(
        project_name, success_message,
        referal_project_name=project,
        promo_link=promo_link,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(15)
