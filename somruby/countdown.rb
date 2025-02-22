require 'selenium-webdriver'

# Classe responsável por manipular o navegador Selenium
class SeleniumWebDriver
  attr_reader :driver

  def initialize
    options = Selenium::WebDriver::Firefox::Options.new
    options.binary = "/usr/bin/firefox" # Ajuste o caminho correto do Firefox
    options.add_preference("media.autoplay.default", 0) # Permitir autoplay
    @driver = Selenium::WebDriver.for(:firefox, options: options)
  end

  def tocar_som(url)
    begin
      driver.navigate.to url

      wait = Selenium::WebDriver::Wait.new(timeout: 10)

      # Agora encontramos o botão correto
      play_button = wait.until { driver.find_element(css: 'button.bw-player__play-btn') }

      # Simular um clique normal
      driver.action.move_to(play_button).click.perform
      sleep 1

      # Pressionar Enter para garantir ativação do botão
      play_button.send_keys(:enter)
      sleep 1

      # Se ainda não funcionar, tentamos um clique via JavaScript
      driver.execute_script("arguments[0].click();", play_button)

      puts "🎵 Som iniciado com sucesso!"
      sleep 10 # Tempo para ouvir o som
    rescue Selenium::WebDriver::Error::TimeoutError
      puts "❌ Erro: O botão de play não foi encontrado dentro do tempo limite!"
    rescue StandardError => e
      puts "❌ Erro ao tentar reproduzir o som: #{e.message}"
    ensure
      driver.quit
    end
  end
end

# Classe que gerencia a contagem regressiva
class ContagemRegressiva
  def initialize(tempo)
    @tempo = tempo
  end

  def iniciar
    puts "⏳ Contagem regressiva iniciada!"
    @tempo.downto(0) do |segundo|
      puts "#{segundo} segundo#{segundo == 1 ? '' : 's'}..."
      sleep 1
    end
    puts "🚀 Tempo esgotado!"
    tocar_som
  end

  private

  def tocar_som
    navegador = SeleniumWebDriver.new
    navegador.tocar_som("https://freesound.org/people/DanJFilms/sounds/786289/")
  end
end

# Inicia a contagem regressiva de 10 segundos
ContagemRegressiva.new(10).iniciar
