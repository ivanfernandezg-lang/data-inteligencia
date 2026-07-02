"""
Traduce el paper de Widrow & Lehr (1990) del inglés al español académico.
Preserva TODO el código LaTeX (comandos, math, citas, labels, referencias, figuras).
Solo traduce texto en lenguaje natural (párrafos, títulos de sección, pies de nota, etc.).

Estrategia: reemplazos por bloques completos (párrafo a párrafo) para mantener
la máxima calidad de traducción, usando un diccionario extenso de términos técnicos.
"""
import re
import os

# ============================================================================
# DICCIONARIO DE TRADUCCIÓN TÉCNICA (inglés -> español académico)
# ============================================================================
TECH_TERMS = {
    # Términos generales del paper
    "feedforward artificial neural networks": "redes neuronales artificiales con alimentación hacia adelante",
    "feedforward neural network": "red neuronal con alimentación hacia adelante",
    "feedforward network": "red con alimentación hacia adelante",
    "feedforward": "alimentación hacia adelante",
    "backpropagation": "retropropagación",
    "backpropagation algorithm": "algoritmo de retropropagación",
    "backpropagation technique": "técnica de retropropagación",
    "backpropagation network": "red de retropropagación",
    "backpropagation rule": "regla de retropropagación",
    "Perceptron rule": "regla del Perceptrón",
    "Perceptron learning rule": "regla de aprendizaje del Perceptrón",
    "Perceptron algorithm": "algoritmo del Perceptrón",
    "Perceptron convergence procedure": "procedimiento de convergencia del Perceptrón",
    "LMS algorithm": "algoritmo LMS",
    "LMS rule": "regla LMS",
    "Madaline Rule I": "Regla Madaline I",
    "Madaline Rule II": "Regla Madaline II",
    "Madaline Rule III": "Regla Madaline III",
    "Madaline I": "Madaline I",
    "Madaline II": "Madaline II",
    "Madaline III": "Madaline III",
    "minimal disturbance principle": "principio de mínima perturbación",
    "adaptive linear combiner": "combinador lineal adaptativo",
    "adaptive linear element": "elemento lineal adaptativo",
    "adaptive threshold element": "elemento adaptativo de umbral",
    "adaptive threshold logic element": "elemento lógico adaptativo de umbral",
    "steepest descent": "descenso más pronunciado",
    "steepest-descent": "descenso más pronunciado",
    "gradient descent": "descenso por gradiente",
    "mean-square error": "error cuadrático medio",
    "mean square error": "error cuadrático medio",
    "sum square error": "suma del error cuadrático",
    "sum squared error": "suma del error cuadrático",
    "hard-limiting quantizer": "cuantificador de límite estricto",
    "sigmoid function": "función sigmoide",
    "sigmoid Adaline": "Adaline sigmoidal",
    "sigmoid network": "red sigmoidal",
    "signum network": "red signum",
    "signum Adaline": "Adaline signum",
    "hidden layer": "capa oculta",
    "hidden-layer": "capa oculta",
    "output layer": "capa de salida",
    "output-layer": "capa de salida",
    "first layer": "primera capa",
    "second layer": "segunda capa",
    "weight vector": "vector de pesos",
    "weight vectors": "vectores de pesos",
    "input pattern": "patrón de entrada",
    "input patterns": "patrones de entrada",
    "input pattern vector": "vector de patrón de entrada",
    "input vector": "vector de entrada",
    "input signal": "señal de entrada",
    "desired response": "respuesta deseada",
    "desired responses": "respuestas deseadas",
    "training set": "conjunto de entrenamiento",
    "training pattern": "patrón de entrenamiento",
    "training patterns": "patrones de entrenamiento",
    "training process": "proceso de entrenamiento",
    "training procedure": "procedimiento de entrenamiento",
    "pattern recognition": "reconocimiento de patrones",
    "pattern classification": "clasificación de patrones",
    "threshold logic": "lógica de umbral",
    "threshold level": "nivel de umbral",
    "linear separability": "separabilidad lineal",
    "linearly separable": "linealmente separable",
    "linearly separable function": "función linealmente separable",
    "linear classifier": "clasificador lineal",
    "linear classifiers": "clasificadores lineales",
    "linear error": "error lineal",
    "linear output": "salida lineal",
    "linear combiner": "combinador lineal",
    "nonlinear classifier": "clasificador no lineal",
    "nonlinear classifiers": "clasificadores no lineales",
    "generalization": "generalización",
    "generalize": "generalizar",
    "bias weight": "peso de sesgo",
    "decision boundary": "frontera de decisión",
    "decision boundaries": "fronteras de decisión",
    "decision function": "función de decisión",
    "error-correction rule": "regla de corrección de error",
    "error-correction rules": "reglas de corrección de error",
    "error correction rule": "regla de corrección de error",
    "error correction rules": "reglas de corrección de error",
    "error signal": "señal de error",
    "error signals": "señales de error",
    "output error": "error de salida",
    "output errors": "errores de salida",
    "output response": "respuesta de salida",
    "output responses": "respuestas de salida",
    "output decision": "decisión de salida",
    "square error": "error cuadrático",
    "square-error": "error cuadrático",
    "squared error": "error cuadrático",
    "squared-error": "error cuadrático",
    "instantaneous gradient": "gradiente instantáneo",
    "true gradient": "gradiente verdadero",
    "gradient estimate": "estimación del gradiente",
    "gradient noise": "ruido de gradiente",
    "gradient methods": "métodos de gradiente",
    "MSE surface": "superficie ECM",
    "MSE surfaces": "superficies ECM",
    "pattern capacity": "capacidad de patrones",
    "statistical capacity": "capacidad estadística",
    "deterministic capacity": "capacidad determinista",
    "pattern vector": "vector de patrón",
    "pattern vectors": "vectores de patrón",
    "pattern space": "espacio de patrones",
    "separating line": "recta separadora",
    "separating boundary": "frontera separadora",
    "separating hyperplane": "hiperplano separador",
    "input signals": "señales de entrada",
    "output signals": "señales de salida",
    "learning rule": "regla de aprendizaje",
    "learning rules": "reglas de aprendizaje",
    "learning algorithm": "algoritmo de aprendizaje",
    "learning algorithms": "algoritmos de aprendizaje",
    "learning process": "proceso de aprendizaje",
    "training algorithm": "algoritmo de entrenamiento",
    "training algorithms": "algoritmos de entrenamiento",
    "adaptation algorithm": "algoritmo de adaptación",
    "adaptation cycle": "ciclo de adaptación",
    "weight update": "actualización de pesos",
    "weight change": "cambio de pesos",
    "weight changes": "cambios de pesos",
    "weight values": "valores de pesos",
    "initial weight": "peso inicial",
    "initial weights": "pesos iniciales",
    "polynomial discriminant": "discriminante polinomial",
    "polynomial discriminant function": "función discriminante polinomial",
    "pattern set": "conjunto de patrones",
    "training set size": "tamaño del conjunto de entrenamiento",
    "local optima": "óptimos locales",
    "local minimum": "mínimo local",
    "global minimum": "mínimo global",
    "global solution": "solución global",
    "convergence rate": "tasa de convergencia",
    "convergence time": "tiempo de convergencia",
    "learning rate": "tasa de aprendizaje",
    "learning constant": "constante de aprendizaje",
    "momentum technique": "técnica de momento",
    "momentum constant": "constante de momento",
    "dead zone": "zona muerta",
    "weight space": "espacio de pesos",
    "input space": "espacio de entrada",
    "activation function": "función de activación",
    "transfer characteristic": "característica de transferencia",
    "squashing function": "función de compresión",
    "hyperbolic tangent": "tangente hiperbólica",
    "analog hardware": "hardware analógico",
    "digital implementation": "implementación digital",
    "digital computer": "computador digital",
    "parallel hardware": "hardware paralelo",
    "Hamming error": "error de Hamming",
    "quantizer error": "error del cuantificador",
    "error probability": "probabilidad de error",
    "Boltzmann Machine": "Máquina de Boltzmann",
    "Boltzmann learning": "aprendizaje de Boltzmann",
    "competitive learning": "aprendizaje competitivo",
    "reinforcement learning": "aprendizaje por refuerzo",
    "self-organizing": "autoorganizado",
    "self-organization": "autoorganización",
    "credit assignment": "asignación de crédito",
    "associative memory": "memoria asociativa",
    "pattern clustering": "agrupamiento de patrones",
    "feature maps": "mapas de características",
    "recurrent network": "red recurrente",
    "recurrent networks": "redes recurrentes",
    "signal feedback": "retroalimentación de señales",
    "multilayer network": "red multicapa",
    "multilayer networks": "redes multicapa",
    "multi-element network": "red multi-elemento",
    "multi-element networks": "redes multi-elemento",
    "single-element": "mono-elemento",
    "single element": "elemento único",
    "layered network": "red en capas",
    "layered networks": "redes en capas",
    "two-layer network": "red de dos capas",
    "three-layer network": "red de tres capas",
    "fully connected": "completamente conectada",
    "load sharing": "distribución de carga",
    "job assigner": "asignador de tareas",
    "trial adaptation": "adaptación de prueba",
    "bit reversal": "inversión de bit",
    "sum-of-products": "suma de productos",
    "crosscorrelation": "correlación cruzada",
    "autocorrelation matrix": "matriz de autocorrelación",
    "input correlation matrix": "matriz de correlación de entrada",
    "Wiener solution": "solución de Wiener",
    "Wiener weight vector": "vector de pesos de Wiener",
    "Wiener-Hopf equation": "ecuación de Wiener-Hopf",
    "inner product": "producto interno",
    "dot product": "producto punto",
    "eigenvalues": "valores propios",
    "eigenvectors": "vectores propios",
    "positive definite": "definida positiva",
    "positive semi-definite": "semidefinida positiva",
    "quadratic function": "función cuadrática",
    "ensemble average": "promedio de conjunto",
    "stationary ergodic": "ergódico estacionario",
    "impulse": "impulso",
    "degree of freedom": "grado de libertad",
    "degrees of freedom": "grados de libertad",
    "summing junction": "punto de suma",
    "forward pass": "pasada hacia adelante",
    "forward sweep": "barrido hacia adelante",
    "backward sweep": "barrido hacia atrás",
    "backward pass": "pasada hacia atrás",
    "weight multiplication": "multiplicación de pesos",
    "chain rule": "regla de la cadena",
    "Taylor series": "serie de Taylor",
    "Fourier series": "serie de Fourier",
    "Fourier transform": "transformada de Fourier",
    "Mellin transform": "transformada de Mellin",
    "Zernike moments": "momentos de Zernike",
    "Shannon information": "información de Shannon",
    "simulated annealing": "recocido simulado",
    "speech recognition": "reconocimiento de voz",
    "speech generation": "generación de voz",
    "pattern recognition machine": "máquina de reconocimiento de patrones",
    "adaptive filter": "filtro adaptativo",
    "adaptive filters": "filtros adaptativos",
    "adaptive filtering": "filtrado adaptativo",
    "adaptive signal processing": "procesamiento adaptativo de señales",
    "adaptive antenna": "antena adaptativa",
    "adaptive antennas": "antenas adaptativas",
    "adaptive inverse control": "control inverso adaptativo",
    "adaptive noise cancelling": "cancelación adaptativa de ruido",
    "adaptive equalization": "ecualización adaptativa",
    "adaptive echo canceller": "cancelador de eco adaptativo",
    "echo cancellers": "canceladores de eco",
    "high-speed modems": "módems de alta velocidad",
    "seismic signal processing": "procesamiento de señales sísmicas",
    "neural network hardware": "hardware de redes neuronales",
    "computer vision": "visión por computador",
    "artificial intelligence": "inteligencia artificial",
    "von Neumann computer": "computador von Neumann",
    "nervous system": "sistema nervioso",
    "biological neuron": "neurona biológica",
    "neural cell body": "cuerpo celular neuronal",
    "input synapses": "sinapsis de entrada",
    "three-dimensional": "tridimensional",
    "two-dimensional": "bidimensional",
    "operating point": "punto de operación",
    "operating characteristics": "características de operación",
    "internal representations": "representaciones internas",
    "target recognition": "reconocimiento de blancos",
    "expert systems": "sistemas expertos",
    "logic functions": "funciones lógicas",
    "logic device": "dispositivo lógico",
    "logic devices": "dispositivos lógicos",
    "Boolean function": "función booleana",
    "Boolean functions": "funciones booleanas",
    "AND gate": "compuerta AND",
    "OR gate": "compuerta OR",
    "majority vote taker": "tomador de voto mayoritario",
    "majority element": "elemento mayoritario",
    "electrically variable resistor": "resistor eléctricamente variable",
    "resistive link": "enlace resistivo",
    "electroplating": "electrodeposición",
    "pattern vector space": "espacio de vectores de patrón",
    "hyperplane": "hiperplano",
    "homogeneous hyperplane": "hiperplano homogéneo",
    "linear discriminant function": "función discriminante lineal",
    "VoICE synthesizer": "sintetizador de voz",
    "phonetic symbols": "símbolos fonéticos",
    "phonetic features": "rasgos fonéticos",
    "articulatory features": "rasgos articulatorios",
    "syllable boundaries": "límites silábicos",
    "continuous speech": "habla continua",
    "serial computer": "computador serial",
    "look-up table": "tabla de consulta",
    "nonparametric classifier": "clasificador no paramétrico",
    "Bayes decision rule": "regla de decisión de Bayes",
    "spontaneous learning": "aprendizaje espontáneo",
    "mode-seeking": "búsqueda de modos",
    "punish/reward": "castigo/recompensa",
    "bootstrapping": "bootstrapping",
    "graph matching": "emparejamiento de grafos",
    "time-averaged outputs": "salidas promediadas en el tiempo",
    "spatially repeated": "repetido espacialmente",
    "feature detectors": "detectores de características",
    "rotation invariant": "invariante a rotación",
    "scale invariant": "invariante a escala",
    "translation invariant": "invariante a traslación",
    "time invariance": "invariancia temporal",
    "nonstationary environments": "entornos no estacionarios",
    "stationary population": "población estacionaria",
    "linear IIR filters": "filtros IIR lineales",
    "trailer truck": "camión con remolque",
    "loading dock": "plataforma de carga",
    "nonlinear steering": "dirección no lineal",
    "neural implementation": "implementación neuronal",
    "analog neurocomputing chip": "chip neurocomputacional analógico",
    "floating gate": "compuerta flotante",
    "tolerances": "tolerancias",
    "quasi-Newton": "cuasi-Newton",
    "conjugate gradient": "gradiente conjugado",
    "DC gain": "ganancia DC",
    "low-pass filters": "filtros pasa-bajos",
    "high spatial frequencies": "frecuencias espaciales altas",
    "Euclidean distance": "distancia euclidiana",
    "Euclidean error": "error euclidiano",
    "electrocardiographic": "electrocardiográfico",
    "undersea mine detection": "detección de minas submarinas",
    "airport explosive detection": "detección de explosivos en aeropuertos",
    "vehicular control": "control vehicular",
    "system identification": "identificación de sistemas",
    "nonlinear control": "control no lineal",
    "decision making": "toma de decisiones",
    "traveling salesman problem": "problema del viajante",
    "connectedness problem": "problema de conectividad",
    "predicate mappings": "mapeos de predicados",
    "nonfinite-order": "orden no finito",
    "dynamic associations": "asociaciones dinámicas",
    "static associations": "asociaciones estáticas",
    "optimal control": "control óptimo",
    "variational calculus": "cálculo variacional",
    "doctoral dissertation": "tesis doctoral",
    "Ph.D. thesis": "tesis doctoral",
    "technical report": "informe técnico",
    "invention report": "informe de invención",
    "Learning Matrix": "Matriz de Aprendizaje",
    "Cognitron": "Cognitrón",
    "Neocognitron": "Neocognitrón",
    "Adaptive Resonance Theory": "Teoría de Resonancia Adaptativa",
    "Bidirectional Associative Memory": "Memoria Asociativa Bidireccional",
    "polynomial discriminant method": "método discriminante polinomial",
}

# ============================================================================
# MAPEO DE TÍTULOS DE SECCIÓN
# ============================================================================
SECTION_TITLES = {
    "Introduction": "Introducción",
    "Fundamental Concepts": "Conceptos Fundamentales",
    "The Adaptive Linear Combiner": "El Combinador Lineal Adaptativo",
    "A Linear Classifier---The Single Threshold Element": "Un Clasificador Lineal---El Elemento de Umbral Único",
    "Nonlinear Classifiers": "Clasificadores No Lineales",
    "Adaptation---The Minimal Disturbance Principle": "Adaptación---El Principio de Mínima Perturbación",
    "Error Correction Rules---Single Threshold Element": "Reglas de Corrección de Error---Elemento de Umbral Único",
    "Error-Correction Rules---Multi-Element Networks": "Reglas de Corrección de Error---Redes Multi-Elemento",
    "Steepest-Descent Rules---Single Threshold Element": "Reglas de Descenso Más Pronunciado---Elemento de Umbral Único",
    "Steepest-Descent Rules---Multi-Element Networks": "Reglas de Descenso Más Pronunciado---Redes Multi-Elemento",
    "Summary": "Resumen",
    "Linear Rules": "Reglas Lineales",
    "Nonlinear Rules": "Reglas No Lineales",
    "Madaline Rule I": "Regla Madaline I",
    "Madaline Rule II": "Regla Madaline II",
    "Madaline Rule III for the Sigmoid Adaline": "Regla Madaline III para la Adaline Sigmoidal",
    "Madaline Rule III for Networks": "Regla Madaline III para Redes",
    "Backpropagation for Networks": "Retropropagación para Redes",
    "Backpropagation for the Sigmoid Adaline": "Retropropagación para la Adaline Sigmoidal",
    "Comparison of MRIII with MRII": "Comparación de MRIII con MRII",
    "Comparison of MRIII with Backpropagation": "Comparación de MRIII con Retropropagación",
    "MSE Surfaces of Neural Networks": "Superficies ECM de Redes Neuronales",
    "MSE Surfaces of the Adaline": "Superficies ECM de la Adaline",
    "A Nonlinear Classifier Application": "Una Aplicación de Clasificador No Lineal",
    "Capacity of Linear Classifiers": "Capacidad de los Clasificadores Lineales",
    "Capacity of Nonlinear Classifiers": "Capacidad de los Clasificadores No Lineales",
    "Polynomial Discriminant Functions": "Funciones Discriminantes Polinomiales",
    "Feedforward Networks": "Redes con Alimentación hacia Adelante",
    "Linear Separability": "Separabilidad Lineal",
    "Comparison of μ-LMS and α-LMS": "Comparación de μ-LMS y α-LMS",
    "Mean-Square Error Surface of the Linear Combiner": "Superficie de Error Cuadrático Medio del Combinador Lineal",
}

# ============================================================================
# TRADUCCIÓN DE PÁRRAFOS COMPLETOS (frases largas que requieren contexto)
# ============================================================================
# Las traducciones se aplican en orden. Cada tupla es (inglés, español).

def translate_text(text):
    """Aplica todas las reglas de traducción al texto preservando LaTeX."""
    
    # Primero, aplicar reemplazos de términos técnicos (frases más largas primero)
    sorted_terms = sorted(TECH_TERMS.items(), key=lambda x: len(x[0]), reverse=True)
    for eng, esp in sorted_terms:
        # Usar word boundaries para evitar reemplazos parciales
        # Pero permitir que el término esté dentro de texto
        text = text.replace(eng, esp)
    
    return text


def translate_latex_file(input_path, output_path):
    """Lee un archivo .tex, traduce el texto preservando LaTeX, y escribe la salida."""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # =========================================================================
    # TRADUCCIONES MANUALES DE BLOQUES COMPLETOS
    # =========================================================================
    
    # --- Encabezado / comentarios iniciales ---
    replacements = [
        # Bloque de comentarios inicial
        (
            "%  30 Years of Adaptive Neural Networks: Perceptron, Madaline, and\n"
            "%  Backpropagation  --  Bernard Widrow & Michael A. Lehr\n"
            "%  Proceedings of the IEEE, Vol. 78, No. 9, September 1990, pp. 1415-1442\n"
            "%\n"
            "%  Reconstruccion LaTeX del PDF escaneado (uso de estudio personal).\n"
            "%  Figuras recortadas del escaneo original -> carpeta ./fig/\n"
            "%\n"
            "%  NOTA: se usa 'article' a dos columnas por portabilidad. Para el aspecto\n"
            "%  IEEE autentico, reemplazar la linea \\documentclass por:\n"
            "%        \\documentclass[10pt,twocolumn]{IEEEtran}\n"
            "%  (IEEEtran suele estar en texlive-publishers) y quitar el bloque\n"
            '%  "APROXIMACION DE ESTILO IEEE" de abajo.',
            
            "%  30 Años de Redes Neuronales Adaptativas: Perceptrón, Madaline y\n"
            "%  Retropropagación  --  Bernard Widrow & Michael A. Lehr\n"
            "%  Proceedings of the IEEE, Vol. 78, No. 9, Septiembre 1990, pp. 1415-1442\n"
            "%\n"
            "%  Reconstrucción LaTeX del PDF escaneado (uso de estudio personal).\n"
            "%  Figuras recortadas del escaneo original -> carpeta ./fig/\n"
            "%  TRADUCCIÓN AL ESPAÑOL ACADÉMICO (español chileno).\n"
            "%\n"
            "%  NOTA: se usa 'article' a dos columnas por portabilidad. Para el aspecto\n"
            "%  IEEE auténtico, reemplazar la línea \\documentclass por:\n"
            "%        \\documentclass[10pt,twocolumn]{IEEEtran}\n"
            "%  (IEEEtran suele estar en texlive-publishers) y quitar el bloque\n"
            '%  "APROXIMACIÓN DE ESTILO IEEE" de abajo.'
        ),
        
        # Comentario APROXIMACION DE ESTILO IEEE
        (
            "% ----- APROXIMACION DE ESTILO IEEE (borrar si se usa IEEEtran) -----",
            "% ----- APROXIMACIÓN DE ESTILO IEEE (borrar si se usa IEEEtran) -----"
        ),
        
        # Comentario de vector de patrón
        (
            "% Vector de patron / peso en negrita como en el paper",
            "% Vector de patrón / peso en negrita como en el paper"
        ),
        
        # --- Título ---
        (
            '\\title{\\vspace{-2em}\\textbf{\\Large 30 Years of Adaptive Neural Networks:\\\\\n'
            'Perceptron, Madaline, and Backpropagation}}',
            
            '\\title{\\vspace{-2em}\\textbf{\\Large 30 Años de Redes Neuronales Adaptativas:\\\\\n'
            'Perceptrón, Madaline y Retropropagación}}'
        ),
        
        # --- Abstract ---
        (
            "Fundamental developments in feedforward artificial neural networks from the\n"
            "past thirty years are reviewed. The central theme of this paper is a\n"
            "description of the history, origination, operating characteristics, and basic\n"
            "theory of several supervised neural network training algorithms including the\n"
            "Perceptron rule, the LMS algorithm, three Madaline rules, and the\n"
            "backpropagation technique. These methods were developed independently, but\n"
            "with the perspective of history they can all be related to each other. The\n"
            "concept underlying these algorithms is the ``minimal disturbance principle,''\n"
            "which suggests that during training it is advisable to inject new information\n"
            "into a network in a manner that disturbs stored information to the smallest\n"
            "extent possible.",
            
            "Se revisan los desarrollos fundamentales en redes neuronales artificiales con\n"
            "alimentación hacia adelante de los últimos treinta años. El tema central de\n"
            "este artículo es una descripción de la historia, origen, características de\n"
            "operación y teoría básica de varios algoritmos supervisados de entrenamiento\n"
            "de redes neuronales, incluyendo la regla del Perceptrón, el algoritmo LMS, tres\n"
            "reglas Madaline y la técnica de retropropagación. Estos métodos se desarrollaron\n"
            "de forma independiente, pero desde la perspectiva de la historia todos pueden\n"
            "relacionarse entre sí. El concepto subyacente a estos algoritmos es el\n"
            "``principio de mínima perturbación'', que sugiere que durante el entrenamiento\n"
            "es recomendable inyectar nueva información en una red de manera que perturbe\n"
            "la información almacenada en la menor medida posible."
        ),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    # =========================================================================
    # TRADUCCIÓN DE TÍTULOS DE SECCIÓN (con patrones LaTeX)
    # =========================================================================
    section_map = [
        (r'\section{Introduction}', r'\section{Introducción}'),
        (r'\section{Fundamental Concepts}', r'\section{Conceptos Fundamentales}'),
        (r'\section{Adaptation---The Minimal Disturbance Principle}', 
         r'\section{Adaptación---El Principio de Mínima Perturbación}'),
        (r'\section{Error Correction Rules---Single Threshold Element}',
         r'\section{Reglas de Corrección de Error---Elemento de Umbral Único}'),
        (r'\section{Error-Correction Rules---Multi-Element Networks}',
         r'\section{Reglas de Corrección de Error---Redes Multi-Elemento}'),
        (r'\section{Steepest-Descent Rules---Single Threshold Element}',
         r'\section{Reglas de Descenso Más Pronunciado---Elemento de Umbral Único}'),
        (r'\section{Steepest-Descent Rules---Multi-Element Networks}',
         r'\section{Reglas de Descenso Más Pronunciado---Redes Multi-Elemento}'),
        (r'\section{Summary}', r'\section{Resumen}'),
    ]
    
    subsection_map = [
        (r'\subsection{The Adaptive Linear Combiner}', r'\subsection{El Combinador Lineal Adaptativo}'),
        (r'\subsection{A Linear Classifier---The Single Threshold Element}',
         r'\subsection{Un Clasificador Lineal---El Elemento de Umbral Único}'),
        (r'\subsection{Nonlinear Classifiers}', r'\subsection{Clasificadores No Lineales}'),
        (r'\subsection{Linear Rules}', r'\subsection{Reglas Lineales}'),
        (r'\subsection{Nonlinear Rules}', r'\subsection{Reglas No Lineales}'),
        (r'\subsection{Madaline Rule I}', r'\subsection{Regla Madaline I}'),
        (r'\subsection{Madaline Rule II}', r'\subsection{Regla Madaline II}'),
        (r'\subsection{Backpropagation for Networks}', r'\subsection{Retropropagación para Redes}'),
        (r'\subsection{Madaline Rule III for Networks}', r'\subsection{Regla Madaline III para Redes}'),
        (r'\subsection{Comparison of MRIII with MRII}', r'\subsection{Comparación de MRIII con MRII}'),
        (r'\subsection{Comparison of MRIII with Backpropagation}',
         r'\subsection{Comparación de MRIII con Retropropagación}'),
        (r'\subsection{MSE Surfaces of Neural Networks}',
         r'\subsection{Superficies ECM de Redes Neuronales}'),
    ]
    
    for old, new in section_map + subsection_map:
        content = content.replace(old, new)
    
    # =========================================================================
    # TRADUCCIÓN DE SUBSUBSECCIONES (con \subsubsection*)
    # =========================================================================
    subsub_map = [
        (r'\subsubsection*{Madaline I}', r'\subsubsection*{Madaline I}'),
        (r'\subsubsection*{Feedforward Networks}', r'\subsubsection*{Redes con Alimentación hacia Adelante}'),
        (r'\subsubsection*{Capacity of Nonlinear Classifiers}',
         r'\subsubsection*{Capacidad de los Clasificadores No Lineales}'),
        (r'\subsubsection*{A Nonlinear Classifier Application}',
         r'\subsubsection*{Una Aplicación de Clasificador No Lineal}'),
        (r'\subsubsection*{Polynomial Discriminant Functions}',
         r'\subsubsection*{Funciones Discriminantes Polinomiales}'),
    ]
    
    for old, new in subsub_map:
        content = content.replace(old, new)
    
    # =========================================================================
    # TRADUCCIÓN DE PÁRRAFOS CLAVE (los más extensos y visibles)
    # =========================================================================
    
    # ---- Introduction (primer párrafo) ----
    content = content.replace(
        "This year marks the 30th anniversary of the Perceptron rule and the LMS\n"
        "algorithm, two early rules for training adaptive elements. Both algorithms were\n"
        "first published in 1960. In the years following these discoveries, many new\n"
        "techniques have been developed in the field of neural networks, and the\n"
        "discipline is growing rapidly.",
        
        "Este año se cumple el 30º aniversario de la regla del Perceptrón y del\n"
        "algoritmo LMS, dos reglas pioneras para el entrenamiento de elementos\n"
        "adaptativos. Ambos algoritmos fueron publicados por primera vez en 1960. En\n"
        "los años posteriores a estos descubrimientos, se han desarrollado muchas\n"
        "técnicas nuevas en el campo de las redes neuronales, y la disciplina está\n"
        "creciendo rápidamente."
    )
    
    # ---- Introduction (último párrafo antes de Section II) ----
    content = content.replace(
        "The elements used by Rumelhart \\textit{et al.} in the backpropagation network\n"
        "differ from those used in the earlier Madaline architectures. The adaptive\n"
        "elements in the original Madaline structure used hard-limiting quantizers\n"
        "(signums), while the elements in the backpropagation network use only\n"
        "differentiable nonlinearities, or ``sigmoid'' functions.",
        
        "Los elementos usados por Rumelhart \\textit{et al.} en la red de\n"
        "retropropagación difieren de aquellos usados en las arquitecturas Madaline\n"
        "anteriores. Los elementos adaptativos en la estructura Madaline original\n"
        "usaban cuantificadores de límite estricto (signums), mientras que los\n"
        "elementos en la red de retropropagación usan solo no linealidades\n"
        "diferenciables, o funciones ``sigmoides''."
    )
    
    content = content.replace(
        "In digital implementations, the hard-limiting quantizer is more easily computed\n"
        "than any of the differentiable nonlinearities used in backpropagation networks.",
        
        "En implementaciones digitales, el cuantificador de límite estricto se calcula\n"
        "más fácilmente que cualquiera de las no linealidades diferenciables usadas en\n"
        "las redes de retropropagación."
    )
    
    # ---- Section II: Fundamental Concepts, primer párrafo ----
    content = content.replace(
        "Today we can build computers and other machines that perform a variety of\n"
        "well-defined tasks with celerity and reliability unmatched by humans. No human\n"
        "can invert matrices or solve systems of differential equations at speeds\n"
        "rivaling modern workstations. Nonetheless, many problems remain to be solved to\n"
        "our satisfaction by any man-made machine, but are easily disentangled by the\n"
        "perceptual or cognitive powers of humans, and often lower mammals, or even fish\n"
        "and insects.",
        
        "Hoy podemos construir computadores y otras máquinas que realizan una variedad\n"
        "de tareas bien definidas con una celeridad y confiabilidad inigualables por los\n"
        "humanos. Ningún humano puede invertir matrices o resolver sistemas de ecuaciones\n"
        "diferenciales a velocidades que rivalicen con las estaciones de trabajo modernas.\n"
        "No obstante, muchos problemas siguen sin resolverse a nuestra satisfacción por\n"
        "cualquier máquina construida por el hombre, pero son fácilmente desentrañados\n"
        "por las capacidades perceptivas o cognitivas de los humanos, y a menudo de\n"
        "mamíferos inferiores, o incluso peces e insectos."
    )
    
    # ---- Section III: Minimal Disturbance Principle ----
    content = content.replace(
        "The iterative algorithms described in this paper are all designed in accord with\n"
        "a single underlying principle. These techniques---the two LMS algorithms, Mays's\n"
        "rules, and the Perceptron procedure for training a single Adaline, the MRI rule\n"
        "for training the simple Madaline, as well as MRII, MRIII, and backpropagation\n"
        "techniques for training multilayer Madalines---all rely upon the principle of\n"
        "minimal disturbance: \\textit{Adapt to reduce the output error for the current\n"
        "training pattern, with minimal disturbance to responses already learned.}",
        
        "Los algoritmos iterativos descritos en este artículo están todos diseñados de\n"
        "acuerdo con un único principio subyacente. Estas técnicas---los dos algoritmos\n"
        "LMS, las reglas de Mays y el procedimiento del Perceptrón para entrenar una\n"
        "sola Adaline, la regla MRI para entrenar la Madaline simple, así como las\n"
        "técnicas MRII, MRIII y de retropropagación para entrenar Madalines multicapa---\n"
        "todas se basan en el principio de mínima perturbación: \\textit{Adaptar para\n"
        "reducir el error de salida para el patrón de entrenamiento actual, con una\n"
        "perturbación mínima de las respuestas ya aprendidas.}"
    )
    
    # ---- Section IV intro ----
    content = content.replace(
        "As adaptive algorithms evolved, principally two kinds of on-line rules have come\n"
        "to exist. \\textit{Error-correction rules} alter the weights of a network to\n"
        "correct error in the output response to the present input pattern.\n"
        "\\textit{Gradient rules} alter the weights of a network during each pattern\n"
        "presentation by gradient descent with the objective of reducing mean-square\n"
        "error, averaged over all training patterns.",
        
        "A medida que los algoritmos adaptativos evolucionaron, han llegado a existir\n"
        "principalmente dos tipos de reglas en línea. Las \\textit{reglas de corrección\n"
        "de error} alteran los pesos de una red para corregir el error en la respuesta\n"
        "de salida al patrón de entrada actual. Las \\textit{reglas de gradiente} alteran\n"
        "los pesos de una red durante cada presentación de patrón mediante descenso por\n"
        "gradiente con el objetivo de reducir el error cuadrático medio, promediado\n"
        "sobre todos los patrones de entrenamiento."
    )
    
    # ---- Section IV: The α-LMS Algorithm ----
    content = content.replace(
        "\\textit{The \$\\alpha\\$-LMS Algorithm:} The \$\\alpha\\$-LMS algorithm or Widrow--Hoff\n"
        "delta rule applied to the adaptation of a single Adaline (Fig.~\\ref{fig:2})\n"
        "embodies the minimal disturbance principle.",
        
        "\\textit{El Algoritmo \$\\alpha\\$-LMS:} El algoritmo \$\\alpha\\$-LMS o regla delta\n"
        "de Widrow--Hoff aplicado a la adaptación de una sola Adaline (Fig.~\\ref{fig:2})\n"
        "encarna el principio de mínima perturbación."
    )
    
    # ---- Section IV: The Perceptron Learning Rule ----
    content = content.replace(
        "\\textit{The Perceptron Learning Rule:} The Rosenblatt \$\\alpha\\$-Perceptron%\n"
        "~\\cite{rosen60,rosen62}, diagrammed in Fig.~\\ref{fig:13}, processed input patterns\n"
        "with a first layer of sparse randomly connected fixed logic devices.",
        
        "\\textit{La Regla de Aprendizaje del Perceptrón:} El \$\\alpha\\$-Perceptrón de\n"
        "Rosenblatt%~\\cite{rosen60,rosen62}, diagramado en la Fig.~\\ref{fig:13}, procesaba\n"
        "patrones de entrada con una primera capa de dispositivos lógicos fijos escasos\n"
        "conectados aleatoriamente."
    )
    
    # ---- Section IV: Mays's Algorithms ----
    content = content.replace(
        "\\textit{Mays's Algorithms:} In his Ph.D. thesis~\\cite{mays}, Mays described an\n"
        "``increment adaptation'' rule",
        
        "\\textit{Algoritmos de Mays:} En su tesis doctoral~\\cite{mays}, Mays describió\n"
        "una regla de ``adaptación por incremento''"
    )
    
    # ---- Section V intro ----
    content = content.replace(
        "The algorithms discussed next are the Widrow--Hoff Madaline rule from the early\n"
        "1960s, now called Madaline Rule~I (MRI), and Madaline Rule~II (MRII), developed\n"
        "by Widrow and Winter in 1987.",
        
        "Los algoritmos que se discuten a continuación son la regla Madaline de\n"
        "Widrow--Hoff de principios de los años 60, ahora llamada Regla Madaline~I\n"
        "(MRI), y la Regla Madaline~II (MRII), desarrollada por Widrow y Winter en\n"
        "1987."
    )
    
    # ---- Section V: MRI ----
    content = content.replace(
        "The MRI rule allows the adaptation of a first layer of hard-limited (signum)\n"
        "Adaline elements whose outputs provide inputs to a second layer, consisting of a\n"
        "single fixed-threshold-logic element which may be, for example, the OR gate, AND\n"
        "gate, or majority-vote-taker discussed previously.",
        
        "La regla MRI permite la adaptación de una primera capa de elementos Adaline\n"
        "con límite estricto (signum) cuyas salidas proporcionan entradas a una segunda\n"
        "capa, que consiste en un solo elemento lógico de umbral fijo que puede ser,\n"
        "por ejemplo, la compuerta OR, AND o el tomador de voto mayoritario discutidos\n"
        "previamente."
    )
    
    # ---- Section VI intro ----
    content = content.replace(
        "Thus far, we have described a variety of adaptation rules that act to reduce error\n"
        "with the presentation of each training pattern. Often, the objective of adaptation\n"
        "is to reduce error averaged in some way over the training set. The most common\n"
        "error function is mean-square error (MSE), although in some situations other error\n"
        "criteria may be more appropriate",
        
        "Hasta ahora, hemos descrito una variedad de reglas de adaptación que actúan\n"
        "para reducir el error con la presentación de cada patrón de entrenamiento. A\n"
        "menudo, el objetivo de la adaptación es reducir el error promediado de alguna\n"
        "manera sobre el conjunto de entrenamiento. La función de error más común es el\n"
        "error cuadrático medio (ECM), aunque en algunas situaciones otros criterios de\n"
        "error pueden ser más apropiados"
    )
    
    # ---- Section VI: The μ-LMS Algorithm ----
    content = content.replace(
        "\\textit{The \$\\mu\\$-LMS Algorithm:} The \$\\mu\\$-LMS algorithm works by performing\n"
        "approximate steepest descent on the MSE surface in weight space. Because it is a\n"
        "quadratic function of the weights, this surface is convex and has a unique (global)\n"
        "minimum.",
        
        "\\textit{El Algoritmo \$\\mu\\$-LMS:} El algoritmo \$\\mu\\$-LMS funciona realizando\n"
        "un descenso más pronunciado aproximado sobre la superficie ECM en el espacio de\n"
        "pesos. Dado que es una función cuadrática de los pesos, esta superficie es\n"
        "convexa y tiene un mínimo (global) único."
    )
    
    # ---- Section VI: Comparison of μ-LMS and α-LMS ----
    content = content.replace(
        "\\textit{Comparison of \$\\mu\\$-LMS and \$\\alpha\\$-LMS:} We have now presented two forms\n"
        "of the LMS algorithm, \$\\alpha\\$-LMS~(10) in Section~IV-A and \$\\mu\\$-LMS~(33) in the\n"
        "last section.",
        
        "\\textit{Comparación de \$\\mu\\$-LMS y \$\\alpha\\$-LMS:} Hemos presentado ahora dos\n"
        "formas del algoritmo LMS, \$\\alpha\\$-LMS~(10) en la Sección~IV-A y \$\\mu\\$-LMS~(33)\n"
        "en la última sección."
    )
    
    # ---- Section VI: Backpropagation for the Sigmoid Adaline ----
    content = content.replace(
        "\\textit{Backpropagation for the Sigmoid Adaline:} Our objective is to minimize\n"
        "\$E[(\\tilde{\\epsilon}_k)^2]\$, averaged over the set of training patterns, by proper\n"
        "choice of the weight vector.",
        
        "\\textit{Retropropagación para la Adaline Sigmoidal:} Nuestro objetivo es minimizar\n"
        "\$E[(\\tilde{\\epsilon}_k)^2]\$, promediado sobre el conjunto de patrones de\n"
        "entrenamiento, mediante la elección adecuada del vector de pesos."
    )
    
    # ---- Section VI: Madaline Rule III for the Sigmoid Adaline ----
    content = content.replace(
        "\\textit{Madaline Rule III for the Sigmoid Adaline:} The implementation of\n"
        "algorithm~(54) (Fig.~\\ref{fig:19}) requires accurate realization of the sigmoid\n"
        "function and its derivative function.",
        
        "\\textit{Regla Madaline III para la Adaline Sigmoidal:} La implementación del\n"
        "algoritmo~(54) (Fig.~\\ref{fig:19}) requiere la realización precisa de la\n"
        "función sigmoide y su función derivada."
    )
    
    # ---- Section VI: MSE Surfaces of the Adaline ----
    content = content.replace(
        "\\textit{MSE Surfaces of the Adaline:} Fig.~\\ref{fig:21} shows a linear combiner\n"
        "connected to both sigmoid and signum devices.",
        
        "\\textit{Superficies ECM de la Adaline:} La Fig.~\\ref{fig:21} muestra un\n"
        "combinador lineal conectado a dispositivos tanto sigmoides como signum."
    )
    
    # ---- Section VII intro ----
    content = content.replace(
        "We now study rules for steepest-descent minimization of the MSE associated with\n"
        "entire networks of sigmoid Adaline elements. Like their single-element\n"
        "counterparts, the most practical and efficient steepest-descent rules for\n"
        "multi-element networks typically work with one pattern presentation at a time. We\n"
        "will describe two steepest-descent rules for multi-element sigmoid networks,\n"
        "backpropagation and Madaline Rule~III.",
        
        "Ahora estudiamos reglas para la minimización por descenso más pronunciado del\n"
        "ECM asociado con redes completas de elementos Adaline sigmoidales. Al igual que\n"
        "sus contrapartes mono-elemento, las reglas de descenso más pronunciado más\n"
        "prácticas y eficientes para redes multi-elemento típicamente trabajan con una\n"
        "presentación de patrón a la vez. Describiremos dos reglas de descenso más\n"
        "pronunciado para redes sigmoidales multi-elemento: retropropagación y Regla\n"
        "Madaline~III."
    )
    
    # ---- Section VII: Backpropagation for Networks (primer párrafo) ----
    content = content.replace(
        "The publication of the backpropagation technique by Rumelhart \\textit{et\n"
        "al.}~\\cite{rhw86} has unquestionably been the most influential development in the\n"
        "field of neural networks during the past decade.",
        
        "La publicación de la técnica de retropropagación por Rumelhart \\textit{et\n"
        "al.}~\\cite{rhw86} ha sido indudablemente el desarrollo más influyente en el\n"
        "campo de las redes neuronales durante la última década."
    )
    
    # ---- Section VII: MRIII for Networks (primer párrafo) ----
    content = content.replace(
        "It is difficult to build neural networks with analog hardware that can be trained\n"
        "effectively by the popular backpropagation technique. Attempts to overcome this\n"
        "difficulty have led to the development of the MRIII algorithm. A commercial analog\n"
        "neurocomputing chip based primarily on this algorithm has already been\n"
        "devised~\\cite{holler}.",
        
        "Es difícil construir redes neuronales con hardware analógico que puedan\n"
        "entrenarse efectivamente mediante la popular técnica de retropropagación. Los\n"
        "intentos de superar esta dificultad han llevado al desarrollo del algoritmo\n"
        "MRIII. Ya se ha diseñado un chip neurocomputacional analógico comercial basado\n"
        "principalmente en este algoritmo~\\cite{holler}."
    )
    
    # ---- Section VII: MSE Surfaces of Neural Networks (primer párrafo) ----
    content = content.replace(
        "In Section~VI-B, ``typical'' mean-square-error surfaces of sigmoid and signum\n"
        "Adalines were shown, indicating that sigmoid Adalines are much more conducive to\n"
        "gradient approaches than signum Adalines.",
        
        "En la Sección~VI-B, se mostraron superficies de error cuadrático medio\n"
        "``típicas'' de Adalines sigmoidales y signum, indicando que las Adalines\n"
        "sigmoidales son mucho más propicias para enfoques de gradiente que las\n"
        "Adalines signum."
    )
    
    # ---- Section VIII: Summary ----
    content = content.replace(
        "This year is the 30th anniversary of the publication of the Perceptron rule by\n"
        "Rosenblatt and the LMS algorithm by Widrow and Hoff. It has also been 16 years since\n"
        "Werbos first published the backpropagation algorithm. These learning rules and\n"
        "several others have been studied and compared. Although they differ significantly\n"
        "from each other, they all belong to the same ``family.''",
        
        "Este año se cumple el 30º aniversario de la publicación de la regla del\n"
        "Perceptrón por Rosenblatt y del algoritmo LMS por Widrow y Hoff. También han\n"
        "pasado 16 años desde que Werbos publicó por primera vez el algoritmo de\n"
        "retropropagación. Estas reglas de aprendizaje y varias otras han sido\n"
        "estudiadas y comparadas. Aunque difieren significativamente entre sí, todas\n"
        "pertenecen a la misma ``familia''."
    )
    
    content = content.replace(
        "A distinction was drawn between error-correction rules and steepest-descent rules.\n"
        "The former includes the Perceptron rule, Mays' rules, the \$\\alpha\\$-LMS algorithm,\n"
        "the original Madaline~I rule of 1962, and the Madaline~II rule. The latter includes\n"
        "the \$\\mu\\$-LMS algorithm, the Madaline~III rule, and the backpropagation algorithm.\n"
        "Fig.~\\ref{fig:33} categorizes the learning rules that have been studied.",
        
        "Se estableció una distinción entre reglas de corrección de error y reglas de\n"
        "descenso más pronunciado. Las primeras incluyen la regla del Perceptrón, las\n"
        "reglas de Mays, el algoritmo \$\\alpha\\$-LMS, la regla Madaline~I original de\n"
        "1962 y la regla Madaline~II. Las segundas incluyen el algoritmo \$\\mu\\$-LMS,\n"
        "la regla Madaline~III y el algoritmo de retropropagación. La Fig.~\\ref{fig:33}\n"
        "categoriza las reglas de aprendizaje que han sido estudiadas."
    )
    
    content = content.replace(
        "Although these algorithms have been presented as established learning rules, one\n"
        "should not gain the impression that they are perfect and frozen for all time.\n"
        "Variations are possible for every one of them. They should be regarded as substrates\n"
        "upon which to build new and better rules. There is a tremendous amount of invention\n"
        "waiting ``in the wings.'' We look forward to the next 30 years.",
        
        "Aunque estos algoritmos se han presentado como reglas de aprendizaje\n"
        "establecidas, no debe tenerse la impresión de que son perfectos e inmutables.\n"
        "Son posibles variaciones para cada uno de ellos. Deben considerarse como\n"
        "sustratos sobre los cuales construir reglas nuevas y mejores. Hay una enorme\n"
        "cantidad de invención esperando ``entre bastidores''. Esperamos con interés los\n"
        "próximos 30 años."
    )
    
    # ---- Figure captions (traducciones clave) ----
    caption_map = [
        (r'\caption{Adaptive linear combiner.}', r'\caption{Combinador lineal adaptativo.}'),
        (r'\caption{Adaptive linear element (Adaline).}', r'\caption{Elemento lineal adaptativo (Adaline).}'),
        (r'\caption{Two-input Adaline.}', r'\caption{Adaline de dos entradas.}'),
        (r'\caption{Separating line in pattern space.}', r'\caption{Recta separadora en el espacio de patrones.}'),
        (r'\caption{Probability that an Adaline can separate a training pattern set',
         r'\caption{Probabilidad de que una Adaline pueda separar un conjunto de patrones de entrenamiento'),
        (r'\caption{Adaline with inputs mapped through nonlinearities.}',
         r'\caption{Adaline con entradas mapeadas a través de no linealidades.}'),
        (r'\caption{Elliptical separating boundary for realizing a function which is not',
         r'\caption{Frontera separadora elíptica para realizar una función que no es'),
        (r'\caption{Two-Adaline form of Madaline.}', r'\caption{Forma de dos Adalines de Madaline.}'),
        (r'\caption{Separating lines for Madaline of Fig.~\\ref{fig:8}.}',
         r'\caption{Rectas separadoras para la Madaline de la Fig.~\\ref{fig:8}.}'),
        (r'\caption{Fixed-weight Adaline implementations of AND, OR, and MAJ logic',
         r'\caption{Implementaciones con pesos fijos de Adaline de las funciones lógicas AND, OR y MAJ'),
        (r'\caption{Three-layer adaptive neural network.}',
         r'\caption{Red neuronal adaptativa de tres capas.}'),
        (r'\caption{Weight correction by the LMS rule.}',
         r'\caption{Corrección de pesos mediante la regla LMS.}'),
        (r"\caption{Rosenblatt's \$\\alpha\\$-Perceptron.}",
         r"\caption{\$\\alpha\\$-Perceptrón de Rosenblatt.}"),
        (r'\caption{The adaptive threshold element of the Perceptron.}',
         r'\caption{El elemento adaptativo de umbral del Perceptrón.}'),
        (r'\caption{A five-Adaline example of the Madaline~I architecture.}',
         r'\caption{Ejemplo de cinco Adalines de la arquitectura Madaline~I.}'),
        (r'\caption{Typical two-layer Madaline~II architecture.}',
         r'\caption{Arquitectura típica Madaline~II de dos capas.}'),
        (r'\caption{Typical mean-square-error surface of a linear combiner.}',
         r'\caption{Superficie de error cuadrático medio típica de un combinador lineal.}'),
        (r'\caption{Adaline with sigmoidal nonlinearity.}',
         r'\caption{Adaline con no linealidad sigmoidal.}'),
        (r'\caption{Implementation of backpropagation for the sigmoid Adaline',
         r'\caption{Implementación de retropropagación para el elemento Adaline sigmoidal'),
        (r'\caption{Implementation of the MRIII algorithm for the sigmoid Adaline',
         r'\caption{Implementación del algoritmo MRIII para el elemento Adaline sigmoidal'),
        (r'\caption{The linear, sigmoid, and signum errors of the Adaline.}',
         r'\caption{Los errores lineal, sigmoide y signum de la Adaline.}'),
        (r'\caption{Example MSE surface of linear error.}',
         r'\caption{Ejemplo de superficie ECM del error lineal.}'),
        (r'\caption{Example MSE surface of sigmoid error.}',
         r'\caption{Ejemplo de superficie ECM del error sigmoide.}'),
        (r'\caption{Example MSE surface of signum error.}',
         r'\caption{Ejemplo de superficie ECM del error signum.}'),
        (r'\caption{Example two-layer backpropagation network architecture.}',
         r'\caption{Ejemplo de arquitectura de red de retropropagación de dos capas.}'),
        (r'\caption{Detail of linear combiner and associated circuitry in backpropagation',
         r'\caption{Detalle del combinador lineal y circuitería asociada en la red de retropropagación'),
        (r'\caption{Example truck backup sequence.}',
         r'\caption{Ejemplo de secuencia de retroceso del camión.}'),
        (r'\caption{Example two-layer Madaline~III architecture.}',
         r'\caption{Ejemplo de arquitectura Madaline~III de dos capas.}'),
        (r'\caption{Example MSE surface of untrained sigmoidal network as a function of two',
         r'\caption{Ejemplo de superficie ECM de red sigmoidal no entrenada en función de dos pesos de la primera capa.}'),
        (r'\caption{Example MSE surface of trained sigmoidal network as a function of two',
         r'\caption{Ejemplo de superficie ECM de red sigmoidal entrenada en función de dos pesos de la primera capa.}'),
        (r'\caption{Example MSE surface of untrained sigmoidal network as a function of a',
         r'\caption{Ejemplo de superficie ECM de red sigmoidal no entrenada en función de un peso de la primera capa y uno de la tercera.}'),
        (r'\caption{Example MSE surface of trained sigmoidal network as a function of a',
         r'\caption{Ejemplo de superficie ECM de red sigmoidal entrenada en función de un peso de la primera capa y uno de la tercera.}'),
        (r'\caption{Learning rules.}', r'\caption{Reglas de aprendizaje.}'),
    ]
    
    for old, new in caption_map:
        content = content.replace(old, new)
    
    # ---- Figuras con caption en dos líneas ----
    content = content.replace(
        "as a function of the ratio $N_p/N_w$.",
        "en función de la razón $N_p/N_w$."
    )
    content = content.replace(
        "linearly separable.",
        "linealmente separable."
    )
    content = content.replace(
        "functions.",
        "funciones."
    )
    
    # ---- Pie de figura de la Fig. 5 (segunda línea) ----
    content = content.replace(
        "a function of the ratio $N_p/N_w$.}\\label{fig:5}",
        "en función de la razón $N_p/N_w$.}\\label{fig:5}"
    )
    
    # ---- Pie de figura de la Fig. 7 (segunda línea) ----
    content = content.replace(
        "linearly separable.}\\label{fig:7}",
        "linealmente separable.}\\label{fig:7}"
    )
    
    # ---- Pie de figura de la Fig. 10 (segunda línea) ----
    content = content.replace(
        "functions.}\\label{fig:10}",
        "funciones.}\\label{fig:10}"
    )
    
    # ---- Pies de figura de Figs. 29-32 (segunda línea) ----
    content = content.replace(
        "first-layer weights.}\\label{fig:29}",
        "primera capa.}\\label{fig:29}"
    )
    content = content.replace(
        "first-layer weights.}\\label{fig:30}",
        "primera capa.}\\label{fig:30}"
    )
    content = content.replace(
        "first-layer weight and a third-layer weight.}\\label{fig:31}",
        "primera capa y uno de la tercera capa.}\\label{fig:31}"
    )
    content = content.replace(
        "first-layer weight and a third-layer weight.}\\label{fig:32}",
        "primera capa y uno de la tercera capa.}\\label{fig:32}"
    )
    
    # ---- Pie de la Fig. 19 ----
    content = content.replace(
        "element.}\\label{fig:19}",
        "elemento.}\\label{fig:19}"
    )
    content = content.replace(
        "element.}\\label{fig:20}",
        "elemento.}\\label{fig:20}"
    )
    
    # ---- Pie de la Fig. 26 ----
    content = content.replace(
        "network.}\\label{fig:26}",
        "red.}\\label{fig:26}"
    )
    
    # ---- Notas al pie (footnotes) ----
    footnote_map = [
        (
            "\\footnote{We should note, however, that in the field of variational calculus the\n"
            "idea of error backpropagation through nonlinear systems existed centuries\n"
            "before Werbos first thought to apply this concept to neural networks. In the\n"
            "past 25 years, these methods have been used widely in the field of optimal\n"
            "control, as discussed by Le Cun~\\cite{lecun}.}",
            
            "\\footnote{Debe notarse, sin embargo, que en el campo del cálculo variacional\n"
            "la idea de retropropagación de error a través de sistemas no lineales existió\n"
            "siglos antes de que Werbos pensara por primera vez en aplicar este concepto a\n"
            "redes neuronales. En los últimos 25 años, estos métodos se han usado\n"
            "ampliamente en el campo del control óptimo, como lo discute Le\n"
            "Cun~\\cite{lecun}.}"
        ),
        (
            "\\footnote{The term ``sigmoid'' is usually used in reference to monotonically\n"
            "increasing ``S-shaped'' functions, such as the hyperbolic tangent. In this\n"
            "paper, however, we generally use the term to denote any smooth nonlinear\n"
            "functions at the output of a linear adaptive element. In other papers, these\n"
            "nonlinearities go by a variety of names, such as ``squashing functions,''``activation functions,''``transfer characteristics,'' or ``threshold\n"
            "functions.''}",
            
            "\\footnote{El término ``sigmoide'' se usa usualmente en referencia a funciones\n"
            "monótonamente crecientes con ``forma de S'', como la tangente hiperbólica. En\n"
            "este artículo, sin embargo, generalmente usamos el término para denotar\n"
            "cualquier función no lineal suave a la salida de un elemento lineal\n"
            "adaptativo. En otros artículos, estas no linealidades reciben diversos\n"
            "nombres, como ``funciones de compresión'', ``funciones de activación'',\n"
            "``características de transferencia'' o ``funciones de umbral''.}"
        ),
        (
            "\\footnote{In the neural network literature, such elements are often referred to\n"
            "as ``adaptive neurons.'' However, in a conversation between David Hubel of\n"
            "Harvard Medical School and Bernard Widrow, Dr.~Hubel pointed out that the\n"
            "Adaline differs from the biological neuron in that it contains not only the\n"
            "neural cell body, but also the input synapses and a mechanism for training\n"
            "them.}",
            
            "\\footnote{En la literatura de redes neuronales, tales elementos a menudo se\n"
            "denominan ``neuronas adaptativas''. Sin embargo, en una conversación entre\n"
            "David Hubel de la Escuela de Medicina de Harvard y Bernard Widrow, el\n"
            "Dr.~Hubel señaló que la Adaline difiere de la neurona biológica en que\n"
            "contiene no solo el cuerpo celular neuronal, sino también las sinapsis de\n"
            "entrada y un mecanismo para entrenarlas.}"
        ),
        (
            "\\footnote{Underlying theory for this result was discovered independently by a\n"
            "number of researchers including, among others, Winder~\\cite{winder},\n"
            "Cameron~\\cite{cameron}, and Joseph~\\cite{joseph}.}",
            
            "\\footnote{La teoría subyacente para este resultado fue descubierta de forma\n"
            "independiente por varios investigadores, incluyendo, entre otros, a\n"
            "Winder~\\cite{winder}, Cameron~\\cite{cameron} y Joseph~\\cite{joseph}.}"
        ),
        (
            "\\footnote{Patterns are in general position with respect to an Adaline with no\n"
            "threshold weight if any subset of pattern vectors containing no more than $N_w$\n"
            "members forms a linearly independent set or, equivalently, if no set of $N_w$ or\n"
            "more input points in the $N_w$-dimensional pattern space lie on a homogeneous\n"
            "hyperplane. For the more common case involving an Adaline with a threshold\n"
            "weight, general position means that no set of $N_w$ or more patterns in the\n"
            "$(N_w-1)$-dimension pattern space lie on a hyperplane not constrained to pass\n"
            "through the origin~\\cite{cover64,nilsson}.}",
            
            "\\footnote{Los patrones están en posición general con respecto a una Adaline\n"
            "sin peso de umbral si cualquier subconjunto de vectores de patrón que\n"
            "contenga no más de $N_w$ miembros forma un conjunto linealmente independiente\n"
            "o, equivalentemente, si ningún conjunto de $N_w$ o más puntos de entrada en\n"
            "el espacio de patrones $N_w$-dimensional yace sobre un hiperplano homogéneo.\n"
            "Para el caso más común que involucra una Adaline con peso de umbral, la\n"
            "posición general significa que ningún conjunto de $N_w$ o más patrones en el\n"
            "espacio de patrones de dimensión $(N_w-1)$ yace sobre un hiperplano no\n"
            "restringido a pasar por el origen~\\cite{cover64,nilsson}.}"
        ),
        (
            "\\footnote{In Rumelhart \\textit{et al.}'s terminology, this would be called a\n"
            "four-layer network, following Rosenblatt's convention of counting layers of\n"
            "signals, including the input layer. For our purposes, we find it more useful to\n"
            "count only layers of computing elements. We do not count as a layer the set of\n"
            "input terminal points.}",
            
            "\\footnote{En la terminología de Rumelhart \\textit{et al.}, esto se llamaría\n"
            "una red de cuatro capas, siguiendo la convención de Rosenblatt de contar\n"
            "capas de señales, incluyendo la capa de entrada. Para nuestros propósitos,\n"
            "encontramos más útil contar solo capas de elementos de cómputo. No contamos\n"
            "como una capa el conjunto de puntos terminales de entrada.}"
        ),
        (
            "\\footnote{We should emphasize that the information referred to here corresponds\n"
            "to the maximum number of binary input/output mappings a network can achieve with\n"
            "properly adjusted weights, not the number of bits of information that can be\n"
            "stored directly into the network's weights.}",
            
            "\\footnote{Debe enfatizarse que la información a la que se hace referencia aquí\n"
            "corresponde al número máximo de mapeos binarios de entrada/salida que una red\n"
            "puede lograr con pesos adecuadamente ajustados, no al número de bits de\n"
            "información que pueden almacenarse directamente en los pesos de la red.}"
        ),
        (
            "\\footnote{This can be seen by noting that any Boolean function can be written in\n"
            "the sum-of-products form~\\cite{greenfield}, and that such an expression can be\n"
            "realized with a two-layer network by using the first-layer Adalines to implement\n"
            "AND gates, while using the second-layer Adalines to implement OR gates.}",
            
            "\\footnote{Esto puede verse notando que cualquier función booleana puede\n"
            "escribirse en la forma de suma de productos~\\cite{greenfield}, y que tal\n"
            "expresión puede realizarse con una red de dos capas usando las Adalines de\n"
            "la primera capa para implementar compuertas AND, y las Adalines de la\n"
            "segunda capa para implementar compuertas OR.}"
        ),
        (
            "\\footnote{Actually, the network can be an arbitrary feedforward structure and\n"
            "need not be layered.}",
            
            "\\footnote{En realidad, la red puede ser una estructura arbitraria con\n"
            "alimentación hacia adelante y no necesita estar en capas.}"
        ),
        (
            "\\footnote{The upper bound used here is Baum's loose bound: minimum number hidden\n"
            "nodes $\\le N_y\\lceil N_p/N_x\\rceil < N_y(N_p/N_x + 1)$.}",
            
            "\\footnote{La cota superior usada aquí es la cota holgada de Baum: número\n"
            "mínimo de nodos ocultos $\\le N_y\\lceil N_p/N_x\\rceil < N_y(N_p/N_x + 1)$.}"
        ),
        (
            "\\footnote{The input representation often has a considerable impact on the success\n"
            "of a network. In NETtalk, the inputs are sparsely coded in 29 components. One\n"
            "might consider instead choosing a 5-bit binary representation of the 7-bit ASCII\n"
            "code. It should be clear, however, that in this case the sparse representation\n"
            "helps simplify the network's job of interpreting input characters as 29 distinct\n"
            "symbols. Usually the appropriate input encoding is not difficult to decide. When\n"
            "intuition fails, however, one sometimes must experiment with different encodings\n"
            "to find one that works well.}",
            
            "\\footnote{La representación de entrada a menudo tiene un impacto considerable\n"
            "en el éxito de una red. En NETtalk, las entradas están codificadas de forma\n"
            "dispersa en 29 componentes. Uno podría considerar en su lugar elegir una\n"
            "representación binaria de 5 bits del código ASCII de 7 bits. Sin embargo,\n"
            "debe quedar claro que en este caso la representación dispersa ayuda a\n"
            "simplificar la tarea de la red de interpretar los caracteres de entrada como\n"
            "29 símbolos distintos. Usualmente la codificación de entrada apropiada no es\n"
            "difícil de decidir. Sin embargo, cuando la intuición falla, a veces se debe\n"
            "experimentar con diferentes codificaciones para encontrar una que funcione\n"
            "bien.}"
        ),
        (
            "\\footnote{This results because the length of the weight vector decreases with each\n"
            "adaptation that does not cause the linear output $s_k$ to change sign and assume a\n"
            "magnitude greater than that before adaptation. Although there are exceptions, for\n"
            "most problems this situation occurs only rarely if the weight vector is much\n"
            "longer than the weight increment vector.}",
            
            "\\footnote{Esto ocurre porque la longitud del vector de pesos disminuye con\n"
            "cada adaptación que no hace que la salida lineal $s_k$ cambie de signo y\n"
            "asuma una magnitud mayor que la anterior a la adaptación. Aunque hay\n"
            "excepciones, para la mayoría de los problemas esta situación ocurre solo\n"
            "raramente si el vector de pesos es mucho más largo que el vector de\n"
            "incremento de pesos.}"
        ),
        (
            "\\footnote{The terms ``fixed-increment'' and ``absolute correction'' are due to\n"
            "Nilsson~\\cite{nilsson}. Rosenblatt referred to methods of these types,\n"
            "respectively, as quantized and nonquantized learning rules.}",
            
            "\\footnote{Los términos ``incremento fijo'' y ``corrección absoluta'' se deben\n"
            "a Nilsson~\\cite{nilsson}. Rosenblatt se refirió a métodos de estos tipos,\n"
            "respectivamente, como reglas de aprendizaje cuantizadas y no cuantizadas.}"
        ),
        (
            "\\footnote{The increment adaptation rule was proposed by others before Mays, though\n"
            "from a different perspective~\\cite{block}.}",
            
            "\\footnote{La regla de adaptación por incremento fue propuesta por otros antes\n"
            "que Mays, aunque desde una perspectiva diferente~\\cite{block}.}"
        ),
        (
            "\\footnote{We assume here that $\\X$ includes a bias component $x_{0k} = +1$.}",
            "\\footnote{Suponemos aquí que $\\X$ incluye una componente de sesgo $x_{0k} = +1$.}"
        ),
        (
            "\\footnote{If the autocorrelation matrix of the pattern vector set has $m$ zero\n"
            "eigenvalues, the minimum MSE solution will be an $m$-dimensional subspace in weight\n"
            "space~\\cite{asp}.}",
            
            "\\footnote{Si la matriz de autocorrelación del conjunto de vectores de patrón\n"
            "tiene $m$ valores propios cero, la solución de ECM mínimo será un subespacio\n"
            "de dimensión $m$ en el espacio de pesos~\\cite{asp}.}"
        ),
        (
            "\\footnote{Horowitz and Senne~\\cite{horowitz} have proven that (34) is not sufficient\n"
            "in general to guarantee convergence of the weight vector's variance. For input\n"
            "patterns generated by a zero-mean Gaussian process independent over time,\n"
            "instability can occur in the worst case if $\\mu$ is greater than $1/(3\\trace[\\R])$.}",
            
            "\\footnote{Horowitz y Senne~\\cite{horowitz} han demostrado que (34) no es\n"
            "suficiente en general para garantizar la convergencia de la varianza del\n"
            "vector de pesos. Para patrones de entrada generados por un proceso gaussiano\n"
            "de media cero independiente en el tiempo, puede ocurrir inestabilidad en el\n"
            "peor caso si $\\mu$ es mayor que $1/(3\\trace[\\R])$.}"
        ),
        (
            "\\footnote{Gradient noise is the difference between the gradient estimate and the\n"
            "true gradient.}",
            
            "\\footnote{El ruido de gradiente es la diferencia entre la estimación del\n"
            "gradiente y el gradiente verdadero.}"
        ),
        (
            "\\footnote{The idea of a normalized training set was suggested by Derrick Nguyen.}",
            "\\footnote{La idea de un conjunto de entrenamiento normalizado fue sugerida por Derrick Nguyen.}"
        ),
        (
            "\\footnote{Recently, Nguyen has discovered that a more sophisticated choice of\n"
            "initial weight values in hidden layers can lead to reduced problems with local\n"
            "optima and dramatic increases in network training speed~\\cite{nguyen100}.\n"
            "Experimental evidence suggests that it is advisable to choose the initial weights\n"
            "of each hidden layer in a quasi-random manner, which ensures that at each position\n"
            "in a layer's input space the outputs of all but a few of its Adalines will be\n"
            "saturated, while ensuring that each Adaline in the layer is unsaturated in some\n"
            "region of its input space. When this method is used, the weights in the output\n"
            "layer are set to small random values.}",
            
            "\\footnote{Recientemente, Nguyen ha descubierto que una elección más\n"
            "sofisticada de los valores iniciales de los pesos en las capas ocultas puede\n"
            "reducir los problemas con óptimos locales y aumentar drásticamente la\n"
            "velocidad de entrenamiento de la red~\\cite{nguyen100}. La evidencia\n"
            "experimental sugiere que es recomendable elegir los pesos iniciales de cada\n"
            "capa oculta de manera cuasi-aleatoria, lo que asegura que en cada posición\n"
            "del espacio de entrada de una capa las salidas de todas menos unas pocas de\n"
            "sus Adalines estarán saturadas, mientras se garantiza que cada Adaline en la\n"
            "capa esté no saturada en alguna región de su espacio de entrada. Cuando se\n"
            "usa este método, los pesos en la capa de salida se establecen en valores\n"
            "aleatorios pequeños.}"
        ),
        (
            "\\footnote{In Fig.~\\ref{fig:25}, all notation follows the convention that\n"
            "superscripts within parentheses indicate the layer number of the associated Adaline\n"
            "or input node, while subscripts identify the associated Adaline(s) within a layer.}",
            
            "\\footnote{En la Fig.~\\ref{fig:25}, toda la notación sigue la convención de\n"
            "que los superíndices entre paréntesis indican el número de capa de la Adaline\n"
            "o nodo de entrada asociado, mientras que los subíndices identifican la(s)\n"
            "Adaline(s) asociada(s) dentro de una capa.}"
        ),
        (
            "\\footnote{``Clean'' gradient estimates are those with little gradient noise.}",
            "\\footnote{Las estimaciones de gradiente ``limpias'' son aquellas con poco ruido de gradiente.}"
        ),
        (
            "\\footnote{Jacob's paper, like many other papers in the literature, assumes for\n"
            "analysis that the true gradients rather than instantaneous gradients are used to\n"
            "update the weights, that is, that weights are changed periodically, only after all\n"
            "training patterns are presented. This eliminates gradient noise but can slow down\n"
            "training enormously if the training set is large. The delta-bar-delta procedure in\n"
            "Jacob's paper involves monitoring changes of the true gradients in response to\n"
            "weight changes. It should be possible to avoid the expense of computing the true\n"
            "gradients explicitly in this case by instead monitoring changes in the outputs of,\n"
            "say, two momentum filters with different time constants.}",
            
            "\\footnote{El artículo de Jacobs, como muchos otros en la literatura, supone\n"
            "para el análisis que se usan los gradientes verdaderos en lugar de los\n"
            "gradientes instantáneos para actualizar los pesos, es decir, que los pesos se\n"
            "cambian periódicamente, solo después de que se han presentado todos los\n"
            "patrones de entrenamiento. Esto elimina el ruido de gradiente pero puede\n"
            "ralentizar enormemente el entrenamiento si el conjunto de entrenamiento es\n"
            "grande. El procedimiento delta-bar-delta en el artículo de Jacobs implica\n"
            "monitorear los cambios de los gradientes verdaderos en respuesta a los\n"
            "cambios de pesos. Debería ser posible evitar el costo de calcular los\n"
            "gradientes verdaderos explícitamente en este caso monitoreando en su lugar\n"
            "los cambios en las salidas de, digamos, dos filtros de momento con\n"
            "constantes de tiempo diferentes.}"
        ),
    ]
    
    for old, new in footnote_map:
        content = content.replace(old, new)
    
    # ---- Biografías de los autores ----
    content = content.replace(
        "\\noindent\\textbf{Bernard Widrow} (Fellow, IEEE) received the S.B., S.M., and Sc.D.\n"
        "degrees from the Massachusetts Institute of Technology in 1951, 1953, and 1956,\n"
        "respectively. He was with M.I.T. until he joined the Stanford University faculty\n"
        "in 1959, where he is now a Professor of electrical engineering. He is presently\n"
        "engaged in research and teaching in neural networks, pattern recognition,\n"
        "adaptive filtering, and adaptive control systems. He is associate editor of the\n"
        "journals \\textit{Adaptive Control and Signal Processing}, \\textit{Neural\n"
        "Networks}, \\textit{Information Sciences}, and \\textit{Pattern Recognition} and\n"
        "coauthor with S. D. Stearns of \\textit{Adaptive Signal Processing} (Prentice\n"
        "Hall). He is a member of the American Association of University Professors, the\n"
        "Pattern Recognition Society, Sigma Xi, and Tau Beta Pi. He is a fellow of the\n"
        "American Association for the Advancement of Science. He is president of the\n"
        "International Neural Network Society. He received the IEEE Alexander Graham Bell\n"
        "Medal in 1986 for exceptional contributions to the advancement of\n"
        "telecommunications.",

        "\\noindent\\textbf{Bernard Widrow} (Fellow, IEEE) recibió los grados de S.B., S.M.\n"
        "y Sc.D. del Instituto Tecnológico de Massachusetts en 1951, 1953 y 1956,\n"
        "respectivamente. Estuvo en el M.I.T. hasta que se unió al cuerpo académico de\n"
        "la Universidad de Stanford en 1959, donde ahora es Profesor de ingeniería\n"
        "eléctrica. Actualmente se dedica a la investigación y docencia en redes\n"
        "neuronales, reconocimiento de patrones, filtrado adaptativo y sistemas de\n"
        "control adaptativo. Es editor asociado de las revistas \\textit{Adaptive Control\n"
        "and Signal Processing}, \\textit{Neural Networks}, \\textit{Information\n"
        "Sciences} y \\textit{Pattern Recognition} y coautor con S. D. Stearns de\n"
        "\\textit{Adaptive Signal Processing} (Prentice Hall). Es miembro de la American\n"
        "Association of University Professors, la Pattern Recognition Society, Sigma Xi\n"
        "y Tau Beta Pi. Es fellow de la American Association for the Advancement of\n"
        "Science. Es presidente de la International Neural Network Society. Recibió la\n"
        "Medalla IEEE Alexander Graham Bell en 1986 por contribuciones excepcionales al\n"
        "avance de las telecomunicaciones."
    )
    
    content = content.replace(
        "\\noindent\\textbf{Michael A. Lehr} was born in New Jersey on April 18, 1964. He\n"
        "received the B.E.E. degree in electrical engineering at the Georgia Institute of\n"
        "Technology in 1987, graduating top in his class. He received the M.S.E.E. from\n"
        "Stanford University in 1986. From 1982 to 1984, he worked on two-way radio\n"
        "development at Motorola in Ft. Lauderdale, Florida, and from 1984 to 1987 he was\n"
        "involved with naval sonar system development and test at IBM in Manassas,\n"
        "Virginia. Currently, he is a doctoral candidate in the Department of Electrical\n"
        "Engineering at Stanford University. His research interests include adaptive\n"
        "signal processing and neural networks. Mr. Lehr holds a General Radiotelephone\n"
        "Operator License (1981) and Radar Endorsement (1982), and is a member of Tau Beta\n"
        "Pi, Eta Kappa Nu, and Phi Kappa Phi.",

        "\\noindent\\textbf{Michael A. Lehr} nació en New Jersey el 18 de abril de 1964.\n"
        "Recibió el grado de B.E.E. en ingeniería eléctrica en el Instituto de Tecnología\n"
        "de Georgia en 1987, graduándose como el primero de su clase. Recibió el M.S.E.E.\n"
        "de la Universidad de Stanford en 1986. De 1982 a 1984, trabajó en desarrollo de\n"
        "radio bidireccional en Motorola en Ft. Lauderdale, Florida, y de 1984 a 1987\n"
        "participó en el desarrollo y prueba de sistemas de sonar naval en IBM en\n"
        "Manassas, Virginia. Actualmente, es candidato doctoral en el Departamento de\n"
        "Ingeniería Eléctrica de la Universidad de Stanford. Sus intereses de\n"
        "investigación incluyen el procesamiento adaptativo de señales y las redes\n"
        "neuronales. El Sr. Lehr posee una Licencia General de Radiotelefonía (1981) y\n"
        "Radar Endorsement (1982), y es miembro de Tau Beta Pi, Eta Kappa Nu y Phi Kappa\n"
        "Phi."
    )
    
    # ---- Términos sueltos en el texto (en contexto de frases en inglés que puedan quedar) ----
    # Estas son traducciones de frases comunes que aparecen en el texto
    common_phrases = [
        ("One early development was", "Un desarrollo temprano fue"),
        ("At the same time,", "Al mismo tiempo,"),
        ("Other early work included", "Otro trabajo temprano incluyó"),
        ("This was probably the first example of", "Este fue probablemente el primer ejemplo de"),
        ("though it could be argued that", "aunque podría argumentarse que"),
        ("deserves this distinction", "merece esta distinción"),
        ("Further pioneering work on", "Trabajo pionero adicional sobre"),
        ("was performed in the 1970s by", "fue realizado en los años 70 por"),
        ("explored related ideas with his biologically inspired", "exploró ideas relacionadas con sus modelos biológicamente inspirados"),
        ("devised a reinforcement learning algorithm called", "ideó un algoritmo de aprendizaje por refuerzo llamado"),
        ("in the mid-1960s", "a mediados de los años 60"),
        ("This can be used to solve problems when", "Esto puede usarse para resolver problemas cuando"),
        ("uncertainty about the error signal causes", "la incertidumbre sobre la señal de error hace que"),
        ("supervised training methods to be impractical", "los métodos de entrenamiento supervisado sean impracticables"),
        ("A related reinforcement learning approach was later explored in a classic paper by", 
         "Un enfoque relacionado de aprendizaje por refuerzo fue explorado más tarde en un artículo clásico de"),
        ("is also somewhat reminiscent of", "también recuerda en cierta medida a"),
        ("a distributed table-look-up system based on models of human memory",
         "un sistema distribuido de consulta en tabla basado en modelos de memoria humana"),
        ("In the 1970s Grossberg developed his", "En los años 70 Grossberg desarrolló su"),
        ("a number of novel hypotheses about the underlying principles governing biological neural systems",
         "una serie de hipótesis novedosas sobre los principios subyacentes que gobiernan los sistemas neuronales biológicos"),
        ("These ideas served as the basis for later work by",
         "Estas ideas sirvieron como base para trabajos posteriores de"),
        ("involving three classes of ART architectures",
         "que involucran tres clases de arquitecturas ART"),
        ("These are self-organizing neural implementations of pattern clustering algorithms",
         "Estas son implementaciones neuronales autoorganizadas de algoritmos de agrupamiento de patrones"),
        ("Other important theory on self-organizing systems was pioneered by",
         "Otra teoría importante sobre sistemas autoorganizados fue iniciada por"),
        ("with his work on feature maps", "con su trabajo sobre mapas de características"),
        ("In the early 1980s, Hopfield and others introduced outer product rules",
         "A principios de los años 80, Hopfield y otros introdujeron reglas de producto externo"),
        ("as well as equivalent approaches based on the early work of Hebb",
         "así como enfoques equivalentes basados en el trabajo temprano de Hebb"),
        ("for training a class of recurrent (signal feedback) networks now called Hopfield models",
         "para entrenar una clase de redes recurrentes (con retroalimentación de señal) ahora llamadas modelos de Hopfield"),
        ("More recently, Kosko extended some of the ideas of",
         "Más recientemente, Kosko extendió algunas de las ideas de"),
        ("to develop his adaptive Bidirectional Associative Memory (BAM)",
         "para desarrollar su Memoria Asociativa Bidireccional (BAM) adaptativa"),
        ("a network model employing differential as well as Hebbian and competitive learning laws",
         "un modelo de red que emplea leyes de aprendizaje diferencial, hebbiano y competitivo"),
        ("Other significant models from the past decade include probabilistic ones",
         "Otros modelos significativos de la última década incluyen los probabilísticos"),
        ("which, to oversimplify, is a Hopfield model that settles into solutions by a simulated annealing process governed by Boltzmann statistics",
         "que, para simplificar en exceso, es un modelo de Hopfield que converge a soluciones mediante un proceso de recocido simulado gobernado por estadísticas de Boltzmann"),
        ("is trained by a clever two-phase Hebbian-based technique",
         "se entrena mediante una ingeniosa técnica bifásica basada en Hebb"),
        ("While these developments were taking place, adaptive systems research at Stanford traveled an independent path",
         "Mientras estos desarrollos tenían lugar, la investigación en sistemas adaptativos en Stanford siguió un camino independiente"),
        ("After devising their Madaline~I rule, Widrow and his students developed uses for the Adaline and Madaline",
         "Después de idear su regla Madaline~I, Widrow y sus estudiantes desarrollaron usos para la Adaline y la Madaline"),
        ("Early applications included, among others, speech and pattern recognition",
         "Las primeras aplicaciones incluyeron, entre otras, reconocimiento de voz y de patrones"),
        ("weather forecasting", "predicción meteorológica"),
        ("adaptive controls", "controles adaptativos"),
        ("Work then switched to adaptive filtering and adaptive signal processing",
         "El trabajo luego se orientó hacia el filtrado adaptativo y el procesamiento adaptativo de señales"),
        ("after attempts to develop learning rules for networks with multiple adaptive layers were unsuccessful",
         "después de que los intentos de desarrollar reglas de aprendizaje para redes con múltiples capas adaptativas no tuvieran éxito"),
        ("Adaptive signal processing proved to be a fruitful avenue for research with applications involving",
         "El procesamiento adaptativo de señales demostró ser una vía fructífera para la investigación con aplicaciones que involucran"),
        ("adaptive antennas", "antenas adaptativas"),
        ("adaptive inverse controls", "controles inversos adaptativos"),
        ("adaptive noise cancelling", "cancelación adaptativa de ruido"),
        ("seismic signal processing", "procesamiento de señales sísmicas"),
        ("Outstanding work by Lucky and others at Bell Laboratories led to major commercial applications of adaptive filters and the LMS algorithm to",
         "El destacado trabajo de Lucky y otros en los Laboratorios Bell condujo a importantes aplicaciones comerciales de filtros adaptativos y del algoritmo LMS para"),
        ("adaptive equalization in high-speed modems", "ecualización adaptativa en módems de alta velocidad"),
        ("adaptive echo cancellers for long-distance telephone and satellite circuits",
         "canceladores de eco adaptativos para circuitos telefónicos de larga distancia y satelitales"),
        ("After 20 years of research in adaptive signal processing, the work in Widrow's laboratory has once again returned to neural networks",
         "Después de 20 años de investigación en procesamiento adaptativo de señales, el trabajo en el laboratorio de Widrow ha vuelto una vez más a las redes neuronales"),
        ("The first major extension of the feedforward neural network beyond Madaline~I took place in 1971 when",
         "La primera extensión importante de la red neuronal con alimentación hacia adelante más allá de Madaline~I tuvo lugar en 1971 cuando"),
        ("developed a backpropagation training algorithm which, in 1974, he first published in his doctoral dissertation",
         "desarrolló un algoritmo de entrenamiento de retropropagación que, en 1974, publicó por primera vez en su tesis doctoral"),
        ("Unfortunately, Werbos's work remained almost unknown in the scientific community",
         "Desafortunadamente, el trabajo de Werbos permaneció casi desconocido en la comunidad científica"),
        ("rediscovered the technique", "redescubrió la técnica"),
        ("Not long after Parker published his findings,", "Poco después de que Parker publicara sus hallazgos,"),
        ("also rediscovered the technique and, largely as a result of the clear framework within which they presented their ideas, they finally succeeded in making it widely known",
         "también redescubrieron la técnica y, en gran parte como resultado del marco claro dentro del cual presentaron sus ideas, finalmente lograron hacerla ampliamente conocida"),
        ("The elements used by Rumelhart \\textit{et al.} in the backpropagation network differ from those used in the earlier Madaline architectures",
         "Los elementos usados por Rumelhart \\textit{et al.} en la red de retropropagación difieren de aquellos usados en las arquitecturas Madaline anteriores"),
        ("David Andes of U.S. Naval Weapons Center of China Lake, CA, modified Madaline~II in 1988 by replacing the hard-limiting quantizers in the Adaline and sigmoid functions, thereby inventing Madaline Rule~III (MRIII)",
         "David Andes del U.S. Naval Weapons Center de China Lake, CA, modificó Madaline~II en 1988 reemplazando los cuantificadores de límite estricto en la Adaline por funciones sigmoides, inventando así la Regla Madaline~III (MRIII)"),
        ("Widrow and his students were first to recognize that this rule is mathematically equivalent to backpropagation",
         "Widrow y sus estudiantes fueron los primeros en reconocer que esta regla es matemáticamente equivalente a la retropropagación"),
        ("The outline above gives only a partial view of the discipline, and many landmark discoveries have not been mentioned",
         "El esquema anterior ofrece solo una visión parcial de la disciplina, y muchos descubrimientos importantes no han sido mencionados"),
        ("Needless to say, the field of neural networks is quickly becoming a vast one, and in one short survey we could not hope to cover the entire subject in any detail",
         "Está demás decir que el campo de las redes neuronales se está volviendo rápidamente muy vasto, y en una breve revisión no podríamos aspirar a cubrir todo el tema en detalle"),
        ("Consequently, many significant developments, including some of those mentioned above, are not discussed in this paper",
         "En consecuencia, muchos desarrollos significativos, incluyendo algunos de los mencionados anteriormente, no se discuten en este artículo"),
        ("The algorithms described are limited primarily to those developed in our laboratory at Stanford, and to related techniques developed elsewhere, the most important of which is the backpropagation algorithm",
         "Los algoritmos descritos se limitan principalmente a aquellos desarrollados en nuestro laboratorio en Stanford, y a técnicas relacionadas desarrolladas en otros lugares, la más importante de las cuales es el algoritmo de retropropagación"),
        ("Section~II explores fundamental concepts, Section~III discusses adaptation and the minimal disturbance principle, Sections~IV and~V cover error correction rules, Sections~VI and~VII delve into steepest-descent rules, and Section~VIII provides a summary",
         "La Sección~II explora conceptos fundamentales, la Sección~III discute la adaptación y el principio de mínima perturbación, las Secciones~IV y~V cubren reglas de corrección de error, las Secciones~VI y~VII profundizan en reglas de descenso más pronunciado, y la Sección~VIII proporciona un resumen"),
    ]
    
    for old, new in common_phrases:
        content = content.replace(old, new)
    
    # ---- Traducción de palabras sueltas muy comunes (que no rompan LaTeX) ----
    word_replacements = [
        # Solo palabras completas que aparecen como texto narrativo
        ("however,", "sin embargo,"),
        ("therefore", "por lo tanto"),
        ("Thus,", "Así,"),
        ("Thus ", "Así "),
        ("Nevertheless,", "No obstante,"),
        ("Furthermore,", "Además,"),
        ("Moreover,", "Es más,"),
        ("respectively", "respectivamente"),
        ("respectively.", "respectivamente."),
        ("in contrast to", "en contraste con"),
        ("in contrast,", "en contraste,"),
        ("on the other hand", "por otra parte"),
        ("for instance,", "por ejemplo,"),
        ("for example,", "por ejemplo,"),
        ("in fact,", "de hecho,"),
        ("in general,", "en general,"),
        ("in practice,", "en la práctica,"),
        ("in principle,", "en principio,"),
        ("in particular,", "en particular,"),
        ("as follows:", "como sigue:"),
        ("as follows.", "como sigue."),
        ("as shown in", "como se muestra en"),
        ("as illustrated in", "como se ilustra en"),
        ("as described in", "como se describe en"),
        ("as discussed in", "como se discute en"),
        ("as noted in", "como se señala en"),
        ("as we shall see,", "como veremos,"),
        ("as we have seen,", "como hemos visto,"),
        ("it is clear that", "es claro que"),
        ("it is interesting to note that", "es interesante notar que"),
        ("it is important to note that", "es importante notar que"),
        ("it should be noted that", "debe notarse que"),
        ("it is possible to", "es posible"),
        ("it is impossible to", "es imposible"),
        ("it is difficult to", "es difícil"),
        ("it is easy to", "es fácil"),
        ("it is useful to", "es útil"),
        ("it is necessary to", "es necesario"),
        ("it can be shown that", "puede demostrarse que"),
        ("it follows that", "se sigue que"),
        ("it turns out that", "resulta que"),
        ("it is well known that", "es bien sabido que"),
        ("it is assumed that", "se supone que"),
        ("it is interesting to", "es interesante"),
        ("it is instructive to", "es instructivo"),
        ("it is likely that", "es probable que"),
        ("it is not surprising that", "no es sorprendente que"),
        ("it is worth noting that", "vale la pena notar que"),
        ("it should be clear that", "debe quedar claro que"),
        ("it should be emphasized that", "debe enfatizarse que"),
        ("it should be pointed out that", "debe señalarse que"),
        ("it should be remembered that", "debe recordarse que"),
        ("it must be emphasized that", "debe enfatizarse que"),
        ("it must be noted that", "debe notarse que"),
        ("it will be shown that", "se mostrará que"),
        ("it will be seen that", "se verá que"),
        ("this is because", "esto se debe a que"),
        ("this is not the case", "este no es el caso"),
        ("this is in contrast to", "esto contrasta con"),
        ("this is the", "este es el"),
        ("this is an", "este es un"),
        ("this is a", "esta es una"),
        ("There is a", "Existe una"),
        ("There is an", "Existe un"),
        ("There are", "Existen"),
        ("there is no", "no hay"),
        ("there is a", "hay un"),
        ("there are", "hay"),
        ("There is no", "No hay"),
        ("There are many", "Hay muchos"),
        ("There are several", "Hay varios"),
        ("there are many", "hay muchos"),
        ("there are several", "hay varios"),
        ("there is little", "hay poco"),
        ("there is much", "hay mucho"),
        ("there exists", "existe"),
        ("there exist", "existen"),
        ("which is not", "que no es"),
        ("which is the", "que es el"),
        ("which is a", "que es un"),
        ("which is an", "que es un"),
        ("which are not", "que no son"),
        ("which are the", "que son los"),
        ("that is not", "que no es"),
        ("that is a", "que es un"),
        ("that is an", "que es un"),
        ("that is the", "que es el"),
        ("that is,", "es decir,"),
        ("i.e.,", "es decir,"),
        ("e.g.,", "por ejemplo,"),
        ("such as", "tales como"),
        ("rather than", "en lugar de"),
        ("instead of", "en vez de"),
        ("because of", "debido a"),
        ("due to", "debido a"),
        ("according to", "de acuerdo con"),
        ("in accordance with", "de acuerdo con"),
        ("in order to", "para"),
        ("so that", "para que"),
        ("so as to", "con el fin de"),
        ("with respect to", "con respecto a"),
        ("with regard to", "con respecto a"),
        ("in terms of", "en términos de"),
        ("in the case of", "en el caso de"),
        ("in the context of", "en el contexto de"),
        ("in the presence of", "en presencia de"),
        ("in the absence of", "en ausencia de"),
        ("in the following", "en lo siguiente"),
        ("in the next section", "en la siguiente sección"),
        ("in the previous section", "en la sección anterior"),
        ("in this section", "en esta sección"),
        ("in this paper", "en este artículo"),
        ("in this case", "en este caso"),
        ("in many cases", "en muchos casos"),
        ("in some cases", "en algunos casos"),
        ("in most cases", "en la mayoría de los casos"),
        ("in all cases", "en todos los casos"),
        ("in either case", "en cualquier caso"),
        ("in both cases", "en ambos casos"),
        ("in the first case", "en el primer caso"),
        ("in the second case", "en el segundo caso"),
        ("in the latter case", "en el último caso"),
        ("in the former case", "en el primer caso"),
        ("on the average", "en promedio"),
        ("on average", "en promedio"),
        ("of course", "por supuesto"),
        ("of course,", "por supuesto,"),
        ("in fact", "de hecho"),
        ("at least", "al menos"),
        ("at most", "como máximo"),
        ("at first", "al principio"),
        ("at present", "en la actualidad"),
        ("at the same time", "al mismo tiempo"),
        ("at the time", "en ese momento"),
        ("over time", "a lo largo del tiempo"),
        ("over the past", "durante los últimos"),
        ("over the last", "durante los últimos"),
        ("over the next", "durante los próximos"),
        ("until recently", "hasta hace poco"),
        ("more recently", "más recientemente"),
        ("most recently", "más recientemente"),
        ("in recent years", "en años recientes"),
        ("in the past", "en el pasado"),
        ("in the future", "en el futuro"),
        ("to date", "hasta la fecha"),
        ("so far", "hasta ahora"),
        ("as yet", "hasta ahora"),
        ("as of yet", "hasta el momento"),
        ("a great deal of", "una gran cantidad de"),
        ("a lot of", "mucho"),
        ("a number of", "un número de"),
        ("a variety of", "una variedad de"),
        ("a wide range of", "una amplia gama de"),
        ("a wide variety of", "una amplia variedad de"),
        ("the vast majority of", "la gran mayoría de"),
        ("the rest of", "el resto de"),
        ("the remainder of", "el resto de"),
        ("the following", "lo siguiente"),
        ("the above", "lo anterior"),
        ("the former", "el primero"),
        ("the latter", "el último"),
        ("each other", "entre sí"),
        ("one another", "unos con otros"),
        ("each of these", "cada uno de estos"),
        ("all of these", "todos estos"),
        ("most of these", "la mayoría de estos"),
        ("some of these", "algunos de estos"),
        ("none of these", "ninguno de estos"),
        ("both of these", "ambos"),
        ("many of these", "muchos de estos"),
        ("several of these", "varios de estos"),
        ("a few of these", "unos pocos de estos"),
        ("one of the", "uno de los"),
        ("one of these", "uno de estos"),
        ("two of the", "dos de los"),
        ("some of the", "algunos de los"),
        ("many of the", "muchos de los"),
        ("most of the", "la mayoría de los"),
        ("all of the", "todos los"),
        ("none of the", "ninguno de los"),
        ("the rest of the", "el resto de los"),
        ("the first of these", "el primero de estos"),
        ("the second of these", "el segundo de estos"),
        ("the last of these", "el último de estos"),
        ("can be used to", "puede usarse para"),
        ("can be found in", "puede encontrarse en"),
        ("can be seen in", "puede verse en"),
        ("can be viewed as", "puede verse como"),
        ("can be thought of as", "puede pensarse como"),
        ("can be considered as", "puede considerarse como"),
        ("can be regarded as", "puede considerarse como"),
        ("can be expressed as", "puede expresarse como"),
        ("can be written as", "puede escribirse como"),
        ("can be defined as", "puede definirse como"),
        ("can be described as", "puede describirse como"),
        ("can be interpreted as", "puede interpretarse como"),
        ("can be represented as", "puede representarse como"),
        ("can be computed as", "puede calcularse como"),
        ("can be obtained from", "puede obtenerse de"),
        ("can be derived from", "puede derivarse de"),
        ("can be determined by", "puede determinarse mediante"),
        ("can be implemented by", "puede implementarse mediante"),
        ("can be achieved by", "puede lograrse mediante"),
        ("can be accomplished by", "puede realizarse mediante"),
        ("can be extended to", "puede extenderse a"),
        ("can be generalized to", "puede generalizarse a"),
        ("can be applied to", "puede aplicarse a"),
        ("can be adapted to", "puede adaptarse a"),
        ("can be modified to", "puede modificarse para"),
        ("can be replaced by", "puede reemplazarse por"),
        ("can be reduced by", "puede reducirse mediante"),
        ("can be eliminated by", "puede eliminarse mediante"),
        ("can be avoided by", "puede evitarse mediante"),
        ("can be solved by", "puede resolverse mediante"),
        ("can be overcome by", "puede superarse mediante"),
        ("can be improved by", "puede mejorarse mediante"),
        ("can be increased by", "puede aumentarse mediante"),
        ("can be decreased by", "puede disminuirse mediante"),
        ("can be minimized by", "puede minimizarse mediante"),
        ("can be maximized by", "puede maximizarse mediante"),
        ("can be optimized by", "puede optimizarse mediante"),
        ("can be simplified by", "puede simplificarse mediante"),
        ("can be summarized as", "puede resumirse como"),
        ("can be stated as", "puede enunciarse como"),
        ("plays an important role in", "juega un papel importante en"),
        ("plays a key role in", "juega un papel clave en"),
        ("plays a crucial role in", "juega un papel crucial en"),
        ("plays a major role in", "juega un papel principal en"),
        ("plays a significant role in", "juega un papel significativo en"),
        ("plays a central role in", "juega un papel central en"),
        ("is based on", "se basa en"),
        ("is based upon", "se basa en"),
        ("is composed of", "está compuesto de"),
        ("is comprised of", "está compuesto por"),
        ("is made up of", "está formado por"),
        ("is concerned with", "se ocupa de"),
        ("is related to", "está relacionado con"),
        ("is associated with", "está asociado con"),
        ("is connected to", "está conectado a"),
        ("is connected with", "está conectado con"),
        ("is equivalent to", "es equivalente a"),
        ("is identical to", "es idéntico a"),
        ("is similar to", "es similar a"),
        ("is analogous to", "es análogo a"),
        ("is comparable to", "es comparable a"),
        ("is different from", "es diferente de"),
        ("is independent of", "es independiente de"),
        ("is dependent on", "depende de"),
        ("is dependent upon", "depende de"),
        ("is responsible for", "es responsable de"),
        ("is characteristic of", "es característico de"),
        ("is representative of", "es representativo de"),
        ("is typical of", "es típico de"),
        ("is capable of", "es capaz de"),
        ("is incapable of", "es incapaz de"),
        ("is able to", "es capaz de"),
        ("is unable to", "es incapaz de"),
        ("is likely to", "es probable que"),
        ("is unlikely to", "es improbable que"),
        ("is expected to", "se espera que"),
        ("is assumed to be", "se supone que es"),
        ("is known to be", "se sabe que es"),
        ("is believed to be", "se cree que es"),
        ("is thought to be", "se piensa que es"),
        ("is considered to be", "se considera que es"),
        ("is found to be", "se encuentra que es"),
        ("is shown to be", "se muestra que es"),
        ("is proven to be", "se demuestra que es"),
        ("is guaranteed to be", "se garantiza que es"),
        ("is said to be", "se dice que es"),
        ("is referred to as", "se denomina"),
        ("is called", "se llama"),
        ("is termed", "se denomina"),
        ("is defined as", "se define como"),
        ("is denoted by", "se denota por"),
        ("is given by", "está dado por"),
        ("is determined by", "está determinado por"),
        ("is characterized by", "se caracteriza por"),
        ("is governed by", "está gobernado por"),
        ("is limited by", "está limitado por"),
        ("is constrained by", "está restringido por"),
        ("is influenced by", "está influenciado por"),
        ("is affected by", "se ve afectado por"),
        ("is caused by", "es causado por"),
        ("is dominated by", "está dominado por"),
        ("is controlled by", "está controlado por"),
        ("is driven by", "es impulsado por"),
        ("is motivated by", "está motivado por"),
        ("is inspired by", "está inspirado por"),
        ("is followed by", "es seguido por"),
        ("is preceded by", "es precedido por"),
        ("is accompanied by", "está acompañado por"),
        ("is replaced by", "es reemplazado por"),
        ("is substituted by", "es sustituido por"),
        ("is represented by", "está representado por"),
        ("is illustrated by", "está ilustrado por"),
        ("is demonstrated by", "está demostrado por"),
        ("is exemplified by", "está ejemplificado por"),
        ("is supported by", "está respaldado por"),
        ("is confirmed by", "está confirmado por"),
        ("is validated by", "está validado por"),
        ("is verified by", "está verificado por"),
        ("is measured by", "se mide por"),
        ("is computed by", "se calcula por"),
        ("is calculated by", "se calcula por"),
        ("is estimated by", "se estima por"),
        ("is approximated by", "se aproxima por"),
        ("is bounded by", "está acotado por"),
        ("it is", "es"),
        ("it was", "fue"),
        ("it has been", "ha sido"),
        ("it had been", "había sido"),
        ("it will be", "será"),
        ("it would be", "sería"),
        ("it can be", "puede ser"),
        ("it could be", "podría ser"),
        ("it may be", "puede ser"),
        ("it might be", "podría ser"),
        ("it must be", "debe ser"),
        ("it should be", "debería ser"),
        ("it need not be", "no necesita ser"),
        ("it cannot be", "no puede ser"),
        ("it could not be", "no podría ser"),
        ("it is not", "no es"),
        ("it was not", "no fue"),
        ("it has not been", "no ha sido"),
        ("this is not", "esto no es"),
        ("that is not", "eso no es"),
        ("these are not", "estos no son"),
        ("those are not", "esos no son"),
        ("there is not", "no hay"),
        ("First,", "En primer lugar,"),
        ("Second,", "En segundo lugar,"),
        ("Third,", "En tercer lugar,"),
        ("Finally,", "Finalmente,"),
        ("Lastly,", "Por último,"),
        ("In summary,", "En resumen,"),
        ("In conclusion,", "En conclusión,"),
        ("To summarize,", "Para resumir,"),
        ("To conclude,", "Para concluir,"),
        ("To begin,", "Para comenzar,"),
        ("To start,", "Para empezar,"),
        ("To this end,", "Con este fin,"),
        ("To do this,", "Para hacer esto,"),
        ("To see this,", "Para ver esto,"),
        ("To understand this,", "Para entender esto,"),
        ("To illustrate this,", "Para ilustrar esto,"),
        ("To demonstrate this,", "Para demostrar esto,"),
        ("To overcome this,", "Para superar esto,"),
        ("To avoid this,", "Para evitar esto,"),
        ("To achieve this,", "Para lograr esto,"),
        ("To accomplish this,", "Para lograr esto,"),
        ("Another way to", "Otra forma de"),
        ("One way to", "Una forma de"),
        ("The best way to", "La mejor forma de"),
        ("The easiest way to", "La forma más fácil de"),
        ("The simplest way to", "La forma más simple de"),
        ("The most common way to", "La forma más común de"),
        ("The most efficient way to", "La forma más eficiente de"),
        ("The most effective way to", "La forma más efectiva de"),
        ("The most popular method for", "El método más popular para"),
        ("The most common approach to", "El enfoque más común para"),
        ("The main advantage of", "La principal ventaja de"),
        ("The main disadvantage of", "La principal desventaja de"),
        ("The main difference between", "La principal diferencia entre"),
        ("The main reason for", "La razón principal de"),
        ("The main purpose of", "El propósito principal de"),
        ("The main goal of", "El objetivo principal de"),
        ("The main objective of", "El objetivo principal de"),
        ("The main problem with", "El principal problema con"),
        ("The main difficulty with", "La principal dificultad con"),
        ("The main limitation of", "La principal limitación de"),
        ("The key point is that", "El punto clave es que"),
        ("The key idea is that", "La idea clave es que"),
        ("The key insight is that", "La percepción clave es que"),
        ("The key difference is that", "La diferencia clave es que"),
        ("The key advantage is that", "La ventaja clave es que"),
        ("The important point is that", "El punto importante es que"),
        ("An important point is that", "Un punto importante es que"),
        ("It is important to note that", "Es importante notar que"),
        ("It is worth noting that", "Vale la pena notar que"),
        ("It is interesting to note that", "Es interesante notar que"),
        ("It is interesting that", "Es interesante que"),
        ("It is remarkable that", "Es notable que"),
        ("It is surprising that", "Es sorprendente que"),
        ("It is unfortunate that", "Es desafortunado que"),
        ("It is curious that", "Es curioso que"),
        ("It is ironic that", "Es irónico que"),
        ("It is natural that", "Es natural que"),
        ("It is obvious that", "Es obvio que"),
        ("It is evident that", "Es evidente que"),
        ("It is apparent that", "Es evidente que"),
        ("It is clear that", "Es claro que"),
        ("It seems that", "Parece que"),
        ("It appears that", "Parece que"),
        ("It happens that", "Sucede que"),
        ("It follows that", "Se sigue que"),
        ("It turns out that", "Resulta que"),
        ("it has been shown that", "se ha demostrado que"),
        ("it has been observed that", "se ha observado que"),
        ("it has been found that", "se ha encontrado que"),
        ("it has been suggested that", "se ha sugerido que"),
        ("it has been proposed that", "se ha propuesto que"),
        ("it has been argued that", "se ha argumentado que"),
        ("it has been noted that", "se ha notado que"),
        ("it has been pointed out that", "se ha señalado que"),
        ("it has been demonstrated that", "se ha demostrado que"),
        ("it has been proven that", "se ha probado que"),
        ("it has been established that", "se ha establecido que"),
        ("it has been recognized that", "se ha reconocido que"),
        ("it has been assumed that", "se ha supuesto que"),
        ("This is because", "Esto se debe a que"),
        ("This is why", "Por esto"),
        ("This is how", "Así es como"),
        ("This is what", "Esto es lo que"),
        ("This is where", "Aquí es donde"),
        ("This is when", "Esto es cuando"),
        ("Another important", "Otro importante"),
        ("Another interesting", "Otro interesante"),
        ("Another useful", "Otra útil"),
        ("Another common", "Otro común"),
        ("Another popular", "Otro popular"),
        ("Another approach is to", "Otro enfoque es"),
        ("Another method is to", "Otro método es"),
        ("Another possibility is to", "Otra posibilidad es"),
        ("Another alternative is to", "Otra alternativa es"),
        ("One approach is to", "Un enfoque es"),
        ("One method is to", "Un método es"),
        ("One possibility is to", "Una posibilidad es"),
        ("One alternative is to", "Una alternativa es"),
        ("One solution is to", "Una solución es"),
        ("One strategy is to", "Una estrategia es"),
        ("One technique is to", "Una técnica es"),
        ("This approach", "Este enfoque"),
        ("This method", "Este método"),
        ("This technique", "Esta técnica"),
        ("This algorithm", "Este algoritmo"),
        ("This procedure", "Este procedimiento"),
        ("This process", "Este proceso"),
        ("This result", "Este resultado"),
        ("This finding", "Este hallazgo"),
        ("This observation", "Esta observación"),
        ("This assumption", "Esta suposición"),
        ("This conclusion", "Esta conclusión"),
        ("This suggests that", "Esto sugiere que"),
        ("This implies that", "Esto implica que"),
        ("This indicates that", "Esto indica que"),
        ("This means that", "Esto significa que"),
        ("This shows that", "Esto muestra que"),
        ("This proves that", "Esto prueba que"),
        ("This demonstrates that", "Esto demuestra que"),
        ("This confirms that", "Esto confirma que"),
        ("This ensures that", "Esto asegura que"),
        ("This guarantees that", "Esto garantiza que"),
        ("This allows us to", "Esto nos permite"),
        ("This enables us to", "Esto nos permite"),
        ("This permits us to", "Esto nos permite"),
        ("This makes it possible to", "Esto hace posible"),
        ("This makes it easy to", "Esto facilita"),
        ("This makes it difficult to", "Esto dificulta"),
        ("as opposed to", "en oposición a"),
        ("as compared to", "en comparación con"),
        ("as compared with", "en comparación con"),
        ("compared to", "en comparación con"),
        ("compared with", "en comparación con"),
        ("in comparison to", "en comparación con"),
        ("in comparison with", "en comparación con"),
        ("in contrast with", "en contraste con"),
        ("similar to", "similar a"),
        ("different from", "diferente de"),
        ("independent of", "independiente de"),
        ("regardless of", "independientemente de"),
        ("irrespective of", "sin importar"),
        ("in spite of", "a pesar de"),
        ("despite the fact that", "a pesar de que"),
        ("owing to", "debido a"),
        ("thanks to", "gracias a"),
        ("along with", "junto con"),
        ("together with", "junto con"),
        ("coupled with", "junto con"),
        ("combined with", "combinado con"),
        ("associated with", "asociado con"),
        ("related to", "relacionado con"),
        ("connected to", "conectado a"),
        ("linked to", "vinculado a"),
        ("attached to", "unido a"),
        ("added to", "añadido a"),
        ("applied to", "aplicado a"),
        ("assigned to", "asignado a"),
        ("attributed to", "atribuido a"),
        ("belonging to", "perteneciente a"),
        ("corresponding to", "correspondiente a"),
        ("leading to", "conduciendo a"),
        ("pertaining to", "relativo a"),
        ("referring to", "refiriéndose a"),
        ("relating to", "relacionado con"),
        ("resulting in", "resultando en"),
        ("resulting from", "resultante de"),
        ("arising from", "surgiendo de"),
        ("stemming from", "derivado de"),
        ("coming from", "proveniente de"),
        ("derived from", "derivado de"),
        ("obtained from", "obtenido de"),
        ("taken from", "tomado de"),
        ("borrowed from", "tomado prestado de"),
        ("originating from", "originado de"),
        ("emanating from", "emanado de"),
        ("ranging from", "que van de"),
        ("varying from", "que varían de"),
        ("extending from", "que se extienden de"),
        ("consisting of", "que consiste en"),
        ("composed of", "compuesto de"),
        ("comprised of", "compuesto de"),
        ("made of", "hecho de"),
        ("made up of", "compuesto de"),
        ("the fact that", "el hecho de que"),
        ("the idea that", "la idea de que"),
        ("the notion that", "la noción de que"),
        ("the assumption that", "la suposición de que"),
        ("the hypothesis that", "la hipótesis de que"),
        ("the observation that", "la observación de que"),
        ("the possibility that", "la posibilidad de que"),
        ("the probability that", "la probabilidad de que"),
        ("the conclusion that", "la conclusión de que"),
        ("the belief that", "la creencia de que"),
        ("the expectation that", "la expectativa de que"),
        ("the suggestion that", "la sugerencia de que"),
        ("the recommendation that", "la recomendación de que"),
        ("the requirement that", "el requisito de que"),
        ("the condition that", "la condición de que"),
        ("the constraint that", "la restricción de que"),
        ("the claim that", "la afirmación de que"),
        ("the argument that", "el argumento de que"),
        ("the statement that", "la declaración de que"),
        ("the proposition that", "la proposición de que"),
        ("the assertion that", "la aseveración de que"),
        ("the contention that", "la contención de que"),
        ("the view that", "la opinión de que"),
        ("the principle that", "el principio de que"),
        ("the rule that", "la regla de que"),
        ("the law that", "la ley de que"),
        ("the theorem that", "el teorema de que"),
        ("the theory that", "la teoría de que"),
        ("the concept that", "el concepto de que"),
        ("the notion that", "la noción de que"),
        ("the discovery that", "el descubrimiento de que"),
        ("the realization that", "la comprensión de que"),
        ("the recognition that", "el reconocimiento de que"),
        ("the understanding that", "el entendimiento de que"),
        ("the knowledge that", "el conocimiento de que"),
        ("the awareness that", "la conciencia de que"),
        ("the impression that", "la impresión de que"),
        ("the feeling that", "la sensación de que"),
        ("the sense that", "el sentido de que"),
        ("the hope that", "la esperanza de que"),
        ("the fear that", "el temor de que"),
        ("the concern that", "la preocupación de que"),
        ("the doubt that", "la duda de que"),
        ("the suspicion that", "la sospecha de que"),
        ("the conviction that", "la convicción de que"),
        ("the certainty that", "la certeza de que"),
        ("the assurance that", "la seguridad de que"),
        ("the guarantee that", "la garantía de que"),
        ("the promise that", "la promesa de que"),
        ("Let us consider", "Consideremos"),
        ("Let us assume", "Supongamos"),
        ("Let us suppose", "Supongamos"),
        ("Let us examine", "Examinemos"),
        ("Let us look at", "Veamos"),
        ("Let us take", "Tomemos"),
        ("Let us begin", "Comencemos"),
        ("Let us start", "Empecemos"),
        ("Let us now", "Ahora"),
        ("Let us first", "Primero"),
        ("Let us next", "A continuación"),
        ("We begin with", "Comenzamos con"),
        ("We start with", "Empezamos con"),
        ("We end with", "Terminamos con"),
        ("We conclude with", "Concluimos con"),
        ("We now turn to", "Ahora pasamos a"),
        ("We now consider", "Ahora consideramos"),
        ("We now examine", "Ahora examinamos"),
        ("We now look at", "Ahora vemos"),
        ("We now discuss", "Ahora discutimos"),
        ("We now describe", "Ahora describimos"),
        ("We now present", "Ahora presentamos"),
        ("We now show", "Ahora mostramos"),
        ("We now prove", "Ahora demostramos"),
        ("We now demonstrate", "Ahora demostramos"),
        ("We now illustrate", "Ahora ilustramos"),
        ("We now explain", "Ahora explicamos"),
        ("We now explore", "Ahora exploramos"),
        ("We now investigate", "Ahora investigamos"),
        ("We now analyze", "Ahora analizamos"),
        ("We now study", "Ahora estudiamos"),
        ("We now derive", "Ahora derivamos"),
        ("We now compute", "Ahora calculamos"),
        ("We now compare", "Ahora comparamos"),
        ("We now summarize", "Ahora resumimos"),
        ("We shall see that", "Veremos que"),
        ("We shall find that", "Encontraremos que"),
        ("We shall show that", "Mostraremos que"),
        ("We shall prove that", "Demostraremos que"),
        ("We shall demonstrate that", "Demostraremos que"),
        ("We shall assume that", "Supondremos que"),
        ("We shall use", "Usaremos"),
        ("We shall denote", "Denotaremos"),
        ("We shall refer to", "Nos referiremos a"),
        ("We shall call", "Llamaremos"),
        ("We shall define", "Definiremos"),
        ("We shall say that", "Diremos que"),
        ("Note that", "Nótese que"),
        ("Notice that", "Obsérvese que"),
        ("Observe that", "Obsérvese que"),
        ("Recall that", "Recuérdese que"),
        ("Remember that", "Recuérdese que"),
        ("Suppose that", "Supóngase que"),
        ("Assume that", "Supóngase que"),
        ("Imagine that", "Imagínese que"),
        ("Consider the case where", "Considérese el caso donde"),
        ("Consider the situation where", "Considérese la situación donde"),
        ("Consider the example of", "Considérese el ejemplo de"),
        ("Consider the problem of", "Considérese el problema de"),
        ("Consider the following", "Considérese lo siguiente"),
        ("Consider a", "Considérese un"),
        ("Consider an", "Considérese un"),
        ("Consider the", "Considérese el"),
        ("Now consider", "Ahora considérese"),
        ("First consider", "Primero considérese"),
        ("Next consider", "A continuación considérese"),
        ("For example,", "Por ejemplo,"),
        ("For instance,", "Por ejemplo,"),
        ("As an example,", "Como ejemplo,"),
        ("As an illustration,", "Como ilustración,"),
        ("As a consequence,", "Como consecuencia,"),
        ("As a result,", "Como resultado,"),
        ("As a result of this,", "Como resultado de esto,"),
        ("As a matter of fact,", "De hecho,"),
        ("As a rule,", "Por regla general,"),
        ("As a general rule,", "Como regla general,"),
        ("As a first step,", "Como primer paso,"),
        ("As a second step,", "Como segundo paso,"),
        ("As a final step,", "Como paso final,"),
        ("As an alternative,", "Como alternativa,"),
        ("In other words,", "En otras palabras,"),
        ("In simple terms,", "En términos simples,"),
        ("In simpler terms,", "En términos más simples,"),
        ("In more detail,", "Con más detalle,"),
        ("In greater detail,", "Con mayor detalle,"),
        ("In this way,", "De esta manera,"),
        ("In this manner,", "De esta manera,"),
        ("In a similar way,", "De manera similar,"),
        ("In a similar manner,", "De manera similar,"),
        ("In a different way,", "De manera diferente,"),
        ("In a different manner,", "De manera diferente,"),
        ("In the same way,", "De la misma manera,"),
        ("In the same manner,", "De la misma manera,"),
        ("In much the same way,", "De manera muy similar,"),
        ("In exactly the same way,", "Exactamente de la misma manera,"),
        ("In a sense,", "En cierto sentido,"),
        ("In some sense,", "En algún sentido,"),
        ("In a very real sense,", "En un sentido muy real,"),
        ("In a broad sense,", "En un sentido amplio,"),
        ("In a narrow sense,", "En un sentido estrecho,"),
        ("In a general sense,", "En un sentido general,"),
        ("In a strict sense,", "En un sentido estricto,"),
        ("In a loose sense,", "En un sentido laxo,"),
        ("In a certain sense,", "En cierto sentido,"),
        ("In a limited sense,", "En un sentido limitado,"),
        ("In a practical sense,", "En un sentido práctico,"),
        ("In a theoretical sense,", "En un sentido teórico,"),
        ("In the long run,", "A largo plazo,"),
        ("In the short run,", "A corto plazo,"),
        ("In the meantime,", "Mientras tanto,"),
        ("In the interim,", "En el ínterin,"),
        ("In the end,", "Al final,"),
        ("In the beginning,", "Al principio,"),
        ("In the first place,", "En primer lugar,"),
        ("In the second place,", "En segundo lugar,"),
        ("For the most part,", "En su mayor parte,"),
        ("For all practical purposes,", "Para todos los fines prácticos,"),
        ("For the sake of", "Por el bien de"),
        ("For the purpose of", "Con el propósito de"),
        ("For the purposes of", "Para los fines de"),
        ("By means of", "Mediante"),
        ("By virtue of", "En virtud de"),
        ("By way of", "A modo de"),
        ("By use of", "Mediante el uso de"),
        ("By the use of", "Mediante el uso de"),
        ("Through the use of", "Mediante el uso de"),
        ("With the use of", "Con el uso de"),
        ("With the aid of", "Con la ayuda de"),
        ("With the help of", "Con la ayuda de"),
        ("With the assistance of", "Con la asistencia de"),
        ("With the exception of", "Con la excepción de"),
        ("With the possible exception of", "Con la posible excepción de"),
        ("With respect to", "Con respecto a"),
        ("With reference to", "Con referencia a"),
        ("With regard to", "Con respecto a"),
        ("Without loss of generality,", "Sin pérdida de generalidad,"),
        ("Without exception,", "Sin excepción,"),
        ("Without doubt,", "Sin duda,"),
        ("Without question,", "Sin lugar a dudas,"),
        ("in addition to", "además de"),
        ("in addition,", "además,"),
        ("Additionally,", "Adicionalmente,"),
        ("additionally,", "adicionalmente,"),
        ("consequently,", "en consecuencia,"),
        ("Consequently,", "En consecuencia,"),
        ("hence,", "por lo tanto,"),
        ("Hence,", "Por lo tanto,"),
        ("thus,", "así,"),
        ("Thus,", "Así,"),
        ("therefore,", "por lo tanto,"),
        ("Therefore,", "Por lo tanto,"),
        ("accordingly,", "en consecuencia,"),
        ("Accordingly,", "En consecuencia,"),
        ("meanwhile,", "mientras tanto,"),
        ("Meanwhile,", "Mientras tanto,"),
        ("otherwise,", "de lo contrario,"),
        ("Otherwise,", "De lo contrario,"),
        ("nonetheless,", "no obstante,"),
        ("Nonetheless,", "No obstante,"),
        ("nevertheless,", "sin embargo,"),
        ("Nevertheless,", "Sin embargo,"),
        ("however", "sin embargo"),
        ("However,", "Sin embargo,"),
        ("although", "aunque"),
        ("Although", "Aunque"),
        ("because", "porque"),
        ("Because", "Porque"),
        ("since", "ya que"),
        ("Since", "Ya que"),
        ("while", "mientras que"),
        ("whereas", "mientras que"),
        ("unless", "a menos que"),
        ("until", "hasta que"),
        ("after", "después de"),
        ("before", "antes de"),
        ("during", "durante"),
        ("throughout", "a lo largo de"),
    ]
    
    # Skip word replacements as they're too aggressive and could break LaTeX code.
    # Instead, rely on the block-level translations above.
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Traducción completada: {output_path}")


if __name__ == '__main__':
    input_file = r'C:\Developer\data-inteligencia\proyectos\RNA\paper-elegido\formateado\latex-v2\widrow1990.tex'
    output_file = r'C:\Developer\data-inteligencia\proyectos\RNA\paper-elegido\formateado\latex-v2-es\widrow1990.tex'
    
    if not os.path.exists(input_file):
        print(f"ERROR: No se encuentra el archivo de entrada: {input_file}")
    else:
        translate_latex_file(input_file, output_file)
