---
id: lemma-bt-of-characters
title: The minor bound LemmaBT from characters with bounded minors
kind: theorem
decl: GlobalTheory.PowGerm.lemmaBT_of_characters
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.IsUnitIffNotIsUnitOfCoprime
covers: 409
status: drafted
drafted_by: writer@claude
---
This theorem proves `LemmaBT`, the valuation bound for a product of minors on power data. [`lemmaBT_of_hodgeTate_chart`](/entry/lemma-bt-of-hodge-tate-chart/) supplies its five inputs, and the bound goes on to [`least_value_le`](/entry/least-value-le/).

## Statement

The inputs are the bundles `Laws`, `Laws2`, `Laws4`, the statement `TwistBaseChangeStatement`, and a hypothesis $\mathrm{(Ch)}$ on characters. $\mathrm{(Ch)}$ says: let $p$ be a prime, $E$ a CM field, and $y$ a point with values in an algebraically closed field of characteristic $0$, with valuation $v$ and a ring of integers $O_v$ that is $p$-adically complete, $p$ not a unit. Let $a \in \mathcal{O}_E$ with $a\bar a = p$ and $a, \bar a$ coprime. Let $e_l$ be eigenvectors of the tangent action of $\mathcal{O}_E$, with characters $\tau_t$, $\tau_t(a) \in pO_v$, with dual vectors and idempotents mod $p$. Let $(p-1)v(c) = v(p)$ and let the columns $\mathrm{col}_t$ be injective. Then there are $y_{l,b} \in O_v$ such that each column $b$ is the tangent value of a character on the $a$-torsion (`CharAt`), and each leading minor of size $s+1$ of each block has valuation at most $(s+1)v(c)$.

**Theorem.** These five inputs imply `LemmaBT`.

`LemmaBT` is also stated [here](/entry/depth-below-one-of-hodge-tate-chart-form/). Its data are an integral point of a moduli space over a complete discrete valuation ring $T$, a PEL uniformisation with a quadratic form $Q$, two distinct odd primes $g, g'$ with $g = \pi\bar\pi$ and $g' = \pi'\bar\pi'$, $g$ totally split in $E$, a basis $b_1, \dots, b_r$ with $Q(b_j) \le \Phi$, power data of rank $n_1 + n_2$, and multiplicities $m$ of degree $D < g - 1$ with $4D + 4 \le g'$ and $D M_0 < g'$. The conclusion is nine objects with their properties and the valuation $\rho$ of a product of minors, with

$$\rho \le \frac{\rho_g D}{g-1} + \frac{n_1 r \Phi}{4g'} + \frac{2D^2\Phi}{g'}, \qquad \rho_g = v(g).$$

## Proof

1. `starSt` identifies the star on $\mathcal{O}_E$ with the conjugation of the host. `T.exists_integral_types_and_directions'` gives the embeddings $\sigma$, eigenvectors $e$, dual vectors and idempotents at $g$, and the fact that $v(\sigma(x)) > 0$ exactly when $\sigma(x) \in gO$.
2. `T.integralChart_columns_to_tuple_harmonicValues` gives a chart point and a transfer `htr` to the power data. `integralChart_formalBiext` matches the two tangent actions.
3. `minorSt` writes the product of the two `minorProd` factors as a product of leading minors in injective columns, with multiplicities $m'$ of total degree $D$. `canonGauge_exists` gives a canonical gauge.
4. The main step is `T.depth_bound_from_characters_pointDatum`, applied with $p = g$, $a = \bar\pi$, $k = g'$, the set $S$ of the first $n_1$ columns and $\deg = D$. It uses $\mathrm{(Ch)}$ and gives $\gamma \le D\rho_g/(g-1) + |S| r \Phi/(4g') + D^2\Phi/g'$.
5. `htr` carries the result to the power data and gives the nine properties.
6. The minor product has valuation $\gamma$, by `minors_disjoint_columns_harmonic` and the local lemma `isUnit_iff_not_isUnit_of_coprime`: in a local ring, if $xy$ is not a unit and $ux + u'y = 1$, then $x$ is a unit exactly when $y$ is not. So exactly one of $\tau(\pi)$, $\tau(\bar\pi)$ has positive valuation.
7. $|S| = n_1$, and $D^2\Phi/g' \le 2D^2\Phi/g'$. `linarith` closes the bound.

## In the Lean code

The theorem is in [IsUnitIffNotIsUnitOfCoprime.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/IsUnitIffNotIsUnitOfCoprime.lean#L50). `T.depth_bound_from_characters_pointDatum` is a second name of `DepthFromChars.depth_bound_of_chars` (not opened). `CharAt`, `nabValN` and `minorProd` are not unfolded here.

The proof does not use: that $g$ and $g'$ are odd, the factorization $g' = \pi'\bar\pi'$ and the coprimality of $\pi', \bar\pi'$, the bound $1 \le n_1 + n_2$, and `y.IsAlg`. The last term of `LemmaBT` has a factor $2$ that the proof does not need.
