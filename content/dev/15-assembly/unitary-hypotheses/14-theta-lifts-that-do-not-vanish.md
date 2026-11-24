---
title: Theta lifts that do not vanish
decls:
  - GlobalTheory.Core.Rk.Exh.Top.downNe_k_of_hypotheses'
  - GlobalTheory.T.downNe_of_eulerRight_doubling
  - GlobalTheory.Core.Rk.LiftOnto.liftInj_nonVan_typeNZ_of_hypotheses_alt
  - GlobalTheory.T.liftInj_and_nonVan_typeNZ_of_given
  - GlobalTheory.DownLift.AtReal.lift_splits_locally
  - GlobalTheory.T.galoisRep_descends_at_real_places
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta lifts that do not vanish

This section proves that the [global theta lift](/learn/theta/#the-global-theta-lift) from a positive definite unitary group does not vanish on the forms whose Satake parameters contain a long string, and that a good form with vanishing lift is zero. The tool is [the doubling method](/learn/theta/#the-doubling-method): a pole of the partial $L$-function forces a residue of an Eisenstein series, and the residue is an inner product of theta lifts. [The record of hypotheses](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) of Section 1 uses the two results of this section as inputs of its rows. Injectivity of the lift and the nonvanishing of types are [the lifts of Section 1](/entry/lift-inj-and-non-van-type-nz-of-given/) and [their form at a real datum](/entry/galois-rep-descends-at-real-places/).

Let $E/F$ be the CM extension of a datum $D$, and let $S$ be a finite set of places. For a family $c$ of Satake parameters of $\mathrm{GL}_r$ off $S$, let $L^S(s, c)$ be its partial $L$-function and $\zeta^S$ the partial Dedekind zeta function. Let $A$ and $W$ be [[Hermitian form|8NJ7XY6F1S]] spaces over $E$, and let $\omega$ be the [Weil representation](/learn/theta/#the-weil-representation) of the pair $(U(A), U(W))$. For a Schwartz function $f$ the theta kernel is $\theta(g, h; f)$, for $g \in U(A)(\mathbb{A})$ and $h \in U(W)(\mathbb{A})$.

**Definition 8.14.1 (Three inputs of the doubling method).** The *doubling method input* says: for a space of positive rank, the Siegel Eisenstein series of a section of the degenerate principal series continues meromorphically and is regular up to a fixed order. For cusp forms $f_1, f_2$ the basic identity of the doubling method holds for $\mathrm{Re}(s) > \mathrm{rank}/2$, and the zeta integral continues. The *simple pole input* says: let $c$ be a family of $r$ parameters with absolute values at most $q_w^{(r-1)/2}$ off $S$, and let $P$ be $c$ together with a segment of length $t \ge r + 5$. Then

$$\begin{aligned} L^S(s, P) &= L^S(s, c) \prod_{i=0}^{t-1} \zeta^S\Bigl(s + \tfrac{t-1}{2} - i\Bigr), \end{aligned}$$

$L^S(s, c)$ is holomorphic and nonzero for $\mathrm{Re}(s) > \frac{r+1}{2}$, and $L^S(s, P)$ has a simple pole at $s = \frac{1+t}{2}$. The *unramified computation* at $D$ says: for $\mathrm{Re}(s) > \mathrm{rank}(A) + 1$, the doubling zeta integral equals $L^S(s + \frac12)/d^S(s)$ times an integral over the places in $S$, where $d^S(s)$ is the normalizing product of zeta values.

The first two are the doubling method of Piatetski-Shapiro and Rallis and the factorization of the standard $L$-function of a theta lift. The third is the unramified computation of the local doubling integral.

**Definition 8.14.2 (Downward nonvanishing).** *Downward nonvanishing* at $D$ says the following. Let $A$ and $W$ be hermitian spaces over $E$, with $A$ positive definite, $W$ of positive rank and $\mathrm{rank}(A) = \mathrm{rank}(W) + t$. Let $u$ be an automorphic form on $U(A)$, fixed by a principal congruence subgroup, with Satake parameters off a finite set $Z$ that satisfy the simple pole hypothesis. Let $\Phi$ be a vector of the Fock model, spherical off $Z$, whose integral of matrix coefficients against $u$ is not zero. Then there are a Schwartz function $f$ and a point $h$ with

$$\int_{U(A)(F)\backslash U(A)(\mathbb{A})} \theta(g, h; f)\, u(g)\, dg \neq 0.$$

**Theorem 8.14.3 (Downward nonvanishing).** Assume the doubling method input and the simple pole input. Let $D$ be a datum with the unramified computation. Then downward nonvanishing holds at $D$.

Lean: `GlobalTheory.Core.Rk.Exh.Top.downNe_k_of_hypotheses'` (also `GlobalTheory.T.downNe_of_eulerRight_doubling`, a second name).

*Proof.* Suppose that all theta lifts of $u$ vanish. There are five steps.

1. **Doubling.** A Witt decomposition writes a larger space $B$ as $W$ plus hyperbolic planes. A vacuum vector on the hyperbolic part and $\Phi$ give a Fock vector on the pair $(A, B)$.
2. **The residue vanishes.** Since all lifts vanish, the doubling integrals of $u$ against theta kernels vanish. At $s = t/2$ the coefficients of the regularized Siegel Eisenstein series of order at least $2$ vanish, and the coefficient of order $1$ integrates to $0$ against each form that kills all theta integrals. So the residue coefficient $E_1$ of the doubling integral is $0$.
3. **The zeta integral.** The doubling method input and the unramified computation write the zeta integral as $L^S(s + \frac12)/d^S(s) \cdot C$, and $C \ne 0$ because $\Phi$ has a nonzero matrix coefficient integral.
4. **Its residue.** The residue of the zeta integral at $s = t/2$ is the residue of the Eisenstein series against $u$, so by step 2 the coefficient of $(s - t/2)^{-1}$ is $0$.
5. **The pole.** By the simple pole input, $L^S(s + \frac12)$ has a simple pole at $s = t/2$, and $d^S$ is regular and nonzero there. So the coefficient of step 4 is not $0$. This is a contradiction. $\square$

This is the argument of Rallis: the first occurrence of a theta lift is detected by a pole of the $L$-function, through the [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula) and the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula).

Now we pass to a family. A *real datum* $R$ over a family $A$ of $D$ holds hermitian spaces $V_i$ and $W_i$, Weil representations on the pairs $(V_i, W_i)$, Hecke modules on both sides and linear theta maps $\theta_G$ from the $V$ side to the $W$ side. A *face* $F$ of $A$ is given. The data are *given* if a core condition, a choice of parameters, absolute irreducibility of the characters of $A$, good types, a guard and a gap $\lambda_n - \lambda_{n+1} \ge 100 r^4$ hold, and $R$ is *full* if each Weil representation of $R$ is full. Let $y$ be an eigenvector of a family of Hecke operators compatible with $R$, with eigensystem $s$. The eigensystem *has a string* of length $t$ if at each good place $w$, with $q = Nw$, its Satake multiset is

$$B' + \bigl\{ z\, q^{(t-1)/2 - k} : 0 \le k < t \bigr\},$$

with each $a \in B'$ of absolute value at most $q^{(r-1)/2}$.

**Theorem 8.14.4 (Injectivity and nonvanishing of the lift).** Assume the rapid decay of cusp forms, the doubling method input, the unramified doubling for $\mathrm{GL}$, the continuation of partial Hecke $L$-functions and the unramified Howe correspondence. Let $D$ be a datum, $G$ a finite group, $A$ a family, $K_s$ a number field, $R$ a real datum and $F$ a face, given and full. Then:

1. *(nonvanishing)* for all $i$ and $t$: if $s$ has a string of length $t$ and $y \ne 0$, there are a theta function, a functional $l$ and a point $g$ with $\int \theta(h, g; f)\, l(y(h))\, dh \neq 0$;
2. *(types)* for all $i$ and $t$: if $s$ has a string of length $t$, $y$ is good and $\theta_G(y) = 0$, then $y = 0$;
3. *(injectivity)* at the base length $t = \mu_0$: if $x$ and $y$ have the same eigensystem, $\theta_G(x) \ne 0$, $y$ is good and $\theta_G(y) = 0$, then $y = 0$.

Lean: `GlobalTheory.Core.Rk.LiftOnto.liftInj_nonVan_typeNZ_of_hypotheses_alt` (also `GlobalTheory.T.liftInj_and_nonVan_typeNZ_of_given`, a second name).

*Proof.* There are five steps.

1. **The inputs of downward nonvanishing.** The rapid decay of cusp forms and the unramified doubling for $\mathrm{GL}$ give the unramified computation at $D$. The continuation of partial Hecke $L$-functions gives the simple pole input.
2. **Downward nonvanishing.** The Theorem (Downward nonvanishing) applies.
3. **Nonvanishing on strings.** A string of length $t$ in the eigensystem gives Satake parameters of the shape of the simple pole hypothesis, with $c$ the part $B'$. So downward nonvanishing gives part 1.
4. **Local facts.** Seven local facts hold at each $(i, t)$: eigenforms go to eigenforms, the lift generates at the finite places and at the real places, good vectors stay good, good types exclude the level character, parameters exist, and the [unramified correspondence](/learn/theta/#the-local-theta-correspondence) of parameters holds at the good primes. The unramified Howe correspondence gives three of them, and the rapid decay gives two.
5. **Types and injectivity.** Nonvanishing and the local facts give part 2: a good $y$ with $\theta_G(y) = 0$ and a string would have a nonzero lift by part 1, generated by its local components. Part 2 at $t = \mu_0$ and the local facts give part 3. $\square$

**Corollary 8.14.5 (Types at a real datum).** Assume the rapid decay of cusp forms, the unramified Howe correspondence and the geometric compatibility of the [[Galois representation|JQEYEQJY2G]]s. Let $D$ be a datum with a character frame, a norm choice and a tie, and let $X$ be a real record over them, with a real datum $R$ and a face that are given and full. Then for all $j$ and $t$ part 2 of the Theorem (Injectivity and nonvanishing of the lift) holds for $R$.

Lean: `GlobalTheory.DownLift.AtReal.lift_splits_locally` (also `GlobalTheory.T.galoisRep_descends_at_real_places`, a second name).

*Proof.* The compatibility record contains the doubling method input, the unramified doubling for $\mathrm{GL}$ and the continuation of partial Hecke $L$-functions. The Theorem (Injectivity and nonvanishing of the lift) gives part 1. [The lift from the Rallis inner product](/entry/lift-inj-and-properties-of-rallis-of-non-van/) takes part 1 and the convergence of the Rallis inner product, which comes from the rapid decay and the Weil-Siegel formula of the compatibility record, and gives part 2. $\square$

**Remark 8.14.6 (Formalization).** The theorem on downward nonvanishing is at [KplugFill.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/KplugFill.lean#L18), with its second name at [EulerFactorFromDoubling.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/EulerFactorFromDoubling.lean#L17); the proof is `downNe_of_core hDM resCore hSP`, and step 2 is `ResCore`, proved by `resCore`. The doubling method input `DM` has a conjunct `True` ([DmOfHyp.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinResidues/AnisotropicGlobalForms/DmOfHyp.lean#L18)). The second name speaks of an Euler factor, but the statement is nonvanishing. The theorem on the lift is at [LiftInjNonVanTypeNZOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/LiftInjNonVanTypeNZOfPrints.lean#L14), lines 14 and 51. The word "prints" in the file name matches nothing in the statement. The inputs `HeckeLPartialContinuation` and `HoweUnram` are proved elsewhere as `HeckeLPartialContinuation_holds` and `howeUnram_holds`, but are still taken as hypotheses. The corollary is at [GaloisRepDescendsAtRealPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/GaloisRepDescendsAtRealPlaces.lean#L10), lines 10 and 23. Its route through `RallisConv` is a detour: the types come from part 1 without the Rallis convergence, which feeds only a saturation fact. Eight of the twelve fields of `GeometricGaloisRepCompatibility` are unused there. The names "lift splits locally" and "Galois representation descends at real places" do not describe the statement, which has no splitting, no local condition and no Galois representation. We did not unfold `Hk3.Core`, `GoodTypes`, the guard or the Hecke modules.
