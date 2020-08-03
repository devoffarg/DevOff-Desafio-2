![](https://static-cdn.jtvnw.net/jtv_user_pictures/fb425ddf-5e67-4c84-9210-8065809675f7-profile_banner-480.png)

# Desafío 2 - 02/08/2020

Vamos a implementar una versión moderna de un instrumento milenario que representa uno de los primeros sistemas de cifrado de la historia de la humanidad: una escítala. Construiremos una escítala en forma de REST API para cifrar y descifrar mensajes.

## Un poco de historia

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/1200px-Skytale.png" align="right" width="300">
La escítala es un mecanismo de cifrado que surje en Esparta como forma sencilla para generar mensajes secretos, compartirlos y descifrarlos con la misma facilidad.

El método consistía en utilizar una vara de cierto espesor, alrededor de la cual una cinta de papiro u algún otro material para luego escribir en ella el mensaje de manera horizontal, siguiendo la dirección de la vara.

Al recibir el mensaje, el receptor poseía una vara con el mismo espesor que aquella utilizada para generar el mensaje, por lo que el proceso de descifrado consisitía en enrollar la cinta en la vara y leer el mensaje.

## El algoritmo

A la hora de cifrar un mensaje con este mecanismo podemos pensar a la escitala como una matriz rectangular de la cual sabemos una de sus medidas, por ejemplo, su longitud dada la cantidad de vueltas que la cinta da sobre la vara. Para simplificar, llamaremos a este parámetro `L`.

En base a nuestro parámetro `L`, generamos una matriz de dimensión `N x L`, donde `N` se deriva a partir de `L` y la longitud del mensaje.
Procedemos a rellenar la matriz de manera longitudinal, saltando a una nueva fila a medida que se completa la anterior, hasta haber agotado el mensaje.
A continuación, procedemos a transponer la matriz y recuperar el texto de manera longitudinal, manteniendo espacios si los hubiera.

Por ejemplo, dado el texto `Devoff se puso ATR` y una longitud de `4`, la matriz inicial nos quedaría de la siguiente manera:

```
| D | e | v | o |
| f | f |   | s |
| e |   | p | u |
| s | o |   | A |
| T | R |   |   |
```

Que una vez transpuesto quedaría:

```
| D | f | e | s | T |
| e | f |   | o | R |
| v |   | p |   |   |
| o | s | u | A |   |
```

Por lo que nuestro mensaje cifrado sería `DfesTef oRv p  osuA`.

Para descifrar el mensaje, el proceso sería el mismo pero a la inversa: arrancamos con una matriz de dimensiones `L x N`, siguiendo la misma lógica en la que `N` se calcula en base al parámetro `L` y la longitud del mensaje.

Siguiendo la misma metodología se rellena la matríz, se transpone la misma y se recupera el texto de manera longitudinal respetando espacios.

## La API

El servicio debe proponer dos endpoints, uno para cifrar y otro para cifrar. Ambos deberan procesar `POST`s que contendrán un cuerpo formado en JSON con el mensaje y la cantidad de "vueltas" que se le debe dar al mensaje en la escítala:

```
{
  "vueltas": <number>,
  "mensaje": <string>
}
```

y deberán devolver un JSON con el mensaje cifrado/descifrado con el siguiente formato:

```
{
  "mensaje": <string>
}
```

## Condiciones del desafío

⛔ El algoritmo de cifrado y descifrado no puede utilizar ninguna dependencia externa.

✅ El servidor de la API deberá soportar requests desde dominios que no sean localhost.

✅ Podrás incorporar dependencias para levantar el servidor (ej: si utilizas Node, podrás instalar Express).

✅ Podrás utilizar cualquier lenguaje de programación que tenga un módulo HTTP disponible y [esté soportado en Repl.it](https://repl.it/languages).

## 📚 Herramientas de consulta

Podrás utilizar cualquier herramienta de búsqueda que necesites (amamos buscar en Google y leer Stack Overflow <3).

## ⏳ Tiempo

Tendrás **1 hora** para resolver el desafío.

## 🤔 ¿Cómo presento mi código?

### Si tenés una cuenta en GitHub

Hacé un fork de este repo:

![Presionar el botón Fork, situado al comienzo de la página](https://docs.github.com/assets/images/help/repository/fork_button.jpg)

Cloná tu fork, reemplazando `[TU_ALIAS]` con el nombre de tu cuenta de GitHub. Podés clonarlo utilizando la consola:

```
git clone https://github.com/[TU_ALIAS]/DevOff-Desafio-2
```

También podés utilizar GitHub Desktop, tu IDE favorito, lo que gustes.

Cuando finalices la resolución del desafío, no olvides subir todos tus cambios usando `git push` o el equivalente que ofrezca tu cliente de Git. Envianos por el chat de la transmisión o por DM a la cuenta de Twitter de DevOff Argentina el link a tu repositorio.

### Si no tenés una cuenta en GitHub

[Podés hacer clic aquí y mágicamente se descargará un archivo comprimido con todo lo que contiene este repositorio](https://github.com/devoffarg/DevOff-Desafio-2/archive/master.zip).

Cuando finalices la resolución del desafío, envianos un archivo ZIP con todo tu trabajo a través de [WeTransfer](https://wetransfer.com/).

## 💜 Agradecimientos

### Jurados

- ¡Gracias a [Gonzalo Pozzo](https://twitter.com/goncy) y [Magalí Domínguez](https://twitter.com/printmaga) por ser nuestros jurados!
- ¡Un agradecimiento especial a [Juani Gallo](https://twitter.com/juanigallo), el jurado invitado de esta edición!

### Organizaciones aliadas

¡Gracias a [Migue Moyano](https://twitter.com/elmiguedev), [Joel A. Villarreal Bertoldi](https://twitter.com/joelalejandro) y [Agustín Carrasco](https://twitter.com/asermax) del equipo de [CoDeAr](https://twitter.com/somoscodear) por dar una mano para que este proyecto sea posible! 

### Créditos

DevOff Argentina es un proyecto ideado por [Aldana Denise](https://twitter.com/gizmowis), con el apoyo de [CoDeAr](https://twitter.com/somoscodear).

## 🚀 Soluciones

¡A continuación, listamos todas las soluciones que se fueron presentando para este desafío!

🌟 Participantes EN VIVO:

- https://github.com/rapkyt/DevOff-Desafio-2, por Rapkyt 🏆
- https://github.com/GiulianaOlmos/DevOff-Desafio-2, por Giuli
- https://github.com/JessVel/DevOff-Desafio-2, por Jess
- https://github.com/FedericoLeiva12/DevOff-Desafio-2, por Fede

💜 Participantes de la comunidad:

### Ruby

- https://github.com/aldrinmartoq/DevOff-Desafio-2, por Aldrin Martoq

### Kotlin

- https://github.com/ASarco/DevOff-Desafio-2, por [Ale Sarco](https://twitter.com/asarco_ES_ar/status/1290264906080583680)

### Java

- https://github.com/gbobr/DevOff-Desafio-2, por [Germán Bobr](https://twitter.com/GermanBobr/status/1290133235494608897=

### JavaScript

- https://github.com/Enkdress/DevOff-Desafio-2, por [Sergio Correa](https://twitter.com/xEnkdress/status/1290130283925299201)
- https://github.com/lauritula/DevOff-Desafio-2, por [Laura](https://twitter.com/lauritula/status/1290091276927299585)
- https://github.com/lautarolopez/DevOff-Desafio-2, por Lautaro Lopez

### Python

- https://github.com/lucasshrew/DevOff-Desafio-2, por Lucas Shrewsbury

# ¡Muchos éxitos y a codear!
