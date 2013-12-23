# coding: utf-8
import floppyforms as forms
from django.utils.translation import ugettext as _
from nosvc.core.models import Meeting


class MeetingForm(forms.ModelForm):
    tos = forms.BooleanField(label=_(u'Eu li Como funciona e os Termos de uso do Nós.vc e estou de acordo.'))

    class Meta:
        model = Meeting
        exclude = ('finished', 'confirmed')

        labels = {
            'title': _(u'Qual é o nome do encontro?'),
            'about': _(u'Sobre o encontro'),
            'headline': _(u'Como você explicaria o encontro em um tweet?'),
            'period': _(u'Data(s) do encontro'),
            'schedule': _(u'Data(s) com horário(s) de início e término'),
            'city': _(u'Cidade'),
            'location': _(u'Onde?'),
            'video': _(u'Já tem vídeo?'),
            'image': _(u'Imagem'),
            #'host': _(u'Id, número do perfil da pessoa que vai conduzir o encontro.'),
            'about_host': _(u'Mini, muito mini, biografia'),
            'min_attendees': _(u'Qual é o número mínimo de inscritos?'),
            'max_attendees': _(u'Qual é o número máximo de inscritos?'),
            'deadline': _(u'Quando encerram as inscrições?'),
            'price': _(u'Preço (R$)'),
            #'subscription_kind': _(u'Tipo de inscrição'),
            'questions': _(u'Que pergunta(s) você precisa fazer aos inscritos?'),
        }

        help_texts = {
            'title': _(u'Título bacanudo, auto-explicativo e curto, vale trocadilho.'),
            'about': _(u'Capriche, é hora de vender o peixe. Por que me inscrever? Como será o encontro? Qual será a programação? Para quem é indicado? Tem pré-requisistos? Seja verdadeiro, direto e procure organizar o texto por tópicos. Abra seu coração e mostre o valor do encontro.'),
            'headline': _(u'Até 140 caracteres, direto, reto e convidativo. Evite repetir o que já tem no nome. Este é o texto que vai sempre acompanhá-lo.'),
            'period': _(u'Data(s) do encontro, exemplo: "02 a 04/01/12"'),
            'schedule': _(u'Descreva detalhadamente a(s) data(s) e o(s) horário(s) de início e término do encontro, exemplo: "Segunda, 2 de janeiro de 2013. Das 9:00 às 17:00"'),
            'city': _(u'Escolha a cidade em que o encontro vai acontecer.'),
            'location': _(u'Local, endereço, cidade e estado. Se você ainda não tem um local, temos algumas <a href="http://blog.nos.vc/category/locais/" target="_blank">sugestões</a>.'),
            'video': _(u'Se sim, cole aqui o link do vídeo no Vimeo. Se não, deixe o campo em branco.'),
            'image': _(u'Cole aqui o link da imagem fantástica que ilustra o encontro. Recomendamos imagens grandes, com, pelo menos, 1200 pixels de largura. Você pode usar um link do Flickr, por exemplo.'),
            #'host': _(u'Pode ser você! Exemplo: "X". Se a página do perfil é http://nos.vc/pt/users/X'),
            'about_host': _(u'Fale um pouco sobre quem vai conduzir o encontro. Sua vida e experiência com o assunto.'),
            'min_attendees': _(u'De verdade. Quantas pessoas são realmente necessárias para tornar o encontro possível? Só será realizado se alcançar o número mínimo.'),
            'max_attendees': _(u'Defina um número limite, mesmo, de pessoas. Quando chegar nele, as inscrições serão encerradas.'),
            'deadline': _(u'Tem que ser tempo suficiente pra divulgar e encontrar as pessoas que vão se inscrever. Por outro lado, tem que dar tempo de cancelar e avisar todo mundo sem prejudicar ninguém, caso não alcance o número mínimo de inscritos. Por isso, sugerimos encerrar as inscrições até 2 dias úteis antes da data do encontro.'),
            'price': _(u'Pode ser 0 para inscrições gratuitas. Ou à partir de R$ 10,00 para inscrições pagas.'),
            #'subscription_kind': _(u'Descreva a inscrição de um jeito que desperte o interesse das pessoas. Solta o dedo no teclado!'),
            'questions': _(u'Faça sua(s) pergunta(s). As respostas poderão ajudar a conheer melhor seu público.'),
        }
