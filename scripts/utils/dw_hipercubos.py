"""Genera figuras de hipercubos 3D + dato atómico para los ejercicios de Datawarehouse.

Cada figura tiene dos paneles:
  - Izquierda: cubo 3D con las 3 dimensiones principales y celda atómica resaltada.
  - Derecha:  "ficha" del dato atómico (dimensiones jerárquicas + medidas).

Salida: documentation/aprendizaje/ejercicios-pep-1/figuras/dw_pXX.png
"""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

OUT = Path(__file__).resolve().parents[2] / "documentation" / "aprendizaje" / "ejercicios-pep-1" / "figuras"
OUT.mkdir(parents=True, exist_ok=True)


def cubo_3d(ax, dim_x: tuple[str, list[str]], dim_y: tuple[str, list[str]], dim_z: tuple[str, list[str]],
            celda: tuple[int, int, int], titulo: str):
    """Dibuja un cubo 3D con sub-divisiones según el tamaño de cada dimensión y resalta una celda."""
    nx, ny, nz = len(dim_x[1]), len(dim_y[1]), len(dim_z[1])
    # Grilla
    for i in range(nx + 1):
        for j in range(ny + 1):
            ax.plot([i, i], [j, j], [0, nz], color="lightgray", lw=0.4)
    for i in range(nx + 1):
        for k in range(nz + 1):
            ax.plot([i, i], [0, ny], [k, k], color="lightgray", lw=0.4)
    for j in range(ny + 1):
        for k in range(nz + 1):
            ax.plot([0, nx], [j, j], [k, k], color="lightgray", lw=0.4)
    # Aristas exteriores
    for (s, e) in [((0,0,0),(nx,0,0)), ((0,0,0),(0,ny,0)), ((0,0,0),(0,0,nz)),
                   ((nx,ny,0),(0,ny,0)), ((nx,ny,0),(nx,0,0)), ((nx,ny,0),(nx,ny,nz)),
                   ((nx,0,nz),(0,0,nz)), ((nx,0,nz),(nx,0,0)), ((nx,0,nz),(nx,ny,nz)),
                   ((0,ny,nz),(0,ny,0)), ((0,ny,nz),(0,0,nz)), ((0,ny,nz),(nx,ny,nz))]:
        ax.plot(*zip(s, e), color="black", lw=1.2)

    # Celda atómica resaltada
    cx, cy, cz = celda
    verts = [
        [(cx,cy,cz),(cx+1,cy,cz),(cx+1,cy+1,cz),(cx,cy+1,cz)],          # base
        [(cx,cy,cz+1),(cx+1,cy,cz+1),(cx+1,cy+1,cz+1),(cx,cy+1,cz+1)],  # tapa
        [(cx,cy,cz),(cx+1,cy,cz),(cx+1,cy,cz+1),(cx,cy,cz+1)],
        [(cx,cy+1,cz),(cx+1,cy+1,cz),(cx+1,cy+1,cz+1),(cx,cy+1,cz+1)],
        [(cx,cy,cz),(cx,cy+1,cz),(cx,cy+1,cz+1),(cx,cy,cz+1)],
        [(cx+1,cy,cz),(cx+1,cy+1,cz),(cx+1,cy+1,cz+1),(cx+1,cy,cz+1)],
    ]
    col = Poly3DCollection(verts, alpha=0.55, facecolor="#ff7043", edgecolor="black", lw=1.2)
    ax.add_collection3d(col)

    # Ticks con etiquetas
    ax.set_xticks(np.arange(nx) + 0.5); ax.set_xticklabels(dim_x[1], fontsize=7, rotation=15)
    ax.set_yticks(np.arange(ny) + 0.5); ax.set_yticklabels(dim_y[1], fontsize=7)
    ax.set_zticks(np.arange(nz) + 0.5); ax.set_zticklabels(dim_z[1], fontsize=7)
    ax.set_xlabel(dim_x[0], fontsize=10, fontweight="bold", color="#1565c0", labelpad=8)
    ax.set_ylabel(dim_y[0], fontsize=10, fontweight="bold", color="#2e7d32", labelpad=8)
    ax.set_zlabel(dim_z[0], fontsize=10, fontweight="bold", color="#6a1b9a", labelpad=8)
    ax.set_title(titulo, fontsize=11, fontweight="bold")
    ax.view_init(elev=22, azim=-50)
    ax.set_box_aspect((nx, ny, nz))


def panel_atomico(ax, dimensiones: dict[str, str], medidas: dict[str, str], titulo: str = "Dato atómico"):
    """Panel derecho: ficha del dato atómico (dim → valor, medida → valor[unidad])."""
    ax.axis("off")
    ax.set_title(titulo, fontsize=11, fontweight="bold", loc="left")
    y = 0.97
    ax.text(0.02, y, "DIMENSIONES", fontsize=9, fontweight="bold", color="#1565c0",
            transform=ax.transAxes)
    y -= 0.05
    for k, v in dimensiones.items():
        ax.text(0.04, y, f"• {k}:", fontsize=8.5, fontweight="bold", transform=ax.transAxes)
        ax.text(0.45, y, v, fontsize=8.5, transform=ax.transAxes)
        y -= 0.045
    y -= 0.02
    ax.text(0.02, y, "MEDIDAS (hechos)", fontsize=9, fontweight="bold", color="#c62828",
            transform=ax.transAxes)
    y -= 0.05
    for k, v in medidas.items():
        ax.text(0.04, y, f"• {k}:", fontsize=8.5, fontweight="bold", transform=ax.transAxes)
        ax.text(0.45, y, v, fontsize=8.5, transform=ax.transAxes)
        y -= 0.045
    ax.add_patch(Rectangle((0.0, 0.0), 1.0, 1.0, transform=ax.transAxes,
                           fill=False, edgecolor="#ff7043", lw=2))


def generar(problema: str, titulo: str, cubo: dict, atomico: dict):
    fig = plt.figure(figsize=(13, 5.6))
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    cubo_3d(ax1, cubo["x"], cubo["y"], cubo["z"], cubo["celda"], cubo.get("subtitulo", "Hipercubo (3D)"))
    ax2 = fig.add_subplot(1, 2, 2)
    panel_atomico(ax2, atomico["dim"], atomico["med"])
    fig.suptitle(titulo, fontsize=13, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    path = OUT / f"dw_{problema}.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"✅ {path.relative_to(OUT.parents[3])}")


# ------------------------------------------------------------------
# P1. Telemercados
generar("p1_telemercados", "P1 · Telemercados (supermercado online)",
    cubo={
        "x": ("Producto (10 macro)", ["Abarrotes", "Limpieza", "Lácteos", "Bebidas", "..."]),
        "y": ("Tiempo", ["2025-W01", "W02", "W03", "..."]),
        "z": ("Canal/Bodega", ["BodCentro", "BodNorte", "BodSur"]),
        "celda": (0, 1, 0),
        "subtitulo": "Hipercubo: Producto × Tiempo × Bodega",
    },
    atomico={
        "dim": {
            "Producto": "Abarrotes › Arroz › 'Tucapel 1 kg'",
            "Tiempo":   "2025 › S2 › Sem-02 (06-12 ene 2025)",
            "Bodega":   "Bodega Centro (Santiago)",
        },
        "med": {
            "Stock volumen":  "12,5 m³",
            "Stock precio":   "$ 8.430.000 CLP",
            "Ventas $":       "$ 2.150.000 CLP",
            "Ventas unidades":"1.720 unid.",
        },
    })

# ------------------------------------------------------------------
# P2. Materiales de construcción
generar("p2_materiales", "P2 · Materiales de construcción",
    cubo={
        "x": ("Producto\n(categ.→fam.→subfam.→prod.)", ["Cementos", "Fierros", "Pinturas", "Sanitarios", "..."]),
        "y": ("Geografía\n(país→zona→reg.→prov.→com.)", ["Sgto", "Valpo", "BioBio", "..."]),
        "z": ("Tiempo\n(año→sem→trim→mes→sem)", ["2025-Q1", "Q2", "Q3", "Q4"]),
        "celda": (1, 0, 2),
        "subtitulo": "Hipercubo: Producto × Geografía × Tiempo",
    },
    atomico={
        "dim": {
            "Producto":   "Cementos › Grises › Bolsa 25kg › 'Polpaico Especial'",
            "Geografía":  "Chile › Zona Centro › RM › Santiago › Maipú",
            "Tiempo":     "2025 › Sem-1 › Q1 › Marzo › Sem-10",
        },
        "med": {
            "Ventas facturadas $":   "$ 4.580.000 CLP",
            "Ventas a crédito $":    "$ 2.100.000 CLP",
            "Ventas a débito $":     "$ 2.480.000 CLP",
            "Vol. facturado":        "920 sacos",
            "Vol. en depósito":      "150 sacos",
            "Vol. pendiente":        "70 sacos",
        },
    })

# ------------------------------------------------------------------
# P3. Laboratorio de medicamentos
generar("p3_laboratorio", "P3 · Laboratorio de medicamentos (visitadores médicos)",
    cubo={
        "x": ("Médico\n(esp.→region)", ["Cardiol", "Pediat", "Trauma", "..."]),
        "y": ("Producto\n(famil.→fármaco)", ["Antihip", "Analg", "Antib", "..."]),
        "z": ("Tiempo", ["2025-M01", "M02", "M03", "..."]),
        "celda": (0, 2, 1),
        "subtitulo": "Hipercubo: Médico × Producto × Tiempo  (visitador como atributo)",
    },
    atomico={
        "dim": {
            "Médico":     "Dr. Pérez · Cardiología · CESFAM Maipú · RM",
            "Producto":   "Cardiológicos › Antihipertensivos › 'Losartán 50 mg'",
            "Tiempo":     "2025 › Feb › Sem-07",
            "Visitador":  "V. Soto (zona centro-sur)",
        },
        "med": {
            "Nº de visitas":    "3 visitas",
            "Muestras entreg.": "24 unidades",
        },
    })

# ------------------------------------------------------------------
# P4. Crianza de salmones
generar("p4_salmones", "P4 · Crianza de salmones (Chiloé)",
    cubo={
        "x": ("Planta › Criadero", ["Pl-Quellón", "Pl-Castro", "Pl-Ancud", "..."]),
        "y": ("Especie", ["Atlántico", "Coho", "Trucha"]),
        "z": ("Tiempo", ["2025-Q1", "Q2", "Q3", "Q4"]),
        "celda": (1, 0, 1),
        "subtitulo": "Hipercubo: Planta × Especie × Tiempo",
    },
    atomico={
        "dim": {
            "Planta/Criadero": "Planta Castro › Criadero C-3 (jaula 12)",
            "Especie":         "Salmón del Atlántico (Salmo salar)",
            "Tiempo":          "2025 › Q2 › Mayo",
        },
        "med": {
            "Generación de especies": "82 ejemplares / m³",
            "Producción vendida":     "37,4 ton de carne congelada",
        },
    })

# ------------------------------------------------------------------
# P5. Importadora
generar("p5_importadora", "P5 · Importadora",
    cubo={
        "x": ("Cliente\n(tamaño→geografía)", ["Indiv.", "Peq.", "Mediana", "Grande"]),
        "y": ("Producto", ["Línea-A", "Línea-B", "Línea-C", "..."]),
        "z": ("Tiempo", ["2025-Q1", "Q2", "Q3", "Q4"]),
        "celda": (2, 1, 0),
        "subtitulo": "Hipercubo: Cliente × Producto × Tiempo",
    },
    atomico={
        "dim": {
            "Cliente":   "Mediana empresa · 'Comercial Andes Ltda.' · Concepción · BíoBío",
            "Producto":  "Electrónica › Computadores › Notebook 'X-200'",
            "Tiempo":    "2025 › Q1 › Marzo › Sem-12",
        },
        "med": {
            "Costos":      "$ 18.500.000 CLP",
            "Ventas":      "$ 24.700.000 CLP",
            "Descuentos":  "$ 1.200.000 CLP",
        },
    })

# ------------------------------------------------------------------
# P6. Automotora
generar("p6_automotora", "P6 · Automotora",
    cubo={
        "x": ("Auto\n(origen→marca→tipo)", ["Euro", "Amer", "Asiát", "..."]),
        "y": ("Cliente\n(clase preferencia)", ["CarLover", "PadreFam", "Funcional", "Empoderada"]),
        "z": ("Geografía venta", ["Sgto", "Valpo", "Concep", "..."]),
        "celda": (2, 1, 0),
        "subtitulo": "Hipercubo: Auto × Cliente × Geografía  (+ Tiempo)",
    },
    atomico={
        "dim": {
            "Auto":      "Asiático › Toyota › Sedán › 'Corolla 2026'",
            "Cliente":   "PadreDeFamilia · Sr. Rojas (35-50 años, RM)",
            "Geografía": "Sucursal Las Condes · Santiago · RM",
            "Tiempo":    "2025 › Q4 › Diciembre",
        },
        "med": {
            "Costos":      "$ 17.500.000 CLP",
            "Ventas":      "$ 22.900.000 CLP",
            "Descuentos":  "$   900.000 CLP",
        },
    })

# ------------------------------------------------------------------
# P7. Farmacia antroposófica
generar("p7_farmacia", "P7 · Farmacia de medicina antroposófica (e-commerce)",
    cubo={
        "x": ("Producto\n(fam → subfam × 3 niv.)", ["Herbal", "Homeop", "Suplem", "..."]),
        "y": ("Cliente (online)", ["RM", "Valpo", "Sur", "..."]),
        "z": ("Tiempo", ["2025-M01", "M02", "M03", "..."]),
        "celda": (0, 1, 2),
        "subtitulo": "Hipercubo: Producto × Cliente × Tiempo",
    },
    atomico={
        "dim": {
            "Producto":  "Herbales › Tinturas › Calmantes › 'Valeriana 30 ml'",
            "Cliente":   "Cliente #4821 · Mujer · Ñuñoa · RM",
            "Tiempo":    "2025 › Marzo › Sem-11",
        },
        "med": {
            "Ventas $":     "$ 28.400 CLP",
            "Costos $":     "$ 14.900 CLP",
            "Descuentos $": "$  2.840 CLP (10 %)",
        },
    })

# ------------------------------------------------------------------
# P8. Galaxias
generar("p8_galaxias", "P8 · Clasificación de galaxias (Hubble)",
    cubo={
        "x": ("Forma Hubble", ["Elíptica", "Espiral", "Lenticular", "Irregular"]),
        "y": ("Tamaño", ["Gigante", "Grande", "Media", "Pequeña", "Enana"]),
        "z": ("Tiempo de obs.", ["2024", "2025", "2026"]),
        "celda": (1, 0, 1),
        "subtitulo": "Hipercubo: Forma × Tamaño × Tiempo",
    },
    atomico={
        "dim": {
            "Forma":   "Espiral (Sb)",
            "Tamaño":  "Gigante",
            "Tiempo":  "Observación 2025-08-14 (Survey SDSS-V)",
            "Galaxia": "NGC 4321 (M100, Virgo)",
        },
        "med": {
            "Nº aprox. de soles":           "≈ 4 × 10¹¹ M☉",
            "Corrimiento al rojo (z)":      "0,0052 (≈ 1.567 km/s)",
        },
    })

print("\n🎯 Hecho. Figuras en", OUT)
