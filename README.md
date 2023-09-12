# Redes-Cliente-Servidor

# Introdução

Nos últimos anos, houve um aumento notável no nível de automação na indústria supermercadista. Esta tendência ainda está em curso e não mostra sinais de desaceleração à medida que a tecnologia continua a avançar.
O avanço da tecnologia tem aumentado constantemente, com inúmeras tendências contribuindo para o seu crescimento. Entre essas tendências estão os desenvolvimentos na tecnologia dos supermercados.
A empresa está buscando ativamente métodos para aumentar sua eficiência operacional e, ao mesmo tempo, diminuir despesas e aumentar a produtividade.
Uma área específica onde a automação pode melhorar significativamente a experiência do cliente é através da redução das filas no caixa. Ao automatizar o processo de checkout, os clientes podem desfrutar de uma experiência mais rápida e simplificada durante as compras.
A otimização da seleção de produtos é possível através da utilização da tecnologia de identificação por radiofrequência (RFID) neste contexto específico.
A Internet das Coisas (IoT) torna-se cada vez mais viáveis ​​e aplicáveis, tornando-as mais acessíveis à população em geral, os supermercados implementaram técnicas avançadas de automação para rastrear seu estoque com precisão.
O uso da tecnologia RFID facilita a leitura simultânea de etiquetas, possibilitando uma gestão eficiente de estoques e interação com o cliente em ambientes varejistas que envolvem gôndolas.
O sistema de pagamento permite transações contínuas, onde produtos de vários tipos são facilmente reconhecidos e registrados no sistema.

# Fundamentação Teórica

Para a construção desse sistema conceitos deveriam ser bem consolidados, tornando-os base para esse trabalho.

1. Cliente_Servidor

A arquitetura cliente-servidor é um modelo de design de software que descreve a relação e a interação entre dois tipos de componentes em um sistema de computação: o cliente e o servidor. Essa arquitetura apresenta uma divisão de tarefas bem estabelecida para ambas as partes, pois o cliente interage com o usuário e exibe para eles as respostas de solicitações realizadas, já o servidor, centraliza os dados, pois processa, armazena e retorna respostas, desse modo, esse sistema fica modularizado e escalável. Outro ponto importante é a utilização em múltiplas plataformas, pois permite que o cliente seja executado em diferentes sistemas operacionais, desde que o servidor tenha configuração adequada para processar as solicitações. Essa arquitetura é amplamente usada em sistemas distribuídos e aplicações de rede, e é fundamental para a internet e muitos outros serviços computacionais.

O cliente é uma parte fundamental do sistema e desempenha o papel de fazer solicitações ao servidor. Geralmente, o cliente é uma aplicação ou dispositivo que é usado diretamente pelos usuários finais. O cliente apresenta:

Iniciador das Solicitações: O cliente inicia a comunicação, enviando solicitações ao servidor quando precisa de algum serviço, dados ou recursos.

Interface do Usuário: O cliente geralmente fornece uma interface do usuário que permite aos usuários interagirem com o sistema. Isso pode ser uma aplicação desktop, um aplicativo móvel, um navegador da web, ou até mesmo um dispositivo IoT.

Independência: O cliente é independente do servidor em termos de sua lógica e funcionamento. Pode haver vários clientes diferentes interagindo com o mesmo servidor.

Já o servidor é outra parte crítica da arquitetura cliente-servidor e desempenha o papel de atender às solicitações dos clientes. O servidor oferece serviços, recursos ou dados que os clientes solicitam. Algumas características importantes do servidor incluem:

Responder às Solicitações: O servidor está continuamente escutando por solicitações dos clientes e, quando recebe uma solicitação, processa-a e responde com os dados ou serviços apropriados.

Lógica de Negócios: O servidor geralmente contém a lógica de negócios ou a funcionalidade principal do sistema. Ele executa as operações necessárias para atender às solicitações dos clientes.

Escalabilidade: A capacidade de um servidor de lidar com várias solicitações de diferentes clientes ao mesmo tempo é uma consideração importante. Os servidores precisam ser escaláveis para acomodar um grande número de clientes simultaneamente.
