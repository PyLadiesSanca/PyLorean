# PyLorean

## Sobre
Projeto do PyLadies São Carlos para facilitar agendamento de reuniões.

## Contribuidores
Em breve

## Instalando e Configurando Plugins e Ferramentas
Para usar o bower, temos que instalar o node-js e npm.
Feito isso podemos instalar o bower.

###### Configuração usada para installar no Linux Ubuntu e Debian.
> Para outros sistemas operacionais verifique a documenção.

### Instalando o Node-js e npm

##### Instalação e Instrução do Node-js
###### Node.js v5.x:

```
# Usando Ubuntu
curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
sudo apt-get install -y nodejs

# Usando Debian, como root
curl -sL https://deb.nodesource.com/setup_5.x | bash -
apt-get install -y nodejs
```
###### Verificando a instalação.
> $ node -v
> v0.12.0

Mais detalhes em [Distribuição](https://github.com/nodesource/distributions) e [Nodejs](https://nodejs.org/en/download/).

##### Instalando o npm

```
$ sudo npm install npm -g
```
###### Verificando a instalação.
> $ npm -v
> 3.4.0

Mais detalhes em [npm](https://docs.npmjs.com/getting-started/what-is-npm).

### Instalando o Bower
```
$ npm install -g bower
```
Para mais detalhes veja a documentação [Bower](http://bower.io/).


### Como instalar e usar Bootstrap
##### Instalando o Bootstrap
```
$ bower install bootstrap
```

##### Configuração e uso:

```
<!-- Bootstrap -->
<link rel="stylesheet" href="static/bower_components/bootstrap/dist/css/bootstrap.min.css">

<!-- Scripts -->
<script type="text/javascript" src="static/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>
```

Para mais detalhes veja a documentação [Bootstrap](http://getbootstrap.com/getting-started/).


#### Como instalar e usar o Font-Awesome
##### Instalando o fonte-awesome

```
$ bower install font-awesome
```
##### Configuração e uso.

```
<!-- Font-Awesome -->
<link rel="stylesheet" href="static/bower_components/font-awesome/css/font-awesome.min.css">
```

Documentação [Font-Awesome](http://fontawesome.io/get-started/).

## Como usar
