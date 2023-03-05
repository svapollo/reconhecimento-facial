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