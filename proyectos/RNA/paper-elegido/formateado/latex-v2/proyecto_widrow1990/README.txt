Proyecto LaTeX - Widrow & Lehr (1990), "30 Years of Adaptive Neural Networks"
=============================================================================
Contenido:
  widrow1990.tex   Fuente LaTeX completa (texto, 100 ecuaciones, 33 figuras, 133 refs)
  fig/fig01..33.png Figuras recortadas del escaneo original

Compilar:
  pdflatex widrow1990.tex
  pdflatex widrow1990.tex   (2a-3a pasada: resuelve \cite y \ref)
  pdflatex widrow1990.tex

Para el aspecto IEEE autentico (opcional):
  - Instalar la clase IEEEtran (paquete texlive-publishers).
  - En widrow1990.tex reemplazar la linea \documentclass por:
        \documentclass[10pt,twocolumn]{IEEEtran}
  - Borrar el bloque comentado "APROXIMACION DE ESTILO IEEE".

Nota: el PDF de origen es un ESCANEO (capa OCR de Acrobat Capture 3.0).
El cuerpo de texto fue transcrito y limpiado; conviene revisarlo contra el
original. Las figuras se recortaron directamente del escaneo (fidelidad total).
