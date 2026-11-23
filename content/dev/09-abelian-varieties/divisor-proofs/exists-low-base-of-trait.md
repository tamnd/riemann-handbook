---
id: exists-low-base-of-trait
title: A polarised abelian scheme with points over a trait comes from a lower base
kind: theorem
decl: GlobalTheory.TChart.exists_lowBase_of_trait
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLowerBaseOfTraitAbelianPart
covers: 311
status: drafted
drafted_by: writer@claude
---
After a finite extension, a polarised abelian scheme with $r$ points over a complete discrete valuation ring is the pullback of the tautological abelian scheme over a complete local ring of an $r$-fold fibre power of a Siegel family. The [statement entry](/entry/exists-lower-base-of-trait-abelian-part/) repeats it. Through that copy it is step 1 of [`exists_degFrom_of_trait`](/entry/exists-deg-from-of-trait/), where it is applied to the abelian part of a trait.

## Statement

Let $n \geq 3$ be odd and $\Lambda = \mathbb{Z}[\zeta_n, 1/n]$. Call a local domain *CN* (`IsCN`) if it is noetherian, integrally closed, complete and of characteristic zero. Let $V$ be a CN discrete valuation ring, $b \colon \Lambda \to V$ a ring map, $P$ a polarised abelian scheme over $V$ of relative dimension $h$ with bundle $L_P$, and $c \colon \mathbb{Z}^r \to P(V)$ an additive map.

**Theorem.** There are a lower base $L$ (`LowBase`, defined in [`exists_degFrom_of_trait`](/entry/exists-deg-from-of-trait/)) with abelian scheme $B$ over $W$ and points $c_0$, a CN discrete valuation ring $V'$, maps $f \colon V \to V'$ and $\kappa \colon W \to V'$, and an isomorphism $e \colon \mathbb{Z}^{r_L} \to \mathbb{Z}^r$, such that:

1. $L$ has genus $h$;
2. $f$ is injective, finite and local, $\kappa$ is local, and $\kappa \circ b_L = f \circ b$;
3. there is a group scheme $B'$ over $V'$ that is the pullback of $P$ along $f$ and of $B$ along $\kappa$;
4. under these two maps, the Mumford bundles $\Lambda(L_P)$ and $\Lambda(L_B)$ (the bundle $m^*L \otimes p_1^*L^{-1} \otimes p_2^*L^{-1} \otimes 0^*L$ on the square, `abelian₂`) pull back to isomorphic bundles on $B' \times B'$;
5. for each $a \in \mathbb{Z}^{r_L}$ there is a section $x$ of $B'$ that maps to $c(e(a))$ in $P$ and to $c_0(na)$ in $B$.

## Proof

1. `T.exists_fibrePower_point_finite_extension_dvr`: after a finite extension $V \to V_1$, there are a Siegel family $F$ of genus $h$ and a point $v$ of the $r$-fold fibre power of its universal abelian scheme over $V_1$. The abelian scheme at $v$ is the pullback of $P$, with the same Mumford bundle, and its point of index $na$ maps to $c(a)$.
2. `T.siegelFibrePower_point_lifts_to_lower_base`: the point $v$ lifts to a lower base $L$ after a finite extension $V_1 \to V'$, with clauses 1 to 4 for the abelian scheme at $v$ in place of $P$, and clause 5 for its point of index $n e(a)$ in place of $c(e(a))$.

Clauses 3 and 5 follow by composition, and clause 4 by transitivity of the bundle isomorphisms (`lbIso_pull_comp`, `LBIso.trans`). The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsLowerBaseOfTraitAbelianPart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLowerBaseOfTraitAbelianPart.lean#L17). We read the statements of the two lemmas, not their proofs. Neither has an entry.

The name says "trait", but no trait occurs in the statement. Clause 5 matches $c$ with $c_0(n \cdot {-})$, not with $c_0$: the points of $P$ correspond to $n$ times the tautological points.
