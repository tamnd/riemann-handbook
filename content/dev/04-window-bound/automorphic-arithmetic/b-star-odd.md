---
id: b-star-odd
title: A rank bound for odd-degree homology of GL_n over a ring of integers
kind: theorem
decl: PositivityTheory.KB.bStarOdd
module: Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.ReductionBoundsTorsion.FinalOdd
covers: 1779
status: drafted
drafted_by: writer@claude
---
This theorem bounds by $r_2(L)$ the rank of a subgroup of the odd-degree homology of $\mathrm{GL}_n(\mathcal{O}_L)$, for a totally complex field $L$. The subgroup is cut out by an operator that kills the parts of weight 2 to $k+1$. [`bOdd_zk`](/entry/b-odd-zk/) moves the result to another namespace, and from there it goes to [the bound on $H^2$](/entry/lemma-k-lit-n-alt/) as `BOdd`.

## Statement

Let $L$ be a totally complex number field with $r_2$ complex places, $k$ an even number with $k + 1 < r_2$, $\ell \geq 1$ and $n \geq 2(k+1) + 4$. For $x \in H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L), \mathbb{Z})$ put $z_0 = x$ and
$$z_{t+1} = \psi_{\ell *}(z_t) - \ell^{t+2}\, \mathrm{st}_*(z_t),$$
with $\psi_\ell(A) = 1_\ell \otimes A$ and $\mathrm{st}$ the inclusion in the upper left corner, both from $\mathrm{GL}_m$ to $\mathrm{GL}_{\ell m}$.

**Theorem.** The subgroup of $H_{k+1}(\mathrm{GL}_{\ell^k n}(\mathcal{O}_L), \mathbb{Z})$ spanned by all $z_k$ has rank at most $r_2$.

For comparison, A. Borel computed that $K_{2m-1}(\mathcal{O}_L)$ has rank $r_2$ for $m \geq 2$ when $L$ is totally complex (Ann. Sci. ENS 7, 1974). The bound has that form. We do not claim that the Lean proof follows Borel's paper.

## Proof

The proof is `sBStarOdd_of` applied to six inputs, each proved elsewhere:

- `SChain`: the identities of the standard chain complex of a group with real coefficients ($\partial^2 = 0$, functoriality, and inner automorphisms act trivially on homology).
- `SSep`: a cycle that is not a boundary is detected by an invariant cocycle.
- `SBridge`: real cycles modulo boundaries are $\mathbb{R} \otimes H_{k+1}(G, \mathbb{Z})$, naturally in $G$.
- `SStab`: homological stability for $\mathrm{GL}_n$ over a Dedekind domain for $n \geq 2(k+1) + 4$. It has the form of the theorem of W. van der Kallen (Invent. Math. 60, 1980).
- `SSurj`: for large $N$, each invariant cocycle of $\mathrm{GL}_N(\mathcal{O}_L)$ agrees on cycles with the integral of an invariant differential form on the space of tuples of positive definite Hermitian matrices, one for each infinite place.
- `SWtOdd`: for $k$ even, each such integral is $\sum_w c_w \tau_w + \sum_{j=2}^{k+1} a_j$ on cycles. Here $\tau_w$, one for each infinite place $w$, and $a_j$ are weight systems of weight 1 and $j$: functionals that vanish on boundaries, are compatible with $\mathrm{st}$, and satisfy $a(\psi_{d*} z) = d^j a(z)$.

The argument of `sBStarOdd_of` is this. Each step of the recursion multiplies a weight $j$ system by $\ell^j - \ell^{t+2}$ (the lemma `wsys_zc`). So after $k$ steps every $a_j$ with $2 \leq j \leq k+1$ vanishes on the $z_k$. Let $z$ be a real combination of the $z_k$ with $\tau_w(z) = 0$ for all $w$. If $z$ were not a boundary, push it to $\mathrm{GL}_N$. By `SStab` it is still not a boundary. Then `SSep` gives a cocycle that does not vanish on it, `SSurj` writes that cocycle as a form, and `SWtOdd` evaluates the form as $0$. This is a contradiction. So $z$ maps to $0$ in $\mathbb{R} \otimes H_{k+1}$. The map $(\tau_w)_w$ to $\mathbb{R}^{r_2}$ is then injective on the image, and `TwOdd.rank_span_le` gives the bound.

## In the Lean code

The theorem is in [FinalOdd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/FinalOdd.lean#L8):

```
sBStarOdd_of sChain sSep' sBridge sStab
  (sSurj_of sPrime_of sHecke sHt_of sPU sMom sWhit sCen sGap_of sLoc sMean_of sInv)
  (sWtOdd_of sChain sEv sPsi sStokes_of)
```

The statement `BStarOdd` and the implication `SBStarOdd` are in [SBStarOdd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/SBStarOdd.lean#L18). The inputs are stated in [SBridgeAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/SBridgeAlt.lean#L10) and [SBStar.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/SBStar.lean#L9), and the argument above is in [SBStarOddOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/OddSpanRank/SBStarOddOf.lean#L13). We have not unfolded the proofs of the six inputs. The proof of `SSurj` uses eleven lemmas (`sHecke`, `sWhit`, `sGap_of` and others) that we have not opened. `SWtOdd` uses the rule `SPsi`: $\psi_{d+1*} z$ and $(d+1)\,\mathrm{st}_* z$ differ by a boundary for primitive cycles $z$. The hypothesis $k + 1 < r_2$ is used only by `SSurj`.
