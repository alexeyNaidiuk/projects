from string import Template

from spintax import spintax


class Text:
    __texts = {
        'eng': '🔥 {Get|Loot|Use} {your|} 50 {FS|freespins|free spins|spins}'
               ' for a {quick Registration|start|take a part} on by'
               ' {clicking|following|coming} the 👉 https://$link 👈 below\n#\n\n{Hurry up!|Get a move on!|Rush!} '
               'This {offer|promo|stock} is limited in time! 🔥',
        'ru': '🔥 {Получи|Забери|Используй} 50 {фриспинов|FS|freespins|free spins|spins} за '
              '{Регистрацию в клубе|Вход в клуб|Вход в проект|принятие участия|игру} '
              '{переходя|перейдя|} по {следующей|} ссылке {ниже|} 👉 https://$link 👈 '
              '{Поспеши|Поторопись|Торопись|Не задерживайся}, время действия {бонуса|приза|подарка}'
              ' {ограничено|лимитировано}! 🔥',
        'tr': "🔥 {Get|Take|Kullan} 50 {ücretsiz dönüş|FS|freespins|ücretsiz dönüş|ücretsiz dönüş}"
              " {Kulübe kaydolmak|Kulübe girmek|Projeye girmek|katılmak|oynamak} Slottica'yı takip "
              "{etmek|bu} bağlantı {aşağıda |} {-|:|} 👉 https://$link 👈 {Acele|Acele|Acele|Gecikme},"
              " {bonus|ödül|hediye} süresi {sınırlı|sınırlı}! 🔥"
    }

    def __init__(self, promo_link: str, text_lang: str):
        self.text = self.__texts[text_lang]
        self.promo_link = promo_link

    def get_text(self, with_stickers: bool = True):
        spinned_text = spintax.spin(self.text)
        template = Template(spinned_text)
        message = template.substitute(link=self.promo_link)
        if not with_stickers:
            message = message.replace('🔥', '')
            message = message.replace('👉', '')
            message = message.replace('👈', '')
        return message
