---
id: exists-global-step
title: The inductive step of Angehrn-Siu, global form
kind: theorem
decl: GlobalTheory.PairStep.exists_global_step
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsGlobalSectionAngehrnSiuInductiveStep
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem finds a section of $\mathcal{O}(lA)$ whose divisor, scaled by $h/l$ and added to a pair, makes the pair not klt at each point of a finite set $P$ on a non-klt centre $Z$. It is the proof of [the statement form](/entry/exists-global-section-angehrn-siu-inductive-step/). The local work is in [`angehrnSiu_not_klt_at_several_points`](/entry/angehrn-siu-not-klt-at-several-points/). The method is that of Angehrn and Siu (Invent. Math. 122, 1995), who cut down non-klt centres by induction on their dimension.

## Statement

Assume `Published.Principalisation` (principalisation of ideals in characteristic 0). Let $X$ be a normal integral scheme, projective over $\mathbb{C}$, of dimension $n$. Let:

- $\Delta$ be an effective $\mathbb{Q}$-divisor with $(X, \Delta)$ klt at each point;
- $G$ a Cartier divisor with $G \sim m(K_X + \Delta)$ for some $m > 0$ (`IsLogCanonicalMultiple`, stated with a rational $n$-form);
- $A$ an ample Cartier divisor, and $D = D_0/m'$ with $D_0$ an effective Cartier divisor;
- $z \in X$ with closure $Z$ of dimension $k \geq 1$, such that $z$ is the generic point of $X$ or there is a divisorial valuation $E$ with centre $Z$ and discrepancy $a(E; X, \Delta + D) \leq -1$;
- $P$ a finite set of closed points of $Z$, and $h \in \mathbb{Q}_{>0}$ with $|P| \, k^k < h^k (A^k \cdot Z)$.

**Theorem.** For each $l_0$ there are $l \geq l_0$ with $l > h$, a section $f_0 \in H^0(X, \mathcal{O}(lA))$ that generates at $z$, and $\delta_0 \in (0, 1]$, with this property. For each section $u$ of $\mathcal{O}(lA)$ that vanishes at $z$, each $\delta \in [0, \delta_0]$ and each $x \in P$, the pair
$$\Delta + (1 - \delta) D + \tfrac{h}{l} \operatorname{div}(f_0 + u)$$
is not klt at $x$. Here $\operatorname{div}(f_0 + u)$ is the divisor of the section $f_0 + u$.

## Proof

1. `exists_lt_binomial_bound_of_mul_pow_lt`: there is $q < (A^k \cdot Z)$ such that for each $l_0$ there are $l \geq l_0$ and $M \geq 1$ with $kl < hM$, $h < l$ and $|P| \binom{M+k-1}{k} < q l^k / k!$.
2. `h0_lower_bound_of_isAmple_cartierDiv`: for large $l$, $h^0(Z, lA|_Z) \geq q l^k / k!$.
3. `exists_sections_restrict_basis`: for large $l$, there are sections $f_1, \dots, f_r$ of $\mathcal{O}(lA)$, $r = h^0(Z, lA|_Z)$, such that each nonzero combination $\sum a_j f_j$ generates at $z$. So $r > |P| \binom{M+k-1}{k}$.
4. `exists_residueMap_closure_point`: a residue map from the local ring at $z$ onto a field of transcendence degree $k$ over $\mathbb{C}$.
5. With local equations of $A$ and $D$ at each $x \in P$, [`angehrnSiu_not_klt_at_several_points`](/entry/angehrn-siu-not-klt-at-several-points/) gives a nonzero $a \in \mathbb{C}^r$ with a local non-klt property at every $x \in P$. Set $f_0 = \sum a_j f_j$.
6. Choose $\delta_0$. If $z$ is the generic point, $\delta_0 = 1$. Otherwise let $B = \sum_{x \in P} \operatorname{ord}_E(D \text{ at } x)$ and $\delta_0 = \min\bigl(1, (hM/l - k)/(M(B+1))\bigr)$.
7. `not_kltAt_of_local`, in the same file, turns the local property into the global one, with the form $dx_1 \wedge \dots \wedge dx_n$ of a transcendence basis of the local ring.

## In the Lean code

The theorem is at [ExistsGlobalSectionAngehrnSiuInductiveStep.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsGlobalSectionAngehrnSiuInductiveStep.lean#L237). We read the statements of the `GlobalTheory.T` lemmas, not their proofs.

The hypothesis that $(X, \Delta)$ is klt at each point is not used: the proof introduces it as `_` ([line 248](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsGlobalSectionAngehrnSiuInductiveStep.lean#L248)). Principalisation is used only by `angehrnSiu_not_klt_at_several_points`. The intersection number $(A^k \cdot Z)$ is `interNumRed`, defined by Euler characteristics on the reduced closure of $z$. The conclusion does not state the vanishing order of $f_0$ at $P$.
