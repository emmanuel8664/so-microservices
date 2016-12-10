### Introducción a versionamiento con git
Universidad ICESI
Curso: Sistemas Operativos
Docente: Daniel Barragán C.
Tema: Introducción a Python
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer la importancia del manejo de herramientas de control de versiones
* Emplear una herramienta de control de versiones

### Introducción
**Git**  es un software de control de versiones diseñado por Linus Torvalds,
pensando en la eficiencia y la confiabilidad del mantenimiento de versiones
de aplicaciones cuando éstas tienen un gran número de archivos de código fuente.
**GitHub** es una plataforma de desarrollo colaborativo de software para alojar proyectos
utilizando el sistema de control de versiones Git.

### Instalación
En esta guía se iran adicionando comandos básicos para el versionamiento de código fuente empleando GitHub
Para la edición de archivos  se sugiere la utilización del editor **Atom** el cual tiene funcionalidades
integradas para el uso con GitHub.

### Desarrollo
Se sugiere la utilización de ramas como mecanismo de trabajo y la no utilización de la rama maestra (master branch) para el desarrollo.

#### Conexión a GitHub

Existen distintas maneras de conectarse a GitHub a lo largo de las clases emplearemos la conexión por medio
de tokens. La conexión por medio de tokens no solo permite la interacción de un usuario con repositorios de
GitHub, sino tambien permite la conexión de aplicaciones directamente con repositorios.

Desde una cuenta de GitHub vaya a perfil, configuraciones, seleccione la opción de token personal 
___
![][1]
___
Seleccione generar token 
___
![][2]
___
Seleccione los permisos necesarios y cree el token 
___ 
![][3]
___
Tenga en cuenta nunca compartir su token de forma pública, el token presentado a continuación
solo tiene fines demostrativos. 
___
![][4]
___
Cree un repositorio en GitHub. 
___ 
![][5]
___
Clone el repositorio de GitHub creado
```
mkdir git_repositories
cd git_repositories
git clone https://github.com/d4n13lbc/microservices.git
cd microservices
```

Configure el token como medio de autenticación a GitHub
```
git config remote.origin.url "https://58ba0a3f8094322048488e1aa519786c12636adf@github.com/d4n13lbc/microservices.git"
```

#### Enviado a GitHub
Crear un archivo
```
touch README.md
```

Adicionar los cambios realizados a un archivo. Es posible adicionar multiples cambios realizados (--all),
sin embargo es aconsejable en ese caso, que los cambios realizados pertenezcan a la misma funcionalidad.
```
git add README.md
```

Describir el cambio
```
git commit -m "upload README file"
```

Enviar los cambios al repositorio. Si no existe la rama en GitHub, esta se crea automáticamente.
```
git push origin master
```

#### Creación de una rama
Crear una rama (branch) llamada 01_intro_flask y activarla (checkout)
```
git checkout -b 01_intro_flask
```

Verifica la creación de la rama y su activación
```
git branch
```

Crear la rama en GitHub
```
git push origin 01_intro_flask
```

![][6]

#### Haciendo un Pull Request
El pull request o PR permite manifestar la intención de adicionar un cambio realizado en una rama a la rama maestra. Estos cambios son revisados por un miembro del equipo quien aceptará realizar la mezcla (merge) de las ramas o propondra cambios. Los cambios realizados en la rama se reflejaran automaticamente en el pull request antes de ser mezclado.

#### Entendiendo los terminos Upstream y Fork
Fork corresponde a la copia que se hace de un repositorio de GitHub con el fin de adicionar una funcionalidad nueva para uso personal o para ser compartida mas adelante a la comunidad. Al repositorio original que le hemos hecho Fork se le llama Upstream.

#### Etiquetado de versiones
Las versiones se componen de tres digitos, el primero de ellos coresponde a una liberación mayor, el segundo de ellos a una liberación menor y el último a un patch.

#### Referencias
https://try.github.io/levels/1/challenges/1  
http://semver.org/

[1]: images/01_token_profile.png
[2]: images/02_token_generate.png
[3]: images/03_token_configuration.png
[4]: images/04_token.png
[5]: images/05_github_repository.png
[6]: images/05_github_branch.png
