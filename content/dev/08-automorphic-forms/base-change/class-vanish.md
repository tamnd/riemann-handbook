---
id: class-vanish
title: A regular non-elliptic class term vanishes
kind: theorem
decl: PositivityTheory.Rg.BcB.CV.classVanish
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.QuotientVanishing.LocalQuotientIntegrals.ClassVanish
covers: 716
status: drafted
drafted_by: writer@claude
---
This theorem is the one-group form of [the vanishing of non-elliptic class terms](/entry/class-vanish2/). For a regular twisted class $d$ in $\mathrm{GL}_n(E)$ that is not elliptic, the truncated class term of a very cuspidal test function is $0$ once the truncation parameter $\tau$ is large. [`classVanish2`](/entry/class-vanish2/) applies it to one factor of $\mathrm{GL}_a \times \mathrm{GL}_b$ at a time.

## Statement

We use the notation of [the elliptic formula](/entry/ell-formula2-j/): $G_n = \mathrm{GL}_n(\mathbb{A}_E)$, $\theta(g) = \bar g^{-T}$, the cut-off $\chi_\tau$, the degree $\deg(x, W)$, the size $\ell$, and regular and regular elliptic elements. For $d \in \mathrm{GL}_n(E)$, let $Z_d$ be the image in $G_n$ of the rational twisted centralizer of $d$, and

$$T_\tau(\phi; d) = \int_{Z_d \backslash G_n} \chi_\tau(x)\, \phi\bigl(x^{-1} d\, \theta(x)\bigr)\, dx.$$

A function $f$ on $\mathrm{GL}_n(\mathbb{C})$ is *very cuspidal* if it is invariant under twisted conjugation by $\theta$-fixed elements, and $\int_{\mathfrak{n}} f((1+X)d)\, dX = 0$ for each $d$ and each flag $0 \ne W_1 \subseteq W_2$ with $W_1^{\perp_d} = W_2$ and $W_2^{\perp_d} = W_1$, where $\mathfrak{n}$ is the space of $X$ with $X E^n \subseteq W_2$, $XW_2 \subseteq W_1$, $XW_1 = 0$.

**Theorem.** Let $E$ be a CM field with at least two infinite places. There is $C$ such that $T_\tau(\phi; d) = 0$ when $\phi$ is a test function (continuous, compact support, finite-level invariant), $\ell \le r$ on its support, $\phi$ is very cuspidal at each infinite place, $\tau \ge C(1+r)$, and $d$ is regular but not regular elliptic.

## Proof

The proof is `pf_ClassVanish`, reached through `classVanish_of_steps`. The steps, as their statements say:

1. `PairParam` lists the $d$-stable isotropic subspaces as $W_e$, with $e$ in $\{-1,0,1\}^m$. `TorusChar` gives a map $a$ on the adelic twisted centralizer $A_d$ with $\deg(tx, W_e) = \deg(x, W_e) + \langle e, a(t) \rangle$.
2. `ChiGam`: for $\tau \ge C(1 + \ell)$, $\chi_\tau(tx) = \gamma(y(x), a(t))$, a signed sum of indicators over chains of sign vectors, with $y_e(x) = \tau k_e(2n+1-k_e) - \deg(x, W_e)$.
3. `QuotStage` integrates in stages through $A_d$. The inner integral is $V(y(x))$, and `Vfun` gives its properties.
4. If $m = 0$, $V$ is constant, and `Glob1` gives $0$: the twisted orbital integral of a very cuspidal $\phi$ at a regular non-elliptic $d$ vanishes. If $m > 0$, `Glob2` gives $0$ with the weight $V$.

`Glob1` comes from the archimedean lemma `LocVanish` and from `NonEllFlag`: a non-elliptic $d$ has, at some infinite place, a flag $W_1 \subseteq W_2$ as in the definition of very cuspidal. `Glob2` comes from `TwoVanish`, which is built on `LocVanish`, and from `LocFlag`. It uses two different infinite places (`SplitAt2`).

## In the Lean code

The theorem is in [ClassVanish.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/LocalQuotientIntegrals/ClassVanish.lean#L24). It applies [`classVanish_of_steps`](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/LocalQuotientIntegrals/ClassVanishOfSteps.lean#L19) to 18 inputs. Among them are `locVanish`, `NonEll.nonEllFlag`, `PairParam.pairParam`, `TorusCh.torusChar degAdelic`, `ChiGamGlobal.chiGam_of`, `QuotStageInt.quotStage_of`, `mahler` and `sizeBasic`. `classVanish_of_steps` derives 14 intermediate facts and calls `pf_ClassVanish` in [PClassVanish.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/LocalQuotientIntegrals/PClassVanish.lean#L43). We have not opened the proofs of the 18 inputs.

All the class terms are `quotIntegral`, which is $0$ by definition when no quotient normaliser exists.
