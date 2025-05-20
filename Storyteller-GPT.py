#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, GenerationConfig
import numpy as np
import re

# Definición de una excepción personalizada para errores críticos de carga
class InterstellarError(Exception):
    """Excepción personalizada para errores críticos, como fallos en la carga del modelo."""
    pass

class StorytellerGPT:
    """
    Clase principal para el Generador de Cuentos Mágicos.
    Utiliza el modelo GPT-2 en español para generar ideas y comienzos de historias.
    """
    def __init__(self):
        # Determina si se usará la GPU (cuda) o la CPU. Prioriza 'cuda' si está disponible.
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "DeepESP/gpt2-spanish" # Modelo pre-entrenado GPT-2 en español

        print(f"🚀 Iniciando StorytellerGPT en el dispositivo: {self.device.upper()}...")
        
        # Intenta cargar el tokenizer y el modelo. Si falla, intenta un respaldo.
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
            self.model = GPT2LMHeadModel.from_pretrained(self.model_name).to(self.device)
            self.tokenizer.pad_token = self.tokenizer.eos_token # Define el token de padding
            print("✅ Modelo GPT-2 para español cargado con éxito.")
        except Exception as e:
            print(f"⚡ ¡Alerta Cósmica! Falló la carga principal ({e}). Intentando respaldo...")
            self._download_interstellar_backup()

        # Configuración de generación por defecto para inicios de cuento.
        # Estos parámetros buscan un equilibrio entre creatividad y coherencia.
        self.generation_config = GenerationConfig(
            max_length=300,             # Longitud máxima total del texto generado (prompt + generación)
            do_sample=True,             # Permite muestreo (generación aleatoria)
            temperature=1.0,            # Controla la aleatoriedad. 1.0 es un buen balance.
            top_p=0.95,                 # Muestrea de las palabras que suman el 95% de probabilidad acumulada.
            top_k=50,                   # Muestrea de las 50 palabras más probables.
            repetition_penalty=1.2,     # Penaliza la repetición de tokens para mayor diversidad.
            num_return_sequences=3,     # Genera 3 inicios de cuento para ofrecer opciones.
            pad_token_id=self.tokenizer.eos_token_id, # Tokens especiales para el modelo.
            bos_token_id=self.tokenizer.bos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
        )

    def _download_interstellar_backup(self):
        """
        Intenta cargar el modelo desde Hugging Face Hub como un respaldo si la carga inicial falla.
        Lanza InterstellarError si la carga de respaldo también falla.
        """
        print("🛸 Conectando con servidores cuánticos de respaldo para la carga del modelo...")
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
            self.model = GPT2LMHeadModel.from_pretrained(self.model_name).to(self.device)
            self.tokenizer.pad_token = self.tokenizer.eos_token
            print("✅ Carga de respaldo exitosa. ¡Universo narrativo restaurado!")
        except Exception as e:
            raise InterstellarError(f"¡Falló la conexión con el universo alternativo! Error crítico: {e}\n"
                                    "Asegúrate de tener conexión a internet o de que el modelo 'DeepESP/gpt2-spanish' esté disponible.")

    def generate_story_idea(self, theme):
        """
        Genera una idea concisa para un cuento (personaje, escenario o conflicto)
        basada en un tema dado.
        """
        # Variedad de prompts para obtener diferentes tipos de ideas
        prompts = [
            f"Describe un personaje misterioso para un cuento sobre {theme}:",
            f"Propón un escenario inusual para una historia de {theme}:",
            f"Una idea original para el conflicto principal en un cuento de {theme}:"
        ]
        
        selected_prompt = np.random.choice(prompts) # Elige un prompt al azar
        
        inputs = self.tokenizer(selected_prompt, return_tensors="pt").to(self.device)
        
        print(f"\n🧠 Generando idea: '{selected_prompt}'")
        
        try:
            outputs = self.model.generate(
                **inputs,
                max_length=len(inputs["input_ids"][0]) + 60, # Genera hasta 60 tokens adicionales para la idea
                do_sample=True,
                temperature=0.8, # Temperatura moderada para ideas más enfocadas
                top_p=0.95,
                num_return_sequences=1, # Solo necesitamos una idea
                pad_token_id=self.tokenizer.eos_token_id,
                bos_token_id=self.tokenizer.bos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )
            decoded_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Limpieza del texto generado: Elimina el prompt y posibles encabezados
            idea = decoded_text.replace(selected_prompt, "", 1).strip()
            idea = re.sub(r'^(?:[0-9]+\.?\s*)?(?:El personaje es:|El escenario es:|El conflicto es:|Una idea es:)\s*', '', idea, flags=re.IGNORECASE).strip()
            
            # Intenta cortar la idea en la primera o segunda oración completa para mayor concisión.
            sentences = re.split(r'(?<=[.?!])\s*', idea)
            if len(sentences) >= 2 and sentences[0].strip() and sentences[1].strip():
                return " ".join(sentences[:2]).strip() # Toma las dos primeras oraciones si existen
            elif sentences and sentences[0].strip():
                return sentences[0].strip() # Si solo hay una, toma esa
            else:
                return idea.split('\n')[0].strip() # Fallback: toma la primera línea

        except Exception as e:
            return f"❌ No se pudo generar una idea: {e}"

    def generate_story_start(self, theme, starting_phrase=""):
        """
        Genera el inicio de un cuento basándose en un tema y una frase inicial opcional.
        Produce múltiples opciones de inicio.
        """
        # Crea el prompt base que guía al modelo para generar un inicio de cuento detallado.
        if starting_phrase:
            base_prompt = f"Escribe un comienzo detallado para un cuento sobre {theme}, iniciando con la frase: '{starting_phrase}'\n"
        else:
            base_prompt = f"Escribe un comienzo detallado para un cuento sobre {theme}:\n"
            
        print(f"\n✍️ Generando inicio de cuento para: '{theme}'")
        if starting_phrase:
            print(f"   (Comenzando con: '{starting_phrase}')")

        inputs = self.tokenizer(base_prompt, return_tensors="pt").to(self.device)
        
        # Calcula la longitud máxima permitida para la generación, dando amplio margen.
        current_max_length = len(inputs["input_ids"][0]) + 250 # Genera hasta 250 tokens adicionales

        # Actualiza la configuración de generación para esta llamada si es necesario
        # (Aunque en este caso usa la self.generation_config ya optimizada)
        temp_generation_config = GenerationConfig(
            max_length=current_max_length,
            do_sample=self.generation_config.do_sample,
            temperature=self.generation_config.temperature,
            top_p=self.generation_config.top_p,
            top_k=self.generation_config.top_k,
            repetition_penalty=self.generation_config.repetition_penalty,
            num_return_sequences=self.generation_config.num_return_sequences,
            pad_token_id=self.tokenizer.eos_token_id,
            bos_token_id=self.tokenizer.bos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
        )

        try:
            outputs = self.model.generate(
                **inputs,
                generation_config=temp_generation_config # Usa la configuración temporal
            )
            
            generated_starts = []
            for i, output_sequence in enumerate(outputs):
                decoded_text = self.tokenizer.decode(output_sequence, skip_special_tokens=True)
                
                # Limpia el texto: elimina el prompt inicial y cualquier resto de instrucción.
                story_start = decoded_text.replace(base_prompt, "", 1).strip()
                story_start = re.sub(r'^(?:Escribe un comienzo detallado para un cuento sobre .*?:)?\s*\n*', '', story_start, flags=re.IGNORECASE | re.MULTILINE).strip()
                
                # Divide el texto en oraciones para un corte más natural.
                sentences = re.split(r'(?<=[.?!])\s+', story_start)
                
                final_text = ""
                # Intenta tomar hasta 3 oraciones completas para un inicio sustancial.
                if len(sentences) >= 3 and sentences[0].strip() and sentences[1].strip() and sentences[2].strip():
                    final_text = " ".join(sentences[:3]).strip()
                    # Añade puntos suspensivos si hay más texto después de las 3 oraciones
                    if len(sentences) > 3 and sentences[3].strip():
                        final_text += "..."
                elif sentences and sentences[0].strip(): # Si hay menos de 3 pero al menos una oración
                    final_text = sentences[0].strip() + "..." # Toma la primera y añade puntos suspensivos
                else: # Si el texto generado es muy corto o no tiene oraciones válidas
                    final_text = story_start.strip() + "..." if story_start.strip() else "..."

                generated_starts.append(final_text)
            
            return generated_starts
        except Exception as e:
            return [f"❌ No se pudo generar el inicio del cuento: {e}"]

# --------------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# --------------------------------------
if __name__ == "__main__":
    print("""
    ███████╗████████╗ ██████╗ ████████╗██╗     ██╗   ██╗███████╗██████╗ 
    ██╔════╝╚══██╔══╝██╔════╝ ╚══██╔══╝██║     ██║   ██║██╔════╝██╔══██╗
    ███████╗   ██║   ██║  ███╗   ██║   ██║     ██║   ██║█████╗  ██████╔╝
    ╚════██║   ██║   ██║   ██║   ██║   ██║     ██║   ██║██╔══╝  ██╔══██╗
    ███████║   ██║   ╚██████╔╝   ██║   ███████╗╚██████╔╝███████╗██║  ██║
    ╚══════╝   ╚═╝    ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
    GENERADOR DE CUENTOS MÁGICOS V-1.2 (Optimizado para GitHub)
    """)

    try:
        storyteller = StorytellerGPT()
    except InterstellarError as e:
        print(f"¡ERROR CRÍTICO AL INICIAR!: {e}")
        print("El generador no puede funcionar sin el modelo. Saliendo del programa.")
        exit()
    except Exception as e:
        print(f"Ocurrió un error inesperado al inicializar el generador: {e}")
        print("Saliendo del programa.")
        exit()
        
    while True:
        print("\n--- ELIGE TU AVENTURA NARRATIVA ---")
        print("1. Generar una **idea** para un cuento (personaje, escenario, conflicto)")
        print("2. Generar el **inicio** de un cuento (un párrafo o más)")
        print("3. Salir del Generador")
        
        choice = input("👉 ¿Qué quieres hacer? (1/2/3): ")

        if choice == '1':
            theme = input("🌟 Tema de la idea (ej: 'un viaje en el tiempo', 'un detective sobrenatural'): ")
            if not theme:
                print("⚠️ Por favor, introduce un tema válido.")
                continue
            idea = storyteller.generate_story_idea(theme)
            print(f"\n💡 IDEA GENERADA:\n{idea}")
            print("═"*40)

        elif choice == '2':
            theme = input("📚 Tema del cuento (ej: 'la última colonia en Marte', 'un reino de sombras'): ")
            if not theme:
                print("⚠️ Por favor, introduce un tema válido.")
                continue
            starting_phrase = input("✍️ Frase con la que quieres que empiece (opcional, deja vacío para que la cree): ")
            
            story_starts = storyteller.generate_story_start(theme, starting_phrase)
            
            print("\n📖 INICIOS DE CUENTO GENERADOS:")
            for i, start in enumerate(story_starts):
                print(f"--- OPCIÓN {i+1} ---")
                print(start)
                print("-" * 15)
            print("═"*40)

        elif choice == '3':
            print("\n✨ ¡El universo narrativo te espera! ¡Adiós y felices historias!")
            break
        else:
            print("🚫 Opción no válida. Por favor, elige 1, 2 o 3.")
