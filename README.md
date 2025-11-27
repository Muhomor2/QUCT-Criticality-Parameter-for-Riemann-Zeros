# QUCT: Criticality Parameter gamma* for Riemann Zeros

**Author:** Igor Chechelnitsky  
**Affiliation:** Independent Research, Ashkelon, Israel  
**ORCID:** 0009-0007-4607-1946  

This repository contains the **QUCT (Qadmon Universal Criticality Theory)** code and documentation for the numerical extraction of a **dimensionless criticality parameter** `gamma*` from a variational stability functional and its planned comparison with the spectral statistics of the non-trivial zeros of the Riemann zeta function.

The focus of this repository is **Package #1**:

> A clean, reproducible definition and high-precision computation of  
> `gamma* ≈ 0.3958242245`  
> as the unique root of the third derivative  
> `F'''(gamma) = 0`  
> for a fixed set of model parameters.

No speculative or “esoteric” content is included here. Only the **mathematics, code, and reproducibility** aspects of the QUCT gamma* model.

---

## 1. Mathematical model (QUCT functional)

The QUCT stability functional is defined as

\[
F(\gamma) = A e^{-a \gamma} + B e^{-b \gamma} + \mu \gamma^2 + C,
\]

with fixed parameters

- `A = 1.0`  
- `a = 3.2`  
- `B = 0.9`  
- `b = 2.6`  
- `mu = 7.439993889526777`  

The constant `C` is irrelevant for the criticality condition.

The **criticality parameter** `gamma*` is defined as the unique solution of

\[
F'''(\gamma) = 0,
\]

i.e. of the scalar equation

\[
A a^3 e^{-a \gamma} + B b^3 e^{-b \gamma} = 2 \,\mu
\]

in the interval `gamma ∈ (0, 1)`.

With the parameter set above, numerical root finding gives

\[
gamma*_{QUCT} ≈ 0.3958242245151082
\]

with very small residual `|F'''(gamma*)|`.

---

## 2. Repository structure

```text
QUCT-Criticality-Parameter-for-Riemann-Zeros/
├── src/
│   ├── quct_gamma_root.py        # High-precision root finder for F'''(gamma)=0
│   └── quct_compare_riemann.py   # (Optional) future comparison to Riemann zeros
│
├── docs/
│   └── quct_gamma_star.tex       # LaTeX source of the short academic report
│
├── data/
│   └── sample_zeros.csv          # (Optional) small example dataset of zeros
│
├── LICENSE_OSL-ER.txt            # Open Science License with ethical restrictions
├── README.md                     # This file
├── CITATION.cff                  # Citation metadata for GitHub and Zenodo
└── .zenodo.json                  # Zenodo metadata for GitHub → Zenodo archiving
