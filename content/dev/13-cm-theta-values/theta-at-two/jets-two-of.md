---
id: jets-two-of
title: Integral jets at 2 from the fourth tensor power and a frame change
kind: theorem
decl: GlobalTheory.ThLoc.LocJets.jets_two_of
module: Development.AbelianVarietyTheory.Definitions.GaloisGeometry.FourthPowerTheta
covers: 615
status: drafted
drafted_by: writer@claude
---
This theorem proves `IntOpTwoLoc` from four statements about tensor powers, Gram matrices and frames. The 2-adic analysis comes from [integral jets of translated theta functions at 2](/entry/integral-operator-two-orthogonal/). The rest is a transfer of integrality along linear changes of variables. [`jetsTwo`](/entry/jets-two/) applies it to proofs of the four statements.

## Statement

We use the notation of [the parent entry](/entry/loc-jets-all/): the CM lattice $L = \lambda(\mathbb{Z} a_0 + \mathbb{Z}\tfrac{b_0 + i\sqrt d}{2})$, the theta function $\theta$ for $(h, \Lambda)$, the normalization `LocNorm` with the isometry $g_1$ of $h^{\oplus 4}$ onto the standard form of $L$ on $\mathbb{C}^{4 \times n}$, and the frame $M = \iota(v) A$. Let $\gamma$ be the matrix of $g_1^{-1}$, mapped by $\iota$. The four hypotheses are:

- `TensZ`: for a prime $p$ and a translate $t$ with $Nt \in \Lambda$, $p \nmid N$, the fourth tensor power of the Taylor series of $U_t\theta$, mapped by $\iota$ and composed with $\gamma$, equals `thetaZ`: a sum $\sum_k r_k \prod_w (U_{s_{k,w}}\theta_0)(z_w)$ with $|r_k| \le 1$, $N' s_{k,w} \in L$, $p \nmid N'$, where $\theta_0$ is the normalized translated sigma function at $\lambda a_0/2$.
- `GramTransfer`: there is a matrix $D$ with entries of norm $\le 1$ such that $\gamma D$ is block diagonal with blocks $\iota(v)$, and $D^{T} D$ is the block diagonal Gram matrix of the $v_j$ plus $\iota(i\sqrt d)\, q_0$, with $q_0$ integral.
- `FrameCompose`: from such $D$ and an integral $A$, a matrix $C$ with entries of norm $\le 1$ and $\gamma C$ block diagonal with blocks $\iota(v)A$, plus the same Gram relation.
- `JetsLinZ`: if the fourth tensor power of a series $T$, composed with $\gamma$, has integral jets, and $C$ is integral with $\gamma C$ block diagonal with blocks $M$, then $T$ composed with $M$ has integral jets.

**Theorem.** `TensZ`, `GramTransfer`, `FrameCompose` and `JetsLinZ` imply `IntOpTwoLoc`.

## Proof

1. `data` gives `HasCMBy d L`, a CM condition that we did not unfold. The point $\omega_0 = \lambda a_0$ is in $L$, and by `half_notMem` (with signs $\pm 1$ and `conj_omegaK`) with $\omega_K = (1 + \sqrt{-d})/2$, neither $\omega_K \omega_0/2$ nor $\bar\omega_K \omega_0/2$ is in $L$.
2. `GramTransfer` at $p = 2$ gives $D$ and $q_0$. `FrameCompose` gives $C$.
3. Fix a translate $t_k$. `TensZ` at $p = 2$ writes its fourth tensor power as `thetaZ`. Since $d \equiv 7 \pmod 8$ and $\omega_0$ satisfies step 1, the first half of `integral_operator_two_orthogonal` shows that this series has integral jets.
4. `JetsLinZ` with $C$ gives integral jets for the translate by $t_k$ in the frame $M$.
5. `jets_comb` adds these with weights $|r_k| \le 1$. This gives the first conclusion. `intOp` gives the bound on the pairing with an integral polynomial.

## In the Lean code

The theorem is at [FourthPowerTheta.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FourthPowerTheta.lean#L262). `data` is at line 48, `jets_comb` at line 55 and `half_notMem` at line 218. The four hypotheses and `IntOpTwoLoc` are in [StatementH.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementH.lean#L15), [StatementB.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementB.lean#L23) and [StatementA.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussianEigenFrames/StatementA.lean#L64). `intOp` is in [FinalB.lean](lean:Formalism/GaussJetBounds/FinalB.lean#L132). We did not unfold `kernel4` or the product `thetaProd` inside `thetaZ`.

Odd points:

- The hypotheses `Unif`, `IntCurve` and $|a_1(W)| = 1$ are used only through `integral_operator_two_orthogonal`.
- The Gram relation that `FrameCompose` returns, and the bound on $q_1$, are discarded.
