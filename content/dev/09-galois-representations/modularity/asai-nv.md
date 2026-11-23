---
id: asai-nv
title: Two twisted periods of a conjugation-invariant cusp form do not both vanish
kind: theorem
decl: UpperTheory.ConvolutionTheory.RankTwoDescent.asaiNV
module: Development.AutomorphicArithmetic.Foundations.Convolution.SplitEigenfunctions.AsaiNV
covers: 797
status: drafted
drafted_by: writer@claude
---
This theorem is step 6 of [the descent of a normalised cusp form](/entry/down-n/). It says that a conjugation-invariant [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_2$ over an imaginary quadratic field has a nonzero period over $\mathrm{SL}_2$ of the rationals, twisted by $\omega^{-1}$ or by $(\omega\eta)^{-1}$. If both periods vanish, two Dirichlet series with the local factors of twisted Asai L-functions are entire, and a lemma of Landau type rules this out.

## Statement

Let $E$ be a totally complex field with a datum `Dat`: a rational $\delta < 0$ and $\theta \in E$ with $\theta^2 = \delta$ and $E = \mathbb{Q} \oplus \mathbb{Q}\theta$. Let $\mathcal{D}$ be a fundamental domain for $\mathrm{SL}_2(\mathbb{Q})$ in $\mathrm{SL}_2(\mathbb{A}_\mathbb{Q})$ with Haar measure $\mu$, and $\upsilon$ an invariant probability measure on the ideles $t$ with $t_\infty = 1$ and $|t_v|_v = 1$ for finite $v$. For a Hecke character $\chi$ of $\mathbb{Q}$ and a function $\varphi$ on $\mathrm{GL}_2(\mathbb{A}_E)$ put

$$\mathrm{Per}_\chi(\varphi) = \int \chi(t) \int_{\mathcal{D}} \varphi\bigl(g \cdot \mathrm{diag}(1, t)\bigr)\,d\mu(g)\,d\upsilon(t).$$

Let $P$ be a cuspidal subspace for $\mathrm{GL}_2$ over $E$ and $\omega$, $\eta$ Hecke characters of $\mathbb{Q}$ with:

1. $P$ is conjugation invariant (`ConjInv`);
2. the central character of $P$ is $\omega \circ N_{E/\mathbb{Q}}$, and $|\omega| = 1$;
3. $\eta$ is the quadratic character of $E/\mathbb{Q}$ at almost all places.

**Theorem.** It is not the case that $\mathrm{Per}_{\omega^{-1}}$ and $\mathrm{Per}_{(\omega\eta)^{-1}}$ both vanish on all right translates of all $\varphi \in P$.

## Proof

Suppose both vanish. Let $\chi$ be $\omega^{-1}$ or $(\omega\eta)^{-1}$. Then $\eta^2 = 1$ (`quad_sq`), so $(\chi\omega)^2 = 1$.

1. **Test vector.** `trAdm` makes the right translates of $P$ cuspidal, bounded and of rapid decay. `chEx_of` gives conductors for both $\chi$, and a level $m$ absorbs the primes where conditions 1 or 3 fail. Then `exGd_of` gives a $\varphi$ of some level $N$, a Hecke eigenvector at the good places, with nonzero Whittaker coefficient at $1$.
2. **The Dirichlet series.** `asEx_of` gives multiplicative $a_\chi(n)$, summable for $\operatorname{Re} s > 4$. At a split good prime $p = ww'$, with Satake parameters $\gamma \in \{\alpha, \beta\}$ at $w$ and $\gamma' \in \{\alpha', \beta'\}$ at $w'$, the local series is $\prod (1 - \gamma\gamma'\chi(p)X)^{-1}$. At an inert good prime it is $\bigl((1 - \alpha\chi(p)X)(1 - \beta\chi(p)X)(1 - X^2)\bigr)^{-1}$.
3. **Entire series.** By `ext_of`, if $\mathrm{Per}_\chi$ vanishes on $P$, then $\sum a_\chi(n) n^{-s}$ is entire. By its inputs, a zeta integral of $\varphi$ against a theta series is entire (`ent_of`), unfolds to a Whittaker integral (`unf_of`), and factors as the Dirichlet series times archimedean terms (`fac_of`) that are holomorphic (`hol_of`) and can be made nonzero (`nonZ_of`).
4. **Contradiction.** `lan_of` checks, with the bounds on Satake parameters in `satU_of`, that the product of the two series has nonnegative coefficients, at least $1$ at each good prime. Then `landau_of` gives `False`: an entire Dirichlet series with nonnegative coefficients and $b(1) = 1$ has only finitely many $n$ with $b(n) \geq 1$.

## In the Lean code

The theorem is at [line 25 of AsaiNV.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/AsaiNV.lean#L25). Its proof applies `asai_of`, at [line 51 of ExistsBad.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/ExistsBad.lean#L51), to the inputs above. The Props it uses are in [Entire.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/Entire.lean#L64). `AsaiNV`, `Per` and `NoPer` are in [ConjInv.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/ConjInv.lean#L28).

$[E:\mathbb{Q}] = 2$ is not a hypothesis; it follows from the basis in `Dat`. At split primes the local series in `IsAs` is the Rankin-Selberg factor of the two local components, which is the Asai factor there (T. Asai, Math. Ann. 226, 1977). We read the statements of the inputs of `ext_of`, not their proofs.
