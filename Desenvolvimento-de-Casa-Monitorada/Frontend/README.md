💥Explicação do front💥
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
     <!DOCTYPE html>

DOCTYPE: Esta linha informa ao navegador que o documento está escrito em HTML5. Isso ajuda o navegador a interpretar corretamente o conteúdo da página.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"html lang="pt-BR"

Este é o elemento raiz do documento HTML. Tudo o que está dentro dele faz parte da página.

➡lang="pt-BR": Especifica que o idioma da página é português do Brasil. Isso é útil para acessibilidade e SEO (otimização para motores de busca), ajudando os navegadores e leitores de tela a entenderem o idioma do conteúdo
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casa do Professor Hete Caetano</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
      <style>
   
Detalhes do <head>:
<meta charset="UTF-8">: Define a codificação de caracteres para UTF-8. Isso significa que todos os caracteres, incluindo letras acentuadas, serão exibidos corretamente. É especialmente importante para idiomas como o português, que utilizam acentuação.

<meta name="viewport" content="width=device-width, initial-scale=1.0">:

➡viewport: Este meta tag é essencial para tornar a página responsiva, ou seja, adaptável a diferentes tamanhos de tela (como celulares e tablets).
    
➡width=device-width: Define a largura da viewport igual à largura do dispositivo.
    
➡initial-scale=1.0: Define o nível de zoom inicial quando a página é carregada.
    
<title>: Define o título da página, que aparece na aba do navegador e é utilizado por motores de busca. O título aqui é ("Casa do Professor Hete Caetano").

<link>: Este elemento importa o arquivo CSS do Bootstrap:


    
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    >body {background-color: #f8f9fa

body: Seleciona o elemento <body> da página.
background-color: #f8f9fa;: Define a cor de fundo do corpo como um cinza claro (hexadecimal). Isso proporciona um visual mais suave e agradável.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    planta {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    border: 1px solid #dee2e6;
    border-radius: 10px;
    background-color: #e9ecef;
    padding: 20px; /* Ajustado para dar espaço entre os cômodos */
    }
    
planta: Define uma classe CSS chamada "planta" que provavelmente será aplicada a um contêiner (div) que agrupará outros elementos.

Propriedades da classe planta:

➡display: flex: Habilita o layout Flexbox, permitindo um controle mais fácil sobre o alinhamento e o espaçamento dos elementos filhos dentro do contêiner.

➡flex-wrap: wrap: Permite que os elementos filhos que não cabem em uma linha sejam movidos para a linha seguinte. Isso é útil em layouts responsivos.

➡justify-content: center: Centraliza os itens filhos horizontalmente dentro do contêiner. Se houver espaço extra, os itens se acomodam no centro.

➡width: 100%: O contêiner ocupará toda a largura disponível da sua área pai.

➡height: 100%: Define que a altura do contêiner deve ocupar 100% da altura disponível do seu pai.

➡margin: 0 auto;: O contêiner será centralizado horizontalmente na tela, com margens automáticas à esquerda e à direita.

➡border: 1px solid #dee2e6;: Adiciona uma borda sólida de 1 pixel ao redor do contêiner, com uma cor cinza clara.

➡border-radius: 10px: Arredonda os cantos do contêiner em 10 pixels, dando um visual mais suave.

➡background-color: #e9ecef: Define a cor de fundo do contêiner como um cinza muito claro, proporcionando um contraste sutil com o fundo do corpo.

➡padding: 20px: Adiciona um espaço interno de 20 pixels dentro do contêiner, criando espaço entre a borda e o conteúdo interno. Isso é útil para garantir que os elementos dentro do contêiner não fiquem colados nas bordas.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Estilos CSS para os Cômodos e Sensores
Estilos para a classe comodo:

      comodo {
            border: 1px dashed #007bff;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: calc(50% - 20px); /* Largura de 50% menos a margem */
            height: 300px; /* Altura fixa para todos os cômodos */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 10px; /* Margem para espaçamento entre os cômodos */
      }
      comodo: Define a aparência dos cômodos na interface.

➡border: 1px dashed #007bff;: Adiciona uma borda tracejada azul ao redor de cada cômodo.

➡border-radius: 10px;: Arredonda os cantos dos cômodos.

➡background-color: #ffffff;: Define o fundo dos cômodos como branco.

➡box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);: Adiciona uma sombra sutil para dar um efeito de elevação.

➡width: calc(50% - 20px);: Define a largura de cada cômodo como 50% da largura do contêiner pai, subtraindo 20 pixels para considerar as margens.

➡height: 300px;: Altura fixa de 300 pixels para todos os cômodos.

➡display:flex; flex-direction: column; align-items: center; justify-content: center;: Usa Flexbox para organizar os conteúdos dentro do cômodo de forma centralizada.

➡margin: 10px: Adiciona uma margem de 10 pixels ao redor de cada cômodo, criando espaçamento

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Estilos de Sensor
    
    .sensor {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 10px 0;
    }
    
➡Organização Vertical: Os elementos dentro do sensor são organizados em uma coluna, centralizados, facilitando a leitura e a interação.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    .sensor img {
      width: 50px;
      height: 50px;
    }
    
➡Imagens: As imagens dos sensores são dimensionadas para 50x50 pixels, garantindo uniformidade e clareza na apresentação.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Botões e Texto

    .sensor-button {
      width: 50px;
      height: 50px;
      border-radius: 50%;
    }

➡Botões Circulares: O formato circular dos botões facilita a interação do usuário, tornando-os mais intuitivos.

    .countdown {
      font-size: 0.9rem;
      color: #6c757d;
    }

➡Legibilidade: O uso de um tamanho de fonte menor e uma cor cinza suave para o texto do contador garante que as informações sejam discretas, mas legíveis.

    .temperatura {
      font-size: 1.5rem;
      font-weight: bold;
      margin-top: 10px;
    }

➡Destaque: A temperatura é destacada em um tamanho de fonte maior e negrito, chamando a atenção do usuário.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Lógica de Funcionamento com JavaScript
Estrutura de Dados
      
           </style>
         
           <script>
             let token = null; // Variável para armazenar o token JWT
         
             const sensors = [
               { sensor_id: 1, room: 'Cozinha', countdown: 60, lastTemperature: null },
               { sensor_id: 2, room: 'Sala', countdown: 60, lastTemperature: null },
               { sensor_id: 3, room: 'Quarto', countdown: 60, lastTemperature: null },
               { sensor_id: 4, room: 'Escritório', countdown: 60, lastTemperature: null },
             ];
   ➡Armazenamento de Dados: A estrutura de dados é um array de objetos que representa sensores em diferentes cômodos. Cada objeto contém informações relevantes, como o ID do sensor, nome do cômodo, um contador e a última temperatura registrada.
   
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Funções de Simulação

    // Função para simular a temperatura usando dados históricos de São Paulo
    const simulateTemperature = () => {
      const historicalTemperatures = [22, 23, 24, 25, 26, 27, 28, 29, 30]; // Exemplo de temperaturas históricas
      const randomIndex = Math.floor(Math.random() * historicalTemperatures.length);
      return historicalTemperatures[randomIndex]; // Retorna uma temperatura aleatória
    };

    const simulateHumidity = () => {
      return (Math.random() * 50 + 30).toFixed(2); // Umidade entre 30% e 80%
    };
    
   ➡Simulação de Dados: Essas funções geram temperaturas e umidades simuladas, úteis para testes e desenvolvimento. Isso evita a necessidade de um backend completo durante o desenvolvimento inicial.
   
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Autenticação e Envio de Dados
    
    // Função para autenticar e pegar o token JWT
    const authenticate = async (sensor) => {
      try {
        const loginResponse = await fetch('http://localhost:3000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: 'monitor',
            password: '123',
          }),
        });

        if (!loginResponse.ok) {
          throw new Error('Falha na autenticação');
        }

        const loginData = await loginResponse.json();
        token = loginData.token; // Armazena o token JWT para ser usado depois
        console.log(`Autenticado sensor ${sensor.sensor_id}, token obtido.`);
      } catch (error) {
        console.error(`Erro ao autenticar o sensor ${sensor.room}:`, error.message);
      }
    };
    
 ➡Segurança: A função de autenticação realiza uma chamada ao backend para obter um token JWT, essencial para segurança nas requisições subsequentes.

    // Função para enviar dados do sensor para o backend
    const sendData = async (sensor) => {
      try {
        if (!token) {
          await authenticate(sensor); // Autentica se o token não existir
        }

        const temperatura = simulateTemperature();
        const umidade = simulateHumidity();

        await fetch('http://localhost:3000/dados-sensores', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`, // Usa o token no cabeçalho
          },
          body: JSON.stringify({
            sensor_id: sensor.sensor_id,
            temperatura: temperatura,
            umidade: umidade,
          }),
        });

        // Atualiza a última temperatura medida
        sensor.lastTemperature = temperatura;

        // Atualiza a interface
        document.getElementById(`temperatura-${sensor.sensor_id}`).textContent = `${temperatura} °C`;
        console.log(`Dados enviados do sensor ${sensor.room}: Temperatura = ${temperatura}, Umidade = ${umidade}`);
      } catch (error) {
        console.error(`Erro ao enviar dados do sensor ${sensor.room}:`, error.message);
      }
    };
   
  ➡Envio de Dados: A função sendData coleta dados do sensor e os envia para o backend, utilizando o token para autenticação. Isso permite a atualização em tempo real dos dados exibidos na interface.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Atualização do Contador
    
    // Função para atualizar o contador e enviar dados periodicamente
    const updateCountdown = () => {
      sensors.forEach(sensor => {
        const countdownElement = document.getElementById(`countdown-${sensor.sensor_id}`);

        if (sensor.countdown > 0) {
          sensor.countdown--;
          countdownElement.textContent = `Próximo envio automático em ${sensor.countdown} segundos`;
        } else {
          sendData(sensor);
          sensor.countdown = 60;
          countdownElement.textContent = `Próximo envio automático em ${sensor.countdown} segundos`;
        }
      });
    };

    // Função para enviar dados manualmente ao clicar no botão
    const handleSendButtonClick = (sensorId) => {
      const sensor = sensors.find(s => s.sensor_id === sensorId);
      sendData(sensor);
      sensor.countdown = 60;
      document.getElementById(`countdown-${sensor.sensor_id}`).textContent = `Próximo envio automático em ${sensor.countdown} segundos`;
    };

    setInterval(updateCountdown, 1000); // Atualiza o contador a cada 1 segundo
   
    </script>
    </head>
    
  ➡Automação: A função updateCountdown decrementa o contador para cada sensor, enviando dados automaticamente a cada 60 segundos. Isso permite um fluxo contínuo de informações, essencial para monitoramento em tempo real.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Estrutura HTML/
Layout da Página
    
         <body>
           <div class="container mt-5">
             <h1 class="text-center mb-4">Minha Casa</h1>
             <p class="text-center mb-5">Cada sensor enviará dados automaticamente a cada 60 segundos ou manualmente ao clicar no botão correspondente.</p>
     
         <div class="planta">
           <div id="cozinha" class="comodo">
             <h3 class="text-center">Cozinha</h3>
             <div class="sensor">
               <img src="images/sensor.png" alt="Sensor">
               <p id="countdown-1" class="countdown">Próximo envio automático em 60 segundos</p>
               <p id="temperatura-1" class="temperatura">0 °C</p>
               <button class="btn btn-primary sensor-button" onclick="handleSendButtonClick(1)">+</button>
             </div>
           </div>

➡Estrutura Semântica: O uso de cabeçalhos e parágrafos para descrever a funcionalidade do sistema fornece uma clara hierarquia visual e informativa.

➡Container Responsivo: O div com a classe container do Bootstrap proporciona um layout responsivo e bem organizado.

Implementação dos Sensores
Cada cômodo é representado por um bloco de código que inclui informações sobre o sensor, como:

      <div id="sala" class="comodo">
        <h3 class="text-center">Sala</h3>
        <div class="sensor">
          <img src="images/sensor.png" alt="Sensor">
          <p id="countdown-2" class="countdown">Próximo envio automático em 60 segundos</p>
          <p id="temperatura-2" class="temperatura">0 °C</p>
          <button class="btn btn-primary sensor-button" onclick="handleSendButtonClick(2)">+</button>
        </div>
      </div>

      <div id="quarto" class="comodo">
        <h3 class="text-center">Quarto</h3>
        <div class="sensor">
          <img src="images/sensor.png" alt="Sensor">
          <p id="countdown-3" class="countdown">Próximo envio automático em 60 segundos</p>
          <p id="temperatura-3" class="temperatura">0 °C</p>
          <button class="btn btn-primary sensor-button" onclick="handleSendButtonClick(3)">+</button>
        </div>
      </div>

      <div id="escritorio" class="comodo">
        <h3 class="text-center">Escritório</h3>
        <div class="sensor">
          <img src="images/sensor.png" alt="Sensor">
          <p id="countdown-4" class="countdown">Próximo envio automático em 60 segundos</p>
          <p id="temperatura-4" class="temperatura">0 °C</p>
          <button class="btn btn-primary sensor-button" onclick="handleSendButtonClick(4)">+</button>
        </div>
      </div>
    </div>
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    
    </html>

Interatividade: Cada cômodo possui um botão que permite o envio manual de dados, aumentando a interatividade do usuário. O uso de IDs únicos para cada elemento permite a atualização em tempo real.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Resumo:
Este código combina uma estrutura clara, estilização responsiva e funcionalidade robusta para criar uma interface de monitoramento de sensores. A integração de CSS para design e JavaScript para funcionalidade proporciona uma experiência de usuário fluida e dinâmica. Essa abordagem é especialmente eficaz para aplicações que requerem visualização em tempo real e interação do usuário. Se você tiver mais perguntas ou precisar de esclarecimentos adicionais, fique à vontade para perguntar!

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💥Rodando a aplicação💥
 
 ➡ para rodar a aplicação é necessário fazer o fork desse repositório e o repositório do back, baixar eles e abrir o arquivo tando do back como do front no Vscode, em ambos é necessário abrir o terminal utilizando o "Ctrl" + "j", escrever "npm install" no terminal, no back é necessário escrever "npm start", ja no front pode ser feito instalando a extensão live server no próprio Vscode e clicar onde ele aparece no canto inferior direito do Vscode.
 
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







