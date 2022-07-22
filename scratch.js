fetch("https://rest-api.wm.com/user-request-service?userId=&lang=en_CA", {
  "headers": {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "apikey": "E0008A94C99903B68AB5",
    "content-type": "application/json",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
  },
  "referrer": "https://www.wm.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"request_type\":\"SERVICE_REQUEST\",\"product_type\":\"Contact Us\",\"customerId\":\"\",\"lob\":\"R\",\"contact_name\":\"name\",\"organization_name\":\"\",\"contact_phone\":\"\",\"contact_mobile\":\"\",\"contact_email\":\"softumwork@gmail.com\",\"address\":{\"street_address\":\"address\",\"postal_code\":\"12442\",\"state\":\"AL\",\"city\":\"city\"},\"comments\":\"body\"}",
  "method": "POST",
  "mode": "no-cors",
  "credentials": "omit"
});