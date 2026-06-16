## Project: Li electrodeposition - glyme electrolytes

**June 4**

### Goal
Screen electrolyte **240604-B** for stable Li plating at 30°C.

### Electrolyte Composition & Preparation
*   Solvent: 1 M LiTFSI in diglyme : EtOH (4:1 v/v)
*   Volume: 20 mL (ct+)
*   Additive: **8% by weight**, 5 mol% $\text{crown-ether}$ ($\mathbf{12}\cdot$coronae-$e-\beta$ or similar reference notation in source). *Correction based on standard LiTFSI literature context usually implies a specific cyclic ether, but adhering strictly to text logic:* Add **8%** (by weight implied by 'ct+') of 5 mol% 1-crown-4 as additive.
*   Stirring time: 20 min

**Conditions:** $T = 22.4^\circ\text{C}$, glovebox $\mathrm{H_2O} < 1 \,\text{ppm}$.

### Electrochemical Setup
*   **Working electrode:** Glassy C RDE ($A_{geo} = 0.3 \,\text{cm}^2$)
*   **Counter electrode (CE):** Li foil
*   **Reference electrode (ref):** Ag/AgCl

---

## Deposition run: 240604-B1

**Deposition parameters:** Apply $-0.45\, \text{V}$ vs $\mathrm{Ag}/\mathrm{AgCl}$ for 90 min at rotation speed ($w$) = 1600 rpm.

### Charge Calculation
Given current density and geometric area:
$$J = 0.50 \frac{\,\mathrm{mA}}{\,\text{cm}^2}, \quad A_{geo} = 0.3 \,\text{cm}^2$$

Total Current ($I$):
$$I = J \cdot A_{geo} = (0.5\, \mathrm{mA}) \cdot (0.3 \,\text{cm}^2) = 1.5\times10^{-4}\, \mathrm{A}$$

Deposition time ($t$):
$$t = 90\, \text{min} = 5400\, \text{s}$$

Total Charge deposited ($Q$):
$$Q = I \cdot t = (1.5\times10^{-4}\,\mathrm{A}) \cdot (5400\,\mathrm{s}) = 0.81\,\mathrm{A\cdot s} = 0.81\,\text{C}$$

Theoretical Li deposition ($n$) assuming $M_{Li^+}=6.94\, \text{g/mol}$ and Faraday's constant $F=96485\, \mathrm{C/mol}$:
$$n := Q / (2F) = 0.81\,\frac{\text{C}}{2\,(96485\,\text{C/mol})} = 8.4 \times 10^{-6}\,\text{mol Li}^+$$

Mass of Lithium deposited:
$m_{Li} = n \cdot M_{Li} = (8.4 \times 10^{-6}\, \mathrm{mol}) \cdot (6.94\, \mathrm{g/mol})$

Charge transfer efficiency check ($n_e/e^-$):
$$5.8\times 10^{-5} e^- \approx 1\,\text{Li}^+$$

### Electrode Temperature Test: Hot Plate Heating
Target setpoint: **30°C**.  
*Observation (F): Visual appearance "grey + dull".*

| Time | Temperature ($^\circ$C) |
| :--- | :--- |
| 0 min | $22.4\,^\circ\text{C}$ |
| 1 min | $23.1\,^\circ\text{C}$ |
| 5 min | $25.6\,^\circ\text{C}$ |
| 10 min | $27.9\,^\circ\text{C}$ |
| 20 min | $30.1\,^\circ\text{C}$ |
| 40 min | $31.5\,^\circ\text{C}$ |
| 60 min (1 hr) | $32.0\,^\circ\text{C}$ |
| 90 min (1 hr 30 min) | $32.6\,^\circ\text{C}$ |

### Structural Analysis (XRD)
Main peak position ($2\theta$): **$2.1^\circ$** (low intensity).  
Shoulder at: **$4.7^\circ$**.