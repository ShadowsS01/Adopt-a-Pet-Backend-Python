from django.core.mail import send_mail
from decouple import config

def envia_email_confirmacao(adocao):
    assunto = "Adoção realizada com sucesso!"
    conteudo = f"Parabéns por realizar a adoção do pet {adocao.pet.name} com o valor mensal de R${adocao.valor}"
    remetente = config("EMAIL_HOST_USER", default="")
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)
