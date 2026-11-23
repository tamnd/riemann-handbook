---
title: The Kummer sequence and the coefficients
decls:
  - GlobalTheory.T.exists_kummer_boundary_etale_cohomology
  - GlobalTheory.kummer_boundary
  - GlobalTheory.EtC.isTwRes_tensor
  - GlobalTheory.EtC.RedCoef.a11
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kummer sequence and the coefficients

This section proves three results on the coefficients $\mathbb{Z}/q(i)$ on spaces. The first gives the long exact sequence of the Kummer sequence $0 \to \mathbb{Z}/q(1) \to \mathbb{G}_m \xrightarrow{q} \mathbb{G}_m \to 0$, with the boundary of a unit equal to its Kummer class and the boundary of a line bundle equal to its Chern class, up to sign. The second says that the tensor product of resolutions of $\mathbb{Z}/q(i)$ and $\mathbb{Z}/q(j)$ resolves $\mathbb{Z}/q(i+j)$. The third says that the reduction of coefficients from $\mathbb{Z}/Q$ to $\mathbb{Z}/q$ is compatible with cup products, units, Chern classes and composition. The three results are inputs of [the local steps](/entry/steps-holds/) of the chapter on Galois representations.

We keep the notation of the earlier sections. $\mathbb{G}_m$ is the sheaf of abelian groups $U \mapsto \Gamma(U, \mathcal{O}_U)^\times$, and $H^n(E, \mathbb{G}_m)$ is the cohomology of a space $E$ with $R = \mathbb{Z}$. We write the group law of $\mathbb{G}_m$ additively when we speak of maps, so "multiplication by $q$" on $\mathbb{G}_m$ is $u \mapsto u^q$. A unit $u \in \Gamma(X, \mathcal{O}_X)^\times$ gives a class $[u] \in H^0(X, \mathbb{G}_m)$, and a line bundle $L$ on $E$ gives a class $[L] \in H^1(E, \mathbb{G}_m)$, the class of the cocycle of its transition units. For a unit $u$ on a scheme on which $q$ is a unit, $\kappa(u) \in H^1(X, \mathbb{Z}/q(1))$ is its Kummer class.

### The Kummer boundary

We use the following results and take them as given.

**Lemma 2.12.1 (The Kummer sequence of sheaves).** Let $q \geq 1$. There is an injective map of sheaves of abelian groups $\iota : \mathbb{Z}/q(1) \to \mathbb{G}_m$ with the following properties.

1. $q \iota = 0$, and $\iota([\zeta]) = \zeta$ for every scheme $U$ and every $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$.
2. Let $U$ be a scheme on which $q$ is a unit. Every $b \in \mathbb{G}_m(U)$ with $b^q = 1$ is $\iota(a)$ for some $a$, and every $b \in \mathbb{G}_m(U)$ is a $q$-th power étale locally on $U$.

Lean: `GlobalTheory.T.kummer_sequence_etale_tateTwist`.

This is the Kummer sequence of J. S. Milne, *Étale Cohomology*, Chapter II, §2, with $\mu_q$ identified with $\mathbb{Z}/q(1)$ by $[\zeta] \mapsto \zeta$.

**Lemma 2.12.2 (Tools for the long exact sequence).**

1. A short exact sequence $0 \to A \to B \to C \to 0$ of sheaves of $R$-modules has a connecting map $\delta : H^n(E, C) \to H^{n+1}(E, A)$, natural in the space $E$, with the usual long exact sequence.
2. Let $\varphi : F \to F'$ be a map of sheaves of $R$-modules, and let $E$ be a space. If $\varphi$ is bijective on sections over every scheme $U$ with $E_0(U) \neq \emptyset$, then $\varphi_* : H^n(E, F) \to H^n(E, F')$ is bijective for every $n$.
3. For a sheaf $F$ of $\mathbb{Z}/q$-modules, the cohomology of $F$ over $\mathbb{Z}/q$ and the cohomology of $F$ as a sheaf of abelian groups are isomorphic by the natural map.
4. Let $\theta : \operatorname{coker} \iota \to \mathbb{G}_m$ be the map induced by multiplication by $q$. Then $\theta$ is bijective on sections over every scheme on which $q$ is a unit.
5. The boundary of the Kummer sequence sends $[u]$ to $\pm \kappa(u)$, and $[L]$ to $\pm c_1(L)$, with signs that depend only on $q$.

Lean: `GlobalTheory.T.exists_connecting_cocycle_hypercohomology_les`, `GlobalTheory.T.etaleCohomology_bijective_of_support_bijective`, `GlobalTheory.T.etaleCohomology_coefficientRing_invariance`, `GlobalTheory.T.kummer_cokernel_to_multiplicativeGroup_bijective`, `GlobalTheory.T.kummerConnecting_unitClass_eq_kummerClass` and `GlobalTheory.T.kummerBoundary_lineBundle_firstChernClass`.

Part 4 is part 2 of the lemma on the Kummer sequence: the kernel of $u \mapsto u^q$ is the image of $\iota$, and the map is surjective as a map of sheaves.

**Theorem 2.12.3 (Kummer boundary).** Let $q \geq 1$. There are a map of sheaves of abelian groups $\iota : \mathbb{Z}/q(1) \to \mathbb{G}_m$ and homomorphisms $\partial : H^n(E, \mathbb{G}_m) \to H^{n+1}(E, \mathbb{Z}/q(1))$, for every space $E$ and every $n \in \mathbb{Z}$, with the following properties.

1. $\iota([\zeta]) = \zeta$ for every scheme $U$ and every $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$.
2. If $f : E \to E'$ is a map of spaces and $q$ is invertible on $E'$, then $f^* \partial = \partial f^*$.
3. If $q$ is invertible on $E$, then the sequence
$$
\begin{aligned}
H^n(E, \mathbb{G}_m) &\xrightarrow{q} H^n(E, \mathbb{G}_m) \xrightarrow{\partial} H^{n+1}(E, \mathbb{Z}/q(1)) \\
&\xrightarrow{\iota_*} H^{n+1}(E, \mathbb{G}_m) \xrightarrow{q} H^{n+1}(E, \mathbb{G}_m)
\end{aligned}
$$
is exact at the three inner places, for every $n \in \mathbb{Z}$.
4. There is $s \in \{1, -1\}$ such that $\partial [u] = s\,\kappa(u)$ for every scheme $X$ on which $q$ is a unit and every unit $u$ on $X$.
5. There is $s' \in \{1, -1\}$ such that $\partial [L] = s'\,c_1(L)$ for every space $E$ on which $q$ is invertible and every line bundle $L$ on $E$.

Lean: `GlobalTheory.T.exists_kummer_boundary_etale_cohomology` (also `GlobalTheory.kummer_boundary`).

*Proof.* Take $\iota$ from the lemma on the Kummer sequence; it has property 1. Let $C = \operatorname{coker} \iota$, so that $0 \to \mathbb{Z}/q(1) \to \mathbb{G}_m \to C \to 0$ is exact, and let $\delta$ be its connecting map. Multiplication by $q$ on $\mathbb{G}_m$ is the composite $\mathbb{G}_m \to C \xrightarrow{\theta} \mathbb{G}_m$.

Let $E$ be a space on which $q$ is invertible. By parts 2 and 4 of the tools, $\theta_* : H^n(E, C) \to H^n(E, \mathbb{G}_m)$ is bijective. Define
$$
\partial = \delta \circ \theta_*^{-1} : H^n(E, \mathbb{G}_m) \to H^{n+1}(E, \mathbb{Z}/q(1)),
$$
where the target is read over $\mathbb{Z}/q$ through part 3 of the tools. On a space on which $q$ is not invertible, let $\partial = 0$.

The long exact sequence of part 1 of the tools contains
$$
H^n(E, \mathbb{G}_m) \to H^n(E, C) \xrightarrow{\delta} H^{n+1}(E, \mathbb{Z}/q(1)) \xrightarrow{\iota_*} H^{n+1}(E, \mathbb{G}_m) \to H^{n+1}(E, C).
$$
Replace $H^n(E, C)$ and $H^{n+1}(E, C)$ by $H^n(E, \mathbb{G}_m)$ and $H^{n+1}(E, \mathbb{G}_m)$ through $\theta_*$. The maps $\mathbb{G}_m \to C$ become multiplication by $q$, and $\delta$ becomes $\partial$. This gives property 3.

For property 2, if $q$ is invertible on $E'$ and $E_0(U) \neq \emptyset$, then $f$ gives a point of $E'_0(U)$, so $q$ is a unit on $U$. So $q$ is invertible on $E$ too. Then $\partial$ is defined by the formula on both spaces, and $\delta$, $\theta_*$ and the change of rings commute with $f^*$. Properties 4 and 5 are part 5 of the tools. $\square$

### Products of resolutions

**Definition 2.12.4 (Resolution of a Tate twist).** Let $q \geq 1$ and $i \in \mathbb{Z}$. A *resolution of $\mathbb{Z}/q(i)$ with generators $e$* is a complex $T$ of sheaves of $\mathbb{Z}/q$-modules, zero in negative degrees, with a quasi-isomorphism $\varepsilon : \mathbb{Z}/q(i)[0] \to T$ and, for each scheme $U$ and $\zeta \in \mathrm{Prim}_q(\Gamma(U, \mathcal{O}_U))$, a section $e(\zeta) \in T^0(U)$ with $\varepsilon([\zeta]) = e(\zeta)$.

The generators keep track of the class $[\zeta]$ in the resolution, so that products of resolutions carry products of generators. A *pairing* $\tau : I \otimes J \to T$ of complexes of sheaves is a family of bilinear maps $I^s(U) \times J^t(U) \to T^{s+t}(U)$, natural in $U$ and compatible with the differentials by the Leibniz rule. It is a *tensor pairing* if it identifies $T^w$ with the sheafification of $\bigoplus_{s+t=w} I^s \otimes J^t$. A sheaf is *flat* if it is the sheafification of a presheaf whose values on nonempty schemes are flat modules.

We use the following results and take them as given.

**Lemma 2.12.5 (Tensor pairings).** Let $q \geq 1$.

1. For $i + j = k$ there is a tensor pairing $\mathbb{Z}/q(i)[0] \otimes \mathbb{Z}/q(j)[0] \to \mathbb{Z}/q(k)[0]$ that sends $[\zeta] \otimes [\zeta]$ to $[\zeta]$.
2. Let $\tau : I \otimes J \to T$ and $\tau' : I' \otimes J \to T'$ be tensor pairings of complexes of sheaves of $R$-modules, with $I$, $I'$ and $J$ zero in negative degrees and $J$ flat in each degree. Let $f : I \to I'$ be a quasi-isomorphism and $u : T \to T'$ a map with $u(\tau(a \otimes b)) = \tau'(f(a) \otimes b)$. Then $u$ is a quasi-isomorphism.
3. For complexes $I$ and $J$ there is a tensor pairing $I \otimes J \to T$, and a tensor pairing has the universal property of the tensor product. A tensor pairing of complexes zero in negative degrees has a target zero in negative degrees.
4. The sheaf $\mathbb{Z}/q(i)$ is flat.

Lean: `GlobalTheory.T.tateTwist_mul_isTensorPairing`, `GlobalTheory.T.tensor_flat_complex_preserves_quasiIso`, `GlobalTheory.T.exists_isTensor_etaleSheafComplexPairing`, `GlobalTheory.T.isTensor_universal_property` and `GlobalTheory.EtC.flatS_tw`.

Part 2 is the statement that tensor product with a complex of flat sheaves, bounded below, preserves quasi-isomorphisms. Part 1 holds because $\mathbb{Z}/q(i)$ is free of rank one locally, with basis $[\zeta]$ wherever $\zeta$ exists.

**Theorem 2.12.6 (Product of resolutions).** Let $q \geq 1$ and $i + j = k$. Let $I$ be a resolution of $\mathbb{Z}/q(i)$ with generators $e$, and $J$ a resolution of $\mathbb{Z}/q(j)$ with generators $e'$, such that $J$ is flat in each degree. Let $\tau : I \otimes J \to T$ be a tensor pairing. Then $T$ is a resolution of $\mathbb{Z}/q(k)$ with generators $\zeta \mapsto \tau(e(\zeta) \otimes e'(\zeta))$.

Lean: `GlobalTheory.EtC.isTwRes_tensor`.

*Proof.* By part 3 of the lemma, $T$ is zero in negative degrees. Let $\mu : \mathbb{Z}/q(i)[0] \otimes \mathbb{Z}/q(j)[0] \to \mathbb{Z}/q(k)[0]$ be the pairing of part 1, and let $\tau_1 : \mathbb{Z}/q(i)[0] \otimes J \to T_1$ be a tensor pairing. By the universal property there are maps
$$
u_1 : \mathbb{Z}/q(k)[0] \to T_1, \qquad u_2 : T_1 \to T,
$$
with $u_1(\mu(a \otimes b)) = \tau_1(a \otimes \varepsilon_J(b))$ and $u_2(\tau_1(a \otimes c)) = \tau(\varepsilon_I(a) \otimes c)$.

The map $u_2$ is a quasi-isomorphism by part 2, applied with $f = \varepsilon_I$, since $J$ is flat. For $u_1$, exchange the two factors: with the sign $(-1)^{st}$ the pairings $\mu$ and $\tau_1$ become tensor pairings with $\mathbb{Z}/q(i)[0]$ as the second factor, which is flat by part 4. Then part 2, applied with $f = \varepsilon_J$, says that $u_1$ is a quasi-isomorphism. So $\varepsilon = u_2 \circ u_1$ is a quasi-isomorphism $\mathbb{Z}/q(k)[0] \to T$.

For the generators, $u_1([\zeta]) = u_1(\mu([\zeta] \otimes [\zeta])) = \tau_1([\zeta] \otimes e'(\zeta))$, and then $u_2$ sends this to $\tau(e(\zeta) \otimes e'(\zeta))$. $\square$

### Reduction of coefficients

**Definition 2.12.7 (Reduction map).** Let $Q \geq 1$ and let $q$ divide $Q$. For $\zeta \in \mathrm{Prim}_Q(A)$ the power $\zeta^{Q/q}$ lies in $\mathrm{Prim}_q(A)$. The *reduction* $\mathrm{red}_{Q,q} : H^n(E, \mathbb{Z}/Q(i)) \to H^n(E, \mathbb{Z}/q(i))$ is the map induced by a map of resolutions $I^\bullet(\mathbb{Z}/Q(i)) \to I^\bullet(\mathbb{Z}/q(i))$, linear over $\mathbb{Z}/Q \to \mathbb{Z}/q$, that sends $[\zeta]$ to $[\zeta^{Q/q}]$ in degree $0$.

On $\mu_Q \to \mu_q$ this is the map $x \mapsto x^{Q/q}$, so the reduction is the map of coefficients $\mu_Q^{\otimes i} \to \mu_q^{\otimes i}$.

We use the following results and take them as given.

**Lemma 2.12.8 (Properties of reduction).** Let $Q \geq 1$, let $q$ divide $Q$, and let $E$ be a space.

1. Two maps of resolutions as in the definition that agree on the classes $[\zeta]$ in degree $0$ induce the same map on cohomology.
2. The map chosen in the definition sends $[\zeta]$ to $[\xi]$ whenever $\xi \in \mathrm{Prim}_q(A)$ and $\xi = \zeta^{Q/q}$.
3. $\mathrm{red}_{Q,q}(a \cup b) = \mathrm{red}_{Q,q}(a) \cup \mathrm{red}_{Q,q}(b)$.
4. If $Q$ is invertible on $E$, then $\mathrm{red}_{Q,q}(1) = 1$ and $\mathrm{red}_{Q,q}(c_1(L)) = c_1(L)$ for every line bundle $L$ on $E$.

Lean: `GlobalTheory.T.tateTwistReduction_cohomology_map_unique`, `GlobalTheory.T.tateTwistReductionResolutionMap_generator`, `GlobalTheory.T.tateTwistCoefficientReduction_cup`, `GlobalTheory.T.tateTwistCoefficientReduction_unitClass` and `GlobalTheory.T.red_c1_eq_c1_of_dvd`.

**Theorem 2.12.9 (Reduction of coefficients).** Let $Q \geq 1$, let $q$ divide $Q$, and let $E$ be a space.

1. $\mathrm{red}_{Q,q}(a \cup b) = \mathrm{red}_{Q,q}(a) \cup \mathrm{red}_{Q,q}(b)$ for all $a \in H^n(E, \mathbb{Z}/Q(i))$ and $b \in H^m(E, \mathbb{Z}/Q(j))$, with $n, m, i, j \in \mathbb{Z}$.
2. If $Q$ is invertible on $E$, then $\mathrm{red}_{Q,q}(1) = 1$, and $\mathrm{red}_{Q,q}(c_1(L)) = c_1(L)$ for every line bundle $L$ on $E$.
3. $\mathrm{red}_{Q,Q}(a) = a$ for all $n, i$ and $a \in H^n(E, \mathbb{Z}/Q(i))$.
4. If $r$ divides $q$, then $\mathrm{red}_{q,r}(\mathrm{red}_{Q,q}(a)) = \mathrm{red}_{Q,r}(a)$ for all $n, i$ and $a \in H^n(E, \mathbb{Z}/Q(i))$.

Lean: `GlobalTheory.EtC.RedCoef.a11`.

*Proof.* Parts 1 and 2 are parts 3 and 4 of the lemma.

Part 3. The map chosen for $\mathrm{red}_{Q,Q}$ sends $[\zeta]$ to $[\zeta^{Q/Q}] = [\zeta]$, by part 2 of the lemma. The identity map of $I^\bullet(\mathbb{Z}/Q(i))$ does the same. By part 1 of the lemma they induce the same map on cohomology, and the identity induces the identity.

Part 4. Since $q \mid Q$ and $r \mid q$, both $q$ and $r$ are at least $1$. Let $\zeta \in \mathrm{Prim}_Q(A)$, let $\eta = \zeta^{Q/q} \in \mathrm{Prim}_q(A)$ and $\xi = \eta^{q/r} \in \mathrm{Prim}_r(A)$. By part 2 of the lemma, the composite of the maps chosen for $\mathrm{red}_{Q,q}$ and $\mathrm{red}_{q,r}$ sends $[\zeta]$ to $[\eta]$ and then to $[\xi]$. Since $(Q/q)(q/r) = Q/r$, we have $\xi = \zeta^{Q/r}$, so the map chosen for $\mathrm{red}_{Q,r}$ also sends $[\zeta]$ to $[\xi]$. The composite of the two maps induces $\mathrm{red}_{q,r} \circ \mathrm{red}_{Q,q}$ on cohomology. By part 1 of the lemma this is $\mathrm{red}_{Q,r}$. $\square$

**Remark 2.12.10 (Formalization).** The Kummer boundary is defined as $0$ on spaces on which $q$ is not invertible, and the statement gives two independent signs for units and for line bundles: [ExistsKummerBoundaryEtaleCohomology.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsKummerBoundaryEtaleCohomology.lean#L50). The reduction of coefficients is the condition $A_{11}$ of the package of axioms in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L67). Its map of resolutions is a choice with the stated property, which is $0$ if no map has the property: [PullHlComp.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PullHlComp.lean#L186). The proof of $A_{11}$ is in a module named after a lemma on divisibility: [NeZeroOfDvd.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NeZeroOfDvd.lean#L64). We opened the statements of the lemmas but not their proofs; the reasons we give after them are ours.
