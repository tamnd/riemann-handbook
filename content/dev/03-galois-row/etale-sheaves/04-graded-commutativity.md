---
title: Graded commutativity
decls:
  - LateralTheory.Fix.CupProductTensor.awFlip
  - LateralTheory.Fix.CupProductTensor.cupFlip
  - LateralTheory.Fix.CupProductTensor.ringComm'
  - LateralTheory.E.RingCommutativity.goal_of
  - LateralTheory.Fix.EtaleChapterDTwo.s40
  - LateralTheory.Fix.EtaleChapterDTwo.s41
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Graded commutativity

This section proves that the cup product is graded commutative:
$$
a \cup b = (-1)^{nm}\, b \cup a \qquad \text{for } a \in H^n(E, \mathbb{Z}/q(i)),\ b \in H^m(E, \mathbb{Z}/q(j)).
$$
With [associativity](/entry/cup-product-tensor-holds-of/) and [the unit law](/entry/s38/), this gives the three ring laws of the cup product. The weights do not enter the sign, since $\mathbb{Z}/q(i) \otimes \mathbb{Z}/q(j) \cong \mathbb{Z}/q(j) \otimes \mathbb{Z}/q(i)$ by the swap of factors, with no sign.

In algebraic topology the same law holds for the cup product of singular cochains (Hatcher, *Algebraic Topology*, Theorem 3.11). There are two proofs. Hatcher uses the reversal of the order of the vertices of each simplex. Steenrod builds a natural cochain homotopy between the Alexander-Whitney product and its swap: the cup-$1$ product. The code uses Steenrod's method.

We keep the pairings and the Alexander-Whitney products of [the second section](/entry/cup-product-tensor-holds-of/).

**Definition 6.4.1 (Flip of a pairing).** Let $\mu : \mathcal{I} \times \mathcal{J} \to \mathcal{K}$ and $\nu : \mathcal{J} \times \mathcal{I} \to \mathcal{K}$ be pairings. Then $\nu$ is a *flip* of $\mu$ if
$$
\nu(b, a) = (-1)^{st}\, \mu(a, b) \qquad \text{for } a \in \mathcal{I}^s(U),\ b \in \mathcal{J}^t(U).
$$

The sign is the Koszul sign for moving $b$ past $a$. For example, $\mu(a, b) = (-1)^{st} \nu(b, a)$ defines a flip $\nu$ of any pairing $\mu$, and $\nu$ satisfies the Leibniz rule.

**Lemma 6.4.2 (Swap of Alexander-Whitney products).** Let $\nu$ be a flip of $\mu$, let $E$ be a space, and let $\alpha$ and $\beta$ be cocycles of degrees $n$ and $m$ with values in $\mathcal{I}$ and $\mathcal{J}$. Let $\gamma$ be an Alexander-Whitney product of $\alpha$ and $\beta$ for $\mu$, and let $\gamma'$ be an Alexander-Whitney product of $\beta$ and $\alpha$ for $\nu$. Then
$$
[\gamma] = (-1)^{nm} [\gamma'] \quad \text{in } H^{n+m}(E, \mathcal{K}).
$$

Lean: `LateralTheory.Fix.CupProductTensor.awFlip`.

*Proof.* For $N \geq 0$ let $\mathrm{Pr}(N)$ be the set of pairs $(f, g)$ of maps of simplices $f : [p] \to [N]$ and $g : [r] \to [N]$. An integer combination $c$ of such pairs acts on cochains: for an $N$-simplex $x$, $c(\alpha, \beta)(x)$ is the sum of the terms $\mu(\alpha_p(x \circ f), \beta_r(x \circ g))$, with the coefficients of $c$. Two combinations are special. Let $\mathrm{aw}_N$ be the sum of the pairs ($[0,p]$, $[p,N]$), front face and back face. Let $\mathrm{wa}_N$ be the sum of the pairs ($[N-r, N]$, $[0, N-r]$), back face and front face, each with the sign $(-1)^{r(N-r)}$. By the flip relation, $\mathrm{aw}_N(\alpha, \beta)$ is the formula for $\gamma_N$, and $\mathrm{wa}_N(\alpha, \beta)$ is $(-1)^{nm}$ times the formula for $\gamma'_N$.

The code proves that there are combinations $h_N$, of degree $N + 1$, with
$$
\begin{aligned}
d h_0 &= \mathrm{aw}_0 - \mathrm{wa}_0, \\
d h_{N+1} + \partial h_N &= \mathrm{aw}_{N+1} - \mathrm{wa}_{N+1},
\end{aligned}
$$
where $d$ is the differential inside each simplex and $\partial$ comes from the faces of the simplices. This is a chain homotopy between the Alexander-Whitney diagonal and its swap, of the kind that Steenrod used to define the cup-$1$ product. Let $\eta$ be the cochain of degree $n + m - 1$ with $\eta_N(x) = h_N(\alpha, \beta)(x)$. Since $\alpha$ and $\beta$ are cocycles, the two relations give
$$
\delta \eta = (-1)^{n+m} \big( \mathrm{aw}(\alpha, \beta) - \mathrm{wa}(\alpha, \beta) \big) = (-1)^{n+m} \big( \gamma - (-1)^{nm} \gamma' \big).
$$
So $\gamma$ and $(-1)^{nm} \gamma'$ differ by a coboundary. $\square$

**Lemma 6.4.3 (Swap of cup products).** Let $\nu$ be a flip of $\mu$ and let $E$ be a space. For classes $a \in H^n(E, \mathcal{I})$ and $b \in H^m(E, \mathcal{J})$,
$$
a \cup_\mu b = (-1)^{nm}\, b \cup_\nu a.
$$

Lean: `LateralTheory.Fix.CupProductTensor.cupFlip`.

*Proof.* Write $a = [\alpha]$ and $b = [\beta]$. The code proves that, for every pairing, Alexander-Whitney products of cocycles exist and $\cup_\mu$ sends the two classes to the class of such a product. Choose $\gamma$ for $(\alpha, \beta, \mu)$ and $\gamma'$ for $(\beta, \alpha, \nu)$. Then $a \cup_\mu b = [\gamma]$ and $b \cup_\nu a = [\gamma']$, and [the previous lemma](/entry/aw-flip/) gives $[\gamma] = (-1)^{nm}[\gamma']$. $\square$

**Theorem 6.4.4 (Graded commutativity).** Let $q \geq 1$ and let $E$ be a space. For $a \in H^n(E, \mathbb{Z}/q(i))$ and $b \in H^m(E, \mathbb{Z}/q(j))$,
$$
a \cup b = (-1)^{nm}\, b \cup a \quad \text{in } H^{n+m}(E, \mathbb{Z}/q(i+j)).
$$

Lean: `LateralTheory.Fix.CupProductTensor.ringComm'` (also `LateralTheory.E.RingCommutativity.goal_of` and `LateralTheory.Fix.EtaleChapterDTwo.s40`, second names).

*Proof.* Let $\mu = \mu_{i,j}$ be the chosen twisted pairing, so $a \cup b = a \cup_\mu b$. The code proves that each pairing has a flip $\nu$ (and that $\mu$ is a flip of $\nu$). In degree $0$ the sign is $1$, so
$$
\nu\big(\iota \langle \zeta \rangle_j,\ \iota \langle \zeta \rangle_i\big) = \mu\big(\iota \langle \zeta \rangle_i,\ \iota \langle \zeta \rangle_j\big) = \iota \langle \zeta \rangle_{i+j}.
$$
So $\nu$ is a twisted pairing of weights $(j, i)$. By [the uniqueness theorem](/entry/cup-product-tensor-holds-of/), $b \cup_\nu a = b \cup a$. Then [the swap of cup products](/entry/cup-flip/) gives $a \cup b = (-1)^{nm} b \cup a$. $\square$

**Corollary 6.4.5 (Ring laws).** Let $q \geq 1$ and let $E$ be a space. The cup product on $H^*(E, \mathbb{Z}/q(*))$ satisfies:

1. if $q$ is invertible on $E$, then $1_E \cup a = a$ for every class $a$;
2. $(a \cup b) \cup c = a \cup (b \cup c)$;
3. $a \cup b = (-1)^{nm} b \cup a$ for $a$ of degree $n$ and $b$ of degree $m$.

Lean: `LateralTheory.Fix.EtaleChapterDTwo.s41`.

*Proof.* This is [the unit law](/entry/s38/), [associativity](/entry/cup-product-tensor-holds-of/) and [graded commutativity](/entry/ring-comm-prime/), put together. $\square$

**Remark 6.4.6.** The Lean names of this section do not say what the statements are. The corollary is the term `s41`, of type `LeafA6ring`, which is a second name of `DivisorRingCompatibility` ([DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L34)). It has nothing to do with divisors. The homotopy $h$ of the first lemma comes from a theorem named `intersectionNumber_baseChange` in the namespace `PrismAlexanderWhitneySwapChainHomotopy`, and the existence of flips from a theorem of the same short name in the namespace `EtaleComplexPairingFlipExists`. Neither is about intersection numbers or base change. The theorem `RingCommutativity.goal_of` is `ringComm'`, and `s40` is `RingCommutativity.goal_of`, with no change.

**Remark 6.4.7.** Graded commutativity and associativity hold for every space $E$ and every $q \geq 1$, also when $q$ is not invertible on $E$. Only the unit law needs the hypothesis. If $q$ is a unit on no scheme, then $\mathrm{Prim}_q$ is always empty and every pairing is twisted, including the zero pairing. The laws then hold, but they may hold for the trivial reason that the chosen cup product is $0$.
