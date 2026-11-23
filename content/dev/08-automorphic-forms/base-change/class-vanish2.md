---
id: class-vanish2
title: Non-elliptic class terms vanish on a pair of groups
kind: theorem
decl: PositivityTheory.Rg.BcB.CV.classVanish2
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.QuotientVanishing.LocalQuotientIntegrals.EllFormula2J
covers: 739
status: drafted
drafted_by: writer@claude
---
This theorem kills the class terms of the truncated twisted trace on $\mathrm{GL}_a \times \mathrm{GL}_b$ in which the two classes are regular but not both elliptic. It is case 2 of the proof of [the elliptic formula](/entry/ell-formula2-j/). It reduces the statement to one group at a time, where the work is done by [`classVanish`](/entry/class-vanish/).

## Statement

We use the notation of [the elliptic formula](/entry/ell-formula2-j/): the twist $\theta$, the cut-off $\chi_\tau$, the size $\ell$, and test functions $\phi$ of level $r$. For $d_1 \in \mathrm{GL}_a(E)$ and $d_2 \in \mathrm{GL}_b(E)$ the class term is the quotient integral

$$T_\tau(\phi; d_1, d_2) = \int_{Z_{d_1} \times Z_{d_2} \backslash G_a \times G_b} \chi_\tau(x_1)\chi_\tau(x_2)\, \phi\bigl(x_1^{-1} d_1 \theta(x_1), x_2^{-1} d_2 \theta(x_2)\bigr)\, dx,$$

where $Z_d$ is the image of the rational twisted centralizer of $d$.

**Theorem.** Let $E$ be a CM field with at least two infinite places. There is $C$ such that $T_\tau(\phi; d_1, d_2) = 0$ whenever $\phi$ is a test function of level $r$, $\tau \ge C(1+r)$, $d_1$ and $d_2$ are regular, and $d_1, d_2$ are not both regular elliptic.

## Proof

Take $C = \max(0, C_a, C_b)$, with $C_a$, $C_b$ the constants of `classVanish` for $\mathrm{GL}_a$ and $\mathrm{GL}_b$.

If $1 + r < 0$, then $\phi = 0$, since $\ell \ge 0$ (`sizeBasic`) and $\ell \le r$ on the support. So the term is $0$.

Let $1 + r \ge 0$. Suppose $d_1$ is regular elliptic. Then $d_2$ is not. By Fubini (`sliceTerm_of mahler`), $T_\tau$ is an outer integral over $x_1$ of $\chi_\tau(x_1)$ times the one-group class term of the slice $g \mapsto \phi(x_1^{-1}d_1\theta(x_1), g)$ at $d_2$. The slice is a very cuspidal test function of size at most $r$, so `classVanish` makes the inner term $0$. If $d_1$ is not regular elliptic, slice the other way and apply `classVanish` at $d_1$.

## In the Lean code

The theorem is one line in [EllFormula2J.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/LocalQuotientIntegrals/EllFormula2J.lean#L10):

```
classVanish2_of (GlobalTheory.CompanionTheory.SliceFubini.sliceTerm_of mahler) classVanish sizeBasic
```

The argument is `classVanish2_of` in [QuotIntegralZero.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/QuotIntegralZero.lean#L57). It is short and uses only the three inputs. The slicing lemma `sliceTerm_of` is stated as `SliceTerm`; we have not opened its proof. The real content is in `classVanish`.
