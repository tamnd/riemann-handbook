---
id: vanishing-ample-snc-char-zero
title: Kawamata-Viehweg vanishing for a relative snc family in characteristic zero
kind: theorem
decl: GlobalTheory.Div.vanishing_ample_snc_charZero
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.KawamataViehwegVanishing
covers: 586
status: drafted
drafted_by: writer@claude
---
This theorem is the Kawamata-Viehweg vanishing theorem of the Lean code over a field of characteristic $0$, for a boundary given by a relative snc family of line bundles with sections. [`vanishing_ample_snc_cartier`](/entry/vanishing-ample-snc-cartier/) reduces its divisor to this form and calls it. The proof spreads everything out over a finitely generated subring $R$ of the field and calls [`kawamata_viehweg_spreading`](/entry/kawamata-viehweg-spreading/). Below this theorem are 586 declarations.

## Statement

Let $k$ be a field of characteristic $0$ and $f \colon X \to \operatorname{Spec} k$ smooth of relative dimension $d$ and projective. Let $L_1, \dots, L_s$ be line bundles on $X$ with global sections $\sigma_1, \dots, \sigma_s$ that form a *relative snc family* over $k$ (`RelSnc`): each point of $X$ has an affine neighbourhood $U$ with functions $t_1, \dots, t_d$ such that $k[T_1, \dots, T_d] \to \mathcal{O}(U)$, $T_j \mapsto t_j$, is étale, and on $U$ each $\sigma_i$ is a unit or a unit times one coordinate $t_{e(i)}$, with distinct $i$ using distinct coordinates. Let $K$ be the canonical bundle of $X/k$ (`CanonLB`: a line bundle with local frames given by nowhere zero $d$-forms). Let $M$ and $A$ be line bundles, $A$ ample, $r > 0$, and $b_1, \dots, b_s$ integers with $0 \leq b_i < r$ and

$$r[M] = r[K] + \sum_i b_i [L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$

Then $H^q(X, M) = 0$ for all $q > 0$.

With $D_i$ the zero divisor of $\sigma_i$, this says $H^q(X, K + N) = 0$ where $N \sim_{\mathbb{Q}} \sum_i (b_i/r) D_i + A/r$. Kawamata-Viehweg vanishing in this form is in Esnault and Viehweg (Lectures on Vanishing Theorems, DMV Seminar 20, Birkhäuser, 1992).

## Proof

1. **Spreading out.** $X$ is proper over $k$. `spread_out_relative_snc` gives a subring $R \subseteq k$ of finite type over $\mathbb{Z}$, a proper $f_1 \colon X_1 \to \operatorname{Spec} R$ with $X = X_1 \times_R k$, line bundles $L_{1,i}$ with sections that form a relative snc family over $R$, and a line bundle $M_1$, such that $[L_i]$ and $[M]$ are the pullbacks of $[L_{1,i}]$ and $[M_1]$. The charts of a relative snc family give smoothness, so $X_1$ is smooth of relative dimension $d$ over $R$.
2. **The ample bundle.** Choose a canonical bundle $K_1$ of $X_1/R$ and a line bundle $A_1$ with $[A_1] = r[M_1] - r[K_1] - \sum_i b_i [L_{1,i}]$. The canonical bundle commutes with base change, so the pullback of $A_1$ to $X$ has the class of $A$. So it is isomorphic to $A$ and is ample. $A_1$ itself need not be ample.
3. **Vanishing.** `kawamata_viehweg_spreading` gives $H^q(X, \pi^* M_1) = 0$ for $q > 0$. Since $[\pi^* M_1] = [M]$, the same holds for $M$.

## In the Lean code

The theorem is in [KawamataViehwegVanishing.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegVanishing.lean#L20). The lemmas it calls:

- `GlobalTheory.T.spread_out_relative_snc` (a second name of `GlobalTheory.ModelSnc.exists_model_relSnc`, whose proof we have not read), in [SpreadOutRelativeSncStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/SpreadOutRelativeSncStatement.lean#L12).
- `GlobalTheory.T.smoothOfRelativeDimension_of_relSncDivisor` and `CanonLB.nonempty`.
- `GlobalTheory.T.cechPicardClass_canonicalBundle_baseChange` and `IsAmpleLB.of_lbIso`, for step 2.
- `GlobalTheory.T.kawamata_viehweg_spreading` and `GlobalTheory.T.cohomology_subsingleton_of_cechPicardClass_eq`, for step 3.

Projectivity of $f$ is used only to get properness. The theorem has a second name, `GlobalTheory.T.kawamata_viehweg_vanishing`, in [KawamataViehwegVanishingStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegVanishingStatement.lean#L10), with the same statement. No file of the Lean code uses that second name.
