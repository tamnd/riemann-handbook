---
id: sph-bound
title: The spherical Siegel Eisenstein series has at most a simple pole at the edge
kind: theorem
decl: PositivityTheory.Rg.Rsw.sphBound
module: Development.WeilBound.RepresentationTheoryGL.RegularisedSiegelWeil.ThetaIdempotents.SphBound
covers: 419
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `SphBound` with no hypotheses. It is one of the inputs of [`resCore`](/entry/res-core/), the simple pole theorem for Siegel Eisenstein series in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). In the same file, `resMu` and `polar` use it. The proof is one application, and the real content is in [`sphBound_of_htExist`](/entry/sph-bound-of-ht-exist/).

## Statement

Let $G = U(p,p)(\mathbb{A}_F)$ be the adelic unitary group of the form $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ over the CM extension $E/F$ of the datum, with Siegel parabolic $P$. Call $H \colon G \to \mathbb{R}_{>0}$ a *height* if $H$ is continuous and $H(qg) = |\det a_q|_{\mathbb{A}_E} H(g)$ for $q \in P$ with Levi block $a_q$ (`IsHt`).

**Theorem.** Let $p \ge 1$, let $H$ be a height and let $C \subset G$ be compact. There is $B$ such that for each $\sigma \in (p/2, p/2 + 1]$ and each $h \in C$ the series $\sum_{\gamma \in P(F) \backslash G(F)} H(\gamma h)^{\sigma + p/2}$ converges and

$$\Bigl(\sigma - \frac{p}{2}\Bigr) \sum_{\gamma \in P(F) \backslash G(F)} H(\gamma h)^{\sigma + p/2} \le B.$$

## Proof

`sphBound` is `spherical_bound_of_heights htExist`. Here `htExist` proves `HtExist`: a height exists, and $G = P \cdot C_0$ for a compact set $C_0$. [`spherical_bound_of_heights`](/entry/spherical-bound-of-heights/) is a second name of `sphBound_of_htExist`.

## In the Lean code

The theorem is at [SphBound.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/SphBound.lean#L33). `SphBound` and `IsHt` are in [MapsExist.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/MapsExist.lean#L206). `IsHt` does not ask for invariance under a maximal compact subgroup. The theorem is a renaming.
