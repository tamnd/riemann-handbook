---
title: The theta measure of a box
decls:
  - GlobalTheory.T.theta_measure_nonzero_vectors_bound
  - GlobalTheory.CompanionTheory.SW.MeanCount.mean_count_box
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta measure of a box

The average of a theta function over the automorphic quotient of a unitary group is the integral of a Schwartz-Bruhat function against a measure on adelic vectors, the theta measure. This section shows that the theta measure of the nonzero rational vectors is finite on each adelic box, with a polynomial bound in the radius. Since every compact set lies in a box, the theta measure is then finite on compact sets, and the average of a theta function is finite. The result serves the step [EveryCharacter](/step/every-character/) of the proof, through the Siegel-Weil formula.

### The theta measure

We keep the notation of the last two sections: $(F, E, \sigma)$ is a CM extension, $J \in M_M(E)$ is nondegenerate Hermitian, $\mu$ is a Haar measure on $U_J(\mathbb{A}_F)$, $\mathcal{F}$ is a fundamental domain for $U_J(F)$, $I_J(S, \Phi)$ is the counting integral, and $B(N, r)$ is the box for a basis $b$ of $E$ over $F$.

**Definition 1.10.1 (Theta measure).** For a set $S \subseteq E^M$ the *theta measure* $\theta_S$ on $\mathbb{A}_E^M$ is
$$\theta_S = \mu(\mathcal{F})^{-1} \sum_{X \in S} (h \mapsto h^{-1} X)_* \bigl(\mu|_{\mathcal{F}}\bigr),$$
the sum over $X \in S$ of the image of $\mu$ restricted to $\mathcal{F}$ under $h \mapsto h^{-1} X$, divided by $\mu(\mathcal{F})$.

Lean: `GlobalTheory.CompanionTheory.SW.thetaMeas`.

For a measurable $\Phi \geq 0$ on $\mathbb{A}_E^M$,
$$\int \Phi\, d\theta_S = \mu(\mathcal{F})^{-1} \int_{\mathcal{F}} \sum_{X \in S} \Phi(h^{-1} X)\, d\mu(h) = \mu(\mathcal{F})^{-1} I_J(S, \Phi).$$
For $S = E^M$ and $\Phi$ a Schwartz-Bruhat function, the inner sum is a theta function of $h$, so the integral is the average of a theta function over the quotient. In particular $\theta_S(B) = \mu(\mathcal{F})^{-1} I_J(S, \mathbf{1}_B)$ for a measurable set $B$.

### The bound

**Theorem 1.10.2 (Theta measure of a box).** Let $(F, E, \sigma)$ be a CM extension, $M \geq 3$, $J \in M_M(E)$ nondegenerate Hermitian, $b$ a basis of $E$ over $F$, $\mu$ a Haar measure on $U_J(\mathbb{A}_F)$, $\mathcal{F}$ a fundamental domain for $U_J(F)$, and $N \geq 1$. Then there is $C$ such that for all $r > 0$
$$\theta_{E^M \setminus 0}\bigl(B(N, r)\bigr) \leq C \bigl( r^{[F:\mathbb{Q}] M} + r^{2[F:\mathbb{Q}] M} \bigr).$$

Lean: `GlobalTheory.T.theta_measure_nonzero_vectors_bound` (also `GlobalTheory.CompanionTheory.SW.MeanCount.mean_count_box`).

*Proof.* Write $d_0 = [F:\mathbb{Q}]$. We use the [theorem on isotropic vectors in a box](/entry/isotropic-vector-count-box-bound/) and the following facts, proved in another part of the development.

1. The integral formula $\int \Phi\, d\theta_S = \mu(\mathcal{F})^{-1} I_J(S, \Phi)$ for measurable $\Phi \geq 0$.
2. Each box $B(N, r)$ is compact, so it is measurable.
3. $\mu(\mathcal{F}) \neq 0$.
4. *Small boxes.* There is $r_0 > 0$ such that, if $Y \in B(N, r_0)$ and $h(Y, Y) = t$ with $t \in F$, then $t = 0$.
5. For $X \in E^M$ the value $h(X, X)$ lies in $F$, and $h(X, X)$ is the same whether computed in $E^M$ or in $\mathbb{A}_E^M$.
6. *Large boxes.* For $M \geq 3$ and $r_1 > 0$ there is $C_2$ with $I_J(E^M \setminus 0, \mathbf{1}_{B(N, r)}) \leq C_2 r^{2 d_0 M}$ for all $r \geq r_1$.

By facts 1 and 2, $\theta_{E^M \setminus 0}(B(N, r)) = \mu(\mathcal{F})^{-1} I(r)$ with $I(r) = I_J(E^M \setminus 0, \mathbf{1}_{B(N, r)})$, and by fact 3 the factor $\mu(\mathcal{F})^{-1}$ is finite. Let $r_1 = \min(r_0, 1)$, take $C_1$ from the theorem on isotropic vectors in a box and $C_2$ from fact 6.

*Small radius.* Let $0 < r \leq r_1$. Let $h \in U_J(\mathbb{A}_F)$ and $X \in E^M$ with $h^{-1} X \in B(N, r)$. The group $U_J(\mathbb{A}_F)$ preserves $h$, so by fact 5, $h(h^{-1} X, h^{-1} X) = h(X, X) = t$ with $t \in F$. Since $B(N, r) \subseteq B(N, r_0)$, fact 4 gives $t = 0$, so $X$ is isotropic. Hence only the vectors in $Z_J$ contribute to $I(r)$, and
$$I(r) = I_J\bigl(Z_J, \mathbf{1}_{B(N, r)}\bigr) \leq C_1 r^{2 d_0 (M-1)}.$$
From $M \geq 2$ we get $M \leq 2(M - 1)$, and since $r \leq 1$, $r^{2 d_0 (M-1)} \leq r^{d_0 M}$.

*Large radius.* For $r \geq r_1$, fact 6 gives $I(r) \leq C_2 r^{2 d_0 M}$.

In both cases $I(r) \leq (|C_1| + |C_2|)(r^{d_0 M} + r^{2 d_0 M})$. Take $C = \mu(\mathcal{F})^{-1}(|C_1| + |C_2|)$. $\square$

The proof gives more for small $r$: the bound $r^{2 d_0 (M-1)}$, which is smaller than $r^{d_0 M}$ for $r < 1$ and $M > 2$. The weaker exponent in the statement is enough for its use, which needs only that the theta measure of a box is finite.

**Remark 1.10.3 (Classical form).** The finiteness of $\int \Phi\, d\theta_{E^M}$ for Schwartz-Bruhat $\Phi$ is the absolute convergence of the theta integral in the Siegel-Weil formula (A. Weil, "Sur la formule de Siegel dans la théorie des groupes classiques", *Acta Math.* 113 (1965)). The theorem here is a quantitative form of it for the nonzero vectors and boxes, under the condition $M \geq 3$; the zero vector contributes $\mathbf{1}_B(0)$, which is finite. The theorem does not give the value of the integral.

**Remark 1.10.4 (Formalization).** In [ThetaMeasureNonzeroVectorsBound.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ThetaMeasureNonzeroVectorsBound.lean#L36) the box is written out in the statement, and it is the set `box b N r`. The facts above are `GlobalTheory.T.theta_measure_integral_formula`, `GlobalTheory.T.adelic_boxes_compact_exhaust`, `GlobalTheory.T.haar_fundamental_domain_exists_unitary`, `GlobalTheory.T.small_box_gram_scalar_zero`, `GlobalTheory.T.rational_gram_adelic_compact_finite` and `GlobalTheory.T.counting_vectors_bounded_large_radius`. The invariance of $h$ under $U_J(\mathbb{A}_F)$ comes from `GlobalTheory.T.adelic_unitary_group_locally_compact`. We have opened their statements, not their proofs. The basis $b$ is indexed by any $d$, but a basis of $E$ over $F$ forces $d = 2$. The hypothesis $M \geq 3$ is passed on to the two counting results; the comparison of exponents at [line 117](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ThetaMeasureNonzeroVectorsBound.lean#L117) needs only $M \geq 2$. The wrapper `GlobalTheory.T.theta_measure_nonzero_vectors_bound` restates `GlobalTheory.CompanionTheory.SW.MeanCount.mean_count_box` without change.
