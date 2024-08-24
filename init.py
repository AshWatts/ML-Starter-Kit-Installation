import subprocess
import sys
import importlib

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_ml_libraries():
    libraries = [
        "numpy",          # Numerical computations
        "pandas",         # Data manipulation and analysis
        "scikit-learn",   # Machine learning algorithms and tools
        "tensorflow",     # Deep learning framework
        "keras",          # High-level neural networks API (runs on top of TensorFlow)
        "pytorch",        # Deep learning framework
        "matplotlib",     # Plotting and visualization
        "seaborn",        # Statistical data visualization
        "scipy",          # Scientific computing and technical computing
    ]
    
    for lib in libraries:
        try:
            importlib.import_module(lib)
            print(f"{lib} is already installed.")
        except ImportError:
            try:
                install(lib)
                print(f"{lib} installed successfully!")
            except Exception as e:
                print(f"Failed to install {lib}: {e}")

if __name__ == "__main__":
    install_ml_libraries()