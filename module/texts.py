from string import Template

from spintax import spintax


class Text:
    __slots__ = ['link', 'project', 'spins', 'text']
    __texts = {
        'eng': '🔥 {Get|Loot|Use} {your|} $spins {FS|freespins|free spins|spins}'
               ' for a {quick Registration|start|take a part} on $project by'
               ' {clicking|following|coming} the 👉 http://google.us/url?q=$link 👈 below\n#\n\n{Hurry up!|Get a move on!|Rush!} '
               'This {offer|promo|stock} is limited in time! 🔥',
        'ru': '🔥 {Получи|Забери|Используй} $spins {фриспинов|FS|freespins|free spins|spins} за '
              '{Регистрацию в клубе|Вход в клуб|Вход в проект|принятие участия в проекте|игру} $project '
              '{переходя|перейдя|} по {следующей|} ссылке {ниже|} 👉 http://google.us/url?q=$link 👈 '
              '{Поспеши|Поторопись|Торопись|Не задерживайся}, время действия {бонуса|приза|подарка}'
              ' {ограничено|лимитировано}! 🔥',
        'tr': "🔥 {Get|Take|Kullan} $spins {ücretsiz dönüş|FS|freespins|ücretsiz dönüş|ücretsiz dönüş}"
              " {Kulübe kaydolmak|Kulübe girmek|Projeye girmek|katılmak|oynamak} $project takip "
              "{etmek|bu} bağlantı {aşağıda |} {-|:|} 👉 http://google.us/url?q=$link 👈 {Acele|Acele|Acele|Gecikme},"
              " {bonus|ödül|hediye} süresi {sınırlı|sınırlı}! 🔥"
    }
    __spins = {
        'supercat': '60',
        'luckybird': '50',
        'allright': '40',
        'fortuneclock': '50'
    }

    def __init__(self, lang: str, link: str, project: str):
        self.link = self.__fix_link(link)
        self.project = project
        self.spins = self.__spins[project]
        self.text = self.__texts[lang]

    def __fix_link(self, link: str) -> str:
        if 'https://' not in link:
            link = 'https://' + link
        return link

    def __encode_link(self, link: str) -> str:
        ...

    def get_text(self, with_stickers: bool = True):
        spinned_text = spintax.spin(self.text)
        template = Template(spinned_text)
        message = template.substitute(
            {'spins': self.spins,
             'project': self.project.capitalize(),
             'link': self.link}
        )
        if not with_stickers:
            message = message.replace('?', '')
            message = message.replace('?', '')
            message = message.replace('?', '')
        return message
