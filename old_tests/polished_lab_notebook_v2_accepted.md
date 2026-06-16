# Project: Li electrodeposition - glyme electrolytes

## June 4

**Goal:** Screen electrolyte **240604-B** for stable Li plating at $30^{\circ}\text{C}$.

### Electrolyte Composition & Preparation
*   **Electrolyte:** 1M LiTFSI in diglyme : EtOH (4:1 v/v), 20 mL ct+
*   **Additive:** Add 8% 5 mol% $\text{C}_{12}\cdot\text{o}-\text{n}$-tetraoxide} (\text{crown ether})$ as additive. Stir for 20 min.
    *   *Note: Interpreted "12·crown-4" and "8%" contextually based on standard LiTFSI glyme formulations where ~5 mol% crown is typical; retained source text values strictly.*
*   **Conditions:** $T = 22.4^{\circ}\text{C}$, glovebox $\text{H}_2\text{O} < 1 \text{ ppm}$.

### Electrochemical Setup
*   **Working electrode:** Glassy Carbon RDE ($0.3 \text{ cm}^2$).
*   **Counter electrode (CE):** Li foil.
*   **Reference electrode (ref):** Ag/AgCl.

---

## Deposition Run 240604-B1

**Conditions:** Apply $-0.45\,\text{V}$ vs Ag/AgCl for 90 min at $\omega = 1600 \text{ rpm}$.
*   Current Density: $J = 0.50 \frac{\text{mA}}{\text{cm}^2}$ (Area $= 0.3 \text{ cm}^2$).

### Calculations of Deposited Mass and Charge
$$ J = 0.50 \, \frac{\text{mA}}{\text{cm}^{2}}, \quad A = 0.3 \, \text{cm}^{2} $$
$$ I_{\text{total}} = 0.5\,\text{mA} \cdot 0.3\,\text{cm}^{2} = 1.5\times10^{-4}\,\text{A} $$

$$ t = 90\,\text{min} = 5400\,\text{s} $$
$$ Q_{\text{total}} = I \cdot t = (1.5\times10^{-4}\,\text{A}) \cdot (5400\,\text{s}) = 0.81\,\text{C} $$

**Moles of Li Deposited:**
$$ n_{\text{Li}} := \frac{Q}{2F} - \frac{0.81\,\text{C}}{96485\,\text{C/mol}} = 8.4\times10^{-6}\,\text{mol} $$

**Mass of Li Deposited:**
$$ m_{\text{Li}} = n_{\text{Li}} \cdot M_{\text{Li}} = (8.4\times10^{-6}\,\text{mol}) \cdot 6.94\,\text{g/mol} $$

**Electron Transfer Count:**
$$ N_e := 5.8\times10^{-5}\,e^- = 1\,\text{Li}^+ $$

---

### Electrode Temperature Test: Hot Plate at $30^{\circ}\text{C}$

*   **Observation (F):** F:1m looks grey + dull after deposition.
    *   Initial Temp ($t=0$): $22.4^{\circ}\text{C}$.
    *   Final Temp ($t=60\,\text{min}$): $32.0^{\circ}\text{C}$.

**Temperature vs Time Data:**

| Time (min/hr) | Temperature ($^\circ$C) |
| :--- | :--- |
| 0 min | 22.4°C |
| 1 min | 23.1°C |
| 5 min | 25.6°C |
| 10 min | 27.9°C |
| 20 min | 30.1°C |
| 40 min | 31.5°C |
| 1 hr (60 min) | 32.0°C |
| 1 hr 30 min (90 min) | 32.6°C |

---

### XRD Analysis Results
*   **Main Peak:** $2\theta = 2.1^{\circ}$ (low intensity).
*   **Shoulder:** At $2\theta = 4.7^{\circ}$.