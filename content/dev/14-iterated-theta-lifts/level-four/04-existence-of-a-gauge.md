---
title: Existence of a gauge
decls:
  - GlobalTheory.GaugeEx.exists_std_family
  - GlobalTheory.GaugeEx.exists_isGauge_of_isCMExt
  - GlobalTheory.GaugeEx.exists_isGauge
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Existence of a gauge

A gauge is a family of Haar measures on the adelic unitary groups $U_{\mathbb{A}}(J)$, one for each nondegenerate hermitian matrix $J$, that is compatible with changes of basis and with the one-vector step of the previous section. In this section we prove that a gauge exists over each CM extension. We first make a family that has the right shape up to constants. Then we use the gauge square to show that the constants form a cocycle, and we remove them by a coboundary. Last, we fix the normalization with the measures of the quadrics $q_J(x) = \beta$ that a nontrivial additive character gives. The background is in Volume 1, at [Haar measure](/learn/analysis/#haar-measure) and [unitary groups](/learn/groups/#unitary-groups).

**Setting.** We keep the setting of the previous section. So $E/F$ is a CM extension with conjugation $\sigma$, $b$ is an $F$-basis of $E$, and $s$ is a standard measure system for $b$. For an invertible matrix $P$ over $E$, write $P^* = \sigma(P)^{\mathsf T}$.

**Definition 1.4.1 (Gauge family).** A *gauge family* $G$ assigns to each $M$ and each $M \times M$ matrix $J$ over $E$ a measure $\mu_{M,J}$ on $U_{\mathbb{A}}(J)$.

1. $G$ is *Haar* when $\mu_{M,J}$ is a Haar measure for each nondegenerate hermitian $J$.
2. $G$ is *basis invariant* when, for each nondegenerate hermitian $J$ and each $P \in \mathrm{GL}_M(E)$ with $J' = P^* J P$, there is an isomorphism $e \colon U_{\mathbb{A}}(J) \to U_{\mathbb{A}}(J')$ with $g P = P\, e(g)$ for all $g$, and each such $e$ sends $\mu_{M,J}$ to $\mu_{M,J'}$.
3. $G$ is *step compatible* when the following holds for each step data $(x, \beta, B, J')$ for a matrix $J$ of size $M + 1 \geq 3$. There is a nontrivial continuous unitary character $\psi$ of $\mathbb{A}_F / F$. For each such $\psi$ there is a quadric measure $\nu_X$ for $(J, \psi, \beta)$. For each such $\nu_X$ there is a frame isomorphism $e \colon \mathrm{Stab}(x) \to U_{\mathbb{A}}(J')$. For each such $e$, the measure $\mu_{M+1,J}$ is $e^{-1}_* \mu_{M,J'}$ integrated against $\nu_X$ on the orbit of $x$.
4. $G$ is a *gauge* when it is Haar, basis invariant and step compatible.

Here a *quadric measure* $\nu_X$ for $(J, \psi, \beta)$ is a measure on $\mathbb{A}_E^{M+1}$ that lives on the quadric $q_J(X) = \beta$ and that is, for suitable test functions, the product of the local fibre measures at $\beta$ of the self-dual measures for the local parts of $\psi$.

### A family up to constants

**Theorem 1.4.2 (A standard family).** Let $s$ be a standard measure system. Then there are a gauge family $G$ and positive constants $\alpha(M, J)$ with these properties.

1. $G$ is Haar and basis invariant.
2. $\alpha(M, P^* J P) = \alpha(M, J)$ for each nondegenerate hermitian $J$ and each $P \in \mathrm{GL}_M(E)$.
3. For each step data $(x, a, B, J')$ for $J$ of size $M + 1$ with $M \geq 2$, the measure $\alpha(M+1, J)\, \mu_{M+1,J}$ is built from $\alpha(M, J')\, \mu_{M,J'}$ along $(x, B)$.

Lean: `GlobalTheory.GaugeEx.exists_std_family`.

*Proof.* *Step 1: a Haar family.* By the theorem on basis-invariant Haar families, there is a gauge family $G$ that is Haar and basis invariant.

*Step 2: the step constants.* Let $(x, a, B, J')$ be step data with $M \geq 2$. Since $\mu_{M,J'}$ is a Haar measure, the one-vector step theorem gives a Haar measure $\mu$ on $U_{\mathbb{A}}(J)$ that is built from $\mu_{M,J'}$ along $(x, B)$, and it says that this measure is unique. Two Haar measures differ by a positive scalar, so $\mu = c\, \mu_{M+1,J}$ for a unique $c > 0$. The step data determine $a$ and $J'$ from $J$, $x$ and $B$, because $q_J(x) = a$ and $J' = B^* J B$. So we get a function
$$c(M, J, x, B) > 0$$
such that $c(M, J, x, B)\, \mu_{M+1,J}$ is built from $\mu_{M,J'}$ along $(x, B)$, for all step data with $M \geq 2$. For other arguments we put $c = 1$.

*Step 3: the constants are invariant.* Let $P \in \mathrm{GL}_{M+1}(E)$ and $Q \in \mathrm{GL}_M(E)$ with $P x_2 = x$ and $P B_2 = B Q$. Put $J_2 = P^* J P$ and $J_2' = Q^* J' Q$. Let $e_P$ and $e_Q$ be the frame isomorphisms of basis invariance. The change of basis theorem for the one-vector step says that $(x_2, a, B_2, J_2')$ is step data for $J_2$, and that the image under $e_P$ of $c(M, J, x, B)\, \mu_{M+1,J}$ is built from the image under $e_Q$ of $\mu_{M,J'}$. By basis invariance, these images are $c(M, J, x, B)\, \mu_{M+1,J_2}$ and $\mu_{M,J_2'}$. So $c(M, J, x, B)\, \mu_{M+1,J_2}$ and $c(M, J_2, x_2, B_2)\, \mu_{M+1,J_2}$ are both built from $\mu_{M,J_2'}$ along $(x_2, B_2)$. By the uniqueness in step 2 they are equal. A Haar measure gives a positive finite volume to a compact neighbourhood of $1$, so the two scalars are equal:
$$c(M, P^* J P, x_2, B_2) = c(M, J, x, B).$$

*Step 4: the constants form a cocycle.* Take two paths of step data from $J$ to $J_0$, as in the gauge square, with $B_1 C_1 = B_2 C_2$ and $M \geq 2$. Write $c_i = c(M+1, J, x_i, B_i)$ and $c_i' = c(M, J_i, y_i, C_i)$. Scale the first step of path $i$ by $c_i'$. Then $c_i c_i'\, \mu_{M+2,J}$ is built from $c_i'\, \mu_{M+1,J_i}$, and this is built from $\mu_{M,J_0}$. The gauge square says that the two results are equal. So $c_1 c_1'\, \mu_{M+2,J} = c_2 c_2'\, \mu_{M+2,J}$, and by step 3 again
$$c(M+1, J, x_1, B_1)\, c(M, J_1, y_1, C_1) = c(M+1, J, x_2, B_2)\, c(M, J_2, y_2, C_2).$$

*Step 5: the coboundary.* The coboundary theorem for invariant step constants, applied in the group of positive reals, takes an invariant cocycle $c$ and gives invariant constants $\alpha(M, J) > 0$ with
$$\alpha(M+1, J) = c(M, J, x, B)\, \alpha(M, J')$$
for all step data with $M \geq 2$. Now scale the relation of step 2 by $\alpha(M, J')$. Then $\alpha(M, J')\, c(M, J, x, B)\, \mu_{M+1,J} = \alpha(M+1, J)\, \mu_{M+1,J}$ is built from $\alpha(M, J')\, \mu_{M,J'}$. This is part 3. $\square$

### Normalization

**Theorem 1.4.3 (A gauge exists for a CM extension).** Let $E/F$ be a CM extension with conjugation $\sigma$. Then there is a gauge family for $(F, E, \sigma)$ that is a gauge.

Lean: `GlobalTheory.GaugeEx.exists_isGauge_of_isCMExt`.

*Proof.* The field $E$ has degree $2$ over $F$, so it is finite dimensional, and $F$ is totally real. Take any $F$-basis $b$ of $E$. By the theorem on standard local Haar measures, there is a standard measure system $s$ for $b$. Let $G$ and $\alpha$ be as in the theorem on a standard family.

*The quadric constants.* By the comparison of quadric measures, there are constants $\kappa(M) > 0$ with this property. Let $J$ be nondegenerate hermitian of size $M \geq 1$, let $\beta \neq 0$, let $\psi$ be a nontrivial character of $\mathbb{A}_F / F$, and let $\nu$ be the standard fibre measure of $(J, \beta)$. Then a measure $\nu_X$ is a quadric measure for $(J, \psi, \beta)$ if and only if $\nu_X = \kappa(M)\, \nu$. Put
$$K(M) = \prod_{i=0}^{M} \kappa(i), \qquad \mu'_{M,J} = K(M)\, \alpha(M, J)\, \mu_{M,J}.$$
Then $K(M) > 0$ and $K(M+1) = \kappa(M+1)\, K(M)$. We show that $\mu'$ is a gauge.

*Haar.* For nondegenerate hermitian $J$, $\mu'_{M,J}$ is a positive multiple of the Haar measure $\mu_{M,J}$.

*Basis invariant.* Let $J' = P^* J P$. Basis invariance of $G$ gives a frame isomorphism $e$, and each such $e$ sends $\mu_{M,J}$ to $\mu_{M,J'}$. Since $\alpha(M, J') = \alpha(M, J)$, it sends $\mu'_{M,J}$ to $\mu'_{M,J'}$.

*Step compatible.* Let $(x, \beta, B, J')$ be step data for $J$ of size $M + 1 \geq 3$. A nontrivial character $\psi$ of $\mathbb{A}_F / F$ exists because $F$ is totally real. The standard fibre measure $\nu$ of $(J, \beta)$ exists because the rank is at least $3$, and the stabilizer theorem gives a frame isomorphism $e$. Let $\psi'$ be any nontrivial character. Then $\kappa(M+1)\, \nu$ is a quadric measure for $\psi'$, and each quadric measure is equal to it. Let $e'$ be any frame isomorphism. Part 3 of the standard family theorem says that $\alpha(M+1, J)\, \mu_{M+1,J}$ is $e'^{-1}_*(\alpha(M, J')\, \mu_{M,J'})$ integrated against $\nu$. Multiply the stabilizer measure by $K(M)$ and the orbit measure by $\kappa(M+1)$. Then
$$K(M)\, \kappa(M+1)\, \alpha(M+1, J)\, \mu_{M+1,J} = \mu'_{M+1,J}$$
is $e'^{-1}_* \mu'_{M,J'}$ integrated against $\kappa(M+1)\, \nu$. This is step compatibility. $\square$

The product $K(M)$ absorbs the quadric constants one step at a time. So the step condition of the gauge is stated with quadric measures that come from a character, while the proof works with the standard fibre measures of the chosen basis $b$.

**Corollary 1.4.4 (A gauge exists).** Let $E$ be a number field with a star ring structure and CM data over a number field $F$, with conjugation $\sigma$. Then there is a gauge family for $(F, E, \sigma)$ that is a gauge.

Lean: `GlobalTheory.GaugeEx.exists_isGauge`.

*Proof.* The CM data say that $F$ is totally real, $E$ is totally complex, $[E : F] = 2$, and $\tau(\sigma x) = \overline{\tau(x)}$ for each complex embedding $\tau$ of $E$. So $E/F$ is a CM extension with conjugation $\sigma$, and the theorem above applies. $\square$

The gauge of the corollary is used in the construction of the core in the last section of this part. There it is a field of the object of the core, and the core records that it is a gauge.

**Remark 1.4.5 (Formalization).** The step constants of step 2 are chosen with `Classical.choose` over the existence of a scalar, a value of $a$ and a matrix $J'$; the lemma `stepData_unique` then shows that the choice does not depend on $a$ and $J'$. The equality of scalars from equal multiples of a Haar measure is `smul_haar_inj` ([ExistsIsGaugeOfIsCMExt.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsGaugeOfIsCMExt.lean#L56)). The basis-invariant Haar family, the one-vector step theorem, the change of basis theorem, the coboundary theorem, the quadric comparison, the stabilizer theorem and the existence of a nontrivial character are cited through statement files. The theorem `exists_isGauge` is stated at the root of the file, outside the namespace block, with an explicit full name.
