## AC/DC
O microserviço ACDC é responsável por capturar links onde um determinado conteúdo está disponível em várias plataformas. Após encontrar o link o ACDC salva os resultados automaticamente no banco de dados MySQL ao receber uma requisição POST do Backend.  

## Tecnologias Utilizadas

<p align="left"> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Arquitetura Idealizada

Na arquitetura proposta tínhamos duas opções: receber o método POST da API e devolver com PUT atualizando os campos JSON ou receber o POST da API e salvar diretamente no banco de dados as colunas responsáveis pelos links. A segunda opção paraceu mais vantajosa do ponto de vista da performance, em um primeiro momento. 

<img src="https://i.ibb.co/gd2bzmQ/Whats-App-Image-2024-02-15-at-14-55-08.jpg" alt="Whats-App-Image-2024-02-15-at-14-55-08" border="0"></a>


## Desligamento do serviço

Durante a evolução da plataforma mudamos como vai ser estruturado o software para que faça mais sentido para os desenvolvedores





