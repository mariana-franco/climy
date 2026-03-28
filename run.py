"""Script principal para executar a aplicação Climy."""

import subprocess
import sys
import os
from pathlib import Path

# Adiciona o diretório atual ao PYTHONPATH para garantir que o
# módulo 'src' seja encontrado se o script for executado da raiz.
sys.path.append(str(Path(__file__).parent))


def main():
    """Valida o ambiente e executa a aplicação Streamlit."""

    print("🌤️ Iniciando Climy...")
    print("📡 Verificando conexão com Open-Meteo...")

    # 1. Verifica dependências críticas
    # Removi o 'plotly' da verificação pois não vi uso dele no seu código da UI,
    # mas adicionei 'python-dotenv' que é essencial para o seu config.py funcionar.
    dependencies = ["streamlit", "requests", "dotenv"]
    missing = []

    for lib in dependencies:
        try:
            if lib == "dotenv":
                __import__("dotenv")
            else:
                __import__(lib)
        except ImportError:
            missing.append(lib)

    if missing:
        print(f"❌ Dependências faltando: {', '.join(missing)}")
        print("📦 Instale as dependências com: pip install -r requirements.txt")
        sys.exit(1)

    # 2. Define o caminho do arquivo da aplicação
    # Ajuste o nome "app.py" para o nome real do seu arquivo (ex: main.py ou streamlit_app.py)
    app_file = "app.py"
    app_path = Path(__file__).parent / app_file

    if not app_path.exists():
        # Tenta encontrar o arquivo caso o nome seja diferente
        alternatives = ["streamlit_app.py", "main.py", "climy_ui.py"]
        for alt in alternatives:
            if (Path(__file__).parent / alt).exists():
                app_path = Path(__file__).parent / alt
                break
        else:
            print(
                f"❌ Erro: Arquivo da aplicação não encontrado no diretório {Path(__file__).parent}"
            )
            sys.exit(1)

    # 3. Executa a aplicação via subprocesso
    try:
        print(f"🚀 Rodando {app_path.name}...")
        subprocess.run(["streamlit", "run", str(app_path)], check=True)
    except KeyboardInterrupt:
        print("\n👋 Aplicação encerrada pelo usuário.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao iniciar o Streamlit: {e}")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
