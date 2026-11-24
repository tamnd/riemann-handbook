---
title: Theta sections, the key degree and the line bound
decls:
  - GlobalTheory.T.exists_theta_sections_bounded
  - GlobalTheory.CompanionTheory.Ar.Sl.Basis.main
  - GlobalTheory.CompanionTheory.Ar.Sl.LineProof.core_applied
  - GlobalTheory.CompanionTheory.Ar.Sl.LineProof.line_of_key
  - GlobalTheory.T.line_of_key_degree
  - GlobalTheory.T.key_degree_of_bad_reduction
  - GlobalTheory.CompanionTheory.Ar.Sl.keyDeg_of_keyBad
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Theta sections, the key degree and the line bound

One of the top level inputs is a bound for the maximal slope of the Lie algebra of a principally polarized semi-abelian scheme. This section and the next prove it from theta functions. Here we prove two statements. The first, the key degree statement, gives a theta section whose mean square norms have a mean logarithm at most $\frac{1}{2} h + C g$, where $h$ is the negative part of the degree of the Lie bundle. The second, the line statement, bounds from below the archimedean lengths of every nonzero vector of the Lie algebra. The method is the classical one: theta functions of high level, a jet basis at the origin, and a slope inequality. The next section turns the line statement into the slope bound.

### Principally polarized data

**Definition 8.18.1 (Principally polarized datum).** Let $L$ be a number field. A principally polarized datum over $L$ is a principally polarized semi-abelian scheme over $\mathcal{O}_L$ with its Lie bundle $\overline{B}$, a hermitian bundle of rank $g$. We put
$$
h = \max \bigl( - \widehat{\deg}_n \overline{B}, 0 \bigr) ,
$$
where $\widehat{\deg}_n$ is the normalized degree, and for $x \in B$ and an embedding $\sigma$ of $L$ we write $\mathrm{len}_\sigma(x)$ for the hermitian length of $x$ at $\sigma$.

**Definition 8.18.2 (Theta bounds).** Let $\vartheta$ be a family of sections of the theta line bundle, one function $\vartheta_\sigma$ at each frame over each embedding.

1. $\vartheta$ has mean square bound $\Phi$ if there are $b_\sigma > 0$ such that every $\vartheta_\sigma$ has mean square norm $b_\sigma$ at every frame, and $\frac{1}{[L:\mathbb{Q}]} \sum_\sigma \log b_\sigma \le \Phi$.
2. $\vartheta$ has sup bound $M$ if $|\vartheta_\sigma(w)| \le M_\sigma$ at all frames and all points $w$.

We use the [bound of the sup by the mean](/entry/exists-theta-sup-bound-log-mean/): if $\vartheta$ has mean square bound $\Phi$, then it has a sup bound $M$ with
$$
\frac{1}{[L:\mathbb{Q}]} \sum_\sigma \log M_\sigma \le \Phi + C_3 \, g \log(2 + g + \Phi) .
$$

**Definition 8.18.3 (Key degree and line statements).** The key degree statement says: there is $C \ge 0$ such that for every principally polarized datum with $g \ge 1$ there are a finite extension $L'/L$, the datum $D'$ over $L'$ and a theta section of $D'$ with mean square bound $\frac{1}{2} h + C g$. The line statement says: there is $C \ge 0$ such that for every principally polarized datum and every $x \ne 0$ in $B$,
$$
- \frac{1}{[L:\mathbb{Q}]} \sum_\sigma \log \mathrm{len}_\sigma(x) \le C \log(2 + g + h) .
$$

### Theta sections of higher level

**Theorem 8.18.4 (Theta sections with bounded sup).** Let a principally polarized datum be given, let $m \ge 1$, and let $\vartheta$ be a theta section with mean square bound $\Phi$ and sup bound $M$. Then there are a finite extension $L'/L$, the datum $D'$ over $L'$, and $m^{2g}$ sections $s_1, \dots, s_{m^{2g}}$ of the $m^2$ power of the theta line bundle over $L'$, such that each $s_i$ has sup bound $M$ (restricted to the embeddings of $L'$), and at every frame over every embedding of $L'$ the $s_i$ span the theta functions of level $m^2$.

Lean: `GlobalTheory.T.exists_theta_sections_bounded` (also `GlobalTheory.CompanionTheory.Ar.Sl.Basis.main`, a second name).

*Proof.* We take the $m$ torsion points $x_1, \dots, x_{m^{2g}}$ of the generic fibre. They are defined over a number field. For each $x_i$, the function $y \mapsto \vartheta(x_i + m y)$ is a theta function of level $m^2$. By descent along a field extension $K'_i$ there is a section $s^0_i$ of the $m^2$ power over $K'_i$ whose functions are, up to a constant $d_i$, these translates. The constant is nonzero, because the mean square norm $b_\sigma$ of $\vartheta$ is positive, so $\vartheta \ne 0$. The section $s^0_i$ is divisible by $d_i$, and we put $s_i = s^0_i / d_i$. We pass to a common extension $L'$ of the $K'_i$ and pull the datum back to it.

The sup of $s_i$ at a point $w$ is the sup of $\vartheta$ at a translate of $w$, so the theta function sup bound gives $|s_i| \le M$. The translates of a theta function by the $m$ torsion points span the theta functions of level $m^2$, since the multiplier of a translate is a quadratic character, and the characters of the $m$ torsion points are the characters of the theta group of level $m^2$. This gives the spanning. $\square$

The mean square bound $\Phi$ is used only to get $\vartheta \ne 0$.

### The core inequality

**Lemma 8.18.5 (Core inequality).** Let a principally polarized datum be given, let $x \ne 0$ in $B$, let $n = 3n'$ with $n' \ge 1$, and let $s_1, \dots, s_r$ with $r > 0$ be sections of level $n$ with sup bound $M$, where $M_\sigma > 0$. Assume that at every frame there is a nonzero theta function of level $1$, and that the $s_j$ span the theta functions of level $n$ at every frame. Then
$$
0 \le \sum_{i=0}^{n'} \sum_\sigma \log \Bigl( \bigl( e \, n \, n' \bigr)^{i/2} \, \mathrm{len}_\sigma(x)^i \, \sqrt{r} \, M_\sigma \Bigr) .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Sl.LineProof.core_applied`.

*Proof.* Take the line $\mathcal{O}_L x$ in $B$ and the jets of order up to $n'$ along it at the origin. The sections $s_j$ give an integral jet basis: the jets of order $i$ of the $s_j$ span a lattice in $\mathrm{Sym}^i$ of the line, and the integral flag embedding criterion says that some jet of each order $i \le n'$ is integral and nonzero. Its norm is at least $1$ in the product over all places, so the sum over $\sigma$ of its log norm is at least $0$.

At an embedding $\sigma$, the $i$th derivative of a theta function of level $n$ along $x$ is bounded by the Cauchy bound for Gaussian growth: it is at most $(e n n')^{i/2} \mathrm{len}_\sigma(x)^i$ times its sup. The jet is a combination of the $s_j$ whose coefficients are bounded by $\sqrt{r}$ in the $L^2$ sense, so the sup is at most $\sqrt{r} M_\sigma$. Taking the sum of the logs over $i$ and $\sigma$ gives the inequality. $\square$

### The line statement

**Theorem 8.18.6 (Line bound from the key degree).** The key degree statement implies the line statement.

Lean: `GlobalTheory.T.line_of_key_degree` (also `GlobalTheory.CompanionTheory.Ar.Sl.LineProof.line_of_key`, a second name).

*Proof.* Let a datum and $x \ne 0$ be given. Then $g \ge 1$. By the key degree statement, after a finite extension there is a theta section with mean square bound $\Phi = \frac{1}{2} h + C g$. The bound of the sup by the mean gives a sup bound $M$ with
$$
\overline{\log M} \le \Phi + C_3 \, g \log(2 + g + \Phi) ,
$$
where the bar is the mean over the embeddings.

Let $K = \lceil 2 + g^2 + h \rceil$ and $m = 3K$. The theorem on theta sections gives $r = m^{2g}$ sections of level $m^2$ with sup bound $M$ that span. Apply the core inequality with $n = m^2$ and $n' = 3K^2$, so that $n = 3n'$. Divide by $n' [L:\mathbb{Q}]$ and isolate the term in $\log \mathrm{len}_\sigma(x)$. The slope sum gives
$$
- \overline{\log \mathrm{len}(x)} \le \frac{1}{2} \log \bigl( e m^2 n' \bigr) + \frac{2}{n'} \bigl( g \log m + \overline{\log M} \bigr) .
$$
Since $n' = 3K^2$ and $K \ge 2 + g^2 + h$, the second term is bounded by a constant, and the first is bounded by a constant times $\log(2 + g + h)$. The choice of the slope parameter collects the constants into one $C'$ with
$$
- \overline{\log \mathrm{len}(x)} \le C' \log(2 + g + h) .
$$
This is the line statement. $\square$

### The key degree from bad reduction

The key degree statement is proved from the key formula and from the integrality of the key at bad reduction. The key formula is the proved exact formula that, for a principally polarized datum, attaches to a basis $e$ of $B$ and a theta section a number $\kappa(x)$ in $L$ whose archimedean norms are the mean square norms of the theta section times a Gram determinant. The bad reduction statement says that, for a rule $\kappa$ that is homogeneous, functorial, invariant under units, normalized on the theta function of level one and with the right archimedean norm, and for a semi-abelian scheme over a discrete valuation ring with finite residue field that has a theta section that no nonunit divides, the value of $\kappa$ is integral.

**Theorem 8.18.7 (Key degree from bad reduction).** The bad reduction statement implies the key degree statement, with $C = 1$.

Lean: `GlobalTheory.T.key_degree_of_bad_reduction` (also `GlobalTheory.CompanionTheory.Ar.Sl.keyDeg_of_keyBad`, a second name).

*Proof.* Let a datum with $g \ge 1$ be given. After a finite extension $L'$ there are a basis $e$ of $B$ and a theta section $s$ that does not vanish, and the key input from the principally polarized datum gives the value $\kappa(x)$. By the bad reduction statement at each finite place, $\kappa(x)$ is integral, and it is not $0$. So its norm is a nonzero integer and
$$
\frac{1}{[L':\mathbb{Q}]} \sum_\sigma \log |\sigma \kappa(x)| \ge 0 .
$$

The Gram matrix of $e$ at each $\sigma$ is positive definite, so its determinant is positive and $s$ is square integrable. The key formula gives the mean square norm
$$
b_\sigma = \Bigl( \frac{(2\pi)^{2g} \, |\det \mathrm{Gram}_\sigma(e)|^2}{|\sigma \kappa(x)|} \Bigr)^{1/8} .
$$
So
$$
\begin{aligned}
\overline{\log b} &= \frac{2g}{8} \log(2\pi) + \frac{1}{4} \overline{\log |\det \mathrm{Gram}(e)|} - \frac{1}{8} \overline{\log |\kappa(x)|} \\
&\le \frac{g}{4} \log (2\pi) + \frac{1}{4} \overline{\log |\det \mathrm{Gram}(e)|} .
\end{aligned}
$$
The basis $e$ spans $B$, so the formula for the normalized degree by Gram determinants gives that the mean of $\log |\det \mathrm{Gram}(e)|$ is $-2 \widehat{\deg}_n \overline{B}$, which is at most $2h$; so the second term is at most $\frac{1}{2} h$. With $\log(2\pi) \le 4$ the first term is at most $g$. This gives the mean square bound $\frac{1}{2} h + g$. $\square$

**Remark 8.18.8 (Formalization).** In ExistsThetaSectionsBounded.lean the mean square bound is discarded by `obtain ⟨b, hb, -⟩ := hΘ` (line 405); only $b$ is used, to get $\vartheta \ne 0$. The relation of the sections to the translates is `Rel` (line 188), and the division by $d_i$ is `exists_div` (line 216). The key formula is not a hypothesis of `keyDeg_of_keyBad`: the proof takes the proved `GlobalTheory.T.exactKeyFormula_proof` (KeyDegreeOfBadReduction.lean:225), and it gives the constant by `refine ⟨1, zero_le_one, ?_⟩` (line 235); `log_two_pi_le` (line 83) is the bound $\log(2\pi) \le 4$. The constant of the line statement comes from `SlopeParameterChoice.full` (GroundTheory/HeightsAndTheta/Heights/FactorialBounds/Assembly.lean:27). The three `T.*` names are renamings proved by `first | exact @...`. We do not unfold the theta group, the jet basis or the key formula.
