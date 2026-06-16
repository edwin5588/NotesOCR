# Project: Li Electrodeposition - Glyme Electrolytes

## June 4

**Goal:** Screen electrolyte **240604-B** for stable Li plating at $30^\circ\text{C}$.

### Experimental Conditions
*   **Electrolyte Composition:** 1 M LiTFSI in diglyme : EtOH (4:1 v/v), 20 mL ct+.
*   **Additive:** 8% by weight, 5 mol% 12·crown-4.
*   **Preparation:** Stirred for 20 min.
    *   Target Temperature ($T$): $22.4^\circ\text{C}$.
    *   Glovebox Conditions: $\text{H}_2\text{O} < 1 \text{ ppm}$.

### Electrochemical Setup
*   **Working Electrode:** Glassy Carbon RDE (0.3 cm²).
*   **Counter Electrode (CE):** Li foil.
*   **Reference Electrode (Ref):** Ag/AgCl.

---

## Deposition Run 240604-B1

**Conditions Applied:** $-0.45 \text{ V}$ vs Ag/AgCl, duration = 90 min, rotation speed ($w$) = 1600 rpm.
*   Current Density: $J = 0.50 \frac{\text{mA}}{\text{cm}^2}$.

### Calculations of Deposited Mass and Charge

$$ J = 0.50 \, \frac{\text{mA}}{\text{cm}^{2}}, \quad A_{\text{elec}} = 0.3 \, \text{cm}^{2} $$
$$ I = (0.5 \times 10^{-3} \,\text{A/cm}^2) \cdot (0.3 \,\text{cm}^2) = 1.5\times10^{-4}\,\text{A} $$

$$ t_{\text{dep}} = 90 \, \text{min} = 5400 \, \text{s} $$
$$ Q = I \cdot t = (1.5\times10^{-4}\,\text{A}) \cdot (5400\,\text{s}) = 0.81 \, \text{C} $$

**Moles of Li Deposited:**
Assuming $n=2$ electrons per $\text{Li}$:
$$ n_{\text{mol}} := \frac{Q}{2F} - \frac{0.81 \,\text{C}}{96485 \, \text{C/mol}} = 8.4 \times 10^{-6} \, \text{mol} $$

**Mass of Li Deposited:**
$$ m_{\text{Li}} = n_{\text{mol}} \cdot M_{\text{Li}} = (8.4 \times 10^{-6} \,\text{mol}) \cdot (6.94 \, \text{g/mol}) $$

**Charge Balance:**
$$ e^- : \text{Li}^+ = 5.8\times10^{-5} : 1 $$

---

## Electrode Temperature Test: Hot Plate at $30^\circ\text{C}$

*   **Observation (F):** 1 M solution appears grey + dull upon deposition.

| Time | Temperature ($^\circ\text{C}$) |
| :--- | :--- |
| **0 min** | $22.4$ |
| **1 min** | $23.1$ |
| **5 min** | $25.6$ |
| **10 min** | $27.9$ |
| **20 min** | $30.1$ |
| **40 min** | $31.5$ |
| **1 hr** | $32.0$ |
| **1 hr 30 min** | $32.6$ |

### XRD Analysis (Main Peak)
*   Position ($2\theta$): $2.1^\circ$ (Low intensity).
*   Feature: Shoulder at $2\theta = 4.7^\circ$.

---

## Conclusion and Findings

The screening of electrolyte **240604-B** (1 M LiTFSI in diglyme/EtOH with 5 mol% crown ether) under deposition conditions ($-0.45 \text{ V}$, $90$ min) resulted in a calculated lithium deposit mass derived from the charge passed ($Q = 0.81 \text{ C}$). The stoichiometry indicates an electron-to-lithium ratio of approximately $5.8\times10^{-5} : 1$.

Thermal stability testing revealed that while the target temperature was set at $30^\circ\text{C}$, significant heating occurred during operation; within one hour and thirty minutes, the solution temperature rose to $32.6^\circ\text{C}$ starting from an initial $22.4^\circ\text{C}$. Visually, the 1 M electrolyte exhibited a grey and dull appearance post-deposition. XRD analysis identified a low-intensity main peak at $2.1^\circ$ with a shoulder at $4.7^\circ$, suggesting potential phase formation or impurity presence that warrants further investigation regarding crystallographic structure stability in this glyme-based system.