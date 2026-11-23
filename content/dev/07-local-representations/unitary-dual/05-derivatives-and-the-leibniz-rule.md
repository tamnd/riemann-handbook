---
title: Derivatives and the Leibniz rule
decls:
  - GlobalTheory.RgGu.Leib.Hand.leibnizOrd
  - GlobalTheory.CompanionTheory.BZPsiPG.Hand.psiPG
  - GlobalTheory.CompanionTheory.BZPsiPG.Hand.core
  - GlobalTheory.CompanionTheory.BZPsiPG.Hand.ker_le_twKer
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Derivatives and the Leibniz rule

The derivatives of Bernstein and Zelevinsky cut a representation of $\mathrm{GL}_n(k)$ into representations of smaller groups. This section proves the Leibniz rule: the derivatives of a product $\pi_1 \times \pi_2$ have a filtration whose layers are the products of the derivatives of $\pi_1$ and $\pi_2$. The rule is used in the proof of the [irreducibility theorem](/entry/bern-at/), where it identifies the highest derivative of a product, and through it in the step [EveryCharacter](/step/every-character/).

Background: [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module), [generic representations](/learn/representations/#generic-representations-and-local-factors).

### Mirabolic functors

Let $k$ be a nonarchimedean local field and $\psi$ a nontrivial continuous additive character of $k$. For $m \ge 0$ let $P_{m+1} \subseteq \mathrm{GL}_{m+1}(k)$ be the mirabolic subgroup of matrices with last row $(0, \dots, 0, 1)$. It is the semidirect product of $\mathrm{GL}_m(k)$, in the upper left corner, and the group $U_{m+1} \cong k^m$ of unipotent matrices that differ from $1$ only in the last column. We view $P_m$ as a subgroup of $P_{m+1}$ through $\mathrm{GL}_m(k)$. Let $\theta$ be the character $u \mapsto \psi(u_{m,m+1})$ of $U_{m+1}$.

For a smooth representation $(\tau, V)$ of a group $H$, a subgroup $U$ and a character $\chi$ of $U$, the *twisted Jacquet module* $V_{U,\chi}$ is the quotient of $V$ by the span of the vectors $\tau(u) v - \chi(u) v$. For $\tau$ a smooth representation of $P_{m+1}$, put
$$\Psi^-(\tau) = V_{U_{m+1}, 1}, \qquad \Phi^-(\tau) = V_{U_{m+1}, \theta}.$$
The first is a representation of $\mathrm{GL}_m(k)$, and the second of $P_m$, the stabilizer of $\theta$. Both functors are exact. Let $\nu = |\det|$. The normalized functors are $\Psi = \nu^{-1/2}\Psi^-$ and $\Phi = \nu^{-1/2}\Phi^-$.

**Definition 7.5.1 (Derivative).** Let $\pi$ be a smooth representation of $\mathrm{GL}_{m+j}(k)$. Its *$j$-th derivative* is the representation of $\mathrm{GL}_m(k)$ given by $\pi^{(0)} = \pi$ and
$$\pi^{(j)} = \Psi^- (\Phi^-)^{j-1} (\pi|_{P_{m+j}}) \quad \text{for } j \ge 1.$$

Lean: `GlobalTheory.BZMir.Leib.derivB`.

For smooth representations $\pi_1$ of $\mathrm{GL}_r(k)$ and $\pi_2$ of $\mathrm{GL}_t(k)$, let $\pi_1 \times \pi_2$ be the normalized parabolic induction of $\pi_1 \otimes \pi_2$ from the block upper triangular parabolic subgroup. There are two mixed products. For $\rho$ a representation of $\mathrm{GL}_m(k)$ and $\tau$ of $P_j$, the product $\rho \times \tau$ is a representation of $P_{m+j}$ induced from the parabolic subgroup of $P_{m+j}$ with blocks $\mathrm{GL}_m(k)$ and $P_j$. For $\tau$ of $P_{i+1}$ and $\sigma$ of $\mathrm{GL}_t(k)$, the product $\tau \times \sigma$ is a representation of $P_{i+t+1}$ induced from the subgroup $Q$ of $P_{i+t+1}$ with blocks $P_{i+1}$ and $\mathrm{GL}_t(k)$, together with its unipotent radical.

### The Leibniz rule

**Theorem 7.5.2 (Leibniz rule).** Let $r, t, \ell, n \ge 0$ with $r + t = n + \ell$. Let $\pi_1$ and $\pi_2$ be smooth representations of $\mathrm{GL}_r(k)$ and $\mathrm{GL}_t(k)$. Then $D = (\pi_1 \times \pi_2)^{(\ell)}$ has subrepresentations
$$D = F_0 \supseteq F_1 \supseteq \dots \supseteq F_{\ell+1} = 0$$
such that, for $0 \le i \le \ell$, the following hold.

1. If $i \le r$ and $\ell - i \le t$, then $F_i / F_{i+1} \cong \pi_1^{(i)} \nu^{(\ell-i)/2} \times \pi_2^{(\ell-i)} \nu^{i/2}$.
2. Otherwise $F_i = F_{i+1}$.

Lean: `GlobalTheory.RgGu.Leib.Hand.leibnizOrd`.

The twists $\nu^{(\ell-i)/2}$ and $\nu^{i/2}$ come from the normalization of the derivative. With the normalized derivative $d_j = \Psi \Phi^{j-1}(\,\cdot\,|_P)$ they disappear, since $\pi^{(j)} \cong (d_j \pi) \nu^{j/2}$.

The proof rests on six facts. Let $\tau$ be a representation of a mirabolic group and $\rho$, $\sigma$ representations of general linear groups.

1. $(\pi_1 \times \pi_2)|_P$ has a subrepresentation isomorphic to $\pi_1|_P \times \pi_2$, with quotient $\pi_1 \times \pi_2|_P$.
2. $\Psi(\rho \times \tau) \cong \rho \times \Psi(\tau)$.
3. $\Phi(\rho \times \tau) \cong \rho \times \Phi(\tau)$.
4. $\Psi(\tau \times \sigma) \cong \Psi(\tau) \times \sigma$.
5. $\Phi(\tau \times \sigma)$ has a subrepresentation isomorphic to $\Phi(\tau) \times \sigma$, with quotient $\Psi(\tau) \times \sigma|_P$.
6. If $\tau$ is a representation of $P_1 = \{1\}$, then $\Phi(\tau \times \sigma) \cong \Psi(\tau) \times \sigma|_P$.

Facts 1, 3 and 5 come from the orbits of $P$ on a flag variety, by the geometric lemma of Bernstein and Zelevinsky. Facts 2 and 4 say that $\Psi$ commutes with induction. We prove fact 4 below, since its proof shows the method.

*Proof of the theorem.* Restrict $\pi_1 \times \pi_2$ to $P$ and apply the exact functor $\Psi \Phi^{\ell - 1}$ to the sequence of fact 1. On the quotient $\pi_1 \times \pi_2|_P$, facts 2 and 3 give $\Psi\Phi^{\ell-1}(\pi_1 \times \pi_2|_P) \cong \pi_1 \times d_\ell(\pi_2)$, and this is $0$ if $\ell > t$. On the subrepresentation $\pi_1|_P \times \pi_2$, use induction on $\ell$. Each application of $\Phi$ splits $\Phi^{j}(\pi_1|_P) \times \pi_2$ by fact 5 into $\Phi^{j+1}(\pi_1|_P) \times \pi_2$ and $\Psi\Phi^{j}(\pi_1|_P) \times \pi_2|_P$. On the second piece, facts 2 and 3 move the remaining functors onto $\pi_2$, and the result is $d_{j+1}(\pi_1) \times d_{\ell-j-1}(\pi_2)$. When $\Phi^j(\pi_1|_P)$ reaches $P_1$, fact 6 ends the induction, and fact 4 ends it at the last step. Collect the pieces in the order of $i$. Each step of the induction gives one layer, and empty layers occur when $i > r$ or $\ell - i > t$. Finally convert $d_j$ into $\pi^{(j)}$ with the twists. $\square$

### The functor $\Psi$ on a product

Let $\tau$ be a smooth representation of $P_{i+1}$ on $V$ and $\sigma$ a smooth representation of $\mathrm{GL}_t(k)$ on $W$. The space of $\tau \times \sigma$ consists of locally constant functions $f$ on $P_{i+t+1}$ with values in $V \otimes W$, compactly supported modulo $Q$, that transform on the left under $Q$ by $\tau \otimes \sigma$. Let $R \subseteq \mathrm{GL}_{i+t}(k)$ be the block upper triangular parabolic subgroup with blocks $\mathrm{GL}_i(k)$ and $\mathrm{GL}_t(k)$.

For $v \in k^t$ let $u(v) \in U_{i+t+1}$ have last column equal to $v$ in the rows $i+1, \dots, i+t$ and $0$ in the other rows above the diagonal. Define, for $g \in \mathrm{GL}_{i+t}(k)$,
$$(\Phi_{\mathrm{fib}} f)(g) = \text{the image in } \Psi^-(\tau) \otimes W \text{ of } \int_{k^t} f(u(v)\, g)\, dv.$$

**Lemma 7.5.3 (Fibre integral).** The map $\Phi_{\mathrm{fib}}$ is a surjection from the space of $\tau \times \sigma$ onto the space of the unnormalized smooth induction from $R$ to $\mathrm{GL}_{i+t}(k)$ of $\Psi^-(\tau) \otimes \sigma$. It intertwines the action of $\mathrm{GL}_{i+t}(k) \subseteq P_{i+t+1}$, and its kernel is the span of the vectors $(\tau \times \sigma)(u) f - f$ for $u \in U_{i+t+1}$.

Lean: `GlobalTheory.CompanionTheory.BZPsiPG.Hand.ker_le_twKer` (also `GlobalTheory.CompanionTheory.BZPsiPG.Hand.twKer_le_ker`).

*Proof.* The function $v \mapsto f(u(v) g)$ is locally constant with compact support, so the integral exists. A change of variables shows that $\Phi_{\mathrm{fib}}$ intertwines the action of $\mathrm{GL}_{i+t}(k)$ and kills each $(\tau\times\sigma)(u) f - f$. The other part of $U_{i+t+1}$, the first $i$ coordinates of the last column, lies in $Q$ and acts through $\tau$, so it dies in $\Psi^-(\tau)$. Surjectivity follows from a smooth right inverse of the projection to $R \backslash \mathrm{GL}_{i+t}(k)$: lift a function on $\mathrm{GL}_{i+t}(k)$ to $f$ supported near the identity in the variable $v$. For the kernel, assume $\Phi_{\mathrm{fib}} f = 0$. Cover the support of $f$ by finitely many small compact open sets and decompose $f$ accordingly. On each piece the vanishing of the integral over $k^t$ and of the image in $\Psi^-(\tau)$ means, by the criterion of Jacquet and Langlands for compact groups, that $f$ is a finite sum of vectors $(\tau\times\sigma)(u)f' - f'$. $\square$

**Proposition 7.5.4 (Core isomorphism).** There is an isomorphism of representations of $\mathrm{GL}_{i+t}(k)$
$$\Psi^-(\tau \times \sigma) \cong \operatorname{ind}_R^{\mathrm{GL}_{i+t}(k)} \big(\Psi^-(\tau) \otimes \sigma\big),$$
with unnormalized induction on the right.

Lean: `GlobalTheory.CompanionTheory.BZPsiPG.Hand.core`.

*Proof.* The group $\mathrm{GL}_{i+t}(k)$ normalizes $U_{i+t+1}$, and the trivial character is invariant. So $\Psi^-(\tau \times \sigma)$ is the quotient of the space of $\tau \times \sigma$ by the kernel described in the lemma. The surjective map $\Phi_{\mathrm{fib}}$ then gives the isomorphism. $\square$

**Proposition 7.5.5 (Fact 4).** For all smooth $\tau$ and $\sigma$, $\Psi(\tau \times \sigma) \cong \Psi(\tau) \times \sigma$.

Lean: `GlobalTheory.CompanionTheory.BZPsiPG.Hand.psiPG`.

*Proof.* Apply the core isomorphism to $\tau$ and $\sigma$ twisted by suitable powers of $\nu$. The twists account for the factor $\nu^{-1/2}$ in $\Psi$ and for the modulus characters of $Q$ and $R$ in the two normalized inductions. $\square$

**Remark 7.5.6 (Formalization).** The Leibniz rule is in [HighestDerivProd.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/HighestDerivativeProducts/HighestDerivProd.lean#L23). The file name speaks of the highest derivative of a product, which is a different statement, and the file imports about a dozen modules whose declarations the proof does not name. The theorem only passes the six facts to an assembly result in [LeibnizOrderOfExactSequencesStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LeibnizOrderOfExactSequencesStatement.lean#L7). The six facts are stated in [LeibnizOrd.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/LeibnizOrders/LeibnizOrd.lean#L26), except fact 6, which has its own file ([PhiPG0.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/LeibnizOrders/PhiPG0.lean#L12)). The derivative is defined in a second file with the same name, [HighestDerivProd.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/MirabolicDerivatives/LeibnizDerivatives/HighestDerivProd.lean#L31), which also states a weaker form of the rule with the layers in an unknown order. Fact 4 and its core are in [IsSmoothCharDpowM.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/HighestDerivativeProducts/IsSmoothCharDpowM.lean#L158), a file named for a two-line lemma on the smoothness of $\nu^s$. The lemma on the kernel gives only the inclusion of the kernel in the span ([IsSmoothCharDpowM.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/HighestDerivativeProducts/IsSmoothCharDpowM.lean#L126)); the converse inclusion is a separate lemma, and the hard step is taken from an external result on the fibre integral. The Leibniz rule and fact 4 live in two different namespaces.
