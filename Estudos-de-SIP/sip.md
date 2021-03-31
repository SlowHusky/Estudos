Overview de SIP

Alguns pontos de interesse do SIP:

1 - SIP é um protocolo de sinalização usado para criar, modificar e terminar uma sessão multimídia sobre o Protocolo de Internet (IP - Camada de Rede). Uma sessão não é nada além de uma chamada entre dois endpoints. Um endpoint pode ser um celular, um laptop ou qualquer dispositivo que pode receber e enviar multimídia sobre IP

2 - SIP embarca uma arquitetura client-server.

3 - SIP usa SDP (Session Description Protocol) que descreve uma sessão de média e RTP (Real-Time Protocol) é usado para entregar mídia e voz sobre uma rede IP.

Entidades do SIP

Todo elemento na rede é identificado por um SIP URI (Uniform Resource Identifier) que é como um endereço. São elementos de rede os seguintes:

- User Agent
- Proxy Server
- Registrar Server
- Redirect Server
- Location Server

User Agent

É o endpoint e um dos mais importantes elementos numa rede SIP. Um endpoint pode iniciar, modificar ou terminar uma sessão. User agents são o dispositivo mais inteligente numa rede SIP. Pode ser um softphone, um dispositivo móvel ou um laptop.

User agents são logicamente divididos em duas partes.
- User Agent Client (UAC) - É a entidade que envia uma requisição e recebe uma resposta.
- User Agent Server (UAS) - É a entidade que recebe uma requisição e envia uma resposta.

Proxy Server

É o elemento na rede que pega a requisição de um user agent e envia para outro usuário

- Basicamente o papel  de um proxy server é parecido com o de um roteador.
- Precisa de alguma inteligência para entender a requisição SIP e enviar ela para frente com a ajuda do URI.
- Um proxy server fica entre dois user agents.
- Só podemos ter no máximo 70 proxy servers entre a fonte e o destino.

Existem dois tipos de proxy servers:

- Stateless Proxy Server - Simplesmente envia a mensagem. Esse tipo de servidor não guarda nenhuma informação da chamada ou da transação.
- Stateful Proxy Server - Esse tipo de servidor mantém registros de qualquer requisição e resposta e, pode usar esses registros no futuro. Ele pode retransmitir a requisição e se não obter resposta, pode tentar em um outro momento.

Registrar Server

O registrar server aceita as requisições de registro dos user agents. Ajuda a autenticar eles mesmos na rede. Ele armazena a URI e a localização dos usuários em uma database que ajuda outros SIP serves com o mesmo domínio.

Redirect Server

O redirect recebe requisiçõese e procura o cliente pretendido na database criada pelo registrar.

O redirect server usa a database para coletar informações e responder com 3xx (Redirect response) para o usuário.

Location Server

O location server providencia informações sobre as localizações possíves do caller (receptor chamado da ligação) nos redirect e proxy servers.
Apenas um proxy server ou um redirect server pode contactar o location server













