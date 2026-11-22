---
id: actual-compact-theorem
title: The compact form of Theorem P
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutSE.actual_compact_theorem
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutSETopFinal
covers: 1302
status: drafted
drafted_by: writer@claude
---
This theorem proves the proposition `ThmPActualCpt` with no hypothesis. Several theorems use it, among them [the carrier inputs from D](/entry/carrier-needs-from-d/), which passes it to [the built bounds](/entry/pb-built-bounds2-cpt/). So its parent is the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/). It proves two facts about radial operators and gives them to [the compact form from the radial operators](/entry/thm-pactual-cpt-of-r/), which holds 1,227 of the 1,302 declarations below.

## Statement

**The setting.** Let $n = 2r + k + 1$ with $k \ge 1$. Let $H$ be the Hermitian form `Hpk` on $\mathbb{C}^n$: it pairs $e_a$ with $e_{n-1-a}$ for $a < r$, and it is $\mathrm{diag}(1, \dots, 1, -1)$ on the middle $k + 1$ coordinates. So $G = U(H)$ is a [[unitary group|0R9R0Y1HDK]] of signature $(r + k, r + 1)$. Let $z, z'$ be vectors in the middle block with $H(z, z) < 0$ and $H(z', z') < 0$. Let $H_z$ (`UWset`) be the group of elements of $G$ that fix $z$ and each $e_a$, $e_{n-1-a}$ with $a < r$. Let $\pi$, a map to operators on a finite-dimensional space $W_p$, be multiplicative on $H_z$, and take $\pi'$, $W_q$ in the same way. For $F \colon G \to \mathrm{Hom}(W_q, W_p)$, the function $J_F$ (`B.JF`) integrates $F$ over $H_z \times N$ on the left and $N \times H_{z'}$ on the right, twisted by $\pi, \pi'$ and a character $\psi$ of a unipotent group $N$.

The radial space $\mathcal{R}$ (`RadSp`) holds the smooth functions $\Phi(c, g)$, $c \in (\mathbb{C}^\times)^r$, $g \in G$, that vanish off a domain `DomR` and satisfy $\Phi(c, h g h') = \pi(h) \Phi(c, g) \pi'(h')$. The map `resG` sends $J$ to $(c, g) \mapsto \prod_a |c_a|^{m_a - 1} J(w(c) g)$, with $w(c)$ given by `wCell`.

**Theorem.** Assume `IsData` for operators $X$, a measure $\mu$, level data $L$, a start datum and an integer $l_0$ with $1 \le l_0 \le k$. Then there are subspaces $K_0, \dots, K_r$ of $\mathcal{R}$ such that:

1. (`ThmPOn`) for each admissible word, the form `RRform` at each level $i$ is sesquilinear and positive semidefinite on $K_i$; at the top level the twisted form is the integral of $e^{s\zeta - \bar{s}\bar{\zeta}}$ times a density `topDens` over $G$; at each level $l < r$ it is the Fourier transform of a continuous function $\varphi$ with $|\varphi(t)| \le C (1 + |t|)^{-4}$;
2. (`SliceIn`) the slice operator at level $l$ maps $K_l$ into $K_{l+1}$;
3. (`CompositeFormulaLevelZero`) the level-zero form is the integral over $(c, g)$, with weight $\prod_l |c_l|^{-2}$, of the top density of the images under all slice operators;
4. if $F$ has compact support, lies in every class `InCC`, and $G_f \ge \varepsilon > 0$ where $F \ne 0$, then some $\Phi \in K_0$ equals $\mathrm{resG}(J_F)$ on `DomR`.

We have not unfolded `topDens`, `ph`, the slice operators `bTl` or the level data.

## Proof

1. `spectral_operator_R` proves `RDSOpR` by `rDSOpR_of_parts` from `spectral_right_group_action`, `spectral_operator_X`, `spectral_right_rho_action` and `spectral_composition_zero`.
2. `spectral_operator_R_adjoint` proves `RDSOpRv` by `rDSOpRv_of_parts` from the adjoint forms of the same four facts.
3. [`thmPActualCpt_of_R`](/entry/thm-pactual-cpt-of-r/) gives `ThmPActualCpt` from these two facts.

`RDSOpR` says that a radial operator $G_i \xi(Y) R_h(Y)$ is the radial part of a differential operator on $G$. The proof takes the composite $T_0 \circ \Theta$ (`dcomp`) of a group operator $\Theta$ and the zero-order term $T_0$ from `spectral_operator_X`.

## In the Lean code

The theorem is at [CutSETopFinal.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSETopFinal.lean#L14). `ThmPActualCpt` is in [HerGenC.lean](lean:Formalism/HermitianCurvature/HerGenC.lean#L63), and the two assembly lemmas are in [CutSERDSOpR.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSERDSOpR.lean#L107).

`ThmPActualCpt` also takes a real $A \ge$ `Auser` and a natural number $m \ge$ `mmUser`. The conclusion never uses them: the classes `InCC` in clause 4 range over new variables. So these hypotheses have no effect.
