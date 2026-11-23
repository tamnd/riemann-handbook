---
id: slope-all-of
title: Integral Satake parameters at all places, from split places of a quadratic CM extension
kind: theorem
decl: UpperTheory.V.Z.Int.slopeAllOf
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.IntegralDeterminants.SlopeAllOf
covers: 2272
status: drafted
drafted_by: writer@claude
---
This theorem proves the integrality statement $\mathrm{SlopeAll}$ for the Satake parameters of a polarizable cuspidal representation at every finite place. Its inputs are a quadratic lifting statement $\mathrm{QuadLift}$ and the same bound $\mathrm{SlopeOn}(\mathrm{good})$ at split places, in $\ell$-adic form. [The theorem on slopes at all places](/entry/slope-all/) supplies both inputs and passes the result to `intP` and `intK`.

## Statement

Let $E$ be a CM field, $n \ge 1$, and $m_1 > m_2 > \dots > m_n$ integers. Let $\pi$ be a cuspidal representation of $\mathrm{GL}_n$ over $E$ (the Lean type `CuspSub E n`) whose infinitesimal character at each complex place is the multiset $\{\tfrac{n-1}{2} + m_i\}$. Suppose that $(\pi, \chi)$ is a polarized pair for some character $\chi$. Let $w$ be a finite place of $E$ with norm $q_w$, and let $B$ be a multiset of Satake parameters of $\pi$ at $w$. Put $b = q_w^{(n-1)/2} \alpha$ for $\alpha \in B$.

**Theorem.** If $\mathrm{QuadLift}$ and $\mathrm{SlopeOn}(\mathrm{good})$ hold, then for each such $b$:

- $q_w^{a} b$ is an algebraic integer for each $a \ge \max_i m_i$;
- $q_w^{a} b^{-1}$ is an algebraic integer for each $a \ge -\min_i m_i$.

$\mathrm{QuadLift}$ says: let $K \subset M$ be totally complex fields with $[M:K] = 2$, and let $\pi$ be cuspidal on $\mathrm{GL}_a$ over $K$. If some place of $M$ is ramified over $K$ and $\pi$ has Satake parameters at the place below it, then $\pi$ has a cuspidal lift $P$ to $M$. A lift matches Satake parameters, infinitesimal characters and local components. This has the shape of quadratic base change (Arthur and Clozel, *Simple algebras, base change, and the advanced theory of the trace formula*, 1989). We have not checked that the hypotheses match.

$\mathrm{SlopeOn}(\mathrm{good})$ gives the same bounds as inequalities $|\iota^{-1}(\cdot)| \le 1$ for each prime $\ell$ and each $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. It applies only at split places, and only to $\pi$ that are regular algebraic, polarized and "good" at a prime $\ell'$. Good means: the field contains some $\sqrt{-d}$, $[E^+:\mathbb{Q}]$ is even, and conditions hold at the non-split places.

## Proof

1. The $m_i$ are distinct, so $\pi$ is regular algebraic.
2. A quadratic extension. `infinite_quadraticCM_goodBaseChange_split` gives infinitely many CM fields $K \supset E$ with $[K:E] = 2$. For each, the decomposition groups at $w$ lie in the image of $G_K$, the places of $K$ above $w$ are split, some place of $K/E$ is ramified with $\pi$ unramified below it, and every lift of $\pi$ to $K$ is good at $2$.
3. The lift. $\mathrm{QuadLift}$ gives a cuspidal lift $P$ of $\pi$ to $K$. `polarizedPair_baseChange_polarized_same_weight` gives a character $\chi'$ with $(P, \chi')$ polarized. So $\mathrm{SlopeOn}(\mathrm{good})$ applies to $P$ at $\ell' = 2$.
4. The place. `exists_place_completion_iso` gives a place $w'$ of $K$ above $w$ with $E_w \cong K_{w'}$. Then $q_{w'} = q_w$, and $P$ has the Satake parameters $B$ at $w'$.
5. Integrality. Apply $\mathrm{SlopeOn}(\mathrm{good})$ to $P$ at $w'$. The product of $|\tau(\varpi_{w'})|$ over the embeddings that see $w'$ is $|q_{w'}|$. So $|\iota^{-1}(q^a b)| \le 1$ for all $\ell$ and $\iota$. The lemma `isIntegral_of_norm_le` turns this into integrality over $\mathbb{Z}$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [SlopeAllOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/IntegralDeterminants/SlopeAllOf.lean#L152). It calls:

- `automorphicFormsFiniteGL`, `jacquetShalikaRigidity_holds` and `gelfandKazhdanDual_of_jacquetShalika`, as inputs to the next lemmas.
- `infinite_quadraticCM_goodBaseChange_split`, `polarizedPair_baseChange_polarized_same_weight` and `exists_place_completion_iso`.
- The private lemmas `normV_eq_of_iso` and `slopesIn_of_slope` in the same file (lines 87 and 120), and `isIntegral_of_norm_le` in [IntCrit.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/IntCrit.lean#L56).

The proof uses $\mathrm{SlopeOn}(\mathrm{good})$ only at $\ell' = 2$. $\mathrm{SlopeOn}$ and $\mathrm{SlopeAll}$ are defined in [PlaceConjAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/IntegralDeterminants/PlaceConjAlt.lean#L97). We have not unfolded `CuspSub` or `PolarizedPair`.
