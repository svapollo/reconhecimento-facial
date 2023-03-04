import boto3

s3 = boto3.resource('s3')


def lista_imagens():
    imagens = []
    bucket = s3.Bucket('inicio-reconhecimento')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    print(imagens)
    return imagens


imagens = lista_imagens()
