# Unidad 3 — Reglas de Asociación

> **Curso**: Inteligencia Computacional · USACH · Prof. Max Chacón
> **Fuente primaria**: [`data/processed/clases/Presentaciones_Prof_Max/capitulo-iii-inteligencia-computaional_ra/`](../../../data/processed/clases/Presentaciones_Prof_Max/capitulo-iii-inteligencia-computaional_ra/capitulo-iii-inteligencia-computaional_ra.md)
> **Bibliografía**: Han, Kamber, Pei — _Data Mining_, caps. 6–7.
> **Carga**: 4 h teoría + Laboratorio L2 · evalúa en **PEP 1**

---

## 1. Objetivos

- Comprender el problema de canasta de mercado (_market basket analysis_).
- Definir formalmente **soporte**, **confianza**, **lift**, **conviction**.
- Dominar **Apriori** y **FP-Growth**.
- Evaluar la calidad de una regla y filtrar reglas espurias.

---

## 2. Marco formal

Sea $\mathcal{I} = \{i_1, i_2, \ldots, i_m\}$ el conjunto de **ítems** y $\mathcal{D} = \{T_1, \ldots, T_n\}$ una base de **transacciones** con $T_k \subseteq \mathcal{I}$.

Una **regla de asociación** tiene la forma:

$$
A \Rightarrow B \quad (s, c), \qquad A, B \subseteq \mathcal{I}, \; A \cap B = \emptyset
$$

- $A$: **antecedente** (cuerpo).
- $B$: **consecuente** (cabeza).
- $s$: soporte. $c$: confianza.

### 2.1 Métricas

| Métrica        | Fórmula                                                                                           | Interpretación                                               |
| -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --- | ----------- | --- | ------------------------------------------ |
| **Soporte**    | $s(A \Rightarrow B) = P(A \cup B) = \dfrac{                                                       | \{T : A \cup B \subseteq T\}                                 | }{  | \mathcal{D} | }$  | Frecuencia conjunta. Mide **prevalencia**. |
| **Confianza**  | $c(A \Rightarrow B) = P(B\mid A) = \dfrac{s(A \cup B)}{s(A)}$                                     | **Probabilidad condicional**.                                |
| **Lift**       | $\text{lift}(A \Rightarrow B) = \dfrac{c(A \Rightarrow B)}{s(B)} = \dfrac{P(A \cap B)}{P(A)P(B)}$ | $>1$ asociación positiva; $=1$ independencia; $<1$ negativa. |
| **Conviction** | $\text{conv}(A \Rightarrow B) = \dfrac{1 - s(B)}{1 - c(A \Rightarrow B)}$                         | $\to \infty$ regla determinista; $=1$ independencia.         |
| **Leverage**   | $P(A\cap B) - P(A)P(B)$                                                                           | Diferencia respecto a independencia.                         |

> **Cuidado con la confianza sola**: una regla puede tener $c$ alta y aun así **no ser informativa** si $s(B)$ es alto (lift $\le 1$).

---

## 3. Tipos de reglas y de items

- **Booleanas**: presencia/ausencia. (`pan ⇒ leche`)
- **Cuantitativas**: requieren discretización previa.
- **Multinivel**: aprovechan jerarquías (`leche` → `leche descremada`).
- **Multidimensionales**: cruzan distintos atributos (`edad ∈ [30,40] ∧ ingreso=alto ⇒ compra=auto`).

---

## 4. El problema combinatorio

Con $m$ ítems hay $2^m - 1$ posibles itemsets y $\sum_{k=1}^{m-1} \binom{m}{k}(2^k - 2)$ posibles reglas. Inviable por fuerza bruta. Toda la familia de algoritmos se basa en una propiedad clave:

> **Propiedad anti-monotónica del soporte** (Apriori property):
> _Si un itemset es frecuente, todos sus subconjuntos son frecuentes. Equivalentemente: si un subconjunto es infrecuente, ningún superconjunto puede serlo._

Esto **poda** drásticamente el espacio de búsqueda.

---

## 5. Algoritmo Apriori (Agrawal & Srikant, 1994)

**Entrada**: $\mathcal{D}$, $s_{\min}$, $c_{\min}$. **Salida**: reglas con $s \ge s_{\min}$ y $c \ge c_{\min}$.

```
L1 ← itemsets de tamaño 1 con soporte ≥ s_min
k ← 2
mientras L_{k-1} ≠ ∅:
    C_k ← apriori_gen(L_{k-1})         # candidatos por unión + poda
    para cada T ∈ D:                   # contar soportes
        para cada c ∈ C_k tal que c ⊆ T:
            c.count += 1
    L_k ← {c ∈ C_k : c.count/|D| ≥ s_min}
    k ← k + 1
F ← ⋃ L_k                              # itemsets frecuentes
para cada f ∈ F y cada partición no vacía (A, B=f\A):
    si s(f)/s(A) ≥ c_min: emitir A ⇒ B
```

**Complejidad**: múltiples pasadas sobre $\mathcal{D}$ (una por nivel). Puede ser costoso en disco.

---

## 6. Algoritmo FP-Growth (Han, 2000)

Mejora a Apriori construyendo un árbol comprimido (**FP-tree**) y minando recursivamente sin generar candidatos.

Pasos:

1. Primer barrido: contar soporte de cada ítem; descartar infrecuentes.
2. Segundo barrido: ordenar ítems de cada transacción por soporte decreciente e insertarlos en el FP-tree.
3. Para cada ítem (de menor a mayor soporte): construir el **conditional pattern base** y un FP-tree condicional, y minarlo recursivamente.

**Ventaja**: dos pasadas sobre $\mathcal{D}$ y sin generación de candidatos. **Desventaja**: alto consumo de memoria si el árbol es ancho.

---

## 7. Ejemplo numérico (Apriori)

Sea $\mathcal{D}$ con 5 transacciones e $\mathcal{I} = \{a,b,c,d,e\}$:

| TID | Items      |
| --- | ---------- |
| 1   | a, b, e    |
| 2   | b, c, d    |
| 3   | a, b, e    |
| 4   | a, c, d    |
| 5   | a, b, c, d |

Con $s_{\min} = 0.4$ (al menos 2 transacciones):

- $L_1$: $\{a\}_4, \{b\}_4, \{c\}_3, \{d\}_3, \{e\}_2$.
- $C_2$: todas las parejas. $L_2$: $\{a,b\}_3, \{a,c\}_2, \{a,d\}_2, \{a,e\}_2, \{b,c\}_2, \{b,d\}_2, \{b,e\}_2, \{c,d\}_3$.
- $C_3$: candidatos generados por unión. $L_3$: $\{a,b,e\}_2$, $\{b,c,d\}_2$.

Regla `e ⇒ {a,b}`:

- $s = 2/5 = 0.40$
- $c = 2/2 = 1.00$
- $\text{lift} = 1.00 / (3/5) = 1.667$ → asociación positiva fuerte.

---

## 8. Filtrado y validación

- **Reglas redundantes**: si $A \Rightarrow B$ tiene la misma confianza que $A' \Rightarrow B$ con $A \subset A'$, $A'\Rightarrow B$ es redundante.
- **Reglas espurias por azar**: aplicar **test estadístico** ($\chi^2$ de independencia) sobre la tabla de contingencia $A$ × $B$.
- **Diversidad**: usar lift y conviction, no sólo confianza.

---

## 9. Reglas de asociación en el pipeline KDD

| Etapa KDD         | Rol                                                               |
| ----------------- | ----------------------------------------------------------------- |
| Pre-procesamiento | Discretización de variables numéricas (binning, equal-frequency). |
| Transformación    | Codificación booleana (one-hot por ítem).                         |
| Minería           | Apriori / FP-Growth.                                              |
| Evaluación        | Lift, conviction, $\chi^2$, expert review.                        |

---

## 10. Conceptos clave para PEP 1

- Definiciones formales de soporte, confianza, lift y conviction (memorizar).
- **Propiedad anti-monotónica** y cómo se usa para podar.
- Saber ejecutar **Apriori a mano** sobre una base pequeña: generación de $C_k$, poda y conteo.
- Distinguir cuándo una regla con alta confianza es **engañosa** (lift ≤ 1).

---

## 11. Recursos

- Notebook: [03_reglas_asociacion.ipynb](../../../notebooks/ejercicios/03_reglas_asociacion.ipynb).
- Han, Kamber, Pei, _Data Mining: Concepts and Techniques_, 3rd ed., Caps. 6–7.
- `mlxtend.frequent_patterns`: `apriori`, `fpgrowth`, `association_rules`.
- Agrawal, R.; Srikant, R. (1994). _Fast Algorithms for Mining Association Rules_. VLDB.
- Han, J.; Pei, J.; Yin, Y. (2000). _Mining Frequent Patterns without Candidate Generation_. SIGMOD.
