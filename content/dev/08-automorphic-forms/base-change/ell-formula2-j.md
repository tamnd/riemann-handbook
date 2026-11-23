---
id: ell-formula2-j
title: The truncated twisted trace on a pair of groups is its elliptic part
kind: theorem
decl: PositivityTheory.Rg.BcB.CV.ellFormula2J
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.QuotientVanishing.LocalQuotientIntegrals.EllFormula2J
covers: 915
status: drafted
drafted_by: writer@claude
---
This theorem says that a truncated twisted trace formula on $\mathrm{GL}_a \times \mathrm{GL}_b$ over the adeles of a CM field has only elliptic terms, once the truncation parameter is large compared with the support of the test function. It is a step below [EveryCharacter](/step/every-character/). Its result goes to four declarations, among them `ellLin_holds` and `growthJ_holds`. The vanishing of the other terms is [`classVanish2`](/entry/class-vanish2/).

## Statement

Let $E$ be a CM field with at least two infinite places, and let $\theta(g) = \bar g^{-T}$ on $G_n = \mathrm{GL}_n(\mathbb{A}_E)$ and on $\mathrm{GL}_n(E)$. For $d \in \mathrm{GL}_n(E)$, let $N(d) = d\,\theta(d)$. Call $d$ *regular* if the characteristic polynomial of $N(d)$ is separable, and *regular elliptic* if also all its complex roots, under every embedding of $E$, have absolute value $1$.

The truncation. For $x \in G_n$ and a subspace $W \subseteq E^n$, let $\deg(x, W)$ be minus the sum over all places of the log norm of $x^{-1}W$. Let $\Omega_\tau$ be the set of $x$ with $\deg(x, W) \le \tau k(2n+1-k)$ for each $W$ of dimension $k$, and $\deg(x, E^n) \ge -\tau$. Let $\chi_\tau$ be its indicator. Let $\ell(g)$ be the log size of $g$ plus that of $g^{-1}$.

Let $\phi$ be a test function on $G_a \times G_b$ with level $r$. That is: $\phi$ is continuous with compact support, $\ell(g_1), \ell(g_2) \le r$ on its support, it is invariant on both sides under an open subgroup of the finite adelic group, and each one-variable slice is a test function that is very cuspidal at each infinite place and is supported on twisted conjugates of regular rational elements.

**Theorem.** There is $C \ge 0$ such that for $r \ge 0$, $\tau \ge C(1+r)$ and fundamental domains $F_1, F_2$ for $\mathrm{GL}_a(E)$ and $\mathrm{GL}_b(E)$,

$$\int_{F_1 \times F_2} \chi_\tau(x_1)\chi_\tau(x_2) \sum_{d_1, d_2} \phi\bigl(x_1^{-1} d_1 \theta(x_1), x_2^{-1} d_2 \theta(x_2)\bigr)\, dx = \sum_{(d_1, d_2)\ \text{reg. ell.}} O_{d_1, d_2}(\phi).$$

The right side runs over pairs of twisted classes, both regular elliptic. $O_{d_1,d_2}$ is the integral of $\phi$ over the twisted orbit, as a quotient integral over the rational twisted centralizers.

## Proof

The proof is `ellFormula2_of` with four inputs. `unfold2_of mahler` unfolds the left side into a finite sum of class terms. Here `mahler` says that $\Omega_\tau$ is closed, left $\mathrm{GL}_n(E)$-invariant, and inside $\mathrm{GL}_n(E)$ times a compact set. Then each pair of classes is one of three kinds.

1. Both regular elliptic. `ellTerm` says that $x \in \Omega_\tau$ when $\tau \ge C(1 + \ell(x^{-1}d\theta(x)))$. On the support of $\phi$ this holds, so the cut-off is $1$ and the class term is $O_{d_1,d_2}(\phi)$.
2. Both regular, not both elliptic. The term is $0$ by [`classVanish2`](/entry/class-vanish2/).
3. Not both regular. The integrand is $0$ by the support condition on the slices.

`sizeBasic` gives $\ell \ge 0$. $C$ is the maximum of $0$ and the three constants.

## In the Lean code

The theorem is in [EllFormula2J.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/LocalQuotientIntegrals/EllFormula2J.lean#L12). `EllFormula2J`, the test condition `IsTest2J` and `ellFormula2_of` are in [QuotIntegralZero.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/QuotientVanishing/QuotIntegralZero.lean#L92). `mahler`, `ellTerm` and `sizeBasic` are one-line wrappers in the namespace `D1`.

The quotient integral `quotIntegral` is $0$ by definition when no quotient normaliser exists. We have not checked that one always exists here.
