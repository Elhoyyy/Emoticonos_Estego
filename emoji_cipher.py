from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def texto_a_binario(texto):
    return ''.join(format(ord(char), '08b') for char in texto)

def binario_a_texto(binario):
    texto = ''
    for i in range(0, len(binario), 8):
        byte = binario[i:i+8]
        if len(byte) == 8:
            texto += chr(int(byte, 2))
    return texto

def cifrar_mensaje(texto, emoji='😎'):
    """Cifra un mensaje en un emoji usando caracteres invisibles"""
    # Convertir texto a binario
    binario = texto_a_binario(texto)
    
    # Mapeo: 0 = U+200C, 1 = U+200B, separador = U+200D
    mensaje_oculto = ''
    for i, bit in enumerate(binario):
        if bit == '0':
            mensaje_oculto += '\u200C'  # Zero Width Non-Joiner
        else:
            mensaje_oculto += '\u200B'  # Zero Width Space
        
        # Añadir separador cada 8 bits (cada byte)
        if (i + 1) % 8 == 0 and i < len(binario) - 1:
            mensaje_oculto += '\u200D'  # Zero Width Joiner
    
    return emoji + mensaje_oculto

def descifrar_mensaje(emoji_cifrado):
    # Eliminar el primer carácter (el emoji visible)
    texto_oculto = ''
    for char in emoji_cifrado:
        # Solo procesar caracteres invisibles (Zero Width)
        if char in ['\u200C', '\u200B', '\u200D']:
            texto_oculto += char
    # Convertir caracteres invisibles a binario
    binario = ''
    for char in texto_oculto:
        if char == '\u200C':
            binario += '0'
        elif char == '\u200B':
            binario += '1'
        # Ignorar separadores U+200D
    
    # Convertir binario a texto
    return binario_a_texto(binario)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/cifrar', methods=['POST'])
def cifrar():
    try:
        data = request.get_json()
        texto = data.get('texto', '')
        emoji = data.get('emoji', '😎')
        
        if not texto:
            return jsonify({'error': 'Texto vacío'}), 400
        
        resultado = cifrar_mensaje(texto, emoji)
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/descifrar', methods=['POST'])
def descifrar():
    try:
        data = request.get_json()
        emoji_cifrado = data.get('emoji_cifrado', '')
        
        if not emoji_cifrado:
            return jsonify({'error': 'Emoji cifrado vacío'}), 400
        
        mensaje = descifrar_mensaje(emoji_cifrado)
        return jsonify({'mensaje': mensaje})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("🚀 Servidor iniciado en http://localhost:5000")
    print("📂 Abre http://localhost:5000 en tu navegador")
    app.run(debug=True, port=5000)
