---
id: model-small-encard-le
title: Small model sections are at most a power of the small cusp sections
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Plug.SlopeVol.modelSmall_encard_le
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformAllNormHeightBound
covers: 326
status: drafted
drafted_by: writer@claude
---
This lemma is step 5 of the proof of [the slope comparison](/entry/slope-sub-cost-le-comp-vol-slope/). It counts the small sections on a root model by the small cusp sections on a component $Z$. The count on the model is at most the $d$-th power of the count on $Z$, with $d$ the flag degree. The map sends $s$ to the traces of $s f_1, \dots, s f_d$, cleared of denominators at $S_B$.

## Statement

We use the notation of [the slope comparison](/entry/slope-sub-cost-le-comp-vol-slope/). Fix a good origin $o$ of a root tower $T$, a level $B$, a component $b$ of $T$ and its root origin $o_{B,b}$, a generic frame, and a reading of a component $Z$ that satisfies `GeoRead`. Let $u$ be a weight with strictly decreasing rows. For $u$ and $R \geq 0$, let $\mathcal M(u, R)$ (`modelSmall`) be the set of $s$ in the chart lattice of degree $u$ with a Hodge bound of size $R$. Let $\mathrm{tr}_u(s)$ (`trOf`) be the trace from the field of the model to the function field of $Z$ of $s$ divided by a gauge. Let $N(u) = \prod_{p \in S_B} p^{\lceil 2 e_2(p) \|u\|_1 \rceil}$ (`clearN`).

Assume `Top.Given`, `CompLaws`, `Ref.UnifAll`, the norm condition $\|\tau(\xi_0)\| = x$, and `HTLow`. Assume that $S_B$ is the set `htPrimes l B_d` for a real number $B_d$, and that $d > 0$. Let $k_0 \in \mathbb{N}$ and $R_0 \geq 0$, and let $f_1, \dots, f_d \in \mathcal M(k_0 u, R_0)$ be nondegenerate: if $\mathrm{tr}_v(s f_i) = 0$ for all $i$, then $s = 0$. Let $\tau > 0$, $R \geq 0$ and $R'$ with $N((\tau + k_0)u)\, d\, R R_0 \leq R'$. Then
$$\#\,\mathcal M(\tau u, R) \leq \Bigl(\#\,\mathrm{Small}_{Z}\bigl((\tau + k_0)\,u,\ R'\bigr)\Bigr)^{d}.$$
Here $\mathrm{Small}_Z$ (`smallOn` with `mixVals`) is the set of cusp sections on $Z$ that are integral for the mixed valuations and have norm at most $R'$ at each frame. The counts are in $\mathbb{N} \cup \{\infty\}$.

## Proof

The proof applies `encard_le_pow_of_rel`: a total and injective relation from $\mathcal M(\tau u, R)$ to $d$-tuples of small sections bounds the count. Let $s \in \mathcal M(\tau u, R)$ and $N = N((\tau + k_0)u)$.

1. `T.model_small_sections_mul` gives $s f_i \in \mathcal M((\tau + k_0)u, R R_0)$.
2. [`T.uniform_norm_all_tower_bound`](/entry/uniform-norm-all-tower-bound/) gives a cusp section $g_i$ on $Z$ whose value at the generic frame is $\mathrm{tr}(s f_i)$, with norm at most $d R R_0$ and with a lower bound for its valuations at the primes of $S_B$.
3. `clear_integral` uses `HTLow` and that lower bound: $N g_i$ is integral for the mixed valuations. Its norm is at most $N d R R_0 \leq R'$. So $N g_i \in \mathrm{Small}_Z$.
4. Injectivity: if $s$ and $s'$ give the same $N g_i$ for each $i$, then $g_i = g'_i$, so $\mathrm{tr}((s - s') f_i) = 0$ for each $i$ (by `trOf_sub`), and $s = s'$ by nondegeneracy.

## In the Lean code

The lemma is in [UniformAllNormHeightBound.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllNormHeightBound.lean#L248). The helpers `encard_le_pow_of_rel`, `clearN`, `clear_integral` and `trOf_sub` are in the same file. `modelSmall` and `trOf` are in [ModelSmall.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ModelSmall.lean#L36).

The nondegeneracy hypothesis is stated for every weight $v$, but the proof uses it only at $v = (\tau + k_0)u$. Its caller gets it from `generic_frame_component_bound`, and gets `HTLow` from `low_height_of_given`.
