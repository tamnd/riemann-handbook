---
id: h-statement-of
title: Hörmander's estimate from an a priori inequality and weak regularity
kind: theorem
decl: ReciprocityTheory.L2DbarEstimates.F.hStatement_of
module: ReciprocityTheory.L2DbarEstimates.HormanderEstimate.HStatementOf
covers: 320
status: drafted
drafted_by: writer@claude
---
This theorem proves `HStatement`, the estimate of [Hörmander's L2 estimate on étale Stein spaces](/entry/hormander/), from eight analytic statements. The literature layer of the proof ([EveryCharacter from the literature and VWin](/step/every-character-of-literature/)) uses the result through `hormander`.

## Statement

**Theorem.** Suppose `APStatement`, `TStarIbpStatement`, `ChainStatement`, `C.RegStatement` and four mollifier statements on $\mathbb{C}^n$ (`GraphSt`, `SmoothSt`, `SupportSt`, `StdSt`). Then `HStatement n M` holds.

The main analytic input is `APStatement`, a twisted a priori inequality. For a test form $f$, a weight $\varphi$ of class $C^2$, a twist $\psi$ of class $C^1$ and $\varepsilon > 0$, it bounds $\int (\operatorname{Re}\mathcal{L}_\varphi(f, f) - (1 + 1/\varepsilon)|\partial\psi|^2 |f|^2) e^{-\varphi}$ by $(1 + \varepsilon)\|T^* f\|^2$ plus a $\bar\partial f$ term. Here $T^*$ is the formal adjoint from `TStarIbpStatement`.

## Proof

The proof builds two statements and gives them to `F.hormander`.

1. **The test inequality** (`TestIneqStatement`). Put $A = \int h\, e^{-\varphi}$ and suppose $A < \infty$. For each test form $f$, $|\langle \bar\partial F_0, f\rangle_\varphi|^2 \le A\, \|T^* f\|_\varphi^2$. The proof `testIneq` joins a choice of cutoff and twist (`choice`, from `ChainStatement`), a primed inequality from `APStatement`, and a closure step (`closureIneq`). The closure step uses density of test forms, which comes from localisation, a flat chart and the mollifier statements. We did not open these lemmas.
2. **Weak regularity** (`RegMStatement`, built by `regM` from `C.RegStatement`). A locally $L^2$ function $F$ with $\int F\, \bar\partial_j \phi\, d\mathrm{vol} = 0$ for all test functions $\phi$ is almost everywhere equal to a holomorphic function.

`F.hormander` then runs the functional analysis.

- If $A = \infty$, take $F = 0$.
- If not, the test inequality and `rieszOnRange` give $u$ in the weighted $L^2$ space with $\|u\|^2 \le A$ and $\langle u, T^* f\rangle = \langle \bar\partial F_0, f\rangle$ for all test forms $f$.
- Then $F_0 - u$ is weakly holomorphic, and step 2 gives a holomorphic $G$ with $G = F_0 - u$ almost everywhere. So $\int |F_0 - G|^2 e^{-\varphi} \le A$.

This is the classical duality proof of Hörmander's estimate (L. Hörmander, Acta Math. 113, 1965).

## In the Lean code

The theorem is at [HStatementOf.lean](lean:ReciprocityTheory/L2DbarEstimates/HormanderEstimate/HStatementOf.lean#L27). `F.hormander` is in [Hormander.lean](lean:ReciprocityTheory/L2DbarEstimates/HormanderEstimate/Hormander.lean#L13). `TestIneqStatement` and `RegMStatement` are in [UnweightBackStatement.lean](lean:ReciprocityTheory/L2DbarEstimates/Localization/UnweightBackStatement.lean#L332), and `APStatement` is in [BasicIdentityStatement.lean](lean:ReciprocityTheory/L2DbarEstimates/BasicIdentity/BasicIdentityStatement.lean#L79).

- The measure `vol n z` in [IsLocalHomeomorph.lean](lean:ReciprocityTheory/L2DbarEstimates/IsLocalHomeomorph.lean#L88) is the zero measure if the fibre-counting function is not countably additive. For such $z$, `HStatement` holds with $F = 0$. We did not check if this case can occur for a local homeomorphism.
- `RegMStatement` assumes `LocalL2Isometry (vol n z) F` ([UnweightBackStatement.lean](lean:ReciprocityTheory/L2DbarEstimates/Localization/UnweightBackStatement.lean#L58)). Despite the name, this only says that $F$ is measurable and square integrable on compact sets. No isometry is involved.
