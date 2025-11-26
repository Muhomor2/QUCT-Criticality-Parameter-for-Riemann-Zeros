# QUCT: Criticality Parameter γ* for Riemann Zeros

This repository contains the reproducibility package for the QUCT (Qadmon Universal Criticality Theory) result: 
the existence and numerical verification of the universal criticality parameter γ*, defined as the unique root 
of F'''(γ)=0 for the QUCT functional.

The project includes:

- Full academic monograph (`docs/quct_monograph.pdf`)
- Python scripts for reproducing γ*
- Measurement protocol comparing γ* with Riemann zeros
- Data samples and metadata
- Ethical license (OSL-ER 1.0)
- CITATION.cff for DOI integration (Zenodo)

This repository corresponds to **Package #1** out of several independent publication units.

## Main result

The QUCT criticality parameter is obtained as the root of:

F'''(γ) = −A a³ e^(−aγ) − B b³ e^(−bγ) + 2μ = 0

with fixed model parameters:

A = 1.0  
a = 3.2  
B = 0.9  
b = 2.6  
μ = 7.439993889526777  

The numerical solution yields:

γ* = 0.3958242245151082

which coincides with the minimizer in the Riemann statistics functional D(γ).

## Contents

- docs/quct_monograph.pdf — full academic paper  
- src/quct_gamma_root.py — analytical γ* solver  
- src/quct_compare_riemann.py — comparison with actual Riemann zeros  
- data/ — sample dataset  
- LICENSE_OSL-ER.txt — ethical research license  
- CITATION.cff — citation metadata  
- checksums.json — cryptographic reproducibility record

## Author

**Igor Chechelnitsky**  
Independent Research, Ashkelon, Israel  
ORCID: https://orcid.org/0009-0007-4607-1946
