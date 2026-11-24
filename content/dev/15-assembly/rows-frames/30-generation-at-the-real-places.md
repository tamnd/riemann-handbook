---
title: Generation at the real places
decls:
  - GlobalTheory.GenReal.genInf
  - GlobalTheory.T.realFockThetaLift_vanishing_of_generating_vectors
  - GlobalTheory.GenRealFock.gen
  - GlobalTheory.T.equivariant_bilinearForms_vanish_of_io_generation_real
  - GlobalTheory.GenByIo.forms_vanish_of_io
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Generation at the real places

[Generation at the finite places](/entry/gen-fin/) reduced the vanishing of downward integrals on all theta functions to their vanishing on the theta functions of finite type. This section proves that vanishing, starting from the vanishing of the theta lift of $y$. The argument has three layers. First, a density argument in a Sobolev norm reduces theta functions of finite type to Fock vectors. Second, the downward integrals against Fock vectors form a family of bilinear forms with an equivariance and a Lie stability. Third, such a family vanishes once it vanishes on the vectors that come from the lowest types. The third layer is representation theory of compact dual pairs, and it is proved in Sections 31 and 32.

### The Fock vectors

We keep the notation of Section 28. Write $\tau$ for the archimedean indices, and $G_\infty \subseteq U(V)(\mathbb{A})$ for the elements with trivial finite component. The real data give:

1. the *Fock polynomial ring* $\mathcal{P}$, the polynomial ring over $\mathbb{C}$ in variables $x_{\tau, a, b}$ with $a < \operatorname{rank} W$ and $b < \operatorname{rank} V$;
2. the *Fock vectors*: a linear map $P \mapsto \phi_P$ from $\mathcal{P}$ to theta functions, which reads $P$ in the raising operators and applies it to a fixed vector of the real data;
3. the *lowest types*: the tensor product $L$ over $\tau$ of the lowest-type subspaces, with a map $\iota \colon L \to \operatorname{Hom}(\mathcal{E}, \mathcal{P})$;
4. the *theta map* $\theta_{i,t}$ on $H_V$.

The Lie algebra of $U(W)$ at $\tau$ is the set of matrices $Y$ with $Y^* G_\tau + G_\tau Y = 0$, where $G_\tau$ is the Gram matrix of $W$ at $\tau$. For such $Y$ the elements $\exp(sY)$, $s \in \mathbb{R}$, form a one-parameter subgroup of $U(W)(\mathbb{A})$ at $\tau$.

### Equivariant forms

**Theorem 7.30.1 (Equivariant forms vanish).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $(B_j)_{j \in I}$ be bilinear forms $\mathcal{P} \times \mathcal{E}^* \to \mathbb{C}$ with the following properties.

1. (Equivariance) If $u \in G_\infty$ and $\phi_{P'} = \omega(u, 1) \phi_P$, then $B_j(P', \lambda) = B_j(P, \lambda \circ \rho(u))$ for all $j$ and $\lambda$.
2. (Lie stability) Let $Y$ lie in the Lie algebra of $U(W)$ at $\tau$, and let $\phi_{P'}(z)$ be the derivative at $s = 0$ of $\omega(1, \exp(sY)) \phi_P(z)$ for each $z$. If $B_j(P, \cdot) = 0$ for all $j$, then $B_j(P', \cdot) = 0$ for all $j$.
3. (Lowest types) $B_j(\iota(x)(e), \cdot) = 0$ for all $x \in L$, $e \in \mathcal{E}$ and $j$.

Then $B_j = 0$ for all $j$.

Lean: `GlobalTheory.T.equivariant_bilinearForms_vanish_of_io_generation_real` (also `GlobalTheory.GenByIo.forms_vanish_of_io`).

*Proof.* Let $U = \bigcap_j \{\, P : B_j(P, \cdot) = 0 \,\}$. By property 1, $U$ is stable under $G_\infty$ in the sense that $P \in U$ and $\phi_{P'} = \omega(u, 1)\phi_P$ give $P' \in U$. By property 2, $U$ is stable under the Lie algebra of $U(W)$. By property 3, the image of $\iota$ lies in $U$.

1. Let $P \in \mathcal{P}$. Then $P = Q + (P - Q)$, where $Q$ is in the span of the vectors $\varphi(e)$ with $\varphi \colon \mathcal{E} \to \mathcal{P}$ linear and $G_\infty$-equivariant through $\phi$, and $P - Q$ lies in a finite-dimensional $G_\infty$-stable subspace on which every equivariant form vanishes. This is the isotypic decomposition of $\mathcal{P}$ under the compact group $G_\infty$: $Q$ is the component of type $\mathcal{E}$.
2. By [the isotypic membership of Section 31](/entry/cv-type-mem-of-stable/), a subspace with the three properties of $U$ contains $\varphi(e)$ for every equivariant $\varphi$ and every $e$. So $Q \in U$.
3. By property 1, each $B_j$ is equivariant, so $B_j(P - Q, \cdot) = 0$ by step 1, and $B_j(Q, \cdot) = 0$ by step 2.

So $B_j(P, \cdot) = 0$. $\square$

Property 2 is stated on the common kernel, not on each form. This is the form in which it is checked below: the derivative of a downward integral at $g$ is a downward integral at nearby points, so the vanishing is needed at every $g$.

### Downward integrals of Fock vectors

**Theorem 7.30.2 (Vanishing on Fock vectors).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $y \in H_V$ with
$$d\bigl(y, \phi_{\iota(x)(e)}, l, g\bigr) = 0$$
for all $x \in L$, $e \in \mathcal{E}$, $l \in \mathcal{E}^*$ and $g \in U(W)(\mathbb{A})$. Then $d(y, \phi_P, l, g) = 0$ for all $P \in \mathcal{P}$, $l$ and $g$.

Lean: `GlobalTheory.T.realFockThetaLift_vanishing_of_generating_vectors` (also `GlobalTheory.GenRealFock.gen`).

*Proof.* For $g \in U(W)(\mathbb{A})$ put $B_g(P, l) = d(y, \phi_P, l, g)$. Each $\phi_P$ is a theta function, so the integrand is integrable and $d$ is additive and homogeneous in $f$ and in $l$. So each $B_g$ is bilinear on $\mathcal{P} \times \mathcal{E}^*$. We check the three properties of the theorem above for the family $(B_g)_g$.

1. For $u \in G_\infty$, $d(y, \omega(u, 1) f, l, g) = d(y, f, l \circ \rho(u), g)$, by a change of variables $h \mapsto h u$ in the integral and the equivariance of $\tilde{y}$.
2. Let $B_g(P, \cdot) = 0$ for all $g$, and let $\phi_{P'}$ be the derivative of $\omega(1, \exp(sY))\phi_P$ at $s = 0$. Then $B_g(P', l)$ is the derivative at $s = 0$ of $B_{g \exp(sY)}(P, l)$, which is identically zero. So $B_g(P', \cdot) = 0$ for all $g$.
3. Property 3 is the hypothesis.

So each $B_g$ is zero. $\square$

### Generation at the real places

For a theta function $f$ of finite type, the *Sobolev norm* $\|f\|_N$ is built from the $L^2$ norm on a fundamental domain $\mathcal{F}$ of the rational matrices, with a Haar measure $\mu$ normalized by $\mu(\mathcal{F}) = 1$, and from the real Heisenberg derivatives up to order $N$.

**Theorem 7.30.3 (Generation at the real places).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $y \in H_V$ with $\theta_{i,t}(y) = 0$. Then $d(y, f, l, g) = 0$ for each theta function $f$ of finite type, each $l \in \mathcal{E}^*$ and each $g \in U(W)(\mathbb{A})$.

Lean: `GlobalTheory.GenReal.genInf`.

*Proof.* We argue by contradiction.

1. Fix the Haar measure $\mu$ and the fundamental domain $\mathcal{F}$ with $\mu(\mathcal{F}) = 1$.
2. Since $\theta_{i,t}(y) = 0$, the downward integrals of $y$ vanish on the Fock vectors of the lowest types: a single coefficient of the theta lift is such an integral. By the theorem above, $d(y, \phi_P, l, g) = 0$ for all $P \in \mathcal{P}$.
3. Suppose $d(y, f, l, g) \neq 0$ and put $\epsilon = |d(y, f, l, g)|$. The downward integral is continuous in the Sobolev norm: there are $N$ and $\delta > 0$ with
$$\begin{aligned} \bigl| d(y, f, l, g) - d(y, \phi_P, l, g) \bigr| &< \epsilon \quad \text{whenever} \quad \|f - \phi_P\|_N < \delta. \end{aligned}$$
4. A theta function of finite type is a Sobolev limit of Fock vectors. So some $P$ has $\|f - \phi_P\|_N < \delta$. With step 2 this gives $\epsilon < \epsilon$.

This contradiction proves the claim. $\square$

The three theorems together say that a form $y$ with $\theta_{i,t}(y) = 0$ pairs to zero with every theta function of finite type. With [generation at the finite places](/entry/gen-fin/), the pairing with every theta function vanishes. This is used in step 3 of the type properties of [the lift of rows](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/).

**Remark 7.30.4 (Formalization).** The theorem `genInf` is at line 22 of [ThetaLiftGenerationAtRealPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaLiftGenerationAtRealPlaces.lean#L22), and `GenInf` is at line 79 of [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L79). The relay for Fock vectors is at line 18 of [RealFockThetaLiftVanishingOfGeneratingVectorsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealFockThetaLiftVanishingOfGeneratingVectorsStatement.lean#L18), and its target `gen` is at line 93 of [RealFockThetaLiftVanishingOfGeneratingVectors.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RealFockThetaLiftVanishingOfGeneratingVectors.lean#L93). Its helpers `downInt_add_f` and `downInt_smul_f` repeat `downInt_add` and `downInt_smul` of the file of `genFin`. The relay for equivariant forms is at line 18 of [EquivariantBilinearFormsVanishOfIoGenerationRealStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/EquivariantBilinearFormsVanishOfIoGenerationRealStatement.lean#L18), and its target `forms_vanish_of_io` is at line 21 of [EquivariantBilinearFormsVanishOfIoGenerationReal.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/EquivariantBilinearFormsVanishOfIoGenerationReal.lean#L21). In `forms_vanish_of_io` the hypotheses `Given R F` and `R.FullP` are only passed to the two lemmas it cites. The proofs of steps 1 and 2 of `gen` are cited lemmas (`downInt_realEquiv` and `GenReal.downInt_lie`); the change of variables and the derivative argument above are the classical arguments, given here instead of those Lean proofs. In the same way the isotypic decomposition of step 1 of `forms_vanish_of_io` is the lemma `polynomial_mem_span_lifted_maps`, and the Sobolev continuity and density in `genInf` are cited lemmas.
