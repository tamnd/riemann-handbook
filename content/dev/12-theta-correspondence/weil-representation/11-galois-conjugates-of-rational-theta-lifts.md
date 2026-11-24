---
title: Galois conjugates of rational theta lifts
decls:
  - GlobalTheory.GalOne.identity_of_frConst_ofFive
  - GlobalTheory.GalOne.oneMap_of_ext_ofFive
  - GlobalTheory.ConjRatLiftFive.oneMapConj5
  - GlobalTheory.ConjRatLiftFive.conj_lift5
  - GlobalTheory.ConjRatLiftFive.conjugateRationalLift_at_nonBaseEmbedding
  - GlobalTheory.ConjRatLiftFive.conjRatLift5
  - GlobalTheory.T.conjugatesOfRationalThetaLift_from_characterisation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Galois conjugates of rational theta lifts

This section proves that a theta lift with rational coordinates behaves well under the automorphisms of $\mathbb{C}$. A rational theta lift is a vector of coordinates in a number field $L$ whose image under the base embedding of $L$ is, up to a fixed phase, the [global theta lift](/learn/theta/#the-global-theta-lift) of an algebraic vector. The main theorem says three things: the rational coordinates exist and are unique; for each embedding $\sigma$ of $L$ over the CM field, the image of the coordinates under $\sigma$ is the theta lift for the conjugate data, up to a unitary normalization, a central shift and a constant of absolute value $1$; and for the other embeddings, the inner products are the complex conjugates of those at $\bar\sigma$. It is used in [the nonemptiness of the hypotheses](/step/nonempty-hyps/) on the definite side, where the conjugate lifts give the conjugate members of a family of automorphic forms.

### The setting

Let $F$ be a totally real number field, $E/F$ a CM extension, and $K$ a CM field. Let $L$ be a number field with a base embedding $\sigma_0 : L \to \mathbb{C}$. An embedding $\sigma$ of $L$ is *over $K$* if its restriction to $K$ is the restriction of $\sigma_0$ or is in the set of good embeddings of the data; for $\sigma$ not over $K$, the embedding $\bar\sigma$ is over $K$.

Let $G$ be a finite group with a character $\chi : G \to L^\times$. For each index $i$ of the family, let $V_i$ and $W_i$ be the Hermitian spaces of the $i$th pair, with a model $\omega$ of the [Weil representation](/learn/theta/#the-weil-representation) of $\mathrm{U}(V_i) \times \mathrm{U}(W_i)$ for a standard additive character of sign $-1$, and let $\Theta_i$ be the theta lift of algebraic vectors $x$ of $V_i$ with coefficients in $L$ to automorphic forms on $\mathrm{U}(W_i)$.

For each embedding $\sigma$ of $L$ let $\mathcal{H}_{i,\sigma}$ be a Hilbert space of automorphic forms on $\mathrm{U}(W_i)$ with an action $g \mapsto \rho_{i,\sigma}(g)$ of $G$, and let
$$j_\sigma : L^{n_i} \to \mathcal{H}_{i,\sigma}$$
be the $\sigma$-semilinear map that sends coordinates to the form with those coordinates in a fixed basis.

**Definition 1.11.1 (Rational lift).** Let $\varphi \in \mathbb{C}$. A vector $y \in L^{n_i}$ is a *rational lift* of $x$ with phase $\varphi$ if $j_{\sigma_0}(y) = \varphi\, \Theta_i(x)$.

**Definition 1.11.2 (Conjugate datum).** For an embedding $\sigma$ over $K$, a *conjugate datum* consists of the characters $\mu'$ and $\eta'$ obtained from the [[Hecke characters|KPYFGB342X]] of the pair by $\sigma$, a coefficient space $C$ with a $\sigma$-semilinear coefficient map $c_1$, a module $H$ of automorphic forms with values in $C$, a $\sigma$-semilinear map $j$ from algebraic vectors to $H$, and a theta map $\vartheta : H \to \mathcal{H}_{i,\sigma}$ built from the Weil representation $\omega^\sigma$ for $\mu'$ and $\eta'$.

**Definition 1.11.3 (Conjugation at $\sigma$).** The rational lifts are *conjugate at $\sigma$* with phase $\varphi$ if the weights of the pair at $\sigma$ and at $\sigma_0$ agree, a conjugate datum exists, and there are a phase function $u$ on $\mathrm{U}(W_i)(\mathbb{A}_F)$ with a unitary map $U$ of $\mathcal{H}_{i,\sigma}$ that multiplies by $u$, equal to $1$ when $\sigma = \sigma_0$, and a central element $z \in G$, such that for each conjugate datum there is $\kappa \in \mathbb{C}$ with $|\kappa| = 1$ and
$$U\bigl(j_\sigma(y)\bigr) = \kappa\, \rho_{i,\sigma}(z)\, \vartheta\bigl(j(x)\bigr)$$
for each rational lift $y$ of $x$.

### The identity at an extension

Let $\sigma$ be over $K$, and let $\sigma'$ be an extension of $\sigma$ to the coefficient field $L'$ of the data, so $\sigma' \circ \iota = \sigma$ for the inclusion $\iota : L \to L'$. Let $(h_j)$ be representatives of the classes of $\mathrm{U}(V_i)$ modulo the level, with orders $\gamma_j$ of their stabilizers and the volume $\operatorname{vol}$ of the level.

**Proposition 1.11.4 (Conjugate theta identity).** In this setting there are $c_0 \in \mathbb{C}$ with $|c_0| = 1$ and a central $z \in G$ such that, for each upper vector $x_1$ over the class representatives, each theta class form $f'$ at the classes $x_1$, each decomposition of $z f'$ as a combination $\sum_k a_k f_k$ of basis forms, and each $k_0 \in \mathrm{U}(W_i)(\mathbb{A}_F)$,
$$\begin{aligned} \varphi\, c_0 \sum_j \sigma'\bigl(\operatorname{vol}\,\gamma_j^{-1}\bigr)\, \theta^\omega(h_j, k_0) &= \sum_k \sigma'(a_k)\, \lambda\, c\, \mu\, r(f_k), \end{aligned}$$
where $\theta^\omega(h_j, k_0)$ is the theta kernel of the conjugate Weil representation at the vector of $x_1(j)$, and $\lambda$, $c$, $\mu$ and $r(f_k)$ are the Lie factor, the frame constant, the measure scalar and the reading of $f_k$ at $k_0$.

Lean: `GlobalTheory.GalOne.identity_of_frConst_ofFive`.

*Proof.* Each side is computed in two ways. On the adelic side, the vacuum of the conjugate pair is a tensor product of local vacua, and its theta kernel at $h_j$ is the product of the adelic value at the finite places and the classical value at the infinite places. On the geometric side, the class form $f'$ is read at the framed point of each class, and the reading at an embedding is the conjugate of the reading at the base embedding, up to the dilation of the coefficients. The central shift $z$ comes from the action of the center of $G$ on the classes, and the constant $c_0$ from the cover constant of the two markings, which has absolute value $1$. With the marking laws and the duality of markings, the two computations agree term by term, and a linear combination of the relations gives the identity. $\square$

**Proposition 1.11.5 (One map from an extension).** In the setting above, with a conjugate datum at $\sigma$, there are a phase function $u$, a central $z \in G$ and $\kappa \in \mathbb{C}$ with $|\kappa| = 1$ such that:

1. for each lift pair $(g, k)$ with $g \in G$ and $k \in \mathrm{U}(W_i)(\mathbb{A}_F)$, each form $f$ of the family and each $h$,
$$u(h)\, \phi(g f)(h) = \sigma(\chi(g))\, u(hk)\, \phi(f)(hk),$$
where $\phi(f)$ is the automorphic function of $f$ at $\sigma$;
2. for each class sum $x_0 = \sum_k a_k f_k$, with $v$ the tensor of the vacuum vectors at $\sigma$, and each $g$,
$$\kappa\, \vartheta\bigl(j(x_0)\bigr)(v)(g) = \sum_k \sigma(a_k)\, u(g)\, \phi(z f_k)(g).$$

Lean: `GlobalTheory.GalOne.oneMap_of_ext_ofFive`.

*Proof.* Put $u(g) = c(g)/c_E(g)$, the frame constant at $\sigma'$ divided by the base constant. Both have absolute value $1$, so $u$ is a phase function. The first clause is the equivariance of the frame constant at $\sigma'$ under $G$: the character of $g$ at $\sigma$ is the image under $\sigma'$ of an element $b$ of the base field, and the frame constant is moved by $b$. For the second clause take $c_0$ and $z$ from the conjugate theta identity, and $\varphi'$ with $|\varphi'| = 1$ from the comparison of the coefficient maps at $\sigma$ and $\sigma'$. Then $\kappa = \varphi' c_0$ has absolute value $1$, and the identity, read at $g$, is the second clause. $\square$

**Corollary 1.11.6 (One map at a conjugate datum).** For each $\sigma$ over $K$ and each conjugate datum at $\sigma$ the conclusions of the last proposition hold.

Lean: `GlobalTheory.ConjRatLiftFive.oneMapConj5`.

*Proof.* Choose class representatives. The embedding $\sigma$ of $L$ extends to an embedding $\sigma'$ of $L'$, since $L'$ is a finite extension of $L$. The function $f$ of the datum is a theta function, since it is the theta lift of the constant polynomial $1$. The proposition applies. $\square$

### Conjugates of rational lifts

**Proposition 1.11.7 (Conjugate of a rational lift).** Let $\sigma$ be over $K$ and fix a conjugate datum at $\sigma$. Then there are a theta map $\vartheta$, a phase function $u$ with its unitary map $U$, a central $z \in G$ and $\kappa \in \mathbb{C}$ with $|\kappa| = 1$ such that $\vartheta$ is the projection of the theta map of the datum and
$$U\bigl(j_\sigma(y)\bigr) = \kappa\, \rho_{i,\sigma}(z)\, \vartheta\bigl(j(x)\bigr)$$
for each rational lift $y$ of $x$.

Lean: `GlobalTheory.ConjRatLiftFive.conj_lift5`.

*Proof.* The proof has five steps.

First, the base case. At $\sigma_0$ there are an action of $G$ on the forms of the family, a central $z_0$, a root of unity $\zeta$ with $\zeta^m = 1$ for some $m > 0$, and for each $x$ a class sum $x = \sum_k a_k f_k$ whose rational lift is
$$y = \zeta\,\chi(z_0)^{-1}\textstyle\sum_k a_k\, \rho(z_0) f_k,$$
written in coordinates.

Second, the corollary gives $u$, $z$ and $\kappa_1$ at $\sigma$.

Third, equivariance. Put $J = U \circ j_\sigma$. The evaluation of forms at the vacuum vectors is injective, and the first clause of the corollary gives
$$J(g f) = \sigma(\chi(g))\, \rho_{i,\sigma}(g)\, J(f)$$
for each $g \in G$ and each form $f$.

Fourth, the theta map. By the second clause of the corollary, for each $x$ the value of the theta map of the datum at the vacuum is the evaluation of a vector of $\mathcal{H}_{i,\sigma}$, so the theta map factors through a map $\vartheta$ to $\mathcal{H}_{i,\sigma}$.

Fifth, the constants. Put
$$\kappa = \sigma(\zeta)\, \sigma(\chi(z_0))\, \sigma(\chi(z))^{-1}\, \kappa_1, \qquad z_1 = z_0 z^{-1}.$$
The values of $\chi$ are roots of unity, $\sigma(\zeta)$ is a root of unity, and $|\kappa_1| = 1$, so $|\kappa| = 1$, and $z_1$ is central. A rational lift is unique, since $j_{\sigma_0}$ is injective, so $y$ is the vector of the first step. Apply $J$ to it, use the equivariance for $z_0$, and compare with the second clause of the corollary. This gives the formula with $\kappa$ and $z_1$. $\square$

**Proposition 1.11.8 (Conjugation at a non-base embedding).** Let $\sigma \neq \sigma_0$ be over $K$. Then the rational lifts are conjugate at $\sigma$.

Lean: `GlobalTheory.ConjRatLiftFive.conjugateRationalLift_at_nonBaseEmbedding`.

*Proof.* The characters of the pair at $\sigma$ give $\mu'$ and $\eta'$, the clauses of the characterization of conjugate lifts give the coefficient data $C$, $c_1$, $H$, $j$, a Weil representation $\omega^\sigma$, a vacuum, an orthonormal basis and a theta map, and these form a conjugate datum. The proposition on conjugates of rational lifts gives $U$, $u$, $z$ and $\kappa$. The phase condition at $\sigma_0$ is empty, since $\sigma \neq \sigma_0$. $\square$

**Theorem 1.11.9 (Galois conjugates of rational theta lifts).** Let the data satisfy the five core conditions, with a standard character of sign $-1$, a tie of the forms to the weights, its bar condition, the extension of the coefficient map, uniformity of the family, and the pins of the one-map data. For each index $i$ and each phase $\varphi$ of the one-map data:

1. each algebraic vector $x$ has a unique rational lift with phase $\varphi$;
2. for each comparison datum and each $\sigma$ over $K$, the rational lifts are conjugate at $\sigma$;
3. for each $\sigma$ not over $K$, the embedding $\bar\sigma$ is over $K$, and
$$\langle j_\sigma(y), j_\sigma(y')\rangle = \overline{\langle j_{\bar\sigma}(y), j_{\bar\sigma}(y')\rangle}$$
for all $y$, $y'$.

Lean: `GlobalTheory.ConjRatLiftFive.conjRatLift5` (also `GlobalTheory.T.conjugatesOfRationalThetaLift_from_characterisation`, a second name).

*Proof.* The tie of the forms to the weights evaluates, and the evaluation is injective, by the model conditions. The map $j_{\sigma_0}$ is injective since the basis forms are independent. For (1), the base case gives a rational lift of each $x$, and it is unique since $j_{\sigma_0}$ is injective. For (2), if $\sigma = \sigma_0$ the conjugation holds with $u = 1$ by the base case, and if $\sigma \neq \sigma_0$ it is the last proposition. For (3), an embedding not over $K$ has a conjugate over $K$, and the inner products are related by the conjugate readings of the central shift and the phase. $\square$

**Remark 1.11.10.** The theorem is a form of the rationality of theta lifts for unitary groups: the theta lift of an algebraic vector, normalized by a phase, has coordinates in a number field, and its Galois conjugates are theta lifts of the conjugate data. Compare M. Harris, *L-functions and periods of polarized regular motives*, J. Reine Angew. Math. 483 (1997), 75 to 161, where the rationality of theta lifts between unitary groups is proved through the action of $\operatorname{Aut}(\mathbb{C})$ on Fourier coefficients. Here the action is followed through the [Fock model](/learn/theta/#the-fock-model) and the class sums of the definite side.

**Remark 1.11.11 (Formalization).** The conjugate theta identity is `identity_of_frConst_ofFive` (CoefMapNormEquivariantBasisOfFive.lean, line 2651), and the proposition on one map is `oneMap_of_ext_ofFive` (same file, line 2760, under `maxHeartbeats 1600000` at line 2758). The theorem is the proposition `GlobalTheory.LowRow.ConjRatLift5`, whose conclusion is `GalOut` (Definitions/Divisors/FormalDegreeUpperC.lean, lines 101 and 86); conjugation at $\sigma$ is `ConjAt` and the rational lift is `IsRatLift` (BlockTheory/DivisorBase/WeilGramSignature.lean, lines 137 and 134). The remaining results are in ConjugatesOfRationalThetaLiftFromCharacterisatio.lean, a file name cut short, with `oneMapConj5` at line 28, `conj_lift5` at line 71 (under `maxHeartbeats 800000`), `conjugateRationalLift_at_nonBaseEmbedding` at line 192 and `conjRatLift5` at line 227. In `oneMapConj5` the comparison hypothesis `Comparison₂` is bound as `_` and not used (line 29). In `conjRatLift5` the hypotheses `IsStdChar` and `IoExt` are bound as `_` and not used (line 228). The proof of the identity uses many named results, among them `factsAt_ofFive`, `cover_const_at_ofFive`, `adelic_value_ofFive` and `geometric_value_ofFive`, and ends with `linear_combination`; the clauses of the characterization come from `conjugateLift_of_characterisationClauses` and `conjugateCharacters_embeddings_of_characterisation`, and the third clause of the theorem from `centralShift_phase_conjReadings_fiveClauses`. We have not opened these proofs, so the arguments for them above are ours. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (ConjugatesOfRationalThetaLiftFromCharacterisatioStatement.lean, line 9).
