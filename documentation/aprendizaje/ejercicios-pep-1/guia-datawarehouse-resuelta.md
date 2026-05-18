# Guía de Ejercicios Resueltos — Datawarehouse (DW)

> **Inteligencia Computacional · USACH · Prof. Max Chacón**
> Ayudante: Sebastián Chávez Orellana · Primer semestre 2026
> Fuente: `data/raw/ayudantias/IC_Ejercicios_Datawarehouse.pdf`
> Material procesado en: `data/processed/ayudantias/ic_ejercicios_datawarehouse/`

---

## Marco teórico común

La **estructura de datos más usada en un Datawarehouse** es el **modelo multidimensional** materializado como **esquema en estrella (star schema)**:

- Una **tabla de hechos** (fact table) central → contiene las **medidas** numéricas y aditivas del negocio.
- Varias **tablas de dimensión** (dimension tables) → describen el **contexto** (quién, qué, cuándo, dónde) y suelen ser **jerárquicas** (drill-down / roll-up).
- El **hipercubo (OLAP cube)** es la **vista lógica**: un arreglo n-dimensional donde cada celda es un **dato atómico** = combinación única de valores de todas las dimensiones, junto a sus medidas.

```
       ┌──────────────┐
       │   DIM_TIEMPO │
       └──────┬───────┘
              │
DIM_PROD ────►┌──────────┐◄──── DIM_GEOGRAFIA
              │  HECHOS  │
DIM_CLIENTE ─►│  ventas$ │◄──── ...
              │  unidades│
              └──────────┘
```

- **Dato atómico**: la fila más fina de la tabla de hechos (no agregada). Define el **grano (grain)** del DW.
- **Cuando hay más de 3 dimensiones**, hablamos de **hipercubo**; gráficamente se dibujan en 3D los 3 ejes principales y el resto se incorpora como "rebanadas" (slicing).

> Nomenclatura usada en cada problema: **#dim** = número de dimensiones; **grano** = nivel atómico de la tabla de hechos.

---

## P1 · Telemercados (supermercado online)

**Enunciado.** Telemercados con 10 macro grupos (Abarrotes, Limpieza, …). Medir **stock** (volumen y precio) y **ventas**.

### Modelado

| Componente | Detalle |
|---|---|
| **Dimensiones** | **Producto** (Macro-grupo → Familia → SKU); **Tiempo** (Año → Semestre → Mes → Semana → Día); **Bodega/Canal** (CD nacional → Bodega regional) |
| **Medidas (hechos)** | `stock_volumen` [m³] · `stock_precio` [CLP] · `ventas_monto` [CLP] · `ventas_unidades` [unid] |
| **Grano** | 1 fila por **(SKU, día, bodega)** |

![P1 Hipercubo y dato atómico](figuras/dw_p1_telemercados.png)

**Dato atómico (ejemplo).**

| Producto | Tiempo | Bodega | Stock vol. | Stock $ | Ventas $ | Ventas unid. |
|---|---|---|---|---|---|---|
| Abarrotes › Arroz › "Tucapel 1 kg" | 2025 · S2 · Sem-02 | Bodega Centro (Stgo) | 12,5 m³ | $ 8.430.000 | $ 2.150.000 | 1.720 |

> **Nota:** stock y ventas son aditivas en Producto y Geografía, pero el **stock no es aditivo en el tiempo** (snapshot). Se usa el operador `LAST_NON_EMPTY` para roll-up temporal.

---

## P2 · Materiales de construcción

**Enunciado.** Distribuidora con jerarquías ricas en Producto, Geografía y Tiempo. Mide ventas en dinero y en volumen, con varios sub-tipos.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_PRODUCTO** | Categoría → Grupo familia → Familia → Sub-familia → Producto |
| **DIM_GEOGRAFIA** | País → Zona → Región → Provincia → Comuna |
| **DIM_TIEMPO** | Año → Semestre → Trimestre → Mes → Semana |
| **Medidas $** | `ventas_facturadas_$` · `ventas_credito_$` · `ventas_debito_$` |
| **Medidas volumen** | `vol_facturado` · `vol_deposito` · `vol_pendiente` (unid. del producto) |
| **Grano** | 1 fila por **(Producto, Comuna, Semana)** |

![P2 Hipercubo y dato atómico](figuras/dw_p2_materiales.png)

**Dato atómico (ejemplo).**

| Producto | Geografía | Tiempo | Ventas $ (fact/créd/déb) | Vol. (fact/depós/pend) |
|---|---|---|---|---|
| Cementos › Grises › Bolsa 25 kg › "Polpaico Especial" | Chile › Centro › RM › Stgo › Maipú | 2025 · Q1 · Mar · S-10 | $ 4.580.000 / $ 2.100.000 / $ 2.480.000 | 920 / 150 / 70 sacos |

> Verificación de consistencia: `ventas_facturadas_$ = ventas_credito_$ + ventas_debito_$` (debe cumplirse fila a fila).

---

## P3 · Laboratorio de medicamentos (visitadores médicos)

**Enunciado.** DW para conocer **penetración territorial y de productos** vía visitas y muestras entregadas.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_MEDICO** | Médico → Especialidad → Centro → Comuna → Región |
| **DIM_PRODUCTO** | Familia terapéutica → Sub-familia → Fármaco (principio activo + presentación) |
| **DIM_TIEMPO** | Año → Mes → Semana → Día |
| **DIM_VISITADOR** | Visitador → Zona → Distrito (a veces se modela como dimensión, a veces como atributo del hecho) |
| **Medidas** | `n_visitas` [conteo] · `n_muestras_entregadas` [unid.] |
| **Grano** | 1 fila por **(Médico, Producto, Día, Visitador)** |

![P3 Hipercubo y dato atómico](figuras/dw_p3_laboratorio.png)

**Dato atómico (ejemplo).**

| Médico | Producto | Tiempo | Visitador | Nº visitas | Muestras |
|---|---|---|---|---|---|
| Dr. Pérez · Cardiología · CESFAM Maipú · RM | Cardiológicos › Antihipertensivos › Losartán 50 mg | 2025 · Feb · S-07 | V. Soto | 3 | 24 |

> **KPIs derivados típicos:** muestras/visita, cobertura territorial (% médicos visitados al menos 1 vez en el período), frecuencia de visita por especialidad.

---

## P4 · Crianza de salmones (Chiloé)

**Enunciado.** Plantas en distintos lugares de Chiloé; cada planta tiene varios criadores. Medir **generación de especies por m³** y **producción vendida (ton carne congelada)**.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_PLANTA** | Región → Comuna → Planta → Criadero (jaula) |
| **DIM_ESPECIE** | Especie comercial (Atlántico, Coho, Trucha) |
| **DIM_TIEMPO** | Año → Trimestre → Mes |
| **Medidas** | `generacion` [ejemplares / m³] · `produccion_vendida` [ton carne congelada] · `volumen_jaula` [m³] (atributo) |
| **Grano** | 1 fila por **(Criadero, Especie, Mes)** |

![P4 Hipercubo y dato atómico](figuras/dw_p4_salmones.png)

**Dato atómico (ejemplo).**

| Planta/Criadero | Especie | Tiempo | Generación | Producción vendida |
|---|---|---|---|---|
| Planta Castro › Criadero C-3 (jaula 12) | Salmón del Atlántico | 2025 · Q2 · Mayo | 82 ejemp./m³ | 37,4 ton |

> **Cuidado con la aditividad:** `generacion` es una **razón** (ejemp./m³) ⇒ **no aditiva** — para roll-up debe usarse `SUM(ejemplares) / SUM(m³)` y no promediar la razón.

---

## P5 · Importadora

**Enunciado.** Importadora orientada al estudio de clientes (clasificados por localización geográfica y tamaño: individuales / pequeñas / medianas / grandes). Analizar **costos, ventas y descuentos**.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_CLIENTE** | Tamaño (Indiv/Peq/Med/Grande) → País → Región → Comuna → Cliente |
| **DIM_PRODUCTO** | Línea → Familia → SKU |
| **DIM_TIEMPO** | Año → Trimestre → Mes → Semana → Día |
| **Medidas** | `costos_$` · `ventas_$` · `descuentos_$` |
| **Grano** | 1 fila por **(Cliente, SKU, Día)** |

![P5 Hipercubo y dato atómico](figuras/dw_p5_importadora.png)

**Dato atómico (ejemplo).**

| Cliente | Producto | Tiempo | Costos | Ventas | Descuentos |
|---|---|---|---|---|---|
| Mediana · "Comercial Andes Ltda." · Concepción · BíoBío | Electrónica › Computadores › Notebook "X-200" | 2025 · Q1 · Mar · S-12 | $ 18.500.000 | $ 24.700.000 | $ 1.200.000 |

> **Métricas derivadas:** margen = ventas − costos − descuentos; tasa de descuento = descuentos / ventas; análisis por **segmento** (Tamaño × Región).

---

## P6 · Automotora

**Enunciado.** Automotora nacional con >60 marcas. Autos clasificados por **origen** (europeos/americanos/asiáticos…) → **marca** → **tipo carrocería** (sedán, citycar, hatchback…). Clientes segmentados por **clase de preferencia** (CarLovers, PadreDeFamilia, Funcional, Empoderada…). Hay sucursales en todo Chile. Analizar **costos, ventas y descuentos**.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_AUTO** | Origen → Marca → Modelo → Tipo (sedán/citycar/hatchback/SUV/…) → VIN |
| **DIM_CLIENTE** | Clase preferencia (CarLover/PadreFam/Funcional/Empoderada/…) → Cliente |
| **DIM_GEOGRAFIA** | País → Región → Comuna → Sucursal |
| **DIM_TIEMPO** | Año → Trimestre → Mes → Día |
| **Medidas** | `costos_$` · `ventas_$` · `descuentos_$` · `unidades_vendidas` [conteo] |
| **Grano** | 1 fila por **(VIN, Cliente, Sucursal, Día)** |

![P6 Hipercubo y dato atómico](figuras/dw_p6_automotora.png)

**Dato atómico (ejemplo).**

| Auto | Cliente | Geografía | Tiempo | Costos | Ventas | Descuentos |
|---|---|---|---|---|---|---|
| Asiático › Toyota › Sedán › "Corolla 2026" | PadreDeFamilia · Sr. Rojas | Sucursal Las Condes · Stgo · RM | 2025 · Q4 · Dic | $ 17.500.000 | $ 22.900.000 | $ 900.000 |

> Como el ejercicio pide **esquemas en 3 dimensiones**, el hipercubo se grafica con `Auto × Cliente × Geografía` y la dimensión **Tiempo** se introduce como rebanadas (slicing); en práctica el cubo OLAP es 4-D.

---

## P7 · Farmacia de medicina antroposófica

**Enunciado.** 15 familias de productos con **3 niveles** de subdivisión, ventas sólo por internet. Medir descuentos, costos y ventas.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_PRODUCTO** | Familia (15) → Subfamilia → Sub-subfamilia → SKU |
| **DIM_CLIENTE** | Cliente → Comuna → Región (canal e-commerce) |
| **DIM_TIEMPO** | Año → Mes → Semana → Día |
| **Medidas** | `ventas_$` · `costos_$` · `descuentos_$` |
| **Grano** | 1 fila por **(SKU, Cliente, Día)** |

![P7 Hipercubo y dato atómico](figuras/dw_p7_farmacia.png)

**Dato atómico (ejemplo).**

| Producto | Cliente | Tiempo | Ventas | Costos | Descuentos |
|---|---|---|---|---|---|
| Herbales › Tinturas › Calmantes › "Valeriana 30 ml" | Cliente #4821 · Ñuñoa · RM | 2025 · Mar · S-11 | $ 28.400 | $ 14.900 | $ 2.840 (10 %) |

> **Particularidad del e-commerce:** la dimensión geográfica reside en el **cliente** (no hay sucursal); la dimensión "Canal" se omite o es constante = "Web".

---

## P8 · Clasificación de galaxias

**Enunciado.** DW astronómico. Clasificar por **estructura de Hubble** (elípticas/espirales/lenticulares/irregulares) y **tamaño** (gigante/grande/mediana/pequeña/enana). Medir **n° aproximado de soles** y **corrimiento al rojo (z)** por efecto Doppler.

### Modelado

| Componente | Detalle |
|---|---|
| **DIM_FORMA** | Hubble (E / S / S0 / Irr) → sub-tipo (Sa, Sb, Sc, …) |
| **DIM_TAMAÑO** | Gigante / Grande / Mediana / Pequeña / Enana |
| **DIM_TIEMPO** | Año observación → Survey/Misión |
| **DIM_GALAXIA** (degenerada) | Identificador (NGC/M/…) → constelación |
| **Medidas (hechos)** | `n_soles` [masas solares M☉] · `redshift_z` [adim. → km/s vía c·z] |
| **Grano** | 1 fila por **(Galaxia, observación)** |

![P8 Hipercubo y dato atómico](figuras/dw_p8_galaxias.png)

**Dato atómico (ejemplo).**

| Forma | Tamaño | Tiempo | Galaxia | Nº soles | z (Doppler) |
|---|---|---|---|---|---|
| Espiral (Sb) | Gigante | 2025-08-14 (SDSS-V) | NGC 4321 (M100) | ≈ 4·10¹¹ M☉ | 0,0052 (≈ 1.567 km/s) |

> **Cuidado:** `redshift_z` es **no aditiva** (es un cociente físico). Para agregación se usa el **promedio ponderado por luminosidad** o se trabaja con la velocidad recesional `v = c·z` y se promedia.

---

## Resumen — modelo común y diferencias

| Problema | Dimensiones (principales) | Medidas | Grano | Particularidad |
|----------|---------------------------|---------|-------|-----------------|
| P1 Telemercados | Producto · Tiempo · Bodega | stock vol/$, ventas $/u | (SKU, día, bodega) | Stock no aditivo en tiempo |
| P2 Mat. construcción | Producto · Geografía · Tiempo (3 jerarquías) | 3 medidas $ + 3 medidas vol. | (SKU, comuna, semana) | Coherencia fact = créd + déb |
| P3 Laboratorio | Médico · Producto · Tiempo (+Visitador) | visitas, muestras | (médico, prod, día, visit.) | Visitador como atributo o dimensión |
| P4 Salmones | Planta/Criadero · Especie · Tiempo | generación/m³, ton vendidas | (criadero, especie, mes) | Razón no aditiva |
| P5 Importadora | Cliente (tamaño+geo) · Producto · Tiempo | costos, ventas, dctos | (cliente, SKU, día) | Segmentación por tamaño |
| P6 Automotora | Auto · Cliente · Geografía · Tiempo | costos, ventas, dctos | (VIN, cliente, suc., día) | 4-D, se grafica en 3-D + slicing |
| P7 Farmacia antrop. | Producto (3 niveles) · Cliente · Tiempo | ventas, costos, dctos | (SKU, cliente, día) | Sólo canal online |
| P8 Galaxias | Forma · Tamaño · Tiempo (+galaxia) | nº soles, redshift z | (galaxia, observación) | Medidas no aditivas |

### Reglas para identificar dimensiones y medidas (chuleta PEP 1)

1. **Sustantivos descriptivos → dimensiones** (quién, qué, cuándo, dónde).
2. **Verbos / cantidades numéricas → medidas** (cuánto, cuántas veces).
3. **Toda jerarquía** (`País › Región › Comuna` o `Familia › SubFam › SKU`) es una **dimensión única** con varios niveles, no varias dimensiones.
4. **Tiempo siempre es dimensión** aunque no se mencione explícitamente.
5. **Aditividad** de la medida: revisar antes de definir el OLAP — `aditiva` (ventas, unidades), `semi-aditiva` (stock = sólo en no-tiempo) o `no aditiva` (razones, porcentajes, z).

---

## Cómo se generaron las figuras

Script: [`scripts/utils/dw_hipercubos.py`](../../../scripts/utils/dw_hipercubos.py) — usa `matplotlib` 3D para dibujar cada hipercubo con etiquetas en los 3 ejes y resaltar la **celda atómica** correspondiente al dato de ejemplo, junto a una ficha lateral con dimensiones y medidas.

Regenerar:

```powershell
python scripts/utils/dw_hipercubos.py
```
