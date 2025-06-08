# Webex Bot con Python

Este proyecto muestra cómo crear un **bot de Webex** utilizando Python y las APIs oficiales de Webex.

---

## 🤖 ¿Qué es un bot de Webex?

Un bot es una aplicación que puede enviar y recibir mensajes en Webex, automatizando interacciones en espacios y facilitando flujos de comunicación.

---

## 🚀 Objetivo

Construir un bot que pueda:

- Escuchar mensajes en espacios Webex donde esté agregado
- Responder automáticamente a mensajes o comandos
- Gestionar eventos en tiempo real usando Webhooks

---

## 📚 Requisitos

- Cuenta Webex con un bot creado (https://developer.webex.com/my-apps)
- Token de acceso del bot
- Python 3.7+
- Ngrok (opcional, para exponer servidor local durante desarrollo)

---

## 🛠 Tecnologías usadas

- Python 3
- Flask (servidor web para recibir eventos)
- python-dotenv (para variables de entorno)
- requests (para llamadas API a Webex)

---

## 🔧 Cómo empezar

### 1. Crear un bot en Webex

- Ve a [My Apps](https://developer.webex.com/my-apps)
- Crea un nuevo bot y guarda el token de acceso

# 🤖 Crear un Bot en Webex

En esta sección aprenderás a crear un **Webex Bot** desde el portal de desarrolladores de Webex. Este bot nos permitirá realizar diversas integraciones utilizando un token de larga duración (hasta 100 años), ideal para desarrollo y pruebas iniciales.

> ⚠️ **Importante:** Aunque este token de larga duración es útil, también representa un riesgo de seguridad si cae en manos equivocadas. En caso de compromiso, deberás **regenerar manualmente** el token desde el portal. Más adelante exploraremos opciones más seguras para producción.

---

### 🛠 Paso 1: Ingresar al portal

Accede a tu portal de desarrollador en [developer.webex.com](https://developer.webex.com) y dirígete a la sección **My Webex Apps**, donde podrás visualizar, modificar o crear tus integraciones.

![Bot1](pictures/web_app.png)

---

### 🧩 Paso 2: Crear una nueva aplicación

Haz clic en **"Create a New App"**.

![NewAPP](pictures/createnewapp.png)

---

### 🤖 Paso 3: Seleccionar tipo de aplicación

Selecciona la opción **"Create a Bot"**, ya que vamos a trabajar con un bot tradicional.

![Createbot](pictures/createbot.png)

---

### ✍️ Paso 4: Configurar tu Bot

Rellena los siguientes campos:

- **`Bot Name`**: Nombre descriptivo para tu bot.
- **`Bot Username`**: Este será el identificador único que usarás para mencionar o llamar al bot dentro de los espacios Webex.
- **`Icon`**: Imagen de perfil del bot que aparecerá en los espacios.
- **`App Hub Description`**: Breve descripción sobre el propósito del bot o sus funcionalidades, útil para otros desarrolladores que lo mantendrán o integrarán.

![Createbot_caracteristicas](pictures/bot_carac.png)

---

### 🔑 Paso 5: Obtener el token de acceso

Una vez creado el bot, se mostrará un **token de acceso**.  
⚠️ **Este token solo se muestra una vez**, por lo tanto, **debes guardarlo en un lugar seguro**.  
Si en algún momento se ve comprometido, deberás **regenerarlo manualmente** y actualizar todas las integraciones que lo utilicen.

![Createbot_token](pictures/token_bot.png)

---

## ✅ ¡Bot creado!

Con esto, ya tienes listo tu **Webex Bot**, el cual podrás usar para automatizar tareas, responder mensajes, integrarte con APIs externas y mucho más.

Más adelante en este proyecto aprenderemos a:

- Enviar mensajes a un espacio Webex desde Python
- Usar Webhooks para escuchar eventos en tiempo real
- Crear integraciones más seguras usando OAuth2