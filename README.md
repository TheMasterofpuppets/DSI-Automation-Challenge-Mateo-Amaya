# DSI-Automation-Challenge-Mateo-Amaya

### Descripción general del proyecto

El proyecto DSI-Automation-Challenge-Mateo-Amaya consiste en un sistema RPA local que automatiza diversas tareas utilizando bots desarrollados en Python. Cada bot realiza una función específica para mejorar la eficiencia en procesos cotidianos.

### Funcionalidades de los Bots

1. **Bot de Copia de Seguridad en Google Drive:**
   - Realiza una copia de seguridad de una carpeta específica del sistema en Google Drive.

2. **Bot de Análisis de Facturas y Envío de Correo:**
   - Analiza el valor total de una factura.
   - Basado en el valor total, envía un correo al dueño de la factura informando sobre el gasto realizado.

3. **Bot de Envío de Mensajes por Gmail:**
   - Envía un mensaje por Gmail con destinatario, asunto y mensaje como parámetros.

### Instrucciones de configuración y ejecución

#### Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes requisitos:

1. **Python**:
   - La versión de Python utilizada para este proyecto es:
     ```powershell
     > python --version
     Python 3.12.4
     ```

2. **Librerías Python**:
   - Las principales librerías utilizadas en este proyecto son *pyautogui* y *pytesseract*, las cuales son necesarias para la ejecución del programa.
   - Asegúrate de instalar todas las dependencias necesarias de Python utilizando el comando:
     ```powershell
     > pip install -r requirements.txt
     ```

3. **Tesseract**:
   - Descarga e instala Tesseract desde el [Sitio oficial de Tesseract](https://github.com/tesseract-ocr/tesseract).
   - Después de instalarlo, agrega la ruta de instalación de Tesseract al PATH o a las variables de entorno del sistema operativo. **Este paso es necesario** para que funcione el sistema de OCR.
   - En Windows, la ruta por defecto es **C:\Program Files\Tesseract-OCR**.

### Ejecución

Para ejecutar la aplicación, asegúrate de seguir estos pasos desde el directorio `/src/app`:

Ejecuta el siguiente comando:

```powershell
> fastapi dev main.py
```

#### Gestión de Usuarios y Credenciales

Antes de realizar cualquier solicitud a la API, debes obtener un token de autenticación. Esto se logra enviando una solicitud POST al endpoint de login, diseñado para autenticar usuarios y devolver un token válido si las credenciales son correctas.

Las credenciales de usuario están definidas en el archivo `/src/app/auth/token_manager.py`. Este archivo contiene parte de la lógica para verificar las credenciales y generar tokens de autenticación válidos. Puedes consultar este archivo para conocer los usuarios con los que puedes autenticarte y obtener acceso a la API.

Una vez que tengas el token de autenticación, puedes usarlo en las solicitudes para acceder a cualquiera de los endpoints que despliegan los bots de la aplicación.

### Diseño y Arquitectura del Sistema

El sistema sigue una arquitectura modular donde cada bot está diseñado para cumplir una tarea específica de manera independiente. Facilita el mantenimiento del sistema al permitir actualizaciones y correcciones de errores de manera localizada en cada módulo, sin afectar al sistema en su totalidad.

#### Módulos principales

- **auth**: Se encarga de la autorización de los usuarios que pueden utilizar la API. Su propósito es gestionar la autenticación y asegurar que solo los usuarios autorizados accedan a los recursos protegidos por la API.

  - Base de Datos de Usuarios: Define una base de datos de prueba que contiene información de usuarios autorizados para acceder a la API.
  - Funciones de Autenticación: Incluye funciones para verificar credenciales de usuarios y generar tokens de autenticación utilizando técnicas como JWT (JSON Web Tokens).

- **endpoints**: Contiene todos los endpoints de la API que permiten interactuar con los bots y realizar funciones específicas como iniciar procesos de automatización o gestionar la autenticación.

  - Endpoints para Bots: Define endpoints para cada bot individual, permitiendo a los usuarios iniciar procesos específicos como la copia de seguridad en Google Drive, análisis de facturas, envío de correos, etc.
  - Endpoint de Autenticación: Incluye endpoints para el login y gestión de tokens de autenticación, asegurando un acceso seguro a los recursos de la API.

- **services**: Define los servicios relacionados con la llamada a los bots y la gestión de las funcionalidades principales de la aplicación.

- **utils**: Contiene utilidades esenciales para la funcionalidad de los bots, incluyendo manejo de OCR con pytesseract y automatización de interfaz con pyautogui.

  - bot_utils: Contiene funciones que ejecutan las acciones de cada bot.
  - ocr_utils: Proporciona funciones específicas para integración y uso de pytesseract, permitiendo la extracción de texto de imágenes.
  - scripts_utils: Contiene scripts y utilidades para la automatización de acciones específicas mediante pyautogui, facilitando la interacción con la interfaz gráfica del usuario y permitiendo la automatización con los bots.