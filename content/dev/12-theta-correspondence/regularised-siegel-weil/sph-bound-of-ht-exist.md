---
id: sph-bound-of-ht-exist
title: The edge bound for every height, by comparison with one good height
kind: theorem
decl: GlobalTheory.CompanionTheory.SphPole.sphBound_of_htExist
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.SphericalBoundOfHeights
covers: 417
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `SphBound` of [`sphBound`](/entry/sph-bound/) for every height, from the bound for one height built in [`height_bound`](/entry/height-bound/). It reaches [`resCore`](/entry/res-core/) under the second name [`spherical_bound_of_heights`](/entry/spherical-bound-of-heights/). The analysis is in `height_bound`. This theorem only compares two heights.

## Statement

Let $G = U(p,p)(\mathbb{A}_F)$ with Siegel parabolic $P$, and call $H \colon G \to \mathbb{R}_{>0}$ a height if it is continuous and $H(qg) = |\det a_q| H(g)$ for $q \in P$ with Levi block $a_q$.

**Theorem.** Suppose that for each $n$ there is a compact $C_0 \subset G$ with $G = P \cdot C_0$ (part of `HtExist`). Let $p \ge 1$, $H$ a height and $C \subset G$ compact. Then there is $B$ such that for all $\sigma \in (p/2, p/2 + 1]$ and $h \in C$ the series $\sum_{\gamma \in P(F) \backslash G(F)} H(\gamma h)^{\sigma + p/2}$ converges and

$$\Bigl(\sigma - \frac{p}{2}\Bigr) \sum_{\gamma \in P(F) \backslash G(F)} H(\gamma h)^{\sigma + p/2} \le B.$$

## Proof

Write $p = r + 1$ and $\varepsilon = \sigma - p/2 \in (0, 1]$, so that the exponent is $p + \varepsilon$.

1. [`height_bound`](/entry/height-bound/) gives a height $H'$ and $B'$ such that $\sum_\gamma H'(\gamma)^{p + \varepsilon}$ converges and $\varepsilon \sum_\gamma H'(\gamma)^{p + \varepsilon} \le B'$ for all $\varepsilon \in (0, 1]$.
2. The function $(c, h) \mapsto H(ch) / H'(c)$ is continuous and positive, so it is bounded by some $c_1 \ge 1$ on $C_0 \times C$.
3. Let $\gamma \in G$ and $h \in C$. Write $\gamma = q c$ with $q \in P$ and $c \in C_0$. Both heights change by the same factor $|\det a_q|$ under $q$, so $H(\gamma h) \le c_1 H'(\gamma)$.
4. Hence $H(\gamma h)^{p + \varepsilon} \le c_1^{p + 1} H'(\gamma)^{p + \varepsilon}$, since $c_1 \ge 1$ and $p + \varepsilon \le p + 1$. Summation over $P(F) \backslash G(F)$ gives convergence and the bound $B = c_1^{p+1} B'$.

## In the Lean code

The theorem is in [SphericalBoundOfHeights.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SphericalBoundOfHeights.lean#L360). `HtExist` and `SphBound` are in [MapsExist.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/MapsExist.lean#L139). The proof calls only `height_bound` and the hypothesis.

- The first part of `HtExist`, the existence of a height, is not used: the proof discards it and takes $H'$ from `height_bound`. Only the decomposition $G = P \cdot C_0$ is used.
- The sum is over chosen representatives (`q.out`) of $P(F) \backslash G(F)$. The proof compares $H$ and $H'$ at the same representatives, so it does not need the terms to be independent of the choice.
