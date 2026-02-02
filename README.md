# Emoji Steganography - Cifrador de Emojis

Oculta mensajes secretos dentro de emojis usando caracteres invisibles Unicode (Zero Width Characters).

## Características

- Cifra texto dentro de emojis usando esteganografía
- Los mensajes son invisibles a simple vista
- Usa caracteres Zero Width (U+200B, U+200C)
- Interfaz web moderna y fácil de usar

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/emoticonos_stego.git
cd emoticonos_stego

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # En Windows
source .venv/bin/activate  # En Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Iniciar el servidor
python emoji_cipher.py

# Abrir en el navegador
http://localhost:5000
```

## Tecnologías

- Python + Flask
- HTML/CSS/JavaScript
- Unicode Zero Width Characters

## Ejemplo

```
Texto: "Hola"
Emoji: 😎
Resultado: 😎[caracteres invisibles]
```

## Nota

Esto es esteganografía (ocultar datos), NO encriptación fuerte. No usar para información crítica.
