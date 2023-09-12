# Redes-Cliente-Servidor

# 1. Introdução.

Nos últimos anos, houve um aumento notável no nível de automação na indústria supermercadista. Esta tendência ainda está em curso e não mostra sinais de desaceleração à medida que a tecnologia continua a avançar.
O avanço da tecnologia tem aumentado constantemente, com inúmeras tendências contribuindo para o seu crescimento. Entre essas tendências estão os desenvolvimentos na tecnologia dos supermercados.
A empresa está buscando ativamente métodos para aumentar sua eficiência operacional e, ao mesmo tempo, diminuir despesas e aumentar a produtividade.
Uma área específica onde a automação pode melhorar significativamente a experiência do cliente é através da redução das filas no caixa. Ao automatizar o processo de checkout, os clientes podem desfrutar de uma experiência mais rápida e simplificada durante as compras.
A otimização da seleção de produtos é possível através da utilização da tecnologia de identificação por radiofrequência (RFID) neste contexto específico.
A Internet das Coisas (IoT) torna-se cada vez mais viáveis ​​e aplicáveis, tornando-as mais acessíveis à população em geral, os supermercados implementaram técnicas avançadas de automação para rastrear seu estoque com precisão.
O uso da tecnologia RFID facilita a leitura simultânea de etiquetas, possibilitando uma gestão eficiente de estoques e interação com o cliente em ambientes varejistas que envolvem gôndolas.
O sistema de pagamento permite transações contínuas, onde produtos de vários tipos são facilmente reconhecidos e registrados no sistema.

# 2. Fundamentação Teórica.

Para a construção desse sistema conceitos deveriam ser bem consolidados, tornando-os base para esse trabalho.

# 2.1 Cliente-Servidor.

A arquitetura cliente-servidor é um modelo de design de software que descreve a relação e a interação entre dois tipos de componentes em um sistema de computação: o cliente e o servidor. Essa arquitetura apresenta uma divisão de tarefas bem estabelecida para ambas as partes, pois o cliente interage com o usuário e exibe para eles as respostas de solicitações realizadas, já o servidor, centraliza os dados, pois processa, armazena e retorna respostas, desse modo, esse sistema fica modularizado e escalável. Outro ponto importante é a utilização em múltiplas plataformas, pois permite que o cliente seja executado em diferentes sistemas operacionais, desde que o servidor tenha configuração adequada para processar as solicitações. Essa arquitetura é amplamente usada em sistemas distribuídos e aplicações de rede, e é fundamental para a internet e muitos outros serviços computacionais.

O cliente é uma parte fundamental do sistema e desempenha o papel de fazer solicitações ao servidor. Geralmente, o cliente é uma aplicação ou dispositivo que é usado diretamente pelos usuários finais. O cliente apresenta:

Iniciador das Solicitações: O cliente inicia a comunicação, enviando solicitações ao servidor quando precisa de algum serviço, dados ou recursos; Interface do Usuário: O cliente geralmente fornece uma interface do usuário que permite aos usuários interagirem com o sistema. Isso pode ser uma aplicação desktop, um aplicativo móvel, um navegador da web, ou até mesmo um dispositivo IoT; Independência: O cliente é independente do servidor em termos de sua lógica e funcionamento. Pode haver vários clientes diferentes interagindo com o mesmo servidor.

Já o servidor é outra parte crítica da arquitetura cliente-servidor e desempenha o papel de atender às solicitações dos clientes. O servidor oferece serviços, recursos ou dados que os clientes solicitam. Algumas características importantes do servidor incluem:

Responder às Solicitações: O servidor está continuamente escutando por solicitações dos clientes e, quando recebe uma solicitação, processa-a e responde com os dados ou serviços apropriados; Lógica de Negócios: O servidor geralmente contém a lógica de negócios ou a funcionalidade principal do sistema. Ele executa as operações necessárias para atender às solicitações dos clientes; Escalabilidade: A capacidade de um servidor de lidar com várias solicitações de diferentes clientes ao mesmo tempo é uma consideração importante. Os servidores precisam ser escaláveis para acomodar um grande número de clientes simultaneamente.

# 2.2 Socket TCP/IP.

Esse recurso permite a criação e estabelecimento de uma conexão entre ambos os lados, baseados em um host, que seria a máquina onde o sistema está executando, que geralmente possui um endereço de IP, e uma porta, que é um conjunto de números que direciona o tráfego da comunicação, garantindo uma entrega de dados confiável e um controle do fluxo de informações devido ao protocolo de comunicação TCP/IP, esses protocolos são um conjunto de regras que definem a forma de comunicação, na rede, entre dispositivos.

# 2.3 Bibliotecas do Python: http.client, http.server, json.

Para a montagem da arquitetura Cliente-Servidor foi necessário ferramentas para isso.
A biblioteca http.client permite que você faça requisições HTTP a servidores web a partir do Python, podendo criar clientes HTTP personalizados para interagir com APIs web ou acessar recursos na internet. Já a biblioteca http.server fornece uma maneira simples de criar um servidor HTTP em Python, se tornando útil para hospedar conteúdo web localmente ou para criar aplicativos web simples. O módulo json permite a códificação e decodificação de dados no formato JSON (JavaScript Object Notation), que é amplamente usado para a troca de dados entre sistemas.

# 2.4 Docker.

A plataforma Docker foi criada para simplificar o processo de construção, lançamento e gerenciamento de aplicações conteinerizadas. Os contêineres são ambientes independentes que agrupam aplicativos e suas dependências, permitindo que operem de forma consistente em diversas configurações, como produção, desenvolvimento e testes. No desenvolvimento e implantação de microsserviços e aplicativos distribuídos, o Docker é frequentemente utilizado. Conseqüentemente, é altamente prevalente na construção e distribuição de aplicativos.
Um contêiner é uma unidade independente e leve que envolve um aplicativo e todas as suas dependências. Inclui bibliotecas, configurações e códigos necessários para o funcionamento do aplicativo. Os contêineres desempenham um papel importante para garantir que um aplicativo receba um ambiente uniforme, independentemente do ambiente em que é implantado.
Uma imagem Docker é um modelo que define como um contêiner deve ser construído. As imagens são criadas a partir de arquivos chamados Dockerfiles, que especificam as instruções para criar um ambiente específico.Um Dockerfile é um arquivo de configuração que descreve as etapas necessárias para construir uma imagem Docker.

# 2.5 RFID e Raspberry PI

Um dispositivo eletrônico, denominado leitor RFID (Identificação por Radiofrequência), tem a finalidade de extrair informações de etiquetas ou etiquetas RFID. Essas etiquetas são minúsculas e possuem um microchip e uma antena. Eles são implantados para transmitir e armazenar dados sem cabos ou fios por meio de sinais de radiofrequência.

A tecnologia RFID é uma ferramenta altamente prevalente utilizada em inúmeras aplicações, desde monitoramento e gerenciamento de estoque de produtos até controle de pontos de entrada e saída, bem como identificação de animais domésticos.
Uma etiqueta RFID é um dispositivo, ativo ou passivo, que contém dados salvos digitalmente. As tags passivas não possuem fonte interna de energia e são acionadas quando entram em contato com um campo de radiofrequência emitido pelo leitor RFID, porém as tags ativas, possuem uma fonte de energia interna e têm a capacidade de transmitir informações de forma mais independente. Para realizar a leitura dessas tags utiliza-se o leitor RFID, que é uma ferramenta responsável por emitir um sinal de frequência que aciona as etiquetas RFID e recupera os dados que elas contêm.

Para executar o script que vai realizar a leitura e envio das tags utiliza-se a Raspberry PI, que é uma série de computadores de placa única desenvolvida pela Raspberry Pi Foundation, uma organização sem fins lucrativos com sede no Reino Unido, que projetão esses dispositivos para serem computadores de baixo custo, pequenos, versáteis e acessíveis para fins educacionais e projetos.

# Resultados e Discussãos
O sistema de supermercado inteligente baseado em API REST demonstrou ser uma solução eficaz e robusta para a gestão de supermercados, oferecendo uma experiência aprimorada tanto para os clientes quanto para os administradores. Os resultados obtidos após a implementação e operação deste sistema têm sido extremamente satisfatórios e promissores.

Uma das principais vantagens observadas foi a agilidade nas transações e pagamentos. A utilização de um servidor centralizado e a capacidade de comunicação de dados em tempo real através do protocolo API REST permitiram que as compras fossem processadas de forma eficiente. Os clientes podem selecionar produtos e finalizar suas compras de maneira rápida e conveniente, reduzindo significativamente o tempo gasto nas filas do caixa. O sistema de supermercado inteligente proporcionou um controle de estoque extremamente preciso. A leitura das tags dos produtos e a atualização em tempo real no servidor permitiram que os administradores monitorassem os níveis de estoque de forma precisa. Isso resultou em menos produtos fora de estoque e, ao mesmo tempo, evitou o excesso de produtos em prateleiras, economizando recursos financeiros.

A estrutura baseada em API REST tornou a integração de novos recursos e serviços uma tarefa relativamente simples. A capacidade de conectar o sistema a outros aplicativos e serviços é um dos principais benefícios dessa abordagem. Os administradores podem, por exemplo, integrar sistemas de gerenciamento de fornecedores, sistemas de pagamento online e até mesmo programas de fidelidade de clientes sem grandes dificuldades. A capacidade de monitoramento em tempo real é uma das características mais valiosas do sistema. Os administradores podem acompanhar o fluxo de clientes, a movimentação de produtos e até mesmo o desempenho dos caixas em tempo real. Isso permite tomar decisões informadas e ajustar rapidamente a operação do supermercado conforme necessário.

Os caixas também se beneficiaram com a implementação deste sistema. Eles podem processar as compras com mais rapidez e precisão, uma vez que o sistema fornece informações detalhadas sobre os produtos e seus preços. Além disso, o sistema de pagamento foi integrado de maneira eficaz, aceitando diversas formas de pagamento, como dinheiro, cartões e até mesmo sistemas de pagamento digital, como PIX. O sistema foi projetado para ser escalável e flexível, o que significa que pode ser adaptado para atender às necessidades de diferentes tamanhos de supermercados e cadeias de lojas. À medida que o negócio cresce, o sistema pode ser expandido facilmente para acomodar novos pontos de venda e produtos.

# Conclusão

O sistema de supermercado inteligente baseado em API REST é um exemplo notável de como a tecnologia pode melhorar a eficiência, a precisão e a experiência geral de compras para clientes e administradores. Os resultados até o momento demonstram que essa abordagem oferece benefícios significativos e que a sua implementação tem sido um sucesso, claro que melhorias podem ser feitas, principalmente no tratamento de erros.

À medida que a tecnologia continua a avançar, é provável que esse sistema se torne ainda mais sofisticado e eficiente. Ele exemplifica como a integração de tecnologias modernas e a adoção de protocolos de comunicação robustos podem transformar a forma como os supermercados operam e interagem com os clientes, tornando a experiência de compras mais conveniente e eficaz.

# Referências

- TANENBAUM, Andrew S. Redes de Computadores. Pearson, 2014.
- <https://docs.python.org/pt-br/3.6/library/>. Acessado: 08/09/2023.
- <https://embarcados.com.br/rfid-raspberry-pi-python/>. Acessado: 08/09/2023.
- <https://www.gta.ufrj.br/ensino/eel878/redes1-2016-1/16_1/p2p/modelo.html#:~:text=A%20arquitetura%20cliente%20servidor%20%C3%A9,recursos%20ou%20servi%C3%A7os%2C%20denominados%20clientes.>. Acessado: 08/09/2023
