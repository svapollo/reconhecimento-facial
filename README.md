# reconhecimento-facial
Projeto do curso AWS Lambda da Alura


## Comando importantes (AWS CLI)

### Sincronizar pastas de imagens com bucket
aws s3 sync imagens/ s3://reconhecimento-inicio

### Upload de arquivo para o bucket
aws s3 cp karasuno.png s3://reconhecimento-inicio

### Criar collection rekognition (base de faces para comparar)
aws rekognition create-collection --collection-id nomeidcolecao

## Listar faces coletadas
aws rekognition list-faces --collection-id COLLECTIONIDanime
aws rekognition list-faces --collection-id personagem | grep ExternalImageId

## Deletar uma collection id
aws rekognition delete-collection --collection-id collectionname

## Compactar script aws lambda para deploy
zip faceanalise.zip faceanalise.py  (linux)
tar -a -c -f faceanalise.zip faceanalise.py (windows)

## Upload zip para aws lambda function
aws lambda update-function-code --function-name faceAnalise --zip-file fileb://faceanalise.zip

## Versionar função lambda (perde o trigger)
aws lambda publish-version --function-name faceAnalise

## Criar alias para função lambda
aws lambda create-alias --function-name faceAnalise --function-version 1 --name PROD 