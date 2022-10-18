from string import Template

from spintax import spintax


def get_turk_spinned_text(link: str | None = '', with_stickers: bool = True, encoding: str = 'utf-8') -> str:
    text = "🔥 {Get|Take|Kullan} 50 {ücretsiz dönüş|FS|freespins|ücretsiz dönüş|ücretsiz dönüş}" \
           " {Kulübe kaydolmak|Kulübe girmek|Projeye girmek|katılmak|oynamak} Slottica'yı takip " \
           "{etmek|bu} bağlantı {aşağıda |} {-|:|} 👉 https://$link 👈 {Acele|Acele|Acele|Gecikme}," \
           " {bonus|ödül|hediye} süresi {sınırlı|sınırlı}! 🔥"
    spinned_text = spintax.spin(text)
    template = Template(spinned_text)
    message = template.substitute(link=link)
    if not with_stickers:
        message = message.replace('🔥', '')
        message = message.replace('👉', '')
        message = message.replace('👈', '')
    message = message.encode().decode(encoding)
    return message
